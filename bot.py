import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
from utils.config import TOKEN

# Initialize bot and dispatcher
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

# Middlewares
dp.middleware.setup(LoggingMiddleware())

# Import handlers
from handlers import start, cart, payment, delivery

# Register handlers
start.register_handlers_start(dp)
cart.register_handlers_cart(dp)
payment.register_handlers_payment(dp)
delivery.register_handlers_delivery(dp)

if __name__ == '__main__':
    from utils.database import create_db

    create_db()
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
