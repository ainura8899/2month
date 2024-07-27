import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(connection, sql):
    with sqlite3.connect(connection) as connect:
        try:
            cursor = connection.cursor()
            cursor.execute(sql)
        except sqlite3.Error as e:
            print(e)

def insert_products(connection, products):
    with sqlite3.connect(connection) as connect:
        try:
            sql = '''INSERT INTO products
            (product_title, price, quantity)
            VALUES (?, ?, ?)'''
            cursor = connection.cursor()
            cursor.execute(sql, products)
            connection.commit()
        except sqlite3.Error as e:
            print(e)

def update_products_quantity(connection, products):
    with sqlite3.connect(connection) as connect:
        try:
            sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, products)
            connection.commit()
        except sqlite3.Error as e:
            print(e)

def update_products_price(connection, products):
    with sqlite3.connect(connection) as connect:
        try:
            sql = '''UPDATE products SET price = ? WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, products)
            connection.commit()
        except sqlite3.Error as e:
            print(e)

def delete_products(connection, id):
    with sqlite3.connect(connection) as connect:
        try:
            sql = '''DELETE FROM employees WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
        except sqlite3.Error as e:
            print(e)

def select_all_products(connection):
    with sqlite3.connect(connection) as connect:
        try:
            sql = '''SELECT * FROM products'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(e)

def select_products_by_quantity_price(connection, limit):
    with sqlite3.connect(connection) as connect:
        try:
            sql = '''SELECT * FROM employees WHERE price < ? and quantity > ?'''
            cursor = connection.cursor()
            cursor.execute(sql, (limit))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(e)

def select_products_by_title(connection):
    # with sqlite3.connect(db_name) as connection:
        try:
            sql = '''SELECT * FROM products WHERE product_title LIKE '%Колбаса%'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(e)

sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(8, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0  
)
'''

# data_base_name = 'hw.db'

my_connection = create_connection('hw.db')
if my_connection:
    print('Connection successful!')
    create_table(my_connection, sql_to_create_products_table)
    insert_products(my_connection, ('Колбаса ОСТАНКИНО юбилейная', 319.0, 152))
    insert_products(my_connection, ('Колбаса АЛ-ХАЛАЛ сервелат', 179.0, 13))
    insert_products(my_connection, ('Колбаса САЛИХ', 179.0, 41))
    insert_products(my_connection, ('Колбаса РИХА докторская', 45.50, 64))
    insert_products(my_connection, ('Колбаса ОСТАНКИНО салями', 249.0, 78))
    insert_products(my_connection, ('Колбаса РИХА салями', 52.9, 112))
    insert_products(my_connection, ('Майонез ПЕЧАГИН', 98.0, 241))
    insert_products(my_connection, ('Майонез 3 ЖЕЛАНИЯ', 206.0, 29))
    insert_products(my_connection, ('Чай TESS', 98.0, 265))
    insert_products(my_connection, ('Чай GREENFIELD', 254.0, 354))
    insert_products(my_connection, ('Кофе CARTE NOIRE', 499.0, 118))
    insert_products(my_connection, ('Шоколад NUTS', 41.0, 1178))
    insert_products(my_connection, ('Конфета MAMBA', 78.0, 879))
    insert_products(my_connection, ('Пирожное CHOCO-PIE какао', 204.0, 914))
    insert_products(my_connection, ('Пирожное CHOCO-PIE', 184.0, 745))

    update_products_quantity(my_connection, (151, 3))
    update_products_price(my_connection, (131, 7))
    delete_products(my_connection, 2)
    select_all_products(my_connection)
    select_products_by_quantity_price(my_connection, 100, 5)
    select_products_by_title(my_connection)


