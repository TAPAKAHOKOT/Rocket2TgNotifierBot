from aiogram import types

from Configs import translations

class ExampleKeyboard:
    def __init__(self):
        self.test = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.test.add(
            types.KeyboardButton(text='/start'),
        )
    
    def get_main_keyboard(self) -> types.ReplyKeyboardMarkup:
        self.main = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        self.main.add(
            types.KeyboardButton(text=translations.get('keyboards.buttons.hi')),
            types.KeyboardButton(text=translations.get('keyboards.buttons.joke')),
            types.KeyboardButton(text=translations.get('keyboards.buttons.another-keyboard')),
        )

        return self.main
