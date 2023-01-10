import os
import openpyxl

os.chdir('/Users/RISHEE/Desktop/Test')
# os.chdir('C:\Users\RISHEE\Desktop\Test')
name_path = "D:\Road Names.xlsx"

wb = openpyxl.load_workbook(name_path)
worksheet = wb['Sheet1']

for item in os.listdir():
    for cell in worksheet['A']:
        if cell.value == item:
            row_cordinate = cell.row
            column_cordinate = cell.column+1
            # print(row_cordinate, column_cordinate)
            print(worksheet.cell(row_cordinate, column_cordinate).value)

    
