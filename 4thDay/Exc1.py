import sqlite3
conn = sqlite3.connect("mydatabse.db")
cursor=conn.cursor()
print ("listing all reco")
#for row in cursor.execute("select * from books"):
    #print (row)

print ("results")
sql = "select * from books"
cursor.execute(sql)
for id,bookname,author in cursor.fetchall():
    print ("The book {} was written by {}".format(bookname,author))
conn.close()
