from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from datetime import datetime
import logging

class LoggingMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: Message, data: dict):
        logging.info(f'Message: {message}\ttime: {datetime.now()}')
    
    async def on_process_callback_query(self, message: Message, data: dict):
        await self.on_pre_process_message(message, data)