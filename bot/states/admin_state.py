from aiogram.fsm.state import StatesGroup, State


class BroadcastStates(StatesGroup):
    pre_broadcast = State()
    broadcast = State()
