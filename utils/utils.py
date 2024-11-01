import pytz
from datetime import datetime
from aiogram import Bot

def get_now_time():
    now = datetime.now(pytz.timezone('Europe/Bratislava'))
    return now.replace(tzinfo=None)


async def get_username_by_id(user_id: int, bot: Bot):
    try:
        user = await bot.get_chat(user_id)
        return user.username
    except Exception as e:
        print(f"Error getting username for user_id {user_id}: {e}")
        return None