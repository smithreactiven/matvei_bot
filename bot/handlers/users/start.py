from aiogram import types, Dispatcher
from aiogram.filters import CommandStart, Command
from sqlalchemy import select

from bot import keyboards, models
import tools


async def start_handler(message: types.Message, session):
    async with session() as open_session:
        user_in_db = await open_session.execute(select(models.sql.User).filter_by(id=message.from_user.id))
        user_in_db = user_in_db.scalars().first()
        if not user_in_db:
            new_user = models.sql.User(
                id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name
            )

            await open_session.merge(new_user)
            await open_session.commit()

        result = await open_session.execute(select(models.sql.Message))
        this_message = result.scalars().first()
        video_note = this_message.first_message

        await message.bot.send_video_note(
            video_note=video_note,
            reply_markup=keyboards.inline.start.keyboard.as_markup(),
            chat_id=message.from_user.id
        )


def setup(dp: Dispatcher):
    dp.message.register(start_handler, CommandStart())
