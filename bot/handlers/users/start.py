from aiogram import types, Dispatcher
from aiogram.filters import CommandStart, Command
from bot import keyboards
import tools


async def start_handler(message: types.Message):
    name = message.from_user.first_name
    msg_text = await tools.filer.read_txt("start")
    await message.answer(
        text=msg_text.format(name),
        reply_markup=None
    )


def setup(dp: Dispatcher):
    dp.message.register(start_handler, CommandStart())
