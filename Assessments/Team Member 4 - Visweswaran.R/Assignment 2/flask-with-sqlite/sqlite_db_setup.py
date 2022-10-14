import sqlite3

conn = sqlite3.connect('signup_database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE users (name TEXT, username TEXT, address TEXT, password TEXT)')
print("Table created successfully")
conn.close()
