from aiogram import types
from Configs import translations

class CommandsKeyboards:
    def get_start_keyboard(self, is_root=False, is_admin=False) -> types.ReplyKeyboardMarkup:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        start.add(
            types.KeyboardButton(text='/start'), 
            types.KeyboardButton(text='/help'),
            types.KeyboardButton(text='/settings'),

            types.KeyboardButton(''),
            types.KeyboardButton(text=translations.get('keyboards.buttons.black-list')),
            types.KeyboardButton(''),

            types.KeyboardButton(''),
            types.KeyboardButton(text=translations.get('keyboards.buttons.write-to-dev')),
            types.KeyboardButton('')
        )

        if (is_admin or is_root):
            start.add(
                types.KeyboardButton(text='/admin')
            )

        return start
    

    def get_admin_keyboard(self) -> types.ReplyKeyboardMarkup:
        admin = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        admin.add(
            types.KeyboardButton(''),
            types.KeyboardButton('/start'),
            types.KeyboardButton(''),
            
            types.KeyboardButton(''),
            types.KeyboardButton(text=translations.get('keyboards.buttons.write-to-all-users')),
            types.KeyboardButton('')
        )
        return admin
    

    def get_root_keyboard(self) -> types.ReplyKeyboardMarkup:
        return self.get_admin_keyboard()
