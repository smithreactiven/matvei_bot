from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

keyboard = InlineKeyboardBuilder()
btn_sender = InlineKeyboardButton(
    text="Сделать рассылку",
    callback_data="sender"
)
btn_export = InlineKeyboardButton(
    text="Экспорт",
    callback_data="export"
)
keyboard.row(btn_sender)
keyboard.row(btn_export)
