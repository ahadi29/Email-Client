# Email register Page

from tkinter import*
import time
import mysql.connector

conn=mysql.connector.connect(host='localhost',database='Enter name of the database',user='root',password='Enter Password')
cursor=conn.cursor()

class signup:
    def __init__(self,root):
        self.root=root
        self.f=Frame(root.title("Signup Page"),height=600,width=700,bg='dodgerblue3')

        self.f.propagate(0)

        self.f.pack()
        self.n4=Label(text='E-MAIL CLIENT',bg='dodgerblue3',font=('Bold Calibri',30))
        self.n1=Label(text='Email ID:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n2=Label(text='Password:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n3=Label(text='Confirm Password:',fg="black",bg="dodgerblue3",font=('Calibri',14))

        self.b1=Button(text='Save',fg='white',bg='dark red',width=20,height=2,command=lambda: self.buttonclick(0))

        self.e1=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e2=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e3=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
  
        self.n1.place(x=50,y=100)
        self.e1.place(x=250,y=100)
        self.n2.place(x=50,y=150)
        self.e2.place(x=250,y=150)
        self.n3.place(x=50,y=200)
        self.e3.place(x=250,y=200)
        self.n4.place(x=250,y=25)
        
        self.b1.place(x=300,y=250)

    def buttonclick(self,num):
        
        if(self.e3.get()!=self.e2.get()):
            time.sleep(0.5)
            self.n4=Label(text='Password did not match',font=('Calibri',14),fg='darkred',bg="dodgerblue3")
            self.n4.place(x=50,y=200)
            num=1
            self.root.destroy()
            signUp()
            cursor.close()
            conn.close()
               
        a=self.e1.get()
        b=self.e2.get()

        if(num==0):
            sql_insert_query = " insert into info VALUES (%s,%s)"

            insert_tuple_1 = (a, b)

            cursor.execute(sql_insert_query, insert_tuple_1)
            conn.commit()
            cursor.close()
            conn.close()

        else:
            return 

            
def signUp():
    root=Tk()

    mb=signup(root)

    root.mainloop()


        
        











            
            
