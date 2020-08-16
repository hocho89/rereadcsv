import csv
import operator
from pathlib import Path, PureWindowsPath
from datetime import datetime
#"C:/Users/Loco/Desktop/VS project/Data/test.csv"
#filepath = input("ange sökväg till csv: ")
#print("\n")
#filename = Path(filepath) #input file path
#path_on_windows = PureWindowsPath(filename) #make file path python compatible eg / instead of \

with open("C:/Users/Loco/Desktop/VS project/Data/test.csv", "r+", encoding="utf-8") as csv_file:
    content = csv_file.read()

with open("C:/Users/Loco/Desktop/VS project/Data/test.csv", "w+", encoding="utf-8") as csv_file:
    csv_file.write(content.replace('"', ''))

with open("C:/Users/Loco/Desktop/VS project/Data/test.csv") as infile:
    reader = csv.reader(infile, delimiter = ",") #Create a new reader
    next(reader) # Skip the first row
    data = list(reader)

fNumberList = [row[3].split(",")[0] for row in data] #splits the out every value in col 3 from data list
serverNameList = [row[2].split(",")[0] for row in data] #splits the out every value in col 2 from data list
dateList = [row[0].split(",")[0] for row in data] #splits the out every value in col 0 from data list
systemName = [row[1].split(",")[0] for row in data] #splits the out every value in col 1 from data list 

dateListTemp = []
for b in dateList: #replace space and / to - for date row
    j = b.replace(' ', '-')
    j = b.replace("/","-")
    dateListTemp.append(j)

dateStringTemp = str(dateListTemp[0]) #converted one date row to string

tempList = fNumberList

fNumberList = list(map(int, fNumberList)) # convert list from string to int
fNumberList.sort(reverse=False) # sort biggest first in list

tempList = list(map(int, tempList)) # convert list from string to int
tempList.sort(reverse=False) # sort biggest first in list

tempList = ([j-i for i, j in zip(fNumberList[:-1], fNumberList[1:])]) # count the diff between next and prev item


testIndex = 0
usedIndexList = []
counter = 0
for i in tempList: 
    countFDiff = []
    fixedFNumbers = []
    testString = ""
    total = 0
    tempInt = 0
    counter += 1
    #if(i >= 2):
     #   counter += 1
      #  print("kuk",str(i), str(tempList.index(i)))
    print(str(counter))
    #if(i >= 2 and tempList.index(i) != testIndex): 
    if(i >= 2): 
        countFDiff.clear()
        index = tempList.index(i) #get index from templist
        #fixedFNumbers.append((fNumberList[index] if index < len(fNumberList) else default)) #add the value of the input index
        tempInt = ((fNumberList[index] if index < len(fNumberList) else default)) #if next nu,mber in fNUmberList is higher add to templist
        #counter += 1
        testIndex = index
        print("used indexx: ",*fixedFNumbers, str(tempInt), str(index), str(counter))
        while True:
            countFDiff.append(1) #add 1 depedning on tempInt size
            total = sum(countFDiff) #sum of every 1 in confFDiff
            total = total +1
            if total == i: #if sum is more than i break loop
                break
        for b in countFDiff: #fill up teststring with fnumbers
            tempInt += 1
            testString += str(tempInt) + "|"

         
        dateTime = str(datetime.date(datetime.now())) #current date of sytem
        print("Antal missade rader: " + str(i))
        print("Kontrollera innehåll: "+'egrep "\|('+testString+')\|"'+ serverNameList[0]+"-"+dateStringTemp[0:10]+".log"+" "+"|"+" "+"grep -iv heartbeat")
        print("Skapa fil: "+'egrep "\|('+testString+')\|"'+ serverNameList[0]+"-"+dateStringTemp[0:10]+".log"+" "+"|"+" "+"grep -iv heartbeat >" + " " + systemName[0] +"_"+ dateTime + ".log \n" )

        
        
