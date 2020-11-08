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

for num in range(len(roll_list)):
    df=data.get_group(roll_list[num])

    #for individual file 
    df1=pd.DataFrame()
    df1=df1.append([[f'Roll: {roll_list[num]}']])
    df1=df1.append([["Semester Wise Details"]])
    df1=df1.append([['Subject','Credits','Type','Grade','Sem']])

    df[['sub_code','total_credits','sub_type','credit_obtained','sem']]

    for i in df.index:
        df1=df1.append([[df['sub_code'][i],df['total_credits'][i],df['sub_type'][i],df['credit_obtained'][i],df['sem'][i]]],ignore_index=True)

    df1.to_csv(f'grades/{roll_list[num]}_individual.csv',index=False,header=False)