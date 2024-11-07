from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from create_bot import admins

def main_kb(user_telegram_id: int):
    kb_list = [[KeyboardButton(text="Suggest post")]]
    if user_telegram_id in admins:
        kb_list.append([KeyboardButton(text="⚙️ Admin panel")])
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Suggest post"
    )

def skip_kb():
    kb_list = [[KeyboardButton(text="Skip")]]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
    )

def admin_panel_kb():
    kb_list = [
        [KeyboardButton(text="📢 Suggested Posts")],
        [KeyboardButton(text="🔧 Add another admin")],
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
    )

def sug_posts_kb(post_id: int):
    kb_list = [
        [KeyboardButton(text=f"✅ Accept {post_id}")],
        [KeyboardButton(text=f"❌ Decline {post_id}")],
        [KeyboardButton(text="⚒️ Change")],
        [KeyboardButton(text="⚙️ Admin panel")],
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
    )
