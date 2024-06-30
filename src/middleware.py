# at the import level
from datetime import datetime, timedelta

from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from src.constants import MIDDLEWARE_TABLE_NAME


class RateLimitingMiddleware(BaseHTTPMiddleware):

    RATE_LIMIT_DURATION = timedelta(minutes=1)
    RATE_LIMIT_REQUESTS = 20

    def __init__(self, app):
        super().__init__(app)
        self.request_counts = {}
        self.client = db.client.collection(MIDDLEWARE_TABLE_NAME)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host

        request_count, last_request = self.request_counts.get(client_ip, (0, datetime.min))

        elapsed_time = datetime.now() - last_request

        if elapsed_time > self.RATE_LIMIT_DURATION:
            request_count = 1
        else:
            if request_count >= self.RATE_LIMIT_REQUESTS:
                return JSONResponse(
                    status_code=429, content={"message": "Rate limit exceeded. Please try again later."}
                )
            request_count += 1

        self.request_counts[client_ip] = (request_count, datetime.now())

        response = await call_next(request)

        return response
