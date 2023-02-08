ipt = input()

def let_conv(abc):
    try:
        abc = abc.casefold()
        dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    
        try:
            nums = dict[abc]
        except:
            nums = 26*dict[abc[0]]+dict[abc[1]]
    except:
       nums = int(abc)
       
    return nums
out = let_conv(ipt)
print(out)
