from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

keyboard = InlineKeyboardBuilder()
btn_start = InlineKeyboardButton(
    text="Да", callback_data="accept"
)
btn_cancel = InlineKeyboardButton(
    text="Отмена", callback_data="cancel"
)
keyboard.row(btn_start)
keyboard.row(btn_cancel)
