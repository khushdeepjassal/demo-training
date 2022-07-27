from tkinter import*
from tkinter import messagebox
from mysql import connector

def database():
    conn =connector.connect(
        user = 'root',
        password = 'root',
        host= '127.0.0.1',
        port ='3306',
        database = 'demo'
    )
    mycursor = conn.cursor()
    mycursor.execute("insert into info values:%s%s%s%s",entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get())
    messagebox.showinfo('info','submitted')
    conn.commit()
