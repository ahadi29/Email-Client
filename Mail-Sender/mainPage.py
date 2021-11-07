# main page for sending Email

from tkinter import *
from signUp import signUp
from fetchPwd import matchMail
from mail import *
from dropDownDB import *
import mysql.connector

conn=mysql.connector.connect(host='localhost',database='Enter name of the database',user='root',password='Enter Password')
cursor=conn.cursor()
conn.commit()

class startpg:
    def __init__(self,root):
        self.root=root
        self.f=Frame(root.title("Main Page"),height=600,width=700,bg='dodgerblue3')

        self.f.propagate(0)

        self.f.pack()
        
        self.n1=Label(text='E-MAIL CLIENT',bg='dodgerblue3',font=('Bold Calibri',30))
        self.n2=Label(text='From:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n3=Label(text='To:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n4=Label(text='Subject:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n5=Label(text='Message:',fg="black",bg="dodgerblue3",font=('Calibri',14))
    
        self.b1=Button(text='SEND',fg='white',bg='dark red',width=20,height=2,font=('Calibri',15),command=lambda: self.buttonclick(1))
        self.b2=Button(text='Register',fg='white',bg='dark red',width=20,height=2,font=('Calibri',15),command=lambda: self.buttonclick(0))

        options = db_dropdown()

        self.clicked= StringVar()
        self.clicked.set("select mail")

        self.e2=OptionMenu( self.f , self.clicked , *options,command= self.getValue())
        self.e3=Entry(self.f,width=30,fg="black",bg="white",font=('Calibri',14))
        self.e4=Entry(self.f,width=30,fg="black",bg="white",font=('Calibri',14))
        self.e5=Text(self.f,height=10,width=40,fg="black",bg="white",font=('Calibri',14))

        self.n1.place(x=250,y=25)
        self.n2.place(x=50,y=100)
        self.e2.place(x=250,y=100,height=25, width=300)
        self.n3.place(x=50,y=150)
        self.e3.place(x=250,y=150)
        self.n4.place(x=50,y=200)
        self.e4.place(x=250,y=200)
        self.n5.place(x=50,y=250)
        self.e5.place(x=250,y=250)

        self.b1.place(x=50,y=500)
        self.b2.place(x=350,y=500)

    def getValue(self):
            self.choice = self.clicked.get()  

    def buttonclick(self,num):
        if(num==1):
            ml=self.clicked.get()
            pwd=matchMail(ml)
            rows="SELECT pswd from info WHERE email='$pwd'"
            cursor.execute(rows)
            rows=cursor.fetchall()

            senMail(ml,self.e3.get(),pwd,self.e4.get(),self.e5.get("1.0", "end"))
            self.root.destroy()
            cursor.close()
            conn.close()
        else:
            
            self.root.destroy()
            signUp()
            cursor.close()
            conn.close()

root=Tk()

mb=startpg(root)

root.mainloop()
        
