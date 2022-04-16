from Callbacks import settings_callback
from aiogram.types.inline_keyboard import InlineKeyboardMarkup

from Configs import update_user_language

class SettingsService:
    @staticmethod
    def get_settings_main_callback() -> InlineKeyboardMarkup:
        return settings_callback.main_inline
    

    @staticmethod
    def get_settings_languages_callback() -> InlineKeyboardMarkup:
        return settings_callback.language_inline
    

    @staticmethod
    def update_language(language: str):
        update_user_language(language)