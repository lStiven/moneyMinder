from typing import List, Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class BaseRepository:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def add_and_commit(self, model_instance):
        self.db_session.add(model_instance)
        await self.db_session.commit()
        await self.db_session.refresh(model_instance)
        return model_instance

    async def commit_and_refresh(self, model_instance):
        await self.db_session.commit()
        await self.db_session.refresh(model_instance)
        return model_instance

    async def get_all_records(self, model_cls: Type) -> List:
        result = await self.db_session.execute(select(model_cls))
        return result.scalars().all()

    async def get_by_id(self, model_cls: Type, model_id):
        result = await self.db_session.get(model_cls, model_id)
        return result

    async def filter(self, model_cls: Type, **kwargs) -> List:
        query = select(model_cls).filter_by(**kwargs)
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def get_or_none(self, model_cls: Type, **kwargs):
        query = select(model_cls).filter_by(**kwargs)
        result = await self.db_session.execute(query)
        return result.scalars().first()

    async def delete_record(self, model_instance):
        await self.db_session.delete(model_instance)
        await self.db_session.commit()
        return True
