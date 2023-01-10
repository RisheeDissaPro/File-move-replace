import os
import shutil

# Folder path defined for os module to identify 
folder_path = r"C:\Users\RISHEE\Desktop\Test"

if (os.path.exists(folder_path)):
     os.chdir(folder_path)
     # for loop will iterate through all the files in the defined path
     for item in os.listdir():
          # Seperate first 4 strings of the folder name
          road_name = item[0:4]
          if not os.path.exists(road_name):
               os.mkdir(road_name)
          shutil.move(item, road_name)
          print(f"{road_name} Successfully moved")
else:
     print("Folder Path is incorrect or does not exist")
