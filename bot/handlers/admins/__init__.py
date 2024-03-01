from . import admin_menu
from aiogram import Dispatcher


def setup(dp: Dispatcher):
    for module in (
            admin_menu,
    ):
        module.setup(dp)
