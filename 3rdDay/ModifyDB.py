import sqlite3
conn = sqlite3.connect("mydatabse.db")
cursor=conn.cursor()
cursor.execute("Insert into books values (1,'wings of fire','abdul kalam')")
conn.commit()

mybooks = [(2,'my exp','gandghi'),
           (3,'my india','nehru'),
           (4,'my food','ramesh')
           ]
cursor.executemany("Insert into books values(?,?,?)",mybooks)
conn.commit()
conn.close()
