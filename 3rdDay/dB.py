import sqlite3
conn = sqlite3.connect("mydatabse.db")
cursor=conn.cursor()
#create a table
sql="""
create table books(
id int,
title text,
author text
)
"""
cursor.execute(sql)
print ("table got created !1")
conn.close()


conn = sqlite3.connect("mydatabse.db")
cursor=conn.cursor()
cursor.execute("Insert into books values (1,'wings of fire','abdul kalam')")
cursor.commit()

mybooks = [(2,'my exp','gandghi'),
           (3,'my india','nehru'),
           (2,'my food','ramesh')
           ]
cursor.executemany("Insert into books values(???)",mybooks)
conn.commit()
conn.close()
