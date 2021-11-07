# pulls emails from DB to show on the main page

import mysql.connector

def db_dropdown(): 
    conn=mysql.connector.connect(host='localhost',database='Enter name of the database',user='root',password='Enter Password')  
    cursor=conn.cursor()
    conn.commit()

    sql = 'SELECT email FROM info' 

    cursor.execute(sql)
    list_tested = cursor.fetchall()  
    list_tested = [i for sub in list_tested for i in sub]  

    return list_tested

