import sqlite3
conn = sqlite3.connect("mydatabse.db")
cursor=conn.cursor()
print ("listing all reco")
f=open("dbtocsv1.csv","a")

for row in cursor.execute("select * from books"):
    f.write(",".join(map(lambda x:str(x),row)) + "\n")
#using map to convert all field into strings
f.close()
conn.close()
    

