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

def sel_quiz(name,roll):
    print(roll,type(roll))
    n=tk.Label(root,text=f"Name : {name}          Roll : {roll}",font=" 20 ",bg="#ADD8E6")
    n.place(relx=.5,rely=0.1,relheight=.09,relwidth=.9,anchor="center")
    heading=Label(root,text="Which quiz would you like to take??",font=" 25 ",padx=10,pady=10)
    heading.place(relx=0.5,rely=0.2,anchor="center")
    empty_l=[]
    point=0
    y_co=0.4
    x_co=0.2
    for i in range(len(result)):
        button = Button(root,  height=2, width=10,bd=4,text=result[i][:-4],command=lambda i=i: read_c(result[i]))
        button.place(relx=x_co,rely=y_co,anchor="center")
        point+=3
        x_co=0.2+float(point)/10
        if x_co>0.8:
            y_co+=0.1
            point=0
            x_co=0.2
        empty_l.append(button)
    # print(result)
 
    def read_c(quiz):
        for i in empty_l:
            i.place_forget()

        # reading data 
        df=pd.read_csv("quiz_wise_questions/{}".format(quiz))

        # timer function   
        def countdown(t):
            if t==0:
                show_score()
            else:
                mins=int(t/60)
                sec=int(t%60)
                timer = '{:50d}:{:<50d}'.format(mins,sec)
                myLabel1.config(text="{}".format(timer))
                t-=1
                myLabel1.after(1000,lambda:countdown(t))
        time=df.columns[-1]
        time=re.findall(r"[0-9]+",time)
        time=int(time[0])
        myLabel1=Label(root,text=f"{time}:00",bg="#90ee90")
        myLabel1.place(relx=0.5,rely=0.03,anchor="center",relwidth=.9)
        myLabel1.after(1000,lambda:countdown(time*60-1))

        heading.place_forget()
        def next_question(q,g):
        # takes user to next question
   
            if g:
                if g!=1:
                    g.place_forget()
                question.place(relx=0.5,rely=0.25,anchor="center")
                correct.place(relx=0.75,rely=0.3,anchor="center")
                negative.place(relx=0.75,rely=0.35,anchor="center")
                comp.place(relx=0.75,rely=0.4,anchor="center")
                option1.place(relx=0.3,rely=0.5,anchor="center")  
                option2.place(relx=0.7,rely=0.5,anchor="center")                
                option3.place(relx=0.3,rely=0.6,anchor="center")  
                option4.place(relx=0.7,rely=0.6,anchor="center") 
                next_q.place(relx=0.5,rely=0.8,anchor="center")
                submit_b.place(relx=0.8,rely=0.8,anchor="center")
                ask.place_forget()
                ok_button.place_forget()
                q-=1
            q+=1
            if q==len(df.index):
                show_score()
            question.config(text="{}. {}".format(q+1,df['question'].loc[q]))
            correct.config(text="Correct answer : {}".format(df['marks_correct_ans'].loc[q]))
            negative.config(text="Wrong answer : {}".format(df['marks_wrong_ans'].loc[q]))
            comp1="No"
            if df['compulsory'].loc[q]=="n":
                comp1="No"
            else :
                comp1="Yes"
            comp.config(text="Compulsory : {}".format(comp1))

            if q==len(df.index)-1:
                next_q.place_forget()


            option1.config(text="{}".format(df['option1'].loc[q]),bg="white",command=lambda:choose(option1,1,q))
            option2.config(text="{}".format(df['option2'].loc[q]),bg="white",command=lambda:choose(option2,2,q))
            option3.config(text="{}".format(df['option3'].loc[q]),bg="white",command=lambda:choose(option3,3,q))
            option4.config(text="{}".format(df['option4'].loc[q]),bg="white",command=lambda:choose(option4,4,q))
            next_q.config(command=lambda:next_question(q,0))

        ans_dict=dict()
        def choose(o,num,q):      
            # changes background color of chosen option
            ans_dict[q]=num
            for i in list_b:
                i.config(bg="white")
            o.config(bg="#00ff85") 
            pass

        # score calculation
        def score_calc():
            score=0
            correct_ch=0
            wrong_ch=0
            attempted=[]
            for i in ans_dict:
                attempted.append(i)
                if ans_dict[i]==df['correct_option'].loc[i]:
                    score += df['marks_correct_ans'].loc[i]
                    correct_ch+=1
                else:
                    score += df['marks_wrong_ans'].loc[i]
                    wrong_ch+=1
            unattempted=set([i for i in range(len(df.index))])-set(attempted)
            for k in unattempted:
                if df['compulsory'].loc[k]=='y':
                    score+=df['marks_wrong_ans'].loc[k]
            return [score,correct_ch,wrong_ch]
            
        # question label
        question=Label(root,text="{}. {}".format(1,df['question'].loc[0]),wraplength=400,font=" 20 ")
        question.place(relx=0.5,rely=0.25,anchor="center")

        # Correct ans Negative and Compulsory
        correct=Label(root,text="Correct answer : +{}".format(df['marks_correct_ans'].loc[0]),wraplength=400,)
        correct.place(relx=0.8,rely=0.3,anchor="center")
        negative=Label(root,text="Wrong answer : {}".format(df['marks_wrong_ans'].loc[0]),wraplength=400,)
        negative.place(relx=0.8,rely=0.35,anchor="center")

        if df['compulsory'].loc[0]=="n":
            comp1="No"
        else :
            comp1="Yes"

        comp=Label(root,text="Compulsory : {}".format(comp1),wraplength=400,)
        comp.place(relx=0.8,rely=0.4,anchor="center")
        top_labels=[question,correct,negative,comp]

        # option button
        option1=Button(root,text="{}".format(df['option1'].loc[0]),command=lambda:choose(option1,1,0),font=" 9 ",bd=3,bg="white")
        option1.place(relx=0.3,rely=0.5,anchor="center")  
        option2=Button(root,text="{}".format(df['option2'].loc[0]),command=lambda:choose(option2,2,0),font=" 9 ",bd=3,bg="white")
        option2.place(relx=0.7,rely=0.5,anchor="center")  
        option3=Button(root,text="{}".format(df['option3'].loc[0]),command=lambda:choose(option3,3,0),font=" 9 ",bd=3,bg="white")
        option3.place(relx=0.3,rely=0.6,anchor="center")  
        option4=Button(root,text="{}".format(df['option4'].loc[0]),command=lambda:choose(option4,4,0),font=" 9 ",bd=3,bg="white")
        option4.place(relx=0.7,rely=0.6,anchor="center")  
        
        list_b=[option1,option2,option3,option4]
        
        #next button   
        next_q=Button(root,text="NEXT",command=lambda:next_question(0,0),font=" 10 ",bd=4,bg="#00b8ff")  
        next_q.place(relx=0.5,rely=0.8,anchor="center")
        
        # Shortcut info
        
        export_label=Label(root,text="Press 'Ctrl' + 'Alt' + 'e' to export quiz marks to csv",font=("Nunito","8"))
        shortcut_label=Label(root,text="Press 'Ctrl' + 'Alt' + 'g' to go to a question | Press 'Ctrl' + 'Alt' + 'u' to show unattempted question(s)\nPress 'Ctrl' + 'Alt' + 'f' to submit quiz | Press 'Ctrl' + 'Alt' + 'e' to export quiz wise marks to csv",font=("Nunito","8"))
        shortcut_label.place(relx=0.5,rely=0.9,anchor="center")
        export_label.place_forget()
        
        question_nos=[]
        for i in range(len(df.index)):
                question_no = Button(root,  height=1, width=4,bd=4,text=i+1,command=lambda i=i: next_question(i,1))
                question_nos.append(question_no)
        
        ask=Label(root,text=f"Which question would you like to go to? \n Any number between 1 and {len(df.index)}")
        ok_button=Button(root,text="OK",bg="#90ee90")
        
        # Takes us to a question
        def goto(event):
            for i in top_labels:
                i.place_forget()
            next_q.place_forget()
            submit_b.place_forget()
            myLabel1.place_forget()
            for k in list_b:
                k.place_forget()
            ask.place(relx=0.5,rely=0.2,anchor="center")
            ok_button.config(command=lambda : goto_handler(number))
            ok_button.place(relx=0.5,rely=0.6,anchor="center")
            number=Entry(root,width="30",bg="white")
            number.place(relx=0.5,rely=0.5,anchor="center")
            number.bind("<Return>",lambda no : goto_handler(number))
            
        # goto_handler
        def goto_handler(number):
            list_of_questions=[i+1 for i in range(len(df.index))]
            entry_number=number.get()
            check=0 
            if len(entry_number)==0:
                next_question(0,0)
            else :
                for i in range(len(entry_number)):
                    if ord(entry_number[i])>47 and ord(entry_number[i])<58:
                        check+=1
                if check==len(entry_number):
                    entry_number=int(entry_number)
                    if entry_number in list_of_questions:
                        next_question(entry_number-1,number)
                    else:
                        next_question(0,0)
                else:
                    next_question(0,0)
                  
        # goto binding  
        root.bind('<Control_L><Alt_L><g>',goto)
        root.bind('<Control_L><Alt_L><G>',goto)
        root.bind('<Control_L><Alt_R><g>',goto)
        root.bind('<Control_L><Alt_R><G>',goto)
        root.bind('<Control_R><Alt_L><g>',goto)
        root.bind('<Control_R><Alt_L><G>',goto)
        root.bind('<Control_R><Alt_R><g>',goto)
        root.bind('<Control_R><Alt_R><G>',goto)
        
        # unattempted_questions
        def unattempted_questions(event):
            unattempted=[i+1 for i in range(len(df.index))]
            attempted=[]
            for i in ans_dict:
                attempted.append(i+1)
            unattempted=set(unattempted)-set(attempted)  
            msg.showinfo("Unattempted Questions",f"{unattempted}")
            
          
        # Bindings for unattempted question  
        root.bind('<Control_L><Alt_L><u>',unattempted_questions)
        root.bind('<Control_L><Alt_L><U>',unattempted_questions)
        root.bind('<Control_L><Alt_R><u>',unattempted_questions)
        root.bind('<Control_L><Alt_R><U>',unattempted_questions)
        root.bind('<Control_R><Alt_L><u>',unattempted_questions)
        root.bind('<Control_R><Alt_L><U>',unattempted_questions)
        root.bind('<Control_R><Alt_R><u>',unattempted_questions)
        root.bind('<Control_R><Alt_R><U>',unattempted_questions)
       
            
        def show_score():
            export_label.place(relx=0.5,rely=0.9,anchor="center")
            shortcut_label.place_forget()
            myLabel1.place_forget()
            for i in top_labels:
                i.place_forget()
            next_q.place_forget()
            submit_b.place_forget()
            
            for k in list_b:
                k.place_forget()
            wrong=score_calc()[2]
            correct=score_calc()[1]
            score=int(score_calc()[0])
            statement=Label(root,text=f"Total questions : {len(df.index)} \n Total questions attempted : {correct+wrong} \n Total correct questions : {correct} \nTotal wrong questions : {wrong} \n Your score is {score} out of {df['marks_correct_ans'].sum()}",font="13")
            statement.place(relx=0.5,rely=0.5,anchor='center') 
            export_response() 
            c.execute("""
            SELECT * FROM project1_marks
            WHERE roll=(?) AND quiz_num= (?);

            """,(roll,quiz[:-4]))
            if len(c.fetchall())==0:    
                c.execute("INSERT INTO project1_marks VALUES (?,?,?)",(roll,quiz[:-4],score))
                con.commit()
            else:
                c.execute("""
                UPDATE project1_marks
                SET total_marks=(?)
                WHERE roll=(?) AND quiz_num= (?);
                """,(score,roll,quiz[:-4]))
                con.commit()




            def clear1():
                submit_b1.place_forget()
                statement.place_forget()
                # statement1.place_forget()
                # statement2.place_forget()
                sel_quiz(name,roll)
            submit_b1=Button(root,text="Back To Quiz selction",command=clear1,bg="#ffdbb6",font=" 9 " ,bd=3)
            submit_b1.place(relx=0.8,rely=0.8,anchor="center") 

        # submit button
        def conf(event=""):
            a=msg.askyesno(title="Conformation", message="Do you want to submit",)
            if a:
                show_score()
            

        submit_b=Button(root,text="SUBMIT",command=conf,bg="#ffdbb6",font=" 9 " ,bd=3)
        submit_b.place(relx=0.8,rely=0.8,anchor="center")
        
        #submit binding
        root.bind('<Control_L><Alt_L><f>',conf)
        root.bind('<Control_L><Alt_L><F>',conf)
        root.bind('<Control_R><Alt_R><f>',conf)
        root.bind('<Control_R><Alt_R><F>',conf)
        root.bind('<Control_L><Alt_R><f>',conf)
        root.bind('<Control_L><Alt_R><F>',conf)
        root.bind('<Control_R><Alt_L><f>',conf)
        root.bind('<Control_R><Alt_L><F>',conf)
        
        def export_response():
            # global df
            path=os.getcwd()
            path=os.path.join(path,"individual_responses")
            if not os.path.isdir(path):
                os.mkdir(path)
            wrong=score_calc()[2]
            correct=score_calc()[1]
            score=score_calc()[0]
            legend=['Correct Choice','Wrong choice','Unattempted','Marks Obtained','Total Quiz Marks']
            total=[correct,wrong,len(df['question'])-(correct+wrong),score,df['marks_correct_ans'].sum()]
            df['Marked Choice']=None
            df['Total']=None
            df['Legend']=None
           
            for i in ans_dict:
                df['Marked Choice'].loc[i]=ans_dict[i]
            t={"Total":total,"Legend":legend}
            df1=pd.DataFrame(t)
            df3=pd.concat([df,df1],ignore_index="True",axis=1)
            df3.to_csv(f'individual_responses/{quiz[:-4]}_{roll}.csv',index=False)
           
        



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
    