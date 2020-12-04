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