from datetime import datetime
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, BigInteger, DateTime, ForeignKey
from core.database.base import Base

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