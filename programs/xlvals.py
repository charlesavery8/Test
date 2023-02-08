
#print(vals) @ the end will output values of specified cells from specified worksheet

f = '.\code\Checks.txt'
hw2 = '.\code\INFS247HW2.xlsx'
wb = load_workbook(hw2)


def let_conv(abc): #one char can pass through; int is output
        try: #if letter...
            abc = abc.casefold()
            dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16,'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    
            try:
                nums = dict[abc] #if one letter i.e. 'A'; if more than one, key error >> move to except
            except:
                nums = 26*dict[abc[0]]+dict[abc[1]] #if two letters i.e. 'AA', takes first formatted value (A=1)*26 and adds 2nd (26+1)
        except: #if number...
            nums = int(abc)
       
        return nums

def formatcells(cell): #format cells function takes cell range like B 3:B 13 >>> [2, 3, 2, 13]
    cell = cell.split(":")
    clist = []
    intcells = []

    for item in cell:
        item = item.split(" ")
        clist = clist + item
    for c in clist:
    
        c = let_conv(c) #uses user defined function; caution
        intcells.append(c)

    return(intcells) 

def parsechecks(file): #outputs each line in file as [(sheetname, cellrange, arg, value)] as form_chk
    
    checklist = ''
    with open(file) as f:  #open checks, checklist is string with checks as items
        for line in f:
            checklist = checklist + line
    checklist = checklist.split('\n') 
    
    form_ck = []

    for check in checklist: #parses checks in checklist and assigns each term to sheetname, cellrange, arg, and chk_value respectively
        check = check.split(' ')
        sheetname = check[0]
        sheetname = sheetname.replace("_", " ")
        cellrange = check[1]
        cellrange = cellrange.replace("_", " ")
        cellrange = formatcells(cellrange) #calls user defined function formatcells inside of user defined function; caution
        arg = check[2]
        chk_value = check[3]
        ans = (sheetname, cellrange, arg, chk_value)
        form_ck.append(ans)
        
    return form_ck


formcheck = parsechecks(f) #formcheck assigned form_ck>>[(sheetname, cellrange, arg, chk_value)]


def valcheck(formchecks): #takes [(sheetname, [cellrange], arg, value)], returns values for indicated cellrange and sheetname
    list_ck =[]
    name =''
    for tup in formchecks: #returns list_ck containing the cell ranges each as a list [minr, minc, maxc, maxr]; B9>>B9:B9
        c = tup
        cells = c[1]
        sheetname = c[0]
        try: 
            name = sheetname
            minr= int(cells[1])
            minc= int(cells[0])
            maxr= int(cells[3])
            maxc= int(cells[2])
            list = [name, minr, minc, maxc, maxr]
        except:
            name =sheetname
            minr =int(cells[1])
            minc= int(cells[0])
            maxr= int(cells[1])
            maxc= int(cells[0])
            list = [name, minr, minc, maxc, maxr]
        finally: 
            list_ck.append(list)
    values = []
    for list in list_ck: #list_ck is list the holds formated cell ranges; B10 >> [10, 2, 2, 10]; B4:AA6 >> [4, 2, 27, 6]; formatted for .iter_cols()
        name = list[0]
        sheet = wb[name]
        minr = list[1]
        minc = list[2]
        maxc = list[3]
        maxr = list[4]
        for row in sheet.iter_cols(min_row = minr, min_col =minc, max_col = maxc, max_row = maxr, values_only=True):
                values.append(row)
    return values

vals = valcheck(formcheck)


