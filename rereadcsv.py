import csv
import operator
import re

with open("C:/Users/Loco/Desktop/Git project/rereadcsv/Data/rereaddata.csv") as infile:
    reader = csv.reader(infile) # Create a new reader
    next(reader) # Skip the first row
    data = list(reader)
    flexNumberList = [row[3].split(",")[0] for row in data] #splits the out every value in col 3 from data list
    serverNameList = [row[0].split(",")[0] for row in data] #splits the out every value in col 1 from data list
    
tempList = flexNumberList

flexNumberList = list(map(int, flexNumberList)) # convert list from string to int
flexNumberList.sort(reverse=False) # sort biggest first

tempList = list(map(int, tempList)) # convert list from string to int
tempList.sort(reverse=False) # sort biggest first

tempList = ([j-i for i, j in zip(flexNumberList[:-1], flexNumberList[1:])]) # count the diff between next and prev item



for b, c in zip (flexNumberList, tempList): # print every item in both list, zip to iterate both lists in same print
    print (b,c)

counterFlexNumberList = []
#testValue = flexNumberList[12] - flexNumberList[11]
#print(testValue, flexNumberList[11],  flexNumberList[12])

count = 0
for b in flexNumberList:
    if tempList[count] >= 2:
        counterFlexNumberList = tempList[count]
        count += 1

print(counterFlexNumberList)

# 4/5 done
# list med de nummer som är mer än 2 + nästa nummer 
    #iterara varje nummer mellan aktuellt numer och nästa nummer
# if templist[i]>=2:
# flexNumberList [i] - tempList [i] 



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