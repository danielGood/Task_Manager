__author__ = 'dan'

import sqlite3
from bottle import route, run, template, debug, request




@route('/')
@route('/picnic')
def show_picnic():
    db = sqlite3.connect('todo.db')
    c = db.cursor()
    
    c.execute("SELECT task FROM todo")
    data = c.fetchall()
    c.execute("SELECT task FROM daytodo")
    data2 = c.fetchall()
    c.execute("SELECT task FROM weektodo")
    data3 = c.fetchall()
    c.execute("SELECT task FROM monthtodo")
    data4 = c.fetchall()
    c.execute("SELECT task FROM overalltodo")
    data5 = c.fetchall()
    print str(data)
    c.close()
    output = template('show_lists', rows=data, rows2=data2, week=data3, month=data4, overall=data5)
    return output



@route('/new', method='GET')
def new_item():

    if request.GET.get('save','').strip():

        new = request.GET.get('task','').strip()
        table = request.GET.get('table', '').strip()

        db = sqlite3.connect('todo.db')
        c = db.cursor()
        c.execute("INSERT INTO "+table + "(task, status) VALUES (?, ?)", (new, 1))
        new_id = c.lastrowid

        db.commit()
        c.close()
        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        request.GET.get('passtable','').strip()
        table = request.GET.get('table', '').strip()
        return template('new_task.tpl', table=table)

@route('/edit/:no', method='GET')
def edit_item(no):

    if request.GET.get('save','').strip():
        edit = request.GET.get('task','').strip()
        status = request.GET.get('status','').strip()
        table = request.GET.get('table', '').strip()
        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE "+ table+" SET task = ?, status = ? WHERE id LIKE ?", (edit,status,no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' %no

    else:
        request.GET.get('passtable','').strip()
        table = request.GET.get('table', '').strip()

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM " + table + " WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()



        return template('edit_task', old = cur_data, no = no, table = table)



@route('/delete/:no', method='GET')
def delete_task(no):

    if request.GET.get('save','').strip():

        table = request.GET.get('table', '').strip()


        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("DELETE FROM "+ table +" WHERE id LIKE ?", (no))
        conn.commit()

        return '<p>task deleted</p>'

    else:
        request.GET.get('passtable','').strip()
        table = request.GET.get('table', '').strip()

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM " +table+" WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()

        return template('delete_task', old = cur_data, no = no, table = table)




debug(True)
run(host='0.0.0.0', port=8080, reloader=True)
