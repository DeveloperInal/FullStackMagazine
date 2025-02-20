from core.database.model import PromocodTable
from core.database.base import async_session
from core.schemas import Promocod_Data
from sqlalchemy import select, delete

class PromocodeRepository:
    @classmethod
    async def set_promocode_info(cls, promocode: Promocod_Data):
        async with async_session() as session:
            async with session.begin():
                stmt = PromocodTable(
                    promocode=promocode.promocode,
                    title=promocode.title
                )
                session.add(stmt)
            await session.commit()
        return promocode

    @classmethod
    async def get_promocode_info(cls):
        async with async_session() as session:
            stmt = select(PromocodTable)
            result = await session.execute(stmt)
            promocodes = result.scalars().all()
            return promocodes

    @classmethod
    async def get_promocodes_by_title(cls, title: str):
        async with async_session() as session:
            stmt = select(PromocodTable).where(PromocodTable.title == title)
            result = await session.execute(stmt)
            promocodes = result.scalars().all()
            return promocodes

    @classmethod
    async def delete_promocode(cls, promocode: str):
        async with async_session() as session:
            stmt = delete(PromocodTable).where(PromocodTable.promocode == promocode)
            await session.execute(stmt)
            await session.commit()

            return promocode