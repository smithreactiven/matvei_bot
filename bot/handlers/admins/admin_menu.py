from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot import keyboards, filters
import typing
from aiogram import types, Dispatcher, F
from aiogram.filters import Command
from sqlalchemy import select
from bot import models, config


async def admin_menu_handler(message: Message, state: FSMContext, session):
    await state.clear()
    # async with session() as open_session:
    #     users: typing.List[int] = await open_session.execute(select(models.sql.User.id))
    #     users_id = users.scalars().all()
    msg_text = (f"Меню администратора. \r\n\r\n"
                f"Всего пользователей - \r\n")
    await message.answer(
        text=msg_text,
        reply_markup=keyboards.inline.admin.admin_menu.keyboard.as_markup()
    )


def setup(dp: Dispatcher):
    dp.message.register(admin_menu_handler, Command(commands='admin'), F.chat.id.in_(config.BOT_ADMINS))