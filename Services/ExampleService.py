from Callbacks import example_callback
from aiogram.types.inline_keyboard import InlineKeyboardMarkup

class ExampleService:
    @staticmethod
    def get_example_inline_callback() -> InlineKeyboardMarkup:
        return example_callback.example_inline