from . import admin_menu
from . import broadcast
from . import edit_message
from . import export
from aiogram import Dispatcher


def setup(dp: Dispatcher):
    for module in (
            admin_menu, broadcast, edit_message, export
    ):
        module.setup(dp)
