from aiogram.dispatcher.filters.state import State, StatesGroup

class RocketForm(StatesGroup):
    domain = State()
    user_id = State()
    token = State()
