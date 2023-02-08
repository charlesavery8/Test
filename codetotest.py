
#almost works

f = '.\code\Checks.txt'
hw2 = '.\code\INFS247HW2.xlsx'
wb = load_workbook(hw2)


def let_conv(abc): #one char can pass through; int is output
        try: #if letter...
            abc = abc.casefold()
            dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    
            try:
                nums = dict[abc] #if one letter i.e. 'A'; if more than one, key error >> move to except
            except:
                nums = 26*dict[abc[0]]+dict[abc[1]] #if two letters i.e. 'AA', takes first formatted value (A=1)*26 and adds 2nd (26+1)
        except: #if number...
            nums = int(abc)
       
        return nums

def formatcells(cell):
    cell = cell.split(":")
    y = []
    intcells = []

    for item in cell:
        item = item.split(" ")
        y = y + item
    for c in y:
    
        c = let_conv(c)
        intcells.append(c)

    return(intcells) #format cells function takes cell range like B_3:B_13, splits letters from numbers and formats char as int

def parsechecks(file): #outputs each line in file as [(sheetname, cellrange, arg, value)] as form_chk
    
    
    checklist = ''
    with open(file) as f:  #open checks, checklist is list with checks as items
        for line in f:
            checklist = checklist + line
    checklist = checklist.split('\n')
    
    
    form_ck = []

    for check in checklist:
        check = check.split(' ')
        sheetname = check[0]
        sheetname = sheetname.replace("_", " ")
        cellrange = check[1]
        cellrange = cellrange.replace("_", " ")
        cellrange = formatcells(cellrange) #calls user defined function formatcells inside of user defined function; caution
        arg = check[2]
        value = check[3]
        ans = (sheetname, cellrange, arg, value)
        form_ck.append(ans)
        
    return form_ck

#print(parsechecks(f)) #runs checklist against excel; answers == the values of the cells in the checks specified

formchecks = parsechecks(f)
list_ck =[]
for tup in formchecks: #outputs cells in list containing the cell ranges as a list [minr, minc, maxr, maxc]; B9>>B9:B9
    c = tup
    cells = c[1]
    sheetname = c[0]
    sheet = wb[sheetname]
    try: 
        minr= int(cells[1])
        minc= int(cells[0])
        maxr= int(cells[3])
        maxc= int(cells[2])
        list = [minr, minc, maxc, maxr]
    except:
        minr =int(cells[1])
        minc= int(cells[0])
        maxr= int(cells[1])
        maxc= int(cells[0])
        list = [minr, minc, maxc, maxr]
    finally:
        list_ck.append(list)
        for list in list_ck:
            print(list)
            for row in sheet.iter_cols(min_row = minr, min_col =minc, max_col = maxc, max_row = maxr, values_only=True):
                print(row)


