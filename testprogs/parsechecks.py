f = 'testing.txt'


def parsechecks(file): #outputs each line in file as [(sheetname, cellrange, arg, value/n)] in answers
    #file = 'testing.txt'
    
    checklist = open(file, 'r')
    answers = []

    for check in checklist:
        check = check.split(' ')
        sheetname = check[0]
        sheetname = sheetname.replace("_", " ")
        cellrange = check[1]
        arg = check[2]
        value = check[3]
    
        #sheet = wb[sheetname]
        #ans = sheet[cellrange]

        ans = (sheetname, cellrange, arg, value)
        answers.append(ans)
        try:
            answers.append(ans)
        except:
            for row in sheet.iter_cols(min_row = 3, min_col =1, max_col = 1, max_row = 13, values_only=True):
                answers.append(row)
    return answers


print(parsechecks(f))