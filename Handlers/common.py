from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import types

from Settings import settings
from Configs import translations
from States import WriteToDevForm
from Services import (
    WriteToDevService,
    UserRoomListService
)
from Tables import (
    User,
    UserSettings
)
from Enums import UserRoomsListTypesEnum
from Callbacks import user_rooms_list_callback

# <<<<<<<<<<<<<<<<<< Write to dev handler >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(Text(equals=translations.get_in_all_languages('keyboards.buttons.write-to-dev')))
async def write_to_dev_message(message: types.Message):
    await WriteToDevForm.white_to_dev.set()
    await message.answer(translations.get('keyboards.answers.write-to-dev'))


# <<<<<<<<<<<<<<<<<< Write to dev handler >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(state=WriteToDevForm.white_to_dev)
async def write_to_dev_message(message: types.Message, state: FSMContext):
    await WriteToDevService.write_to_dev(message['from']['username'], message.text)
    await state.finish()
    await message.answer(translations.get('keyboards.answers.writed-to-dev'))


# <<<<<<<<<<<<<<<<<< Black list >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(Text(equals=translations.get_in_all_languages('keyboards.buttons.black-list')))
async def black_list(message: types.Message, user: User, user_settings: UserSettings):
    callback = UserRoomListService.get_list_callback(user, user_settings, UserRoomsListTypesEnum.BLACK.name)
    await message.answer(translations.get('callbacks.default.black-list'), reply_markup=callback)


# <<<<<<<<<<<<<<<<<< Black list callback add >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(user_rooms_list_callback.list_inline_data.filter(type=UserRoomsListTypesEnum.BLACK.name, turned_on=str(False)))
async def black_list(call: types.CallbackQuery, callback_data: dict, user: User, user_settings: UserSettings):
    UserRoomListService.add_to_list(user, UserRoomsListTypesEnum.BLACK.name, callback_data.get('rid'))
    callback = UserRoomListService.get_list_callback(user, user_settings, UserRoomsListTypesEnum.BLACK.name)
    await call.message.edit_text(translations.get('callbacks.default.black-list'), reply_markup=callback)


# <<<<<<<<<<<<<<<<<< Black list callback delete >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(user_rooms_list_callback.list_inline_data.filter(type=UserRoomsListTypesEnum.BLACK.name, turned_on=str(True)))
async def black_list(call: types.CallbackQuery, callback_data: dict, user: User, user_settings: UserSettings):
    UserRoomListService.remove_from_list(UserRoomsListTypesEnum.BLACK.name, callback_data.get('rid'))
    callback = UserRoomListService.get_list_callback(user, user_settings, UserRoomsListTypesEnum.BLACK.name)
    await call.message.edit_text(translations.get('callbacks.default.black-list'), reply_markup=callback)


# <<<<<<<<<<<<<<<<<< Any message >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler()
async def any_message(message: types.Message):
    await message.answer(translations.get('answers.dont-understand'))
