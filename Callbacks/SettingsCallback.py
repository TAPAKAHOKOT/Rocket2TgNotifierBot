from this import s
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from Configs import translations, get_available_languages

class SettingsCallback:
    def __init__(self):
        self.generate_settings_inline_data()
        self.generate_menu_inline_data()
        self.generate_state_back_inline_data()

    
    def generate_menu_inline_data(self):
        self.menu_inline_data = CallbackData("button", "value")
    

    def generate_settings_inline_data(self):
        self.settings_inline_data = CallbackData("button", "settings", "value")
    

    def generate_state_back_inline_data(self):
        self.state_back_inline_data = CallbackData("button", "state")

    
    def get_main_inline(self) -> InlineKeyboardMarkup:
        main_inline = InlineKeyboardMarkup(row_width=2)

        menu = {
            'language': 'callbacks.keyboards.settings.language',
            'rocket': 'callbacks.keyboards.settings.rocket'
        }

        for menu_key, menu_value in menu.items():
            main_inline.insert(
                    InlineKeyboardButton(
                        text=translations.get(menu_value), 
                        callback_data=self.menu_inline_data.new(
                            value=menu_key
                        )
                    )
                )
        return main_inline

    
    def get_language_inline(self) -> InlineKeyboardMarkup:
        language_inline = InlineKeyboardMarkup(row_width=2)
        inline_bts = get_available_languages()
        inline_bts['back'] = translations.get('callbacks.default.back')

        for key, value in inline_bts.items():
            language_inline.insert(
                    InlineKeyboardButton(
                    text=value, 
                    callback_data=self.settings_inline_data.new(
                        settings='language',
                        value=key
                    )
                )
            )
        return language_inline

    
    def get_rocket_inline(self) -> InlineKeyboardMarkup:
        rocket_inline = InlineKeyboardMarkup(row_width=2)
        inline_bts = {
            'domain': translations.get('callbacks.settings.rocket.domain'),
            'user_id': translations.get('callbacks.settings.rocket.user-id'),
            'token': translations.get('callbacks.settings.rocket.token'),
            'back': translations.get('callbacks.default.back'),
            'check-settings': translations.get('callbacks.default.check-settings'),
            'instruction': translations.get('callbacks.default.instruction')
        }

        for key, value in inline_bts.items():
            rocket_inline.insert(
                    InlineKeyboardButton(
                    text=value, 
                    callback_data=self.settings_inline_data.new(
                        settings='rocket',
                        value=key
                    )
                )
            )
        return rocket_inline


    def get_state_back_inline(self, state: str) -> InlineKeyboardMarkup:
        state_back_inline = InlineKeyboardMarkup(row_width=1)
        state_back_inline.insert(
                InlineKeyboardButton(
                text=translations.get('callbacks.default.cancel'), 
                callback_data=self.state_back_inline_data.new(
                    state=state
                )
            )
        )
        return state_back_inline