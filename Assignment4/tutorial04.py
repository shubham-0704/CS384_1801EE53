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