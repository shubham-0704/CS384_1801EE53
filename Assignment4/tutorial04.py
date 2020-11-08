import os
import shutil
import pandas as pd


#code to remove previous files
path=os.getcwd()
path=os.path.join(path,"grades")
if  os.path.isdir(path):
    shutil.rmtree(path)

# make grades folder
path=os.getcwd()
path=os.path.join(path,"grades")
if not os.path.isdir(path):
    os.mkdir(path)


grade_equivalent={
    "AA":10,"AB":9,"BB":8,"BC":7,
    "CC":6,"CD":5,"DD":4,"F":0,"I":0
}

# reading csv file and proccesing 
data=pd.read_csv("acad_res_stud_grades.csv")
data=data[['roll','sem','sub_code','total_credits','credit_obtained','sub_type']]

roll_list=data["roll"].unique()
data=data.groupby("roll")
df_misc=pd.DataFrame()