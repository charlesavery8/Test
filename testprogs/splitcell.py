ipt = 'B 3:B 13'
#ipt = input() #input cells like this: B 3:B 13

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

    return(intcells)


print(formatcells(ipt))