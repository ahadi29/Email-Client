# pulls DB to get password for the selected Email

import mysql.connector

def db_pwd():
    conn=mysql.connector.connect(host='localhost',database='Enter name of the database',user='root',password='Enter Password')
    cursor=conn.cursor()
    conn.commit()

    sql = "SELECT * from info "
    cursor.execute(sql)
    pwd = cursor.fetchall()

    return pwd

def matchMail(x):
    call=db_pwd()
    y=x
    for x in call:
        if(x[0]==y):
            z=x[1]
    return z
