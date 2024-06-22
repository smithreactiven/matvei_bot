from aiogram import types, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
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

        keyboard = InlineKeyboardBuilder()

        btn = InlineKeyboardButton(
            text="Подробнее",
            callback_data="forty_message"
        )

        keyboard.row(btn)
        await callback.message.answer(
            text=msg_text,
            reply_markup=keyboard.as_markup()
        )


async def forty_message_handler(callback: types.CallbackQuery, session):
    await callback.answer()
    async with session() as open_session:
        result = await open_session.execute(select(models.sql.Message))
        this_message = result.scalars().first()
        msg_text = this_message.forty_message

        await callback.message.answer(
            text=msg_text
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
    dp.callback_query.register(
        forty_message_handler,
        F.data == "forty_message"
    )
