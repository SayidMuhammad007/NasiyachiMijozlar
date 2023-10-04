from aiogram.dispatcher.filters.state import State, StatesGroup

class Currency(StatesGroup):
    name = State()
    value = State()