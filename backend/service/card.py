from core.database.model import CardTable
from core.database.base import async_session
from core.schemas import Card_UC_Data
from sqlalchemy import select

class CardRepository:
    @classmethod
    async def set_card_info(cls, card: Card_UC_Data) -> Card_UC_Data:
        async with async_session() as session:
            async with session.begin():
                stmt = CardTable(
                    title=card.title,
                    price=card.price,
                    image_url=card.image_url
                )
                session.add(stmt)
        return card

    @classmethod
    async def get_card_info(cls) -> list:
        async with async_session() as session:
            stmt = select(CardTable)
            result = await session.execute(stmt)
            cards = result.scalars().all()
            return cards