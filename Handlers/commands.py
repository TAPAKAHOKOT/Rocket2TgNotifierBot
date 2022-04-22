from aiogram import types
from Filters.RolesFilter import RolesFilter

from Settings import settings
from Configs import translations
from Services import (
    SettingsService
)
from Keyboards import commands_keyboards
from Filters import RolesFilter


# <<<<<<<<<<<<<<<<<< Command /start >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    keyboard = commands_keyboards.start
    await message.answer(
        translations.get('commands.answers.start').format(
            user_name=message['from']['first_name'], 
            bot_name=(await settings.bot.get_me()).first_name
        ),
        reply_markup=keyboard
    )


# <<<<<<<<<<<<<<<<<< Command /settings >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["settings"])
async def command_settings(message: types.Message):
    inline = SettingsService.get_settings_main_callback()
    await message.answer(translations.get('commands.answers.settings'), reply_markup=inline)


# <<<<<<<<<<<<<<<<<< Command /help >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["help"])
async def command_help(message: types.Message):
    await message.answer(translations.get('commands.answers.help'))


# <<<<<<<<<<<<<<<<<< Command /admin >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(RolesFilter(), commands=["admin"])
async def command_admin(message: types.Message, is_root, is_admin):
    answer_message = translations.get('commands.answers.role.root') if is_root else (
        translations.get('commands.answers.role.admin') if is_admin else (
            translations.get('commands.answers.role.user')
        )
    )
    await message.answer(answer_message)
