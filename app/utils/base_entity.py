from typing import Optional

from pydantic import BaseModel


class BaseEntity:
    
    def __init__(self, id: str) -> None:
        self.id = id
        self.is_active: bool = True
        self.created_by: str
        self.updated_by: str
        self.deleted_by: Optional[str]

    
