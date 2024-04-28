import sqlite3

db_connect = sqlite3.connect('NevelUZData.sqlite3')

db_cursor = db_connect.cursor()


def create_table_category():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS category(
        id INTEGER PRIMARY KEY,
        title TEXT
        )
    """)


def create_table_parent():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS parent(
        id INTEGER PRIMARY KEY,
        title TEXT,
        category_id INTEGER
        )
""")


def create_table_child():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS child(
        id INTEGER PRIMARY KEY,
        parent_id INTEGER)
    """)


def create_table_products():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY,
        title TEXT,
        child_id INTEGER
    )
    """)


def create_basket_table():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS basket (
        id INTEGER PRIMARY KEY, title TEXT, price INTEGER, quantity INTEGER)
    """)
    db_connect.commit()


async def db_insert_basket(title):
    db_cursor.execute("""
            INSERT INTO product (title)
            VALUES(?)""", title)
    db_connect.commit()


def create_favorites_table():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
        id INTEGER PRIMARY KEY, title TEXT, price INTEGER, quantity INTEGER)
    """)
    db_connect.commit()


create_favorites_table()
create_basket_table()
