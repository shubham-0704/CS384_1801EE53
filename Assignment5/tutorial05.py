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
    path=os.path.join(os.getcwd(),"subtitles",folder_name)
    title=input("Main Title of the Web Series: ")
    sea_pad=int(input("Season Number Padding: "))
    epi_pad=int(input("Episode Number Padding: "))

    for name in os.listdir(path):
        src=os.path.join(path,name)
        name=name.split(".")
        file_type=name[-1]
        name=name[0].split("-")
        ep_name=name[-1]
        name=name[-2]
        sea_num,ep_num=[str(int(x)) for x in name.split("x")]
        f_name=title+" - "+"Season "+ sea_num.zfill(sea_pad)+" Episode "+ep_num.zfill(epi_pad)+" - "+ep_name+"."+file_type
        des=os.path.join(path,f_name)
        os.rename(src,des)
    

def rename_Sherlock(folder_name):
    # rename Logic 
    path=os.path.join(os.getcwd(),"subtitles",folder_name)
    title=input("Main Title of the Web Series: ")
    sea_pad=int(input("Season Number Padding: "))
    epi_pad=int(input("Episode Number Padding: "))

    for name in os.listdir(path):

            src=os.path.join(path,name)
            file_type=name.split(".")[-1]
            sea_num=str(int(re.search(r'S[0-9]{2}',name).group()[1:]))
            ep_num=str(int(re.search(r'E[0-9]{2}',name).group()[1:]))
            f_name=title+" - "+"Season "+ sea_num.zfill(sea_pad)+" Episode "+ep_num.zfill(epi_pad)+"."+file_type
            des=os.path.join(path,f_name)
            if not os.path.isfile(des):
                os.rename(src,des)
            else :
                os.remove(src) 
    

def rename_Suits(folder_name):
    # rename Logic 
    path=os.path.join(os.getcwd(),"subtitles",folder_name)
    title=input("Main Title of the Web Series: ")
    sea_pad=int(input("Season Number Padding: "))
    epi_pad=int(input("Episode Number Padding: "))

    for name in os.listdir(path):

            src=os.path.join(path,name)
            name=name.split(".")
            file_type=name[-1]
            name=name[0].split("-")
            ep_name='-'.join(name[2:])
            name=name[1]
            sea_num,ep_num=[str(int(x)) for x in name.split("x")]
            f_name=title+" - "+"Season "+ sea_num.zfill(sea_pad)+" Episode "+ep_num.zfill(epi_pad)+" - "+ep_name+"."+file_type
            des=os.path.join(path,f_name)
            if not os.path.isfile(des):
                os.rename(src,des)
            else :
                os.remove(src)
    

def rename_How_I_Met_Your_Mother(folder_name):
    # rename Logic 
    pass
    