from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message): # функция на прием сообщений
    await message.answer('Добро пожаловать в магазин!',
                         reply_markup=kb.menu) # прикрепляем кнопочки