from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram import types

from Settings import settings
from Configs import translations
from Services import SettingsService
from Callbacks import settings_callback
from Keyboards import example_keyboard

from Tables import UserSettings, user_settings
from States import RocketForm


@settings.dp.callback_query_handler(settings_callback.menu_inline_data.filter(value='language'))
async def settings_callback_language(call: types.CallbackQuery):
    inline = SettingsService.get_settings_languages_callback()
    await call.message.edit_text(
        translations.get('callbacks.answers.choose-language'), 
        reply_markup=inline
    )


@settings.dp.callback_query_handler(settings_callback.menu_inline_data.filter(value='rocket'))
async def settings_callback_language(call: types.CallbackQuery, user_settings: UserSettings):
    inline = SettingsService.get_settings_rocket_callback()
    await call.message.edit_text(
        translations.get('callbacks.answers.choose-rocket-setting').format(
            domain=user_settings.rocket_domain,
            user_id=user_settings.rocket_user_id,
            token=user_settings.rocket_token
        ), 
        reply_markup=inline
    )


@settings.dp.callback_query_handler(settings_callback.settings_inline_data.filter(value='back'))
async def settings_callback_language_callback(call: types.CallbackQuery):
    inline = SettingsService.get_settings_main_callback()
    await call.message.edit_text(translations.get('commands.answers.settings'), reply_markup=inline)


@settings.dp.callback_query_handler(settings_callback.settings_inline_data.filter(settings='language'))
async def settings_callback_language_callback(call: types.CallbackQuery, callback_data: dict, user_settings: UserSettings):
    user_settings = SettingsService.update_language(callback_data['value'], user_settings)

    await call.message.answer(
        translations.get('callbacks.answers.language-updated-to').format(language=user_settings.language if user_settings else None),
        reply_markup=example_keyboard.get_main_keyboard()
    )


@settings.dp.callback_query_handler(settings_callback.settings_inline_data.filter(settings='rocket', value=['domain', 'user_id', 'token']))
async def settings_callback_language_callback(call: types.CallbackQuery, callback_data: dict):
    value = callback_data['value']
    state_back = SettingsService.get_settings_state_back_callback(value)

    if value == 'domain':
        await RocketForm.domain.set()
    elif value == 'user_id':
        await RocketForm.user_id.set()
    elif value == 'token':
        await RocketForm.token.set()

    await call.message.edit_text(
        translations.get('callbacks.state-back.rocket-form').format(value=callback_data['value']),
        reply_markup=state_back
    )


@settings.dp.callback_query_handler(settings_callback.settings_inline_data.filter(settings='rocket', value='check-settings'))
async def settings_callback_language_callback(call: types.CallbackQuery, user_settings: UserSettings):
    check_result = SettingsService.check_settings_rocket(user_settings)

    await call.message.answer(
        translations.get('callbacks.default.check-settings-status').format(status='✅' if check_result else '❌')
    )


@settings.dp.callback_query_handler(settings_callback.state_back_inline_data.filter(state='domain'))
async def settings_callback_language_callback(call: types.CallbackQuery, state: FSMContext):
    state.finish()
    inline = SettingsService.get_settings_rocket_callback()
    await call.message.edit_text(
        translations.get('callbacks.answers.choose-rocket-setting').format(
            domain=user_settings.rocket_domain,
            user_id=user_settings.rocket_user_id,
            token=user_settings.rocket_token
        ), 
        reply_markup=inline
    )


@settings.dp.message_handler(state=RocketForm.domain)
async def rocket_form_handler(message: types.Message, state: FSMContext, user_settings: UserSettings):
    print('\n\nstate=', RocketForm.domain == state.get_state(), '\n\n')
    await state.finish()
    SettingsService.set_settings_rocket_domain(user_settings, message.text)

    inline = SettingsService.get_settings_rocket_callback()
    await message.answer(
        translations.get('callbacks.answers.choose-rocket-setting').format(
            domain=user_settings.rocket_domain,
            user_id=user_settings.rocket_user_id,
            token=user_settings.rocket_token
        ),
        reply_markup=inline
    )


@settings.dp.message_handler(state=RocketForm.user_id)
async def rocket_form_handler(message: types.Message, state: FSMContext, user_settings: UserSettings):
    await state.finish()
    SettingsService.set_settings_rocket_user_id(user_settings, message.text)

    inline = SettingsService.get_settings_rocket_callback()
    await message.answer(
        translations.get('callbacks.answers.choose-rocket-setting').format(
            domain=user_settings.rocket_domain,
            user_id=user_settings.rocket_user_id,
            token=user_settings.rocket_token
        ), 
        reply_markup=inline
    )


@settings.dp.message_handler(state=RocketForm.token)
async def rocket_form_handler(message: types.Message, state: FSMContext, user_settings: UserSettings):
    await state.finish()
    SettingsService.set_settings_rocket_token(user_settings, message.text)

    inline = SettingsService.get_settings_rocket_callback()
    await message.answer(
        translations.get('callbacks.answers.choose-rocket-setting').format(
            domain=user_settings.rocket_domain,
            user_id=user_settings.rocket_user_id,
            token=user_settings.rocket_token
        ), 
        reply_markup=inline
    )