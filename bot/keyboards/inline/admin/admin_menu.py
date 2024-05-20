from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

keyboard = InlineKeyboardBuilder()
btn_sender = InlineKeyboardButton(
    text="Сделать рассылку",
    callback_data="sender"
)
btn_change_first = InlineKeyboardButton(
    text="Поменять 1-й кружок",
    callback_data="change_first"
)
btn_change_second = InlineKeyboardButton(
    text="Поменять второе сообщение",
    callback_data="change_second"
)
btn_change_third = InlineKeyboardButton(
    text="Поменять третье сообщение",
    callback_data="change_third"
)
keyboard.row(btn_sender)
keyboard.row(btn_change_first)
keyboard.row(btn_change_second)
keyboard.row(btn_change_third)
