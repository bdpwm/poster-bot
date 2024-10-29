import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.types import Message
from create_bot import bot, channel_id, bot_username
from keyboards.kbs import main_kb
from aiogram.utils.chat_action import ChatActionSender

admin_router = Router()