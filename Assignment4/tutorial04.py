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

    #for overall file

    df2=pd.DataFrame()
    df2=df2.append([[f'Roll: {roll_list[num]}']],ignore_index=True)
    df2=df2.append([['Semester','Semester Credits','Semester Credits Cleared','SPI','Total Credits','Total Credits Cleared','CPI']],ignore_index=True)
    sem_num=df['sem'].unique()
    sorted(sem_num)
    tot_cred=0
    tot_clear=0
    cpi=0
    for num1 in range(len(sem_num)):
        df_temp=df[df['sem']==sem_num[num1]]
        sem_cred=df_temp['total_credits'].sum()
        sem_cleared=0
        spi=0
        for i1 in df_temp.index:
            # if df_temp.loc[i1].isnull().sum()>0:
            #     df_misc.append(df_temp.iloc[i1])
            if df_temp.loc[i1].isnull().sum()>0:
                df_misc=df_misc.append(df_temp.loc[i1])
            elif grade_equivalent[df_temp['credit_obtained'][i1]] !=0:
                sem_cleared+=df_temp['total_credits'][i1]
                spi+=grade_equivalent[df_temp['credit_obtained'][i1]]*df_temp['total_credits'][i1]

        spi/=sem_cred 
        cpi=(cpi*tot_cred+spi*sem_cred)/(tot_cred+sem_cred)
        tot_cred+=sem_cred
        tot_clear+=sem_cleared
        
        df2=df2.append([[sem_num[num1],sem_cred,sem_cleared,round(spi,2),tot_cred,tot_clear,round(cpi,2)]],ignore_index=True)

        df2.to_csv(f'grades/{roll_list[num]}_overall.csv',index=False,header=False)

df_misc.to_csv(f'grades/misc.csv',index=False,columns=["roll","sem","sub_code","total_credits","credit_obtained","sub_type"])