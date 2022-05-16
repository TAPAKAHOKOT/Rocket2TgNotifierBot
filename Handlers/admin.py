from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import types

from Settings import settings
from Configs import translations
from States import WriteToAllUsersForm
from Filters import IsAdminFilter
from Services import WriteToAllUsersService



@settings.dp.message_handler(IsAdminFilter(), Text(equals=translations.get_in_all_languages('keyboards.buttons.write-to-all-users')))
async def write_to_all_users_message(message: types.Message):
    await WriteToAllUsersForm.write_to_all_users.set()
    await message.answer(translations.get('keyboards.answers.write-to-all-users'))


@settings.dp.message_handler(IsAdminFilter(), state=WriteToAllUsersForm.write_to_all_users)
async def write_to_all_users_message(message: types.Message, state: FSMContext):
    await state.finish()
    
    await WriteToAllUsersService.write_to_all_users(message.text)

    await message.answer(translations.get('keyboards.answers.writed-to-all-users'))