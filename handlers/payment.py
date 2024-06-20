from aiogram import Dispatcher, types

async def cmd_payment(message: types.Message):
    await message.reply("Payment processing...")

def register_handlers_payment(dp: Dispatcher):
    dp.register_message_handler(cmd_payment, commands=['pay'])
