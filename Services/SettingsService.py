from sqlalchemy.orm import Session
from aiogram.types.inline_keyboard import InlineKeyboardMarkup

from Callbacks import settings_callback
from Database import engine
from Tables import UserSettings
from Configs import (
    get_available_languages,
    translations
)

class SettingsService:
    @staticmethod
    def get_settings_main_callback() -> InlineKeyboardMarkup:
        settings_callback.generate_main_inline()
        return settings_callback.main_inline
    

    @staticmethod
    def get_settings_languages_callback() -> InlineKeyboardMarkup:
        return settings_callback.language_inline
    

    @staticmethod
    def update_language(language: str, user_settings: UserSettings) -> UserSettings:

        print('\n\n', language.title(), [*get_available_languages()], language.title() not in get_available_languages(), '\n\n')
        if language.title() not in get_available_languages():
            return None

        with Session(engine, expire_on_commit=False) as session, session.begin():
            user_settings.language = language
            session.add(user_settings)
        
        translations.set_translation(user_settings.language)
        return user_settings
