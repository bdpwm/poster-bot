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

async def accept_post(post_id: int):
    from create_bot import channel_id, bot
    from db_handlers.db import get_post
    # ! fix local imports 
    post = await get_post()
    
    if post:
        if post.photo_path:
            await bot.send_photo(chat_id=channel_id, photo=post.photo_path, caption=post.content)
        else:
            await bot.send_message(chat_id=channel_id, text=post.content)
    else:
        raise ValueError("Post content not found.")