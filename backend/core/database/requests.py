import random
from core.database.model import CardTable, async_session, PromocodTable, UsersByProduct
from aiogram import Bot
from core.schemas import Promocod_Data, Card_UC_Data, User_By_Product
from datetime import datetime
from sqlalchemy import select, delete
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


class AdminRepository:
    @classmethod
    async def get_user_by_promocode(cls):
        async with async_session() as session:
            stmt = select(UsersByProduct)
            result = await session.execute(stmt)
            users_by_product = result.scalars().all()
            return users_by_product
class BotRequestsRepository:
    @classmethod
    async def post_request_user_product(cls, user: User_By_Product):
        async with async_session() as session:
            async with session.begin():
                by_product_date = user.by_product_date or datetime.utcnow()
                if by_product_date.tzinfo is not None:
                    by_product_date = by_product_date.replace(tzinfo=None)

                promocod_stmt = select(PromocodTable).where(PromocodTable.title == user.card_title)
                result = await session.execute(promocod_stmt)
                promocods = result.scalars().all()

                if promocods:
                    random_promocode = random.choice(promocods)
                    promocode_text = random_promocode.promocode
                    await session.delete(random_promocode)
                else:
                    promocode_text = "Промокоды не найдены для данного товара."

                stmt = UsersByProduct(
                    tg_id=user.tg_id,
                    by_product_date=by_product_date,
                    card_title=user.card_title,
                    price=user.price,
                    promocode=promocode_text
                )
                session.add(stmt)

                message_text = (
                    f"Покупка успешно зарегистрирована!\n"
                    f"Название товара: {user.card_title}\n"
                    f"Дата покупки: {by_product_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
                    f"Промокод: {promocode_text}"
                )
                await bot.send_message(chat_id=user.tg_id, text=message_text)
                await bot.send_message(chat_id='ID Чата куда будет слаться сообщение', text=message_text)

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