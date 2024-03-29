import os
import re

def rename_FIR(folder_name):
    #rename Logic 
    path=os.path.join(os.getcwd(),"subtitles",folder_name)
    # title=input("Main Title of the Web Series: ")
    title="FIR"
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
    # title=input("Main Title of the Web Series: ")
    title="Game of Thrones"
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
    # title=input("Main Title of the Web Series: ")
    title='Sherlock'
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
    # title=input("Main Title of the Web Series: ")
    title='Suits'
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
    path=os.path.join(os.getcwd(),"subtitles",folder_name)
    # title=input("Main Title of the Web Series: ")
    title='How I Met Your Mother'
    sea_pad=int(input("Season Number Padding: "))
    epi_pad=int(input("Episode Number Padding: "))

    for name in os.listdir(path):
        src=os.path.join(path,name)
        name=name.split(".")
        file_type=name[-1]
        name=name[0].split("-")
        ep_name=name[-1]
        if len(name)==3:
            name=name[-2]
            sea_num,ep_num=[str(int(x)) for x in name.split("x")]
            f_name=title+" - "+"Season "+ sea_num.zfill(sea_pad)+" Episode "+ep_num.zfill(epi_pad)+" - "+ep_name+"."+file_type
        else :
            name,ep_num2=name[-3:-1]
            sea_num,ep_num1=[str(int(x)) for x in name.split("x")]
            f_name=title+" - "+"Season "+ sea_num.zfill(sea_pad)+" Episode "+ep_num1.zfill(epi_pad)+"-"+ep_num2.zfill(epi_pad)+" - "+ep_name+"."+file_type

        des=os.path.join(path,f_name)
        if not os.path.isfile(des):
            os.rename(src,des)
        else :
            os.remove(src)
    

# series=input("Main Title of the Web Series to rename: ")
# if series=="Game of Thrones":
#     try:
#         rename_Game_of_Thrones('Game of Thrones')
#     except:
#         print("Already webseries is renamed")
# elif series=="Sherlock":
#     rename_Sherlock('Sherlock')
# elif series=="Suits":
#     rename_Suits('Suits')
# elif series=="FIR":
#     rename_FIR("FIR")
# elif series=="How I Met Your Mother":
#     rename_How_I_Met_Your_Mother('How I Met Your Mother')

count=13
while  count:
    print("""\n select webseries title options to rename
    1.Game of Thrones
    2.Sherlock
    3.Suits
    4.FIR
    5.How I Met Your Mother
    6.Exit""")
    a=input("Enter option : ")
    if a=="1":
        try:
            rename_Game_of_Thrones('Game of Thrones')
        except:
            print("\n   !!!!!  Already webseries is renamed  !!!!! ")
    elif a=="2":
        try:
            rename_Sherlock('Sherlock')
        except:
            print("\n   !!!!!  Already webseries is renamed  !!!!! ")
    elif a=="3":
        try:
            rename_Suits('Suits')
        except:
            print("\n   !!!!!  Already webseries is renamed  !!!!! ")           
    elif a=="4":
        try:
            rename_FIR("FIR")
        except:
            print("\n   !!!!!  Already webseries is renamed  !!!!! ")
    elif a=="5":
        try:
            rename_How_I_Met_Your_Mother('How I Met Your Mother')
        except:
            print("\n   !!!!!  Already webseries is renamed  !!!!! ")
    elif a=="6":
        break
    else :
        print("\nPlease provide a valid input ..!")

    count-=1

