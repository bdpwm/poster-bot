import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.types import Message
from create_bot import bot, channel_id, bot_username
from keyboards.kbs import main_kb, skip_kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from db_handlers.db import save_post
from aiogram.utils.chat_action import ChatActionSender
from uuid import uuid4


class PostStates(StatesGroup):
    waiting_for_content = State()
    waiting_for_photo = State()


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
async def start_post_suggestion(message: Message, state: FSMContext):
    async with ChatActionSender.typing(bot=bot, chat_id=message.from_user.id):
        await message.answer("📄 Please enter the content of your post:")
    await state.set_state(PostStates.waiting_for_content)


@user_router.message(PostStates.waiting_for_content)
async def post_content(message: Message, state: FSMContext):
    post_content = message.text
    await state.update_data(content=post_content)


    await message.answer(
        "📷 Would you like to add a photo? Please send it, or press 'Skip' if not.",
        reply_markup=skip_kb()
    )
    await state.set_state(PostStates.waiting_for_photo)


@user_router.message(PostStates.waiting_for_photo, F.photo)
async def post_photo(message: Message, state: FSMContext):
    photo = message.photo[-1]
    file_info = await bot.get_file(photo.file_id)
    photo_path = f"photos/{photo.file_id}.jpg"

    await bot.download_file(file_info.file_path, photo_path)
    data = await state.get_data()
    post_content = data.get("content")

    await save_post(message.from_user.id, post_content, photo_path)

    await message.answer("✅ Thank you! Your post with photo has been submitted for review.", reply_markup=main_kb(message.from_user.id))
    await state.clear()


@user_router.message(PostStates.waiting_for_photo, Command("skip"))
@user_router.message(F.text.contains('Skip'))
async def skip_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    post_content = data['content']

    await save_post(message.from_user.id, post_content)
    await message.answer("✅ Thank you! Your post has been submitted for review.", reply_markup=main_kb(message.from_user.id))
    await state.clear()