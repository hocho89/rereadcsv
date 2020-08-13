import csv
import operator
import re
from pathlib import Path, PureWindowsPath
import ast
import shlex

#filepath = input("ange sökväg till csv: ")
#filename = Path(filepath) #input file path
#path_on_windows = PureWindowsPath(filename) #make file path python compatible eg / instead of \



with open("C:/Users/Loco/Desktop/Git project/rereadcsv/Data/rereaddata.csv") as infile:
    reader = csv.reader(infile, delimiter = ",") #Create a new reader
    next(reader) # Skip the first row
    data = []
    data = list(reader)
    #for data1 in reader:
        #data1 = [d.replace('"', ',') for d in data1]
       # data1 = list(data1)
        #print("lol", data1)

flexNumberList = [row[3].split(",")[0] for row in data] #splits the out every value in col 3 from data list
serverNameList = [row[1].split(",")[0] for row in data] #splits the out every value in col 1 from data list
    
tempList = flexNumberList

flexNumberList = list(map(int, flexNumberList)) # convert list from string to int
flexNumberList.sort(reverse=False) # sort biggest first in list

tempList = list(map(int, tempList)) # convert list from string to int
tempList.sort(reverse=False) # sort biggest first in list

tempList = ([j-i for i, j in zip(flexNumberList[:-1], flexNumberList[1:])]) # count the diff between next and prev item

#for b, c in zip (flexNumberList, tempList): # print every item in both list, zip to iterate both lists in same print
   #print (b,c)

tempInt = 0

for i in tempList: 
    if(i >= 2) : 
        fixedFlexNumbers = []
        index = tempList.index(i) #get index from templist
        fixedFlexNumbers.append((flexNumberList[index] if index < len(flexNumberList) else default)) #add the value of the input index
        tempInt = ((flexNumberList[index] if index < len(flexNumberList) else default))
        countFlexDiff = []
        testString = ""
        while True:
            countFlexDiff.append(1)
            total = sum(countFlexDiff)
            if total == i:
                break
        #print(*countFlexDiff, sep = "\n")
        for b in countFlexDiff:
            tempInt -= 1
            testString +=  str(tempInt) + "|"
            #print("egrep \|(",tempInt,"|flexnumber)\| SYSTEMNAMN_DATUM.log",tempInt)
            
        print('egrep "\|('+testString+')\|"'+ serverNameList[0])

            

print("Checking if 4 exists in list ( using in ) : ") 

