from aiogram import types
from Configs import translations

class CommandsKeyboards:
    def get_start_keyboard(self) -> types.ReplyKeyboardMarkup:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        start.add(
            types.KeyboardButton(text='/start'), 
            types.KeyboardButton(text='/help'),
            types.KeyboardButton(text='/settings'),
            types.KeyboardButton(text=translations.get('keyboards.buttons.write-to-dev'))
        )
        return start
