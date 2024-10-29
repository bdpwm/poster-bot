import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.types import Message
from create_bot import bot, admins
from keyboards.kbs import main_kb, admin_panel_kb
from aiogram.utils.chat_action import ChatActionSender

admin_router = Router()


@admin_router.message((F.text.endswith('Admin panel')) & (F.from_user.id.in_(admins)))
async def admin_panel(message: Message):
    async with ChatActionSender.typing(bot=bot, chat_id=message.from_user.id):
        response_text = "admin panel"
        await message.answer(text=response_text, reply_markup=admin_panel_kb())