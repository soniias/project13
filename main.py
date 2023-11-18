import sqlite3

connection = sqlite3.connect("student_DB.db", 5)
cur = connection.cursor()
print(connection)
print(cur)