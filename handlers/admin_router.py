import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.types import Message
from aiogram.types import FSInputFile
from create_bot import bot, admins
from keyboards.kbs import main_kb, admin_panel_kb, sug_posts_kb
from db_handlers.db import get_post, count_posts, delete_post
from utils.utils import get_username_by_id, accept_post
from aiogram.utils.chat_action import ChatActionSender
from dotenv import set_key


admin_router = Router()


@admin_router.message((F.text.endswith('Admin panel')) & (F.from_user.id.in_(admins)))
async def admin_panel(message: Message):
    async with ChatActionSender.typing(bot=bot, chat_id=message.from_user.id):
        posts_count = await count_posts()
        response_text = ( 
            f"🔔 Welcome to Admin panel\n"
            f"📩 Posts suggested: {posts_count}"
            
        )
        await message.answer(text=response_text, reply_markup=admin_panel_kb())

@admin_router.message((F.text.endswith('Suggested Posts')) & (F.from_user.id.in_(admins)))
async def suggested_posts(message: Message):
    async with ChatActionSender.typing(bot=bot, chat_id=message.from_user.id):
        post = await get_post()
        user_username = await get_username_by_id(post.user_id, bot)
        if post:
            if post.photo_path:
                response_text = (
                    f"👤 Suggested by @{user_username}\n"
                    f"🕰️ Suggested time: {post.created_at}\n"
                    f"⭕ Status: {post.content}\n"
                )
                await message.answer(text=response_text)
                photo = FSInputFile(post.photo_path)
                await message.answer_photo(photo=photo, caption=post.content, reply_markup=sug_posts_kb(post.id))
            else:
                await message.answer(text=post.content, reply_markup=sug_posts_kb(post.id))
        else:
            response_text = "No available posts."
            await message.answer(text=response_text, reply_markup=sug_posts_kb(0))



@admin_router.message((F.text.startswith('✅ Accept ')) & (F.from_user.id.in_(admins)))
async def accept(message: Message):
    try:
        post_id = int(message.text.split(' ')[-1])
        await accept_post(post_id)
        await delete_post(post_id)
        await message.answer("Post has been accepted.")
    except ValueError:
        await message.answer("Invalid post ID.")


@admin_router.message((F.text.startswith('❌ Decline ')) & (F.from_user.id.in_(admins)))
async def decline(message: Message):
    try:
        post_id = int(message.text.split(' ')[-1])
        await delete_post(post_id)
        await message.answer("Post has been declined.")
    except ValueError:
        await message.answer("Invalid post ID.")




@admin_router.message((F.text.endswith('Add another admin')) & (F.from_user.id.in_(admins)))
async def add_admin(message: Message):
    await message.answer("Please reply with the ID of the new admin.")

@admin_router.message(F.from_user.id.in_(admins) & F.reply_to_message)
async def add_admin_id(message: Message):
    pass

