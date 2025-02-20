import random
from core.database.model import PromocodTable, UsersByProduct
from core.database.base import async_session
from aiogram import Bot
from core.schemas import User_By_Product
from datetime import datetime
from sqlalchemy import select
from core.settings import settings

class BotRequestsRepository:
    @classmethod
    async def post_request_user_product(cls, user: User_By_Product):
        bot = Bot(token=settings.bot_token)
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