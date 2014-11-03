__author__ = 'dan'

import sqlite3
from datetime import *
import calendar

from bottle import route, run, template, debug, request
from bottle import static_file
from dateutil.parser import *







@route('/')
def multi_list():

    db = sqlite3.connect('todo.db')
    c = db.cursor()
    c.execute("SELECT task from todo")
    data = c.fetchall()



    c.execute("SELECT * from todo INNER JOIN tbnames ON todo.tbleid = tbnames.id")
    join = c.fetchall()
    c.execute("SELECT id from tbnames WHERE active = '1'")
    tblist = c.fetchall()
    c.execute("SELECT name from tbnames WHERE active = '1'")
    tbnames = c.fetchall()
    c.close()
    tables=seperate_tables(join, tblist)
    print tbnames
    output= template('show_lists', list = data, join = join, tblist=tblist, tables=tables, tbnames=tbnames)
    return output




def seperate_tables(join, tblist):

    tables ={}
    for row in join:
        i =0
        row_table=''
        for col in row:
            ###change this later
            if i== 4:

                row_table=(col,)

            i=i+1
        if row_table in tables:
            temp = tables[row_table]
            temp.append(row)
            tables[row_table] = temp
        if not row_table in tables:
            tables[row_table] = [row]

    return tables




@route('/new', method='GET')
def new_item():

    if request.GET.get('save','').strip():

        new = request.GET.get('task','').strip()
        itemid = request.GET.get('itemid', '').strip()
        tbleid = request.GET.get('tbleid', '').strip()


        tbleid =eval(tbleid)
        itemid=eval(itemid)+1
        print tbleid
        print itemid
        db = sqlite3.connect('todo.db')
        c = db.cursor()
        c.execute("INSERT INTO todo (task, status, itemid, tbleid) VALUES (?, ?, ?, ?)", (new, 1, itemid, tbleid))
        new_id = c.lastrowid

        db.commit()
        c.close()
        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        request.GET.get('passtable','').strip()
        itemid = request.GET.get('itemid', '').strip()
        tbleid = request.GET.get('tbleid', '').strip()
        tbleid=eval(tbleid)[0]
        return template('new_task.tpl', itemid=itemid, tbleid=tbleid)



@route('/new_table', method='GET')
def new_table():
    if request.GET.get('save','').strip():
        table = request.GET.get('table', '').strip()
        db = sqlite3.connect('todo.db')
        c = db.cursor()
        new= 'new table'

        c.execute("SELECT COUNT(*) from tbnames")
        tables=c.fetchall()
        tables=  tables[0][0]

        tables = tables + 1
        c.execute("INSERT INTO todo (task, status, itemid, tbleid) VALUES (?, ?, ?, ?)", (new, 1, 1, tables))
        c.execute("INSERT INTO tbnames (name, active) VALUES (?, ?)", (table, 1))
        new_id = c.lastrowid

        db.commit()
        c.close()
    else:
        return template('new_table.tpl')



@route('/edit', method='GET')
def edit_item():

    if request.GET.get('save','').strip():
        edit = request.GET.get('task','').strip()
        status = request.GET.get('status','').strip()
        tbleid = request.GET.get('tbleid', '').strip()
        itemid = request.GET.get('itemid', '').strip()





        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ?, itemid =?, tbleid =? WHERE itemid= ? AND tbleid = ?", (edit,status, itemid, tbleid, itemid, tbleid))
        conn.commit()

        return ''

    else:
        request.GET.get('passtable','').strip()
        tbleid = request.GET.get('tbleid', '').strip()

        itemid = request.GET.get('itemid', '').strip()

        tbleid=eval(tbleid)[0]


        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE itemid = ? AND tbleid = ?", (itemid, tbleid))
        cur_data = c.fetchone()



        return template('edit_task', old = cur_data, tbleid=tbleid, itemid=itemid)



@route('/ref_style')
def server_static():
    return static_file('style.css', root='.')

@route('/left_arrow')
def server_static():
    return static_file('leftarrow.png', root='images')

@route('/plus')
def server_static():
    return static_file('plus.png', root='images')

@route('/red_x')
def server_static():
    return static_file('x.png', root='images')


@route('/delete', method='GET')
def delete_task():

    if request.GET.get('save','').strip():

        itemid = request.GET.get('itemid', '').strip()
        tbleid = request.GET.get('tbleid', '').strip()

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("DELETE FROM todo WHERE tbleid = ? AND itemid = ?", (tbleid, itemid))
        conn.commit()

        return '<p>task deleted</p>'

    else:
        request.GET.get('passtable','').strip()
        tbleid = request.GET.get('tbleid', '').strip()

        itemid = request.GET.get('itemid', '').strip()

        tbleid=eval(tbleid)[0]


        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE itemid = ? AND tbleid = ?", (itemid, tbleid))
        cur_data = c.fetchone()



        return template('delete_task', old = cur_data, tbleid=tbleid, itemid=itemid)





def format_date(date):

    x = time.gmtime(date)
    s = x.tm_mday+"/"+x.tmmon+"/"+x.tm_year
    return s



@route('/debug')
def show_data():
    db = sqlite3.connect('todo.db')
    c = db.cursor()


    c.execute("SELECT * from todo INNER JOIN tbnames ON todo.tble = tbnames.name")
    join = c.fetchall()
    c.execute("SELECT name from tbnames WHERE active = '1'")
    tblist = c.fetchall()
    tables=seperate_tables(join, tblist)

    c.execute("SELECT * from todo")
    data = c.fetchall()
    c.execute("SELECT * from tbnames")
    data2 = c.fetchall()
    return template('debug.tpl', join=join, tblist=tblist, tables=tables, data=data, data2=data2)



debug(True)
run(host='0.0.0.0', port=8080, reloader=True)
