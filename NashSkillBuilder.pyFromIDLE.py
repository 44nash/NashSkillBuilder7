# Marcus Nash
# 12/1/15
# SkillBuilder 7
# Ms.Patel

#1

''' Takes a string as a parameter and returns a string containing the only letters and digits
    User must enter the correct file.
    Output is returning a file with only the Letters, numbers and the spaces.'''

def  removePunctuations(word):
    out = ''
    possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxz0123456789 '
    for x in word:
        if x in possible:
            out = out + x
    return(out)
#(removePunctuations(input("Enter word:")))


#2
'''Takes a file as a parameter and returns a dictionary containing the words as keys and the number of times the key appears in the file as the corresponding valuese
    User must enter the correct file.
    Output is returning a dictionary of all the words and how many time they are in a given file.'''
def countwords(file):
    filename = "C:\\Users\\44nas\\Downloads\\"+file
   # print(filename)
    infile = open(filename,"r").read()
    s = []
    out = removePunctuations(infile)
    wordList = out.split()
    #print(wordList)
    for x in wordList:
            if x not in s:
                p = (x,infile.count(x))
                s.append(p)
    x = (dict(s))
    return x
#(countwords("fileDict.txt"))




#3
'''Prints the keys and their values in alphabetical order.
    User enters file.
    Output is returning a dictionary of all the words and how many time they are in a given file in order.'''
def printDictionary(dict):
    alpha= sorted(dict.keys())
    for i in alpha:
        print(i,dict[i])
#(printDictionary(countwords("fileDict.txt")))


#4
'''Takes file as a parameter and prints the students’ record.
    User has to enter a file.
    Give back a list of a persons Name, D-Number, Total credit,Total grade, and the GPA
    .'''
def printStudentRecord(file):
    filename="C:\\Users\\44nas\\Downloads\\"+file
    #print(filename)
    infile = open(filename,"r").read()
    out = []

    y = infile.split()

    print('{:>39}'.format('Total credit'),end='')
    print('{:>15}'.format('Total grade'))
    print('{:<15}'.format('D-Number'),end='')
    print('{:>7}'.format('Name'),end='')
    print('{:>15}'.format('Hour'),end='')
    print('{:>15}'.format('Points'),end='')
    print('{:>10}'.format('GPA'))
    print('-----'*13)
    print('{:<15}'.format(y[0]),end='')
    print('{:>7}'.format(y[1]),end='')
    print('{:>15}'.format(y[2]),end='')
    print('{:>15}'.format(y[3]),end='')
    print('{:>10.2f}'.format(int(y[3])/int(y[2])))
    print('{:<15}'.format(y[4]),end='')
    print('{:>7}'.format(y[5]),end='')
    print('{:>15}'.format(y[6]),end='')
    print('{:>15}'.format(y[7]),end='')
    print('{:>10.2f}'.format(int(y[7])/int(y[6])))
    print('{:<15}'.format(y[8]),end='')
    print('{:>7}'.format(y[9]),end='')
    print('{:>15}'.format(y[10]),end='')
    print('{:>15}'.format(y[11]),end='')
    print('{:>10.2f}'.format(int(y[11])/int(y[10])))
#printStudentRecord("studentData.txt")


