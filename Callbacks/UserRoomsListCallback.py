from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

class UserRommsListCallback:
    def __init__(self):
        self.generate_list_inline_data()

    
    def generate_list_inline_data(self):
        self.list_inline_data = CallbackData("button", "type", "turned_on", "rid")

    
    def get_list_inline(self, buttons: list[dict]) -> InlineKeyboardMarkup:
        list_inline = InlineKeyboardMarkup(row_width=2)
        
        for btn in buttons:
            list_inline.insert(
                InlineKeyboardButton(
                        text=btn['name'] + ' ' + ('✅' if btn['turned_on'] else '❌'), 
                        callback_data=self.list_inline_data.new(
                            type=btn['type'],
                            turned_on=btn['turned_on'],
                            rid=btn['rid']
                        )
                    )
            )
        return list_inline