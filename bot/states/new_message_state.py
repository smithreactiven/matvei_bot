from aiogram.fsm.state import StatesGroup, State


class MessageStates(StatesGroup):
    get_type = State()
    get_message = State()
