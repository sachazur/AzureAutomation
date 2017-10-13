from bottle import route,run,request,template
@route('/')
def myweb():
    return "hello world"

@route('/env')
def abcd():
    import os
    output = '<table border=1>'
    for x,y in os.environ.items():
        output=output+ "<tr><td>" + x + "</td><td>" + y + "</td></tr>"
    return output + "</table>"


@route('/wish/<name>')
def wish(name):
    return "hello " + name

@route('/hello/<name>')
def index(name):
    return template('<b>Heelo {{yourvar}}</b>',yourvar=name)

@route('/books')
def dbtoweb():
        import sqlite3
        dbconn = sqlite3.connect("C:/sachin/Pythontrain1/3rdDay/mydatabse.db")
        cursor=dbconn.cursor()
        output='<table border=1>'
        print ("listing all reco")
        tablerow = "<tr><td>{}</td><td>{}</td></tr>"
        for id,bookname,author in cursor.execute("select * from books"):
             output+=tablerow.format(bookname,author)
        output+="</table>"

        dbconn.close()
        return output
    
@route('/add')
def showform():
    return """"
<html>
<form method=post action="http://localhost:8080/addbook">
<input type=text name=id>Id<br>
<input type=text name=bookname>Book name<br>
<input type=text name=author>Author<br>
<input type=submit>
</form>
</html>
"""

@route('/addbook',method='post')
def login():
    import sqlite3
    dbconn = sqlite3.connect("C:/sachin/Pythontrain1/3rdDay/mydatabse.db")
    cursor=dbconn.cursor()
    id=request.forms.get('id')
    bookname=request.forms.get('bookname')
    author=request.forms.get('author')
    sql="Insert into books values ({},'{}','{}')".format(id,bookname,author)
    cursor.execute(sql)
    dbconn.commit()
    dbconn.close()
    return "<a href=/books>Book List</a>"

run(host='localhost',port=8080,debug=True)
