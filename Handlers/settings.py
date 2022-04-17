from aiogram import types

from Settings import settings
from Configs import translations
from Services import SettingsService
from Callbacks import settings_callback
from Keyboards import example_keyboard

from Tables import UserSettings


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
async def settings_callback_language_callback(call: types.CallbackQuery, callback_data: dict, user_settings: UserSettings):
    user_settings = SettingsService.update_language(callback_data['value'], user_settings)

    await call.message.answer(
        translations.get('callbacks.answers.language-updated-to').format(language=user_settings.language if user_settings else None),
        reply_markup=example_keyboard.get_main_keyboard()
    )