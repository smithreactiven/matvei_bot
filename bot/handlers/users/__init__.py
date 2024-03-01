from aiogram import Dispatcher
from . import start


def setup(dp: Dispatcher):
    for module in (
            start,
    ):
        module.setup(dp)
