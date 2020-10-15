import csv
import re
import os
import shutil

def del_create_analytics_folder():
    #code to remove previous files
    path=os.getcwd()
    path=os.path.join(path,"analytics")
    if  os.path.isdir(path):
        shutil.rmtree(path)
    # mkdir the analytics folder (only mkdir)
    path=os.getcwd()
    path=os.path.join(path,"analytics")
    if not os.path.isdir(path):
        os.makedirs(path)


def course():
    path=os.getcwd()
    # path=path+r"/analytics/course"
    path=os.path.join(path,"analytics","course")
    if not os.path.isdir(path):
        os.makedirs(path)
    file=open('studentinfo_cs384.csv','r')
    # file=open(os.path.join(os.getcwd(),'studentinfo_cs384.csv'),"r")
    fieldname=""
    reader=csv.DictReader(file)
    fieldname=reader.fieldnames
    pattern=re.compile(r"[0-9]{4}[a-zA-Z]{2}[0-9]{2}")
    course_name={"01":"btech","11":"mtech","12":"msc","21":"phd"}
    course_num=["01","11","12","21"]
    for line in reader:
        if re.fullmatch(pattern,line["id"]):
            branch=line["id"][4:6].lower()
            year=line["id"][0:2].lower()
            course=line["id"][2:4].lower()
            # course=course_name["%s"%course]
            if course in course_num:
                course=course_name[course]

                # if not os.path.isdir(path+r"/%s"%branch):
                #     os.makedirs(path+r"/%s"%branch)
                if not os.path.isdir(os.path.join(path,branch)):
                    os.makedirs(os.path.join(path,branch))

                # if not os.path.isdir(path+r"/%s/%s"%(branch,course)):
                #     os.makedirs(path+r"/%s/%s"%(branch,course))
                if not os.path.isdir(os.path.join(path,branch,course)):
                    os.makedirs(os.path.join(path,branch,course))
                flag=0
                file_name=year+"_"+branch+"_"+course+".csv"
                # if not os.path.isfile(path+r"/%s/%s/%s"%(branch,course,file_name)):flag=1
                if not os.path.isfile(os.path.join(path,branch,course,file_name)):flag=1
                # f=open(path+r"/%s/%s/%s"%(branch,course,file_name),'a+',newline="")
                f=open(os.path.join(path,branch,course,file_name),'a+',newline="")
                writer=csv.DictWriter(f,fieldnames=fieldname)
                if flag:writer.writeheader()
                writer.writerow(line)
            else:
                i="misc"+".csv"
                flag=0

                if not os.path.isfile(os.path.join(path,i)):flag=1
                f=open(os.path.join(path,i),'a+',newline="")
                
                writer=csv.DictWriter(f,fieldnames=fieldname)
                if flag:writer.writeheader()
                writer.writerow(line)

        else:
            i="misc"+".csv"
            flag=0

            if not os.path.isfile(os.path.join(path,i)):flag=1
            f=open(os.path.join(path,i),'a+',newline="")
            
            writer=csv.DictWriter(f,fieldnames=fieldname)
            if flag:writer.writeheader()
            writer.writerow(line)


def country():
    path=os.getcwd()
    # path=path+r"/analytics/country"
    path=os.path.join(path,"analytics","country")
    if not os.path.isdir(path):
        os.makedirs(path)
    file=open('studentinfo_cs384.csv','r')
    fieldname=""
    reader=csv.DictReader(file)
    fieldname=reader.fieldnames
    
    for line in reader:
        i=line["country"].lower()
        if len(i)!=0:
            i=i+".csv"
            flag=0
            # if not os.path.isfile(path+r'/%s.csv'%i):flag=1
            # f=open(path+r'/%s.csv'%i,'a+',newline="")

            if not os.path.isfile(os.path.join(path,i)):flag=1
            f=open(os.path.join(path,i),'a+',newline="")
            
            writer=csv.DictWriter(f,fieldnames=fieldname)
            if flag:writer.writeheader()
            writer.writerow(line)
        else:
            i="misc"+".csv"
            flag=0

            if not os.path.isfile(os.path.join(path,i)):flag=1
            f=open(os.path.join(path,i),'a+',newline="")
            
            writer=csv.DictWriter(f,fieldnames=fieldname)
            if flag:writer.writeheader()
            writer.writerow(line)


