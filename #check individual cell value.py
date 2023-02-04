#check individual cell value

import openpyxl
from openpyxl import load_workbook

hw2 = '.\code\INFS247HW2.xlsx'
wb = load_workbook(hw2)

emp = wb["Employees"]
check = emp['F8']
print(check.value)
