from aiogram import types, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from sqlalchemy import select

from bot import keyboards, states, models, config
import tools


async def edit_start_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    message_model = config.MESSAGE_MODEL[callback.data]
    message_type = message_model['type']
    await state.update_data(message_type=message_type)
    msg_text = 'Пришли новое сообщение'
    await callback.message.answer(
        text=msg_text
    )
    await state.set_state(states.new_message_state.MessageStates.get_message)


async def edit_message_handler(message: types.Message, state: FSMContext, session):
    state_data = await state.get_data()
    message_type = state_data.get('message_type')
    print(message_type)
    async with session() as open_session:
        if message_type == 'Второе':
            result = await open_session.execute(select(models.sql.Message))
            update_message = result.scalars().first()
            update_message.second_message = message.text
            await open_session.commit()
            await message.answer('Второе сообщение успешно обновлено.')
        if message_type == 'Первое':
            video_id = message.video_note.file_id
            result = await open_session.execute(select(models.sql.Message))
            update_message = result.scalars().first()
            update_message.first_message = video_id
            await open_session.commit()
            await message.answer('Кружок успешно обновлен')
        if message_type == 'Третье':
            new_message = message.text
            result = await open_session.execute(select(models.sql.Message))
            update_message = result.scalars().first()
            update_message.third_message = new_message
            await open_session.commit()
            await message.answer('Третье сообщение успешно обновлено')
        if message_type == 'Четвертое':
            new_message = message.text
            result = await open_session.execute(select(models.sql.Message))
            update_message = result.scalars().first()
            update_message.forty_message = new_message
            await open_session.commit()
            await message.answer('Четвертое сообщение успешно обновлено')
    await state.clear()


def setup(dp: Dispatcher):
    dp.callback_query.register(
        edit_start_handler,
        states.new_message_state.MessageStates.get_type
    )
    dp.message.register(
        edit_message_handler,
        states.new_message_state.MessageStates.get_message
    )
