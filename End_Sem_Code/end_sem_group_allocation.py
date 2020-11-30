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


    # making groups
    nog=number_of_groups
    col=list(df_str["BRANCH_CODE"])
    col.insert(0,"total")
    col.insert(0,"group")
    bran_str = dict.fromkeys(list(df_str["BRANCH_CODE"]),0)
    list_grp=list(range(nog))
    list_grp=[bran_str.copy() for x in list_grp]
    df=pd.DataFrame(columns=col)

    for i,x in zip(df_str["BRANCH_CODE"],df_str["STRENGTH"]):
        for n in range(nog):
            list_grp[n][i]=x//nog
        bran_str[i]=(x-((x//nog)*nog))
    a=0
    for i,x in bran_str.items():
        # print(i,x)
        while(x):
            list_grp[a][i]+=1
            x-=1
            a+=1
            a=a%nog
    for i in range(nog):
        list_grp[i]["total"]=sum(list_grp[i].values())
        list_grp[i]["group"]="Group_G"+str(i+1).zfill(2)+".csv"


    df=df.append(list_grp)
    df.to_csv(f"groups/stats_grouping.csv",index=False)
    bran_str = dict.fromkeys(list(df_str["BRANCH_CODE"]),0)
    # print(df)
    for i in range(nog):
        df_gp=pd.DataFrame()
        grp_name=list_grp[i]["group"]
        for nm in list(df_str["BRANCH_CODE"]):
            n=list_grp[i][nm]
            df_temp=data.get_group(nm)
            df_gp=df_gp.append(df_temp.iloc[bran_str[nm]:bran_str[nm]+n,:])
            bran_str[nm]+=n
        df_gp.to_csv(f"groups/{grp_name}",index=False,columns=["Roll","Name","Email"]) 



filename = "Btech_2020_master_data.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)