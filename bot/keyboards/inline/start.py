from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

keyboard = InlineKeyboardBuilder()
btn_start = InlineKeyboardButton(
    text="Хочу урок",
    callback_data="script_two"
)
keyboard.row(btn_start)