def email_domain_extract():
    path=os.getcwd()
    # path=path+r"/analytics/email_domain"
    path=os.path.join(path,"analytics","email_domain")
    if not os.path.isdir(path):
        os.makedirs(path)
    file=open('studentinfo_cs384.csv','r')
    fieldname=""
    reader=csv.DictReader(file)
    fieldname=reader.fieldnames
    
    for line in reader:
        i=line["email"].split("@")[1].split(".")[0].lower()
        if len(i)!=0:
            i=i+".csv"
            flag=0
            # if not os.path.isfile(path+r'/%s.csv'%i):flag=1
            # f=open(path+r'/%s.csv'%i,'a+',newline="")

            if not os.path.isfile(os.path.join(path,i)):flag=1
            f=open(os.path.join(path,i),'a+',newline="")
            
            writer=csv.DictWriter(f,fieldnames=fieldname)
            if flag:writer.writeheader()
            writer.writerow(line)
        else:
            i="misc"+".csv"
            flag=0

            if not os.path.isfile(os.path.join(path,i)):flag=1
            f=open(os.path.join(path,i),'a+',newline="")
            
            writer=csv.DictWriter(f,fieldnames=fieldname)
            if flag:writer.writeheader()
            writer.writerow(line)


def gender():
    path=os.getcwd()
    # path=path+r"/analytics/gender"
    path=os.path.join(path,"analytics","gender")
    if not os.path.isdir(path):
        os.makedirs(path)
    file=open('studentinfo_cs384.csv','r')
    m=open(os.path.join(path,"male.csv"),'w',newline="")
    # f=open(path+r"/female.csv",'w',newline="")
    f=open(os.path.join(path,"female.csv"),'w',newline="")
    with file:        
            reader=csv.DictReader(file)
            fieldname=reader.fieldnames
            with m:
                writer=csv.DictWriter(m,fieldnames=fieldname)
                writer.writeheader()
                for row in reader:
                         if(row["gender"].lower()=="male"):       
                                writer.writerow(row)
    file=open('studentinfo_cs384.csv','r')
    with file:
            reader=csv.DictReader(file)
            fieldname=reader.fieldnames       
            with f:
                writer=csv.DictWriter(f,fieldnames=fieldname)
                writer.writeheader()
                for row1 in reader:
                         if(row1["gender"].lower()=="female"):       
                                writer.writerow(row1)


def dob():
    path=os.getcwd()
    path=os.path.join(path,"analytics","dob")
    if not os.path.isdir(path):
        os.makedirs(path)
    file=open('studentinfo_cs384.csv','r')
    fieldname=""
    reader=csv.DictReader(file)
    fieldname=reader.fieldnames
    for line in reader:
        i=line["dob"]
        i=i.split("-")[2]
        if re.fullmatch(r"199[5-9]{1}",i) :
            i="bday_1995_1999"+".csv"
            flag=0

            if not os.path.isfile(os.path.join(path,i)):flag=1
            f=open(os.path.join(path,i),'a+',newline="")
            
            writer=csv.DictWriter(f,fieldnames=fieldname)
            if flag:writer.writeheader()
            writer.writerow(line)
        elif re.fullmatch(r"200[0-4]{1}",i) :
            i="bday_2000_2004"+".csv"
            flag=0

            if not os.path.isfile(os.path.join(path,i)):flag=1
            f=open(os.path.join(path,i),'a+',newline="")
            
            writer=csv.DictWriter(f,fieldnames=fieldname)
            if flag:writer.writeheader()
            writer.writerow(line)
        elif re.fullmatch(r"200[5-9]{1}",i) :
            i="bday_2005_2009"+".csv"
            flag=0

            if not os.path.isfile(os.path.join(path,i)):flag=1
            f=open(os.path.join(path,i),'a+',newline="")
            
            writer=csv.DictWriter(f,fieldnames=fieldname)
            if flag:writer.writeheader()
            writer.writerow(line)
        elif re.fullmatch(r"201[0-4]{1}",i) :
            i="bday_2010_2014"+".csv"
            flag=0

            if not os.path.isfile(os.path.join(path,i)):flag=1
            f=open(os.path.join(path,i),'a+',newline="")
            
            writer=csv.DictWriter(f,fieldnames=fieldname)
            if flag:writer.writeheader()
            writer.writerow(line)
        elif re.fullmatch(r"20[12]{1}[056789]{1}",i) :
            i="bday_2015_2020"+".csv"
            flag=0

            if not os.path.isfile(os.path.join(path,i)):flag=1
            f=open(os.path.join(path,i),'a+',newline="")
            
            writer=csv.DictWriter(f,fieldnames=fieldname)
            if flag:writer.writeheader()
            writer.writerow(line)
        else:
            i="misc"+".csv"
            flag=0

            if not os.path.isfile(os.path.join(path,i)):flag=1
            f=open(os.path.join(path,i),'a+',newline="")
            
            writer=csv.DictWriter(f,fieldnames=fieldname)
            if flag:writer.writeheader()
            writer.writerow(line)


