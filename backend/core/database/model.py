from datetime import datetime
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, BigInteger, DateTime, ForeignKey
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

    card_info: Mapped["CardTable"] = relationship("CardTable", back_populates="users_by_product")

class CardTable(Base):
    __tablename__ = 'card_info'

    title: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    price: Mapped[float] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, default=f'{price}UC', nullable=True)

    users_by_product: Mapped[list["UsersByProduct"]] = relationship("UsersByProduct", back_populates="card_info")


class PromocodTable(Base):
    __tablename__ = 'promocod_info'

    promocod: Mapped[str] = mapped_column(String, nullable=False, unique=True)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)