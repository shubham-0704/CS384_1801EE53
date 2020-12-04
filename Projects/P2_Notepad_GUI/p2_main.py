from tkinter import *   
from tkinter.messagebox import showinfo ,showerror
from tkinter.simpledialog import askstring
import os
import os.path,time
from tkinter.filedialog import askopenfilename ,asksaveasfilename


def new_file():
    global file
    root.title("Untitled - Notepad")
    file=None
    text.delete("1.0",END)

def open_file():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()

def save_file():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            # print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()

def exit_file():
    root.destroy()

def saveas_file():
    global file

    file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                        filetypes=[("All Files", "*.*"),
                                    ("Text Documents", "*.txt")])
    if file =="":
        pass

    else:
        #Save as a new file
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()

        root.title(os.path.basename(file) + " - Notepad")
        # print("File Saved")


def cut():
    text.event_generate(("<<Cut>>"))

def copy():
    text.event_generate(("<<Copy>>"))

def paste():
    text.event_generate(("<<Paste>>"))

def find():
    word=askstring("Word to find", "Enter the Word" )
    # s=text.search(word,"1.0",END)
    s=word
    # print(s)
      
    text.tag_remove('found', '1.0', END)  
    if s: 
        idx = '1.0'
        while 1: 
            idx = text.search(s, idx, nocase=1,  
                              stopindex=END)  
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(s))  
            text.tag_add('found', idx, lastidx)  
            idx = lastidx 
        text.tag_config('found', foreground='red')



def find_r():
    window=Tk()
    window.geometry("300x150")
    global fe,fe1
    def f_r():
        # print(fe.get(),fe1.get())
        text.tag_remove('found', '1.0', END)  
      
        s = fe.get() 
        r = fe1.get() 
      
        if (s and r):  
            idx = '1.0'
            while 1:  
                # searches for desried string from index 1  
                idx = text.search(s, idx, nocase = 1,  
                                stopindex = END) 
                print(idx) 
                if not idx: break
                
                # last index sum of current index and  
                # length of text  
                lastidx = '% s+% dc' % (idx, len(s)) 
    
                text.delete(idx, lastidx) 
                text.insert(idx, r) 
    
                lastidx = '% s+% dc' % (idx, len(r)) 
                
                # overwrite 'Found' at idx  
                text.tag_add('found', idx, lastidx)  
                idx = lastidx  
    
            # mark located string as red 
            text.tag_config('found', foreground ='red', background = '#add8e6')
            window.destroy() 

        
    f=Label(window,text="Find :").place(relx=.1,rely=.1)
    fe=Entry(window,bd=1,bg="#CFDAD8")
    fe.place(relx=.3,rely=.1)
    f1=Label(window,text="Replace :").place(relx=.1,rely=.4)
    fe1=Entry(window,bd=1,bg="#CFDAD8")
    fe1.place(relx=.3,rely=.4)
    btn=Button(window,text="Replace",bd=3,bg="#add8e6",command=f_r)
    btn.place(relx=.4,rely=.7)
    window.mainloop()

def word_c():
    t=text.get("1.0",'end')
    t=t.split()
    t=len(t)
    showinfo(title="word count", message=f"{t} words ")
def char_c():
    t=text.get("1.0",'end')
    t=t.split()
    t="".join(t)
    t=len(t)
    showinfo(title="Characters count", message=f"{t} characters ")

def c_time():
    # print("Created: %s" % time.ctime(os.path.getctime(file)))
    if file==None or len(file)==0:
        showerror(title="Not availabe",message="You are working with Untracked file")
    else :
        showinfo(title="Created Time", message=f"Created : {time.ctime(os.path.getmtime(file))} ")

def m_time():
    # print("Last modified: %s" % time.ctime(os.path.getmtime(file)))
    if file==None or len(file)==0:
        showerror(title="Not availabe",message="You are working with Untracked file")
    else:
        showinfo(title="Modified Time", message=f"Last modified : {time.ctime(os.path.getmtime(file))} ")



if __name__ == "__main__":
    root=Tk()
    root.title("untitled - Notepad")
    root.geometry("700x500")
    # root.config(bg="#000000")
    text=Text(root,)
    text.pack(fill=BOTH,expand=True)
    file =None

    #menu
    menu=Menu(root,bd=2)

    file_menu=Menu(menu,tearoff=0)
    file_menu.add_command(label="New",command=new_file)
    file_menu.add_command(label="Open",command=open_file)
    file_menu.add_command(label="Save",command=save_file)
    file_menu.add_command(label="Save As",command=saveas_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit",command=exit_file)
    menu.add_cascade(label="File",menu=file_menu)

    edit_menu=Menu(menu,tearoff=0)
    edit_menu.add_command(label="Cut",command=cut)
    edit_menu.add_command(label="Copy",command=copy)
    edit_menu.add_command(label="Paste",command=paste)
    edit_menu.add_command(label="Find",command=find)
    edit_menu.add_command(label="Find & Replace",command=find_r)
    menu.add_cascade(label="Edit",menu=edit_menu)

    stats_menu=Menu(menu,tearoff=0)
    stats_menu.add_command(label="Word Count",command=word_c)
    stats_menu.add_command(label="Char Count",command=char_c)
    stats_menu.add_command(label="Created Time",command=c_time)
    stats_menu.add_command(label="Modified Time",command=m_time)
    menu.add_cascade(label="Stats",menu=stats_menu)

    fontsize_menu=Menu(menu,tearoff=0)
    fontsize_menu.add_command(label="6 px",command=font1)
    fontsize_menu.add_command(label="8 px",command=font2)
    fontsize_menu.add_command(label="10 px",command=font3)
    fontsize_menu.add_command(label="12 px",command=font4)
    fontsize_menu.add_command(label="14 px",command=font5)
    fontsize_menu.add_command(label="16 px",command=font6)
    fontsize_menu.add_command(label="18 px",command=font7)
    fontsize_menu.add_command(label="20 px",command=font8)
    fontsize_menu.add_command(label="22 px",command=font9)
    fontsize_menu.add_command(label="24 px",command=font10)
    menu.add_cascade(label="Font Size",menu=fontsize_menu)

    theme_menu=Menu(menu,tearoff=0)
    theme_menu.add_command(label="Light theme",command=light)
    theme_menu.add_command(label="dark theme",command=dark)
    menu.add_cascade(label="Theme",menu=theme_menu)


    ab=Menu(menu,tearoff=0)
    ab.add_command(label="About",command=about)
    menu.add_cascade(label="Help",menu=ab)

    root.config(menu=menu)

    # scroll bar code 
    scroll=Scrollbar(text)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    text.tag_bind('found','<Button-1>',lambda x: text.tag_remove('found', '1.0', END)) 
    text.bind("<Button-1>",lambda x: text.tag_remove('found', '1.0', END))

    root.mainloop()