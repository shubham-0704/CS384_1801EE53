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