
_author__ = 'dan'
import sqlite3
db = sqlite3.connect('todo.db')

db.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL, tble char(100), tbleid INTEGER)")
db.execute("INSERT INTO todo (task,status, tble, tbleid) VALUES ('Read A-byte-of-python to get a good introduction into Python',0, 'default', 1)")
db.execute("INSERT INTO todo (task,status, tble, tbleid) VALUES ('Visit the Python website',1, 'default', 2)")
db.execute("INSERT INTO todo (task,status, tble, tbleid) VALUES ('Test various editors for and check the syntax highlighting',1, 'default', 3)")
db.execute("INSERT INTO todo (task,status, tble, tbleid) VALUES ('Choose your favorite WSGI-Framework',0, 'default', 4)")


db.execute("CREATE TABLE tbnames (id INTEGER PRIMARY KEY, name char(100), active bool)")
db.execute("INSERT INTO tbnames (name, active) VALUES ('default', 1)")




db.commit()