from core.database.base import async_session

class AdminRepository:
    @classmethod
    async def get_user_by_promocode(cls):
        async with async_session() as session:
            stmt = select(UsersByProduct)
            result = await session.execute(stmt)
            users_by_product = result.scalars().all()
            return users_by_product