def state():
    path=os.getcwd()
    # path=path+r"/analytics/state"
    path=os.path.join(path,"analytics","state")
    if not os.path.isdir(path):
        os.makedirs(path)
    file=open('studentinfo_cs384.csv','r')
    fieldname=""
    reader=csv.DictReader(file)
    fieldname=reader.fieldnames
    
    for line in reader:
        i=line["state"].lower()
        if len(i)!=0:
            i=i+".csv"
            flag=0
            # if not os.path.isfile(path+r'/%s.csv'%i):flag=1
            # f=open(path+r'/%s.csv'%i,'a+',newline="")

            if not os.path.isfile(os.path.join(path,i)):flag=1
            f=open(os.path.join(path,i),'a+',newline="")
            
            writer=csv.DictWriter(f,fieldnames=fieldname)
            if flag:writer.writeheader()
            writer.writerow(line)
        else:
            i="misc"+".csv"
            flag=0

            if not os.path.isfile(os.path.join(path,i)):flag=1
            f=open(os.path.join(path,i),'a+',newline="")
            
            writer=csv.DictWriter(f,fieldnames=fieldname)
            if flag:writer.writeheader()
            writer.writerow(line)


def blood_group():
    path=os.getcwd()
    # path=path+r"/analytics/country"
    path=os.path.join(path,"analytics","blood_group")
    if not os.path.isdir(path):
        os.makedirs(path)
    file=open('studentinfo_cs384.csv','r')
    fieldname=""
    reader=csv.DictReader(file)
    fieldname=reader.fieldnames
    
    for line in reader:
        i=line["blood_group"].lower()
        if len(i)!=0:
            i=i+".csv"
            flag=0
            # if not os.path.isfile(path+r'/%s.csv'%i):flag=1
            # f=open(path+r'/%s.csv'%i,'a+',newline="")

            if not os.path.isfile(os.path.join(path,i)):flag=1
            f=open(os.path.join(path,i),'a+',newline="")
            
            writer=csv.DictWriter(f,fieldnames=fieldname)
            if flag:writer.writeheader()
            writer.writerow(line)
        else:
            i="misc"+".csv"
            flag=0

            if not os.path.isfile(os.path.join(path,i)):flag=1
            f=open(os.path.join(path,i),'a+',newline="")
            
            writer=csv.DictWriter(f,fieldnames=fieldname)
            if flag:writer.writeheader()
            writer.writerow(line)


# Create the new file here and also sort it in this function only.
def new_file_sort():
    path=os.getcwd()
    path=os.path.join(path,"analytics")
    if not os.path.isdir(path):
        os.makedirs(path)
    file=open('studentinfo_cs384.csv','r')
    fieldname=""
    reader=csv.DictReader(file)
    fieldname=reader.fieldnames
    fieldname_new=fieldname.copy()
    fieldname_new.pop(1)
    fieldname_new.insert(1,"first_name")
    fieldname_new.insert(2,"last_name")

    rows=[]

    for line1 in reader:
        first_name=line1["full_name"].split()[0]
        last_name=line1["full_name"].split()[1:]
        last_name=" ".join(last_name)
        line1.pop("full_name")
        line1["first_name"]=first_name
        line1["last_name"]=last_name
        flag=0
        file_name="studentinfo_cs384_names_split.csv"
        if not  os.path.isfile(os.path.join(path,file_name)):flag=1
        f=open(os.path.join(path,file_name),'a',newline="")
        

        writer=csv.DictWriter(f,fieldnames=fieldname_new)
        if flag: writer.writeheader()
        writer.writerow(line1)
        rows.append(line1)

    rows.sort(key=lambda item:item.get("first_name"))
    file_name="studentinfo_cs384_names_split_sorted_first_name.csv"
    f=open(os.path.join(path,file_name),'a',newline="")
    writer=csv.DictWriter(f,fieldnames=fieldname_new)
    writer.writeheader()
    writer.writerows(rows)


