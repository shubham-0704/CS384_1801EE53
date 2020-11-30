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

filename = "Btech_2020_master_data.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)