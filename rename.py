import os
import openpyxl

# Folder path defined for os module to identify 
folder_path = r"C:\Users\RISHEE\Desktop\Test"
name_path = "D:\Road Names.xlsx"

wb = openpyxl.load_workbook(name_path)
worksheet = wb['Sheet1']

os.chdir('/Users/RISHEE/Desktop/Test')
for item in os.listdir():
    for cell in worksheet['A']:
        if cell.value == item:
            row_cordinate = cell.row
            column_cordinate = cell.column+1
            road_name = worksheet.cell(row_cordinate, column_cordinate).value
            new_name = f"{item} - {road_name}"
            os.rename(item, new_name ) 
            print(f"{item} Successfully renamed")
