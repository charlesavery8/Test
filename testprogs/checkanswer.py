# check if the values that are from previous output (even if arranged in different ways) are correct or wrong

formcheck = [('Employees', [2, 3, 2, 12], 'filled'), ('Employees', [2, 13], 'Name'), ('Employees', [8, 12], '=G12*$H$2+G12'), ('New Location Loan Repayment', [2, 9], '=B8*B7')]

vals = [('First Name', 'Gabby', 'Luke ', 'Sally', 'Jon', 'Dean', 'Jackson', 'Oliver', 'Mary', 'Faith'), ('Charles',), ('=G12*$H$2+G12',), ('=B8*B7',)]

correct = []
answers = []

for item in formcheck:
    chk = item[2]
    correct.append(chk)
for item in vals:
    x = item[0]
    answers.append(x)
    for y in item:
        print(y)
print(answers)
print(correct) 
