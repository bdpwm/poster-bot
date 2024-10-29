from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_kb(user_telegram_id: int):
    kb_list = [[KeyboardButton(text="Suggest post")]]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Suggest post"
    )