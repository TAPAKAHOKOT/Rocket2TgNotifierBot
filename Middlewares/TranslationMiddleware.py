from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message

from Tables import (
    UserSettings
)
from Configs import translations

class TranslationMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: Message, data: dict):
        user_settings: UserSettings = data['user_settings']
        translations.set_translation(user_settings.language)
    
    async def on_process_callback_query(self, message: Message, data: dict):
        await self.on_pre_process_message(message, data)

        