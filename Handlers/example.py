from aiogram import types
from aiogram.dispatcher.filters import Text

from Settings import settings
from Configs import translations
from Services import SettingsService
from Callbacks import settings_callback, example_callback
from Keyboards import example_keyboard


# <<<<<<<<<<<<<<<<<< Callback action with [filtering by type=language] >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(settings_callback.main_inline_data.filter(value='language'))
async def settings_callback_language(call: types.CallbackQuery, callback_data: dict):
    inline = SettingsService.get_settings_languages_callback()
    await call.message.edit_text(
        translations.get('callbacks.answers.choose-language'), 
        reply_markup=inline
    )


# <<<<<<<<<<<<<<<<<< Callback action with [filtering by type=language] >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(settings_callback.language_inline_data.filter())
async def settings_callback_language_callback(call: types.CallbackQuery, callback_data: dict):
    SettingsService.update_language(callback_data['value'])
    await call.message.answer(
        translations.get('callbacks.answers.language-updated-to').format(language=callback_data['value'].title()),
        reply_markup=example_keyboard.get_main_keyboard()
    )


# <<<<<<<<<<<<<<<<<< Callback action with [filtering by type=number] >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(example_callback.example_inline_data.filter(type="number"))
async def callback_number_example(call: types.CallbackQuery, callback_data: dict):
    await call.message.edit_text(translations.get('callbacks.answers.number-value').format(value=callback_data['value']))


# <<<<<<<<<<<<<<<<<< Callback action with [filtering by type=letter] >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(example_callback.example_inline_data.filter(type="letter"))
async def callback_letter_example(call: types.CallbackQuery, callback_data: dict):
    await call.message.edit_text(translations.get('callbacks.answers.letter-value').format(value=callback_data['value']))


# <<<<<<<<<<<<<<<<<< Message with filters by many words >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(Text(equals=translations.get_in_all_languages('keyboards.buttons.hi')))
async def hello_message_example(message: types.Message):
    await message.answer(translations.get('keyboards.answers.hello'))


# <<<<<<<<<<<<<<<<<< Message with filters by one word >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(Text(equals=translations.get_in_all_languages('keyboards.buttons.joke')))
async def joke_message_example(message: types.Message):
    await message.answer(translations.get('keyboards.answers.joke'))


# <<<<<<<<<<<<<<<<<< Message with filters by one word >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(Text(equals=translations.get_in_all_languages('keyboards.buttons.another-keyboard')))
async def joke_message_example(message: types.Message):
    await message.answer(
        translations.get('keyboards.answers.another-keyboard'),
        reply_markup=example_keyboard.test
    )


# <<<<<<<<<<<<<<<<<< Any another message >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler()
async def any_message_handler_example(message: types.Message):
    await message.answer(translations.get('answers.dont-understand'))