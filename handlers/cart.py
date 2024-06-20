from aiogram import Dispatcher, types
from utils.database import get_db_connection

async def cmd_cart(message: types.Message):
    user_id = message.from_user.id
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT product_id, quantity FROM cart WHERE user_id = ?', (user_id,))
    cart_items = cursor.fetchall()
    response = "Your cart:\n"
    for item in cart_items:
        cursor.execute('SELECT name, price FROM products WHERE id = ?', (item[0],))
        product = cursor.fetchone()
        response += f"{product[0]} - {item[1]} pcs - ${product[1] * item[1]}\n"
    await message.reply(response)
    conn.close()

def register_handlers_cart(dp: Dispatcher):
    dp.register_message_handler(cmd_cart, commands=['cart'])
