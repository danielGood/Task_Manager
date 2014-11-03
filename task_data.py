
_author__ = 'dan'
import sqlite3
db = sqlite3.connect('todo.db')

db.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL, itemid INTEGER, tbleid INTEGER)")
db.execute("INSERT INTO todo (task,status, itemid, tbleid) VALUES ('Read A-byte-of-python to get a good introduction into Python',0, 1, 1)")
db.execute("INSERT INTO todo (task,status, itemid, tbleid) VALUES ('Visit the Python website',1, 2, 1)")
db.execute("INSERT INTO todo (task,status, itemid, tbleid) VALUES ('Test various editors for and check the syntax highlighting',1, 3, 1)")
db.execute("INSERT INTO todo (task,status, itemid, tbleid) VALUES ('Choose your favorite WSGI-Framework',0, 4, 1)")


db.execute("CREATE TABLE tbnames (id INTEGER PRIMARY KEY, name char(100), active bool)")
db.execute("INSERT INTO tbnames (name, active) VALUES ('default', 1)")




db.commit()