from aiogram import types
from Filters.RolesFilter import RolesFilter

from Settings import settings
from Configs import translations
from Services import SettingsService, ExampleService
from Keyboards import example_keyboard
from Filters import RolesFilter


# <<<<<<<<<<<<<<<<<< Command [answering with keyboard] >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["start"])
async def command_start_example(message: types.Message):
    await message.answer(
        translations.get('commands.answers.start').format(
            user_name=message['from']['first_name'], 
            bot_name=(await settings.bot.get_me()).first_name
        ),
        reply_markup=example_keyboard.get_main_keyboard()
    )


# <<<<<<<<<<<<<<<<<< Command with callback >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["settings"])
async def command_help_example(message: types.Message):
    inline = SettingsService.get_settings_main_callback()
    await message.answer(translations.get('commands.answers.settings'), reply_markup=inline)


# <<<<<<<<<<<<<<<<<< Command with callback >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["help"])
async def command_help_example(message: types.Message):
    inline = ExampleService.get_example_inline_callback()
    await message.answer(translations.get('commands.answers.help'), reply_markup=inline)


# <<<<<<<<<<<<<<<<<< Command with callback >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(RolesFilter(), commands=["admin"])
async def command_admin_example(message: types.Message, is_root, is_admin):
    answer_message = translations.get('commands.answers.role.root') if is_root else (
        translations.get('commands.answers.role.admin') if is_admin else (
            translations.get('commands.answers.role.user')
        )
    )
    await message.answer(answer_message)