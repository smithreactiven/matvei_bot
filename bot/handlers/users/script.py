from aiogram import types, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from sqlalchemy import select

from bot import keyboards, models
import tools


async def message_two_handler(callback: types.CallbackQuery, session):
    await callback.answer()
    async with session() as open_session:
        result = await open_session.execute(select(models.sql.Message))
        this_message = result.scalars().first()
        msg_text = this_message.second_message
        await callback.message.answer(
            text=msg_text,
            reply_markup=keyboards.inline.script_two.keyboard.as_markup()
        )


async def message_three_handler(callback: types.CallbackQuery, session):
    await callback.answer()
    async with session() as open_session:
        result = await open_session.execute(select(models.sql.Message))
        this_message = result.scalars().first()
        msg_text = this_message.third_message
        await callback.message.answer(
            text=msg_text,
            reply_markup=None
        )


def setup(dp: Dispatcher):
    dp.callback_query.register(
        message_two_handler,
        F.data == keyboards.inline.start.btn_start.callback_data
    )
    dp.callback_query.register(
        message_three_handler,
        F.data == keyboards.inline.script_two.btn_script.callback_data
    )
