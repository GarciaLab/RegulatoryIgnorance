import csv
import matplotlib.pyplot as pyplot
import math
#from collections import Iterable
from matplotlib.collections import BrokenBarHCollection

a,b,c,d,e,f = 0,0,0,0,0,0
##def categorychecker(n, listname):
##    a = 0
##    if row[n] in listname:
##        a = a+1
##    else:
##        listname.append(row[n])
    
number = -3
master = []
types= []
with open('interactions.txt', 'r') as tsvfile:
    writer = csv.reader(tsvfile, delimiter='\t')
    next(writer)
    for row in writer:
        x = int(math.ceil(len(row)/3))-2
        for i in range(0,x):
            num1 = number*i-2
            num2 = number*i-1
            master.append((row[num1],row[num2]))
##        a = a+1
##        if 7<len(row)<10:
##            b = b+1
##            master.append((row[6],row[7]))
##        elif len(row) == 10:
##            c = c+1
##            master.append((row[5],row[6]))
##            master.append((row[8],row[9]))
##        elif len(row) == 11:
##            c = c+1
##            master.append((row[6],row[7]))
##            master.append((row[9],row[10]))
##        elif len(row)==14:
##            d = d+1
##            master.append((row[6],row[7]))
##            master.append((row[9],row[10]))
##            master.append((row[12],row[13]))
##        elif len(row)==17:
##            f= f+1
##            master.append((row[6],row[7]))
##            master.append((row[9],row[10]))
##            master.append((row[12],row[13]))
##            master.append((row[15],row[16]))
##        elif len(row)==20:
##            f= f+1
##            master.append((row[6],row[7]))
##            master.append((row[9],row[10]))
##            master.append((row[12],row[13]))
##            master.append((row[15],row[16]))
##            master.append((row[18],row[19]))
##        elif len(row)==23:
##            f= f+1
##            master.append((row[6],row[7]))
##            master.append((row[9],row[10]))
##            master.append((row[12],row[13]))
##            master.append((row[15],row[16]))
##            master.append((row[18],row[19]))
##            master.append((row[21],row[22]))
##        elif len(row)==26:
##            f= f+1
##            master.append((row[6],row[7]))
##            master.append((row[9],row[10]))
##            master.append((row[12],row[13]))
##            master.append((row[15],row[16]))
##            master.append((row[18],row[19]))
##            master.append((row[21],row[22]))
##            master.append((row[24],row[25]))
##        else:
##            print(len(row))
##            if len(row) == 29:
##                print(row)
##            e = e+1

##print (lessthan9)
##print(between9and11)
##print(greater11)
##print (a, b+c+d+e+f)
##print(f)
##print(e)
##def reemovNestings(l): 
##    for i in l: 
##        if type(i) == list: 
##            reemovNestings(i) 
##        else: 
##            l.append(i)
allcis = []
for item in master:
    if item[1] == "Cis_regulated":
        if item[0] not in allcis:
            allcis.append(item[0])
            b = b+1
print (allcis)
print(b)


            
        
     
##print(a)
##print(len(master))
##finallist = list(set(master))
##print(len(finallist))
##for i in finallist:
##    typeof = i[1]
##    if typeof not in types:
##        types.append(typeof)
##print(types)
##alldata = {}
##def flattenNestedList(nestedList):
##    ''' Converts a nested list to a flat list '''
##    flatList = []
##    # Iterate over all the elements in given list
##    for elem in nestedList:
##        # Check if type of element is list
##        if isinstance(elem, list):
##            # Extend the flat list by adding contents of this element (list)
##            flatList.extend(flattenNestedList(elem))
##        else:
##            # Append the elemengt to the list
##            flatList.append(elem)    
##    return flatList
##for i in finallist:
##    if i[0] not in alldata.keys():
##        alldata[i[0]] = i[1]
##    else:
##        val = alldata.get(i[0])
##        val = val,i[1]
##        val = list(val)
##        val = flattenNestedList(val)
##        alldata[i[0]] = val
same = []
same1 =[]
##print(len(alldata.keys()))

