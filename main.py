import logging
from aiogram import executor
from Settings import settings

from Handlers import *
from Middlewares import (
    LoggingMiddleware,
    SetupRoleMiddleware,
    UserMiddleware
)
from Filters import RolesFilter

async def on_startup(x):
    logging.info('Bot started')

async def on_shutdown(x):
    logging.info('Bot finished')

def setup_middlewares():
    settings.dp.middleware.setup(LoggingMiddleware())
    settings.dp.middleware.setup(UserMiddleware())
    settings.dp.middleware.setup(SetupRoleMiddleware())

def bind_filters():
    settings.dp.filters_factory.bind(RolesFilter)

def start_polling():
    setup_middlewares()
    executor.start_polling(settings.dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
    logging.info('Script finished')

if __name__ == '__main__':
    start_polling()