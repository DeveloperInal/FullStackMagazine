from datetime import datetime
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, BigInteger, DateTime, ForeignKey, Boolean
from core.settings import settings

engine = create_async_engine(url=settings.url_database, echo=False)
async_session = async_sessionmaker(bind=engine, expire_on_commit=True)

class Base(DeclarativeBase, AsyncAttrs):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

class UsersByProduct(Base):
    __tablename__ = 'users_by_product'

    tg_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    by_product_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    card_title: Mapped[str] = mapped_column(ForeignKey('card_info.title'), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    promocode: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    card: Mapped["CardTable"] = relationship("CardTable", back_populates="users_by_product")


class CardTable(Base):
    __tablename__ = 'card_info'

    title: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    image_url: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    users_by_product: Mapped[list["UsersByProduct"]] = relationship("UsersByProduct", back_populates="card")

class PromocodTable(Base):
    __tablename__ = 'promocod_info'

    promocode: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    title: Mapped[str] = mapped_column(String, nullable=False)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)