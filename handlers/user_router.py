import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.types import Message
from create_bot import bot, channel_id, bot_username
from keyboards.kbs import main_kb
from aiogram.utils.chat_action import ChatActionSender

user_router = Router()


@user_router.message(CommandStart())
async def start_handler(message: Message, command: CommandObject):
    response_text = (
        "👋 Hello! I'm a bot here to help you with submissions for our news channel.\n\n"
        "📝 You can send your news, and our administrators will review it. "
        "Once your message is approved, it will be published in the channel!\n\n"
        "📢 To get started, just press button below!"
    )
    await message.answer(text=response_text, reply_markup=main_kb(message.from_user.id))


@user_router.message(Command('post'))
@user_router.message(F.text.contains('Suggest post'))
async def post_handler(message: Message):
    async with ChatActionSender.typing(bot=bot, chat_id=message.from_user.id):
        text = (f"Test, {message.from_user.full_name}!")
    await message.answer(text, reply_markup=main_kb(message.from_user.id))