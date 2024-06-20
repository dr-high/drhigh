import sqlite3

def create_db():
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products
                      (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS cart
                      (user_id INTEGER, product_id INTEGER, quantity INTEGER)''')
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect('shop.db')
    return conn
