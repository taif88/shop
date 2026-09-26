import sqlite3

def setup_database():
    conn = sqlite3.connect('database/database.db')
    cursor = conn.cursor()
    
    # Create a sample table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product (
            prodectid INTEGER PRIMARY KEY AUTOINCREMENT,
            productname TEXT NOT NULL UNIQUE,
            description TEXT NOT NULL,
            price INTEGER NOT NULL,
            categories TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database/database.db')
        self.cursor = self.conn.cursor()
    def add_user(self, name, email, password):
        try:
            self.cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, password))
            self.conn.commit()
            self.close()
            return True
        except:
            self.close()
            return False
        
    def get_user(self, email,password):
        try:
            self.cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
            user = self.cursor.fetchone()
            self.close()
            if user[3] == password :
                print(password + user[3])
                return user[1]
            else:
                return 1
        except:
            return 0
    def get_email(self,name):
        self.cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
        user = self.cursor.fetchone()
        self.close()
        return user[2]
    def get_products(self,name):
        try:
            if name :
                self.cursor.execute('SELECT * FROM product WHERE productname=?', (name.upper(),))
            else:
                self.cursor.execute('SELECT * FROM product')
            products = self.cursor.fetchall()
        except:
            products=None
        self.close()
        return products
    def get_product_by_id(self,id=1):
        self.cursor.execute('SELECT * FROM product WHERE prodectid=?', (id,))
        product = self.cursor.fetchone()
        self.close()
        return product
    def get_product_by_ids(self,ids):
            products=[]
            for id in ids:
                self.cursor.execute('SELECT * FROM product WHERE prodectid=?', (id,))
                products.append(self.cursor.fetchone())
            self.close()
            return products
    def close(self):
        self.conn.close()