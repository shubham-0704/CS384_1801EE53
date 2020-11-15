import os
import re

def rename_FIR(folder_name):
    #rename Logic 
    path=os.path.join(os.getcwd(),"subtitles",folder_name)
    title=input("Main Title of the Web Series: ")
    epi_pad=int(input("Episode Number Padding: "))
    l=list()
    s=set()
    for name in os.listdir(path):
        ep_num=str(int(re.search(r'[0-9]+',name).group()))
        src=os.path.join(path,name)
        file_type=name.split(".")[-1]
        f_name=title+" - "+" Episode "+ep_num.zfill(epi_pad)+"."+file_type
        des=os.path.join(path,f_name)
        if not os.path.isfile(des):
            os.rename(src,des)
        else :
            os.remove(src)  
    

def rename_Game_of_Thrones(folder_name):
    # rename Logic
    pass 
    

def rename_Sherlock(folder_name):
    # rename Logic
    pass 
    

def rename_Suits(folder_name):
    # rename Logic 
    pass
    

def rename_How_I_Met_Your_Mother(folder_name):
    # rename Logic 
    pass
    