import sqlite3 
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import *
from tkinter import font
from tkinter.constants import FLAT
import os
import pandas as pd
import shutil
import re



pd.options.mode.chained_assignment = None

con=sqlite3.connect("project1_quiz_cs384.db")
c=con.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS project1_registration (
    name TEXT NOT NULL,
    roll TEXT NOT NULL,
    password TEXT NOT NULL,
    whatsappnumber INTEGER
    )""")
c.execute("""CREATE TABLE IF NOT EXISTS project1_marks (
    roll TEXT NOT NULL,
    quiz_num TEXT,
    total_marks INTEGER
    )""")

result=[]
path=os.path.join(os.getcwd(),"quiz_wise_questions")
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".csv"):
             result.append( file)



def next():
    he.pack_forget()
    a11.pack_forget()
    a12.pack_forget()
    b11.pack_forget()
    b12.pack_forget()
    c11.pack_forget()
    c12.pack_forget()
    d11.pack_forget()
    d12.pack_forget()
    regbtn1.pack_forget()
    logbtn1.pack_forget()

    head.pack()
    head2.pack()
    a.pack(fill='x')
    a1.pack(fill='x',padx=50,ipadx=10,ipady=7)
    b.pack(fill='x',pady=(30,0))
    b1.pack(padx=50,ipadx=10,ipady=7)
    logbtn.pack(pady=10)
    regbtn.pack(pady=10,padx=10)


def login():
    user=a1.get(),
    password=hash_password(b1)
    c.execute("SELECT * FROM project1_registration WHERE roll=(?)",(user))

    if len(c.fetchall())==0:
       msg.showwarning(title="No data found", message="please register")
    else :
        c.execute("SELECT * FROM project1_registration WHERE roll=(?)",(user))
        l=list(c.fetchone())
        if l[2]==password:
            print("succes login")
            head.pack_forget()
            head2.pack_forget()
            a.pack_forget()
            a1.pack_forget()
            b.pack_forget()
            b1.pack_forget()
            regbtn.pack_forget()
            logbtn.pack_forget()
            sel_quiz(l[0],user[0])

        else :
            msg.showwarning(title="Invalid", message="please use valid password and username")




def login1():
    name=a12.get()
    roll=b12.get()
    password=hash_password(c12)
    what_num=d12.get()
    c.execute("INSERT INTO project1_registration VALUES (?,?,?,?)",(name,roll,password,what_num))
    con.commit()
    
    he.pack_forget()
    a11.pack_forget()
    a12.pack_forget()
    b11.pack_forget()
    b12.pack_forget()
    c11.pack_forget()
    c12.pack_forget()
    d11.pack_forget()
    d12.pack_forget()
    regbtn1.pack_forget()
    logbtn1.pack_forget()

    sel_quiz(name,roll)



def hash_password(entry):
    password=entry.get()
    ascii_string=''
    for i in range(len(password)):
        ascii_string+=str(ord(password[i]))
    hex_string=''
    for i in range(len(ascii_string)):
        hex_string+=str(hex(int(ascii_string[i])))
    return hex_string
    
def reg():
    head.pack_forget()
    head2.pack_forget()
    a.pack_forget()
    a1.pack_forget()
    b.pack_forget()
    b1.pack_forget()
    regbtn.pack_forget()
    logbtn.pack_forget()
    global he,a11,a12,b11,b12,c11,c12,d11,d12,logbtn1,regbtn1

    he=tk.Label(root, text="Registration", font="comicsansms 30 bold",fg="blue", pady=15)
    he.pack()

    a11 = tk.Label(root ,text = "Name",font=" 20 ",padx=(100))
    a11.pack(fill='x')

    a12 = tk.Entry(root,width=400,bd=3,bg="#CFDAD8")
    a12.pack(fill='x',padx=50,ipadx=10,ipady=7)

    b11 = tk.Label(root ,text = " Roll",font=" 20 ",padx=(100))
    b11.pack(fill='x',pady=(30,0))

    b12 = tk.Entry(root,width=400,bd=3,bg="#CFDAD8")
    b12.pack(padx=50,ipadx=10,ipady=7)

    c11 = tk.Label(root ,text = " Password",font=" 20 ",padx=(100))
    c11.pack(fill='x',pady=(30,0))

    c12 = tk.Entry(root,width=400,bd=3,bg="#CFDAD8")
    c12.pack(padx=50,ipadx=10,ipady=7)

    d11 = tk.Label(root ,text = " Whatsapp Number",font=" 20 ",padx=(100))
    d11.pack(fill='x',pady=(30,0))

    d12 = tk.Entry(root,width=400,bd=3,bg="#CFDAD8")
    d12.pack(padx=50,ipadx=10,ipady=7)

    logbtn1 = tk.Button(root,text="Register and login",command = login1,background="green",font=" 18 ",padx=20,pady=5,)
    logbtn1.pack(pady=10)

    regbtn1 = tk.Button(root,text="login",command = next,background="red",font=" 18 ",padx=30,pady=5,)
    regbtn1.pack(pady=10,padx=10)

# main geometry  
root=tk.Tk()
root.geometry("700x600") 
root.minsize(600,600)
root.maxsize(1500,900) 
root.title('quiz')


# landing page
head=tk.Label(root, text="QUIZ", font="comicsansms 30 bold",fg="blue", pady=15)
head.pack()

head2=tk.Label(root, text="login", font="comicsansms 24 bold", pady=15)
head2.pack()

a = tk.Label(root ,text = "username",font=" 20 ",padx=(100))
a.pack(fill='x')

a1 = tk.Entry(root,width=400,bd=3,bg="#CFDAD8")
a1.pack(fill='x',padx=50,ipadx=10,ipady=7)

b = tk.Label(root ,text = " password",font=" 20 ",padx=(100))
b.pack(fill='x',pady=(30,0))

b1 = tk.Entry(root,width=400,show="* ",bd=3,bg="#CFDAD8")
b1.pack(padx=50,ipadx=10,ipady=7)

logbtn = tk.Button(root,text="login",command = login,background="green",font=" 18 ",padx=20,pady=5,)
logbtn.pack(pady=10)

regbtn = tk.Button(root,text="Register",command = reg,background="red",font=" 18 ",padx=30,pady=5,)
regbtn.pack(pady=10,padx=10)

def csv(event=""):
    # path=os.getcwd()
    # path=os.path.join(path,"grades")
    # if  os.path.isdir(path):
    #     shutil.rmtree(path)

    # make grades folder
    path=os.getcwd()
    path=os.path.join(path,"quiz_wise_responses")
    if not os.path.isdir(path):
        os.mkdir(path)
    for i in result:
        df=pd.read_sql(f"""SELECT roll ,total_marks FROM project1_marks WHERE quiz_num='{(i[:-4])}'""",con)
        df.to_csv(f"quiz_wise_responses/scores_{i[:-4]}.csv",index=False)

root.bind('<Control_L><Alt_L><e>',csv)
root.bind('<Control_L><Alt_L><E>',csv)
root.bind('<Control_R><Alt_R><e>',csv)
root.bind('<Control_R><Alt_R><E>',csv)
root.bind('<Control_L><Alt_R><e>',csv)
root.bind('<Control_L><Alt_R><E>',csv)
root.bind('<Control_R><Alt_L><e>',csv)
root.bind('<Control_R><Alt_L><E>',csv)

# driver code
if __name__=="__main__":

    root.mainloop()
    con.close()