from aiogram.dispatcher.filters.state import State, StatesGroup
API_KEY = ''

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()