notsame = []
allgenes = [[],[],[],[],[],[]]
othergenes = [[],[],[],[],[],[]]
with open('results.tsv', 'r') as tsvfile2:
    writer = csv.reader(tsvfile2, delimiter='\t')
    for row in writer:
        start = int(row[3])
        stop = int(row[4])
        width = stop-start
        if row[1] in allcis:
            a = a+1
            same.append(row[1])
            same1.append(row[0])
            if row[2] == 'X':
                allgenes[0].append((start,width))
            elif row[2] == 'I':
                allgenes[1].append((start,width))
            elif row[2] == 'II':
                allgenes[2].append((start,width))
            elif row[2] == 'III':
                allgenes[3].append((start,width))
            elif row[2] == 'IV':
                allgenes[4].append((start,width))
            elif row[2] == 'V':
                allgenes[5].append((start,width))
        else:
            notsame.append(row[1])
            if row[2] == 'X':
                othergenes[0].append((start,width))
            elif row[2] == 'I':
                othergenes[1].append((start,width))
            elif row[2] == 'II':
                othergenes[2].append((start,width))
            elif row[2] == 'III':
                othergenes[3].append((start,width))
            elif row[2] == 'IV':
                othergenes[4].append((start,width))
            elif row[2] == 'V':
                othergenes[5].append((start,width))

finaler = []
finaler2 = []
with open('cis.txt', 'r') as tsvfile3:
    writer = csv.reader(tsvfile3, delimiter='\t')
    for row in writer:
        finaler2.append(row[0])
        

diff = set(same1) - set (finaler2)
print(diff)
diff2 = set(finaler2) - set (same1)
print(diff2)

with open('results.tsv', 'r') as tsvfile2:
    writer = csv.reader(tsvfile2, delimiter='\t')
    for row in writer:
        start = int(row[3])
        stop = int(row[4])
        width = stop-start
        if row[0] in diff2:
            a = a+1
            same.append(row[1])
            print(row[1])
            if row[2] == 'X':
                allgenes[0].append((start,width))
            elif row[2] == 'I':
                allgenes[1].append((start,width))
            elif row[2] == 'II':
                allgenes[2].append((start,width))
            elif row[2] == 'III':
                allgenes[3].append((start,width))
            elif row[2] == 'IV':
                allgenes[4].append((start,width))
            elif row[2] == 'V':
                allgenes[5].append((start,width))

print(a)

print(len(same))
print(len(notsame)-4)
differences = set(allcis) - set(same)
print (differences) 


fig = pyplot.figure()
ax = fig.add_subplot(111)

yticklabels = []
yticks = []
yranges = [[20,5],[40,5],[60,5],[80,5],[100,5], [120,5]]
yranges2 = [[18,9],[38,9],[58,9],[78,9],[98,9], [118,9]]
beginner = (-250000,250000)
edge = [(17718942,250000), (15072434,250000),(15279421,250000),(13783801,250000), (17493829,250000), (20924180,250000)]
lengths = [(0,17718942), (0,15072434), (0,15279421),(0,13783801),(0,17493829),(0,20924180)]
bottoms = [19.5, 39.5, 59.5, 79.5, 99.5, 119.5]
tops = [25,45,65,85,105,125]
for i in range(0,6):
    coll = BrokenBarHCollection(allgenes[i], yranges2[i], facecolor="blue", zorder= 1)#, clip_box = from_bounds(0, 20, 100000, 5))
    ax.add_collection(coll)
for i in range(0,6):
    coll = BrokenBarHCollection(othergenes[i], yranges[i], facecolor="red", zorder = 0.75)#, clip_box = from_bounds(0, 20, 100000, 5))
    ax.add_collection(coll)
widthbox = 0.5
heightbox = 6

for i in range(0,6):
    col2 = BrokenBarHCollection([lengths[i]], [bottoms[i],widthbox], facecolor="black")
    col3 = BrokenBarHCollection([lengths[i]], [tops[i],widthbox], facecolor="black")
    col4 = BrokenBarHCollection([beginner,edge[i]], [bottoms[i],heightbox], facecolor="black")
    center = bottoms[i]+3
    yticks.append(center)
    ax.add_collection(col2)
    ax.add_collection(col3)
    ax.add_collection(col4)
labeler2 = ["X","1", "2", "3", "4", "5"]#, "Y"]
for a in labeler2:
    yticklabels.append(a)

ax.set_yticks(yticks)
ax.set_yticklabels(yticklabels)
ax.axis('tight')
##pyplot.savefig('/Users/pranjal/Desktop/Programming/Genomeplot.pdf') 
pyplot.show()
    
 
    

##with open('results.tsv', 'r') as tsvfile2:
##    writer = csv.reader(tsvfile2, delimiter='\t')
##    for row in writer:
##        c = c+1
        


