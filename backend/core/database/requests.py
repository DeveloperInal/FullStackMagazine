import random
from core.database.model import CardTable, async_session, PromocodTable, UsersByProduct
from aiogram import Bot
from core.schemas import Promocod_Data, Card_UC_Data, User_By_Product
from datetime import datetime
from sqlalchemy import select
from core.settings import settings

bot = Bot(token=settings.bot_token)
class CardRepository:

    @classmethod
    async def set_card_info(cls, card: Card_UC_Data) -> Card_UC_Data:
        async with async_session() as session:
            async with session.begin():
                stmt = CardTable(
                    title=card.title,
                    price=card.price,
                    description=card.description,
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


class BotRequestsRepository:
    @classmethod
    async def post_request_user_product(cls, user: User_By_Product):
        async with async_session() as session:
            async with session.begin():
                by_product_date = user.by_product_date or datetime.utcnow()
                if by_product_date.tzinfo is not None:
                    by_product_date = by_product_date.replace(tzinfo=None)

                stmt = UsersByProduct(
                    tg_id=user.tg_id,
                    by_product_date=by_product_date,
                    card_title=user.card_title
                )
                session.add(stmt)
                promocod_stmt = select(PromocodTable)
                result = await session.execute(promocod_stmt)
                promocods = result.scalars().all()

                if promocods:
                    random_promocode = random.choice(promocods)
                    promocode_text = f"{random_promocode.promocod}"
                else:
                    promocode_text = "\nПромокоды не найдены."

                message_text = (
                    f"Покупка успешно зарегистрирована!\n"
                    f"Название товара: {user.card_title}\n"
                    f"Дата покупки: {by_product_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
                    f"Промокод:{promocode_text}"
                )
                await bot.send_message(chat_id=user.tg_id, text=message_text)
        return stmt

    @classmethod
    async def get_request_user_product(cls, tg_id: int):
        async with async_session() as session:
            stmt = select(UsersByProduct).where(UsersByProduct.tg_id == tg_id)
            result = await session.execute(stmt)
            user_product = result.scalars().all()
            return user_product

class PromocodRepository:
    @classmethod
    async def set_promocod_info(cls, promocode: Promocod_Data):
        async with async_session() as session:
            async with session.begin():
                stmt = PromocodTable(
                    promocod=promocode.promocod
                )
                session.add(stmt)
        return stmt