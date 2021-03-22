import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Items")

cur.execute("CREATE TABLE Items (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, price real)")
conn.commit()
conn.close()