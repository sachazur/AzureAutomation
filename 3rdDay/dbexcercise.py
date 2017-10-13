import sqlite3

conn = sqlite3.connect("mydatabse1.db")
cursor=conn.cursor()
cursor.execute("Insert into state values ('MH','nagpur','gondia')")
conn.commit()
conn.close()
