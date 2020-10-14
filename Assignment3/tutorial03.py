import csv
import re
import os


def course():
    # Read csv and process
    pass


def country():
    # Read csv and process
    pass


def email_domain_extract():
    # Read csv and process
    pass


def gender():
    path=os.getcwd()
    path=path+r"/analytics/gender"
    if not os.path.isdir(path):
        os.makedirs(path)
    file=open('studentinfo_cs384.csv','r')
    m=open(path+r"/male.csv",'w',newline="")
    f=open(path+r"/female.csv",'w',newline="")
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
