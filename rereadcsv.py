import csv
import operator
import re

with open("C:/Users/Loco/Desktop/Git project/rereadcsv/Data/rereaddata.csv") as infile:
    reader = csv.reader(infile) # Create a new reader
    next(reader) # Skip the first row
    flexNumberList = [row[3].split(",")[0] for row in reader] #splits the out every value in col 3
    #serverNameList = [row[1].split(",")[0] for row in reader] #splits the out every value in col 3

tempList = flexNumberList

flexNumberList = list(map(int, flexNumberList)) # convert list from string to int
flexNumberList.sort(reverse=True) # sort biggest first

tempList = list(map(int, tempList)) # convert list from string to int
tempList.sort(reverse=True) # sort biggest first

tempList = ([j-i for i, j in zip(tempList[:-1], tempList[1:])])

for p, b in zip (flexNumberList, tempList): # print every item in both list, zip to iterate both lists in same print
    print (p,b)





#for i in tempList: print(i)

#count = 0 4/5
#for p in flexNumberList: 
    #tempList[count] = flexNumberList[count]
    #tempList.remove[count]
    #count +=1
    

#months.append(int(reversed))
#sort_orders = sorted(months.items(), key=lambda x: x[1])

#for i in months:
#	print(months[i+1])



#print(months)

#print(months)

#reader = csv.DictReader(open('C:/Users/Loco/Desktop/Git project/rereadcsv/Data/rereaddata.csv', 'r'))
#result = sorted(reader, key=lambda d: float(d['appnumber']))

#data = []
#for line in result:
 #    months = [row[line].split(",")[line] for row in result]

#print(months)