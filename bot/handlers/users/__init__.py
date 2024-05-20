from aiogram import Dispatcher
from . import start
from . import script


def setup(dp: Dispatcher):
    for module in (
            start, script
    ):
        module.setup(dp)
