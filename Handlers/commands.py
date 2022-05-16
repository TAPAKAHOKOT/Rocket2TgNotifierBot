from aiogram import types
from Filters.RolesFilter import RolesFilter

from Settings import settings
from Configs import translations
from Services import (
    SettingsService
)
from Keyboards import commands_keyboards
from Filters import (
    IsAdminFilter,
    RolesFilter
)


# <<<<<<<<<<<<<<<<<< Command /start >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(RolesFilter(), commands=["start"])
async def command_start(message: types.Message, is_root, is_admin):
    keyboard = commands_keyboards.get_start_keyboard(is_root, is_admin)
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
@settings.dp.message_handler(IsAdminFilter(), commands=["admin"])
async def command_admin(message: types.Message):
    answer_message = translations.get('commands.answers.role.admin')
    keyboard = commands_keyboards.get_admin_keyboard()

    await message.answer(answer_message, reply_markup=keyboard)


# # <<<<<<<<<<<<<<<<<< Command /admin >>>>>>>>>>>>>>>>>>
# @settings.dp.message_handler(RolesFilter(), is_admin=True, commands=["admin"])
# async def command_admin(message: types.Message, is_root, is_admin):
#     answer_message = translations.get('commands.answers.role.root') if is_root else (
#         translations.get('commands.answers.role.admin') if is_admin else (
#             translations.get('commands.answers.role.user')
#         )
#     )

#     keyboard = commands_keyboards.get_root_keyboard() if is_root else (
#         commands_keyboards.get_admin_keyboard() if is_admin else None
#     )
#     await message.answer(answer_message, reply_markup=keyboard)