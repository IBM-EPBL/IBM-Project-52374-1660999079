import sqlite3

conn = sqlite3.connect('student_database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE students2 (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print("Table created successfully")
conn.close()
