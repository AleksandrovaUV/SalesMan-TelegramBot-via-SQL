from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
import os
from dotenv import load_dotenv
load_dotenv()

engine = create_async_engine(url=os.getenv('DB_URL'), echo=True)

# создаем асинхронную сессию, чтобы делать crud щперации

async_session = async_sessionmaker(engine) # функция

class Base(AsyncAttrs, DeclarativeBase): # родительский класс для управления другими классами
    pass


class User(Base):  # пользователи
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) # айди в нашей системе
    tg_id: Mapped[int] = mapped_column(BigInteger)

class Category(Base): # категории товаров
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(25))

class Item(Base): # товары
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(512))
    price: Mapped[int]


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
