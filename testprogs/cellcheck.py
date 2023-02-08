#check individual cell value

import openpyxl
from openpyxl import load_workbook

hw2 = '.\code\INFS247HW2.xlsx'
wb = load_workbook(hw2)

Sheet_emp = wb["Employees"]
cell = 'F8'
check = Sheet_emp[cell]
print(check.value)
