import sqlite3

connection = sqlite3.connect("Student_DB.db", 5)
cur = connection.cursor()

# print(connection)
# print(cur)

# cur.execute("CREATE TABLE person (name TEXT, lastname TEXT, age INTEGER, phone TEXT);")
cur.execute("INSERT INTO person (name, lastname, age, phone) VALUES ('Nick', 'Solovi', 25, '+380123456789');")

cur.execute("SELECT * FROM person WHERE name IS 'Nick';")

for row in cur:
    print(row)

connection.close()