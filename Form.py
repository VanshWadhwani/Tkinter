from tkinter import *
import mysql.connector as con
import time
root=Tk()
root.geometry("500x600")
def getvalue():
    print("The username is",uservalue.get())
    print("The Password is",passvalue.get())
def db():
    x=con.connect(host="localhost",user="root",password="Mouse@2010",database="Happy")
    cur=x.cursor()
    #cur.execute("create table hey(uservalue varchar(30),passvalue varchar(30))")
    cur.execute("insert into hey values('{}','{}')".format(uservalue.get(),passvalue.get()))
    x.commit()
    time.sleep(0.5)
    l3=Label(root,text="Saved!")
    l3.grid(column=0,row=4)
    
    
l1=Label(root,text="Username :")
l2=Label(root,text="Password :")
l1.grid(padx=10,pady=10)
l2.grid(padx=15,pady=10)

uservalue=StringVar()
passvalue=StringVar()
uentry=Entry(root,textvariable=uservalue)
pentry=Entry(root,textvariable=passvalue)
uentry.grid(column=2,row=0)
pentry.grid(column=2,row=1)

b1=Button(text="Submit",command=getvalue)
b1.grid(column=0,row=2)
b2=Button(text="Save",command=db)
b2.grid(column=0,row=3)



root.mainloop()

