import csv
import re
import os


def course():
    path=os.getcwd()
    # path=path+r"/analytics/course"
    path=os.path.join(path,"analytics","course")
    if not os.path.isdir(path):
        os.makedirs(path)
    file=open('studentinfo_cs384.csv','r')
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
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
