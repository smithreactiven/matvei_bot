from aiogram.fsm.context import FSMContext
from aiogram import types, Dispatcher, F
from aiogram.filters import Command
# from magic_filter import F as magic_filter
from bot import keyboards
import typing
from bot.services.broadcaster import BaseBroadcaster
from bot import models, filters, states
from sqlalchemy import select


async def broadcast_start_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(
        "[1/2] Пришлите мне сообщение:"
    )
    await state.set_state(states.admin_state.BroadcastStates.pre_broadcast)


async def getting_msg(message: types.Message, state: FSMContext):
    broadcaster = BaseBroadcaster(
        chats_id=[message.from_user.id],
        message=message,
        disable_web_page_preview=True
    )

    await broadcaster.run()
    await message.answer(
        "[2/2] Начать рассылку?",
        reply_markup=keyboards.inline.admin.admin_broadcast.keyboard.as_markup(),
    )
    await state.update_data(dict(message=message))
    await state.set_state(states.admin_state.BroadcastStates.broadcast)


async def start_broadcast(callback: types.CallbackQuery, state: FSMContext, session):
    state_data = await state.get_data()
    message: types.Message = state_data.get("message")

    await state.clear()
    await callback.answer()

    if callback.data == "cancel":
        return await callback.message.answer("Рассылка отменена.")

    async with session() as open_session:
        users: typing.List[int] = await open_session.execute(select(models.sql.User.id))
        users = users.scalars().all()

    await callback.message.answer("Рассылка началась.")

    broadcaster = BaseBroadcaster(chats_id=users, message=message)
    success_count = await broadcaster.run()
    await callback.message.answer(
        "Рассылка успешно выполнена.\n"
        "Отправлено: {} из {}".format(success_count, len(users))
    )


def setup(dp: Dispatcher):
    dp.callback_query.register(
        broadcast_start_handler,
        F.data == 'sender'
    )
    dp.message.register(
        getting_msg,
        states.admin_state.BroadcastStates.pre_broadcast
    )
    dp.callback_query.register(
        start_broadcast,
        states.admin_state.BroadcastStates.broadcast,
    )
