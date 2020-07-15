import shutil
import os

shutil.copyfile("ceps.csv", r"C:\Users\x_kat\Desktop\Teste")
print(os.listdir(os.getcwd()))


import glob

lst  = glob.glob("*ceps*")
print(lst) # ['ceps.csv']