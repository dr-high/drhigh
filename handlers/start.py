from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart

async def cmd_start(message: types.Message):
    await message.reply("Welcome to the shop bot! Use /cart to view your cart.")

def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, CommandStart())
