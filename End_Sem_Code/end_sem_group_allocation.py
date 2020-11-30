import os
import shutil
import pandas as pd 

def group_allocation(filename, number_of_groups):
    # Entire Logic 
    #code to remove previous files if present
    path=os.getcwd()
    path=os.path.join(path,"groups")
    if  os.path.isdir(path):
        shutil.rmtree(path)

    # make groups folder
    path=os.getcwd()
    path=os.path.join(path,"groups")
    if not os.path.isdir(path):
        os.mkdir(path)
    
    # file opening and proccesing
    data=pd.read_csv(filename)
    data["branch"]=[ x[4:6] for x in data["Roll"]]
    branch=data["branch"].unique()
    # print(branch)
    data=data.groupby("branch")


    df_str=pd.DataFrame(columns=["BRANCH_CODE","STRENGTH"])
    for i in branch:
        df=data.get_group(i)
        # print(i,df.shape[0])
        df=df.sort_values(["Roll"], ascending=[True])
        df.to_csv(f"groups/{i}.csv",index=False,columns=["Roll","Name","Email"])
        df_str=df_str.append({"BRANCH_CODE":i,"STRENGTH":df.shape[0]},ignore_index=True)
    df_str.sort_values(["STRENGTH","BRANCH_CODE"], ascending=[False, True], inplace=True)
    df_str.to_csv(f"groups/branch_strength.csv",index=False)
filename = "Btech_2020_master_data.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)