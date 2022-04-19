from sqlalchemy.orm import Session
from aiogram.types.inline_keyboard import InlineKeyboardMarkup

import requests as r

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
        return settings_callback.get_main_inline()
    

    @staticmethod
    def get_settings_languages_callback() -> InlineKeyboardMarkup:
        return settings_callback.get_language_inline()
    

    @staticmethod
    def get_settings_rocket_callback() -> InlineKeyboardMarkup:
        return settings_callback.get_rocket_inline()
    

    @staticmethod
    def set_settings_rocket(user_settings: UserSettings, field: str, value: str) -> InlineKeyboardMarkup:
        with Session(engine, expire_on_commit=False) as session, session.begin():
            if field == 'domain':
                user_settings.rocket_domain = value
            elif field == 'user_id':
                user_settings.rocket_user_id = value
            elif field == 'token':
                user_settings.rocket_token = value
            session.add(user_settings)
    

    @staticmethod
    def check_settings_rocket(user_settings: UserSettings) -> bool:
        headers = {
            'X-Auth-Token': user_settings.rocket_token,
            'X-User-Id': user_settings.rocket_user_id
        }
        domain = user_settings.rocket_domain

        try:
            response = r.get('https://' + domain + '/api/v1/users.getStatus', headers=headers)
            response_status = response.status_code

            if response_status == 200:
                return True
        except Exception:
            return False

        return False
    

    @staticmethod
    def get_settings_state_back_callback(state: str) -> InlineKeyboardMarkup:
        return settings_callback.get_state_back_inline(state)
    

    @staticmethod
    def update_language(language: str, user_settings: UserSettings) -> UserSettings:
        if language not in get_available_languages().keys():
            return None

        with Session(engine, expire_on_commit=False) as session, session.begin():
            user_settings.language = language
            session.add(user_settings)
        
        translations.set_translation(user_settings.language)
        return user_settings
