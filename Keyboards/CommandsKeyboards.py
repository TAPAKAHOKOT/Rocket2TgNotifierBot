from aiogram import types
from Configs import translations

class CommandsKeyboards:
    def __init__(self):
        self.start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.start.add(
            types.KeyboardButton(text=translations.get('keyboards.commands.random-film')), 
            types.KeyboardButton(text=translations.get('keyboards.commands.random-serial'))
        )