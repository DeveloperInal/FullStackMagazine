from sqlalchemy import Integer
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from core.settings import settings

engine = create_async_engine(url=settings.url_database, echo=False)
async_session = async_sessionmaker(bind=engine, expire_on_commit=True)

class Base(DeclarativeBase, AsyncAttrs):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)