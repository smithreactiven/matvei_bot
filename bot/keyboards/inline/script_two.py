from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

keyboard = InlineKeyboardBuilder()
btn_script = InlineKeyboardButton(
    text="Далее",
    callback_data="script_three"
)
keyboard.row(btn_script)
