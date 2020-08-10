import csv
import matplotlib.pyplot as pyplot

a,b,c,d,e = 0,0,0,0,0
##def categorychecker(n, listname):
##    a = 0
##    if row[n] in listname:
##        a = a+1
##    else:
##        listname.append(row[n])
    
genetic = []
physical = []
regulatory = []
lessthan9 = []
between9and11=[]
greater11 = []

with open('interactions.txt', 'r') as tsvfile:
    writer = csv.reader(tsvfile, delimiter='\t')
    next(writer)
    for row in writer:
        a = a+1
        if 7<len(row)<10:
            b = b+1
            if row[7] not in lessthan9:
                lessthan9.append(row[7])
        elif len(row) == 10:
            c = c+1
            if (row[6],row[9]) not in between9and11:
                between9and11.append((row[6],row[9]))
        elif len(row) == 11:
            c = c+1
            if (row[7],row[10]) not in between9and11:
                between9and11.append((row[7],row[10]))
        elif len(row)>11:
            d = d+1
            if (row[7],row[10],row[13]) not in greater11:
                greater11.append((row[7],row[10],row[13]))
        else:
            e = e+1

##print (lessthan9)
##print(between9and11)
##print(greater11)
print (a, b+c+d+e)


