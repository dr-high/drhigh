from aiogram import Dispatcher, types

async def cmd_delivery(message: types.Message):
    await message.reply("Delivery information...")

def register_handlers_delivery(dp: Dispatcher):
    dp.register_message_handler(cmd_delivery, commands=['delivery'])
