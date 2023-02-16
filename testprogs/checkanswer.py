# check if the values that are from previous output (even if arranged in different ways) are correct or wrong

formcheck = [('Employees', [2, 3, 2, 12], 'SUM_AVERAGE_MIN_MAX_MEDIAN_COUNTIF_IF'), ('Employees', [2, 13], 'Name'), ('Employees', [8, 12], '=G12*$H$2+G12'), ('New Location Loan Repayment', [2, 9], '=B8*B7')]

vals = [('=SUM(B3:B5)', '=AVERAGE(C2:C5)', '=MAX(C2:C5)', '=MIN(C2:C5)', '=MEDIAN(C2:C5)', '=COUNTIF(B3:B5, F2)', '=IF(B6 > F2, "Yes", "No")'), ('Charles',), ('=G12*$H$2+G12',), ('=B8*B7',)]


def sort_cor(form): #takes form as [(x, [1, 2], y), (a, [1, 3], z)] and takes the third term in each item and sorts to a dict as 'ckdict' {check#: correct answer}
    correct = []
    for item in form:
        chk = item[2]
        chk = chk.split("_")
        correct.append(chk)
    ckdict = dict()
    num = 1
    for i in correct:
        x = i
        c = "check" + str(num)
        ckdict.update({c:x})
        num+=1
    return ckdict

def sort_ans(valz): #takes valz as [(x), (y),(z)] and places x y z into list 'answers'
    answers = []
    
    for item in valz:
        items = []
        for i in item:
            items.append(i)
        x = items
        answers.append(x)
    ansdict = dict()
    num = 1 
    for i in answers:
        x = i
        c = "answer" + str(num)
        ansdict.update({c:x})
        num+=1

    return ansdict

crct = sort_cor(formcheck) #crct is the correct answers 
answ = sort_ans(vals) #answ is the provided answers (by student) 

def checkanswers(correct, answers): #checks if answers are right/wrong based on correct dictionary; Correct answers replaced with "Correct"
    cnt = 0
    for x in correct:
        cnt+=1
        c = "check" + str(cnt)
        a = "answer" + str(cnt)
        if len(correct.get(c)) > 1:
            ck = correct.get(c)
            an = answers.get(a)

            for c in ck:
                for n in an:
                    if c in n:
                        answers.update({a:" Correct"})                    
        else:
            ck = correct.get(c)
            an = answers.get(a)
        
            if correct.get(c) == answ.get(a):
                answers.update({a:" Correct"})
                #print("Yes", crct.get(c))
            else:
                an.insert(0, 'ANSWER IS: ' + str(ck))
                answers.update({a: an})
                #print("Answer is:", crct.get(c), "-- not", answ.get(a))
    return answers

grd_hw =(checkanswers(crct, answ))

def score(hw):
    c = 0
    tot = len(hw)
    for x in hw:
        val = hw.get(x)
        if val == " Correct":
            c += 1
    score = c/tot
    return (score)

print(score(grd_hw))
