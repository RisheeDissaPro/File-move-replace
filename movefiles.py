import os
import shutil

#Folder path defined
os.chdir('/Users/RISHEE/Desktop/Test')

for item in os.listdir():
     file_name = item[0:4]
     if not os.path.exists(file_name):
          os.mkdir(file_name)
     shutil.move(os.path.join(item), os.path.join(file_name))