
chk_file = input("File: ")
#in VS>> C:/Users/avery/OneDrive/Documents/GitHub/Test/testing.txt

checklist = ''
#chk_file = '.\code\Checks.txt'

with open(chk_file) as f:
    for line in f:
        checklist = checklist + line
checklist = checklist.split('\n')

