import csv
import operator
import os
from pathlib import Path, PureWindowsPath
from datetime import datetime
#"C:/Users/Loco/Desktop/VS project/Data/test.csv"
#filepath = input("ange sökväg till csv: ")
#print("\n")
#filename = Path(filepath) #input file path
#path_on_windows = PureWindowsPath(filename) #make file path python compatible eg / instead of \

resultList = []
counter = 0
fixedFNumbers = []
testString = ""
total = ""
counter = -1

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
fNumberList.pop(1)

tempList = list(map(int, tempList)) # convert list from string to int
tempList.sort(reverse=False) # sort biggest first in list

tempList = ([j-i for i, j in zip(fNumberList[:-1], fNumberList[1:])]) # count the diff between next and prev item

def get_index_value(i):
        index = fNumberList.index(i) #get index from templist
        fixedFNumbers = ((fNumberList[index] if index < len(fNumberList) else default)) #add the value of the input index        
        return fixedFNumbers

for i in fNumberList: 
    counter2 = 1
    total = get_index_value(i)
    if (tempList[counter]>= 2):
        total = i
        while True:
            total = total - 1
            resultList.append(total)
            counter2 = counter2 + 1
            if(counter2 >= tempList[counter]):
                counter2 = 0
                break       
    counter += 1

resultList = resultList[max(tempList):]
testString = str(resultList).replace(',','|').replace('[','').replace(']','').replace(' ','')

dateTime = str(datetime.date(datetime.now())) #current date of sytem
print("Antal missade rader: " + str(i))
print("Kontrollera innehåll: "+'egrep "\|('+testString+')\|"'+ serverNameList[0]+"-"+dateStringTemp[0:10]+".log"+" "+"|"+" "+"grep -iv heartbeat")
print("Skapa fil: "+'egrep "\|('+testString+')\|"'+ serverNameList[0]+"-"+dateStringTemp[0:10]+".log"+" "+"|"+" "+"grep -iv heartbeat >" + " " + systemName[0] +"_"+ dateTime + ".log \n" )



        
        
