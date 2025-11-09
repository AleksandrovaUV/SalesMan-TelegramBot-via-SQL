from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Наш каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])