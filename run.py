from aiogram import Bot, Dispatcher
import asyncio
from dotenv import load_dotenv
import os

from app.handlers import router
from app.database.models import async_main

async def main():
    load_dotenv()
    await async_main()
    bot = Bot(token=os.getenv('TG_TOKEN')) #инициализируем подключение к боту
    dp = Dispatcher() # обработка запросов: выбирает функцию 
    dp.include_router(router) # сообщаем диспетчеру, что есть такой объект
    await dp.start_polling(bot) # выбирает, по какому юоту диспетчер ловит апдейт

if __name__ == '__main__': 
    asyncio.run(main()) # тк запустить ассинхронную ф-ию в синхронной невозможно
