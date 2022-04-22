from aiogram import types
from Configs import translations

class CommandsKeyboards:
    def __init__(self):
        self.start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.start.add(
            types.KeyboardButton(text='/start'), 
            types.KeyboardButton(text='/help'),
            types.KeyboardButton(text='/settings')
        )