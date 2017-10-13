import sqlite3
conn = sqlite3.connect("mydatabse.db")
cursor=conn.cursor()

sql="""
DELETE FROM books
WHERE id = 4

"""
cursor.execute(sql)
conn.commit()
conn.close()




