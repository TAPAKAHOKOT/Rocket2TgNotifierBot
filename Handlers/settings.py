from email import message
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram import types

import sys

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

    if value == 'domain':
        state = RocketForm.domain
    elif value == 'user_id':
        state = RocketForm.user_id
    elif value == 'token':
        state = RocketForm.token
    
    await state.set()

    state = Dispatcher.get_current().current_state()
    await state.update_data({
        'message_id': call.message.message_id,
        'state_name': value
    })

    state_back = SettingsService.get_settings_state_back_callback(value)
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


@settings.dp.callback_query_handler(settings_callback.settings_inline_data.filter(settings='rocket', value='instruction'))
async def settings_callback_language_callback(call: types.CallbackQuery, user_settings: UserSettings):
    
    root_path = sys.path[0]
    images = {
        '1': root_path + '/Files/Help/Images/1.png',
        '2': root_path + '/Files/Help/Images/2.png',
        '3': root_path + '/Files/Help/Images/3.png',
        '4': root_path + '/Files/Help/Images/4.png',
        '5': root_path + '/Files/Help/Images/5.png',
        '6': root_path + '/Files/Help/Images/6.png'
    }

    await call.message.answer(translations.get('callbacks.settings.rocket.instruction.1'))
    await call.message.answer_photo(photo=open(images['1'], 'rb'))

    await call.message.answer(translations.get('callbacks.settings.rocket.instruction.2'))
    await call.message.answer_photo(photo=open(images['2'], 'rb'))

    await call.message.answer(translations.get('callbacks.settings.rocket.instruction.3'))
    await call.message.answer_photo(photo=open(images['3'], 'rb'))

    await call.message.answer(translations.get('callbacks.settings.rocket.instruction.4'))
    await call.message.answer_photo(photo=open(images['4'], 'rb'))

    await call.message.answer(translations.get('callbacks.settings.rocket.instruction.5'))
    await call.message.answer_photo(photo=open(images['5'], 'rb'))

    await call.message.answer(translations.get('callbacks.settings.rocket.instruction.6'))
    await call.message.answer_photo(photo=open(images['6'], 'rb'))

    await call.message.answer(translations.get('callbacks.settings.rocket.instruction.7'))


@settings.dp.callback_query_handler(settings_callback.state_back_inline_data.filter(), state='*')
async def settings_callback_language_callback(call: types.CallbackQuery, state: FSMContext, user_settings: UserSettings):
    await state.finish()
    inline = SettingsService.get_settings_rocket_callback()
    await call.message.edit_text(
        translations.get('callbacks.answers.choose-rocket-setting').format(
            domain=user_settings.rocket_domain,
            user_id=user_settings.rocket_user_id,
            token=user_settings.rocket_token
        ), 
        reply_markup=inline
    )


@settings.dp.message_handler(state='*')
async def rocket_form_handler(message: types.Message, state: FSMContext, user_settings: UserSettings):
    data = await state.get_data()

    message_id = data.get('message_id')
    state_name = data.get('state_name')

    await settings.bot.delete_message(
        message.chat.id,
        message_id
    )
    await state.finish()

    SettingsService.set_settings_rocket(user_settings, state_name, message.text)

    inline = SettingsService.get_settings_rocket_callback()
    await message.answer(
        translations.get('callbacks.answers.choose-rocket-setting').format(
            domain=user_settings.rocket_domain,
            user_id=user_settings.rocket_user_id,
            token=user_settings.rocket_token
        ),
        reply_markup=inline
    )