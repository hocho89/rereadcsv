import csv
import operator
import os
from pathlib import Path, PureWindowsPath
from datetime import datetime
from os import listdir
from os.path import isfile, join




def read_directory():
    filepath_list = []   
    filepath = input("ange sökväg till mapp: ")
    filename = Path(filepath) #input file path
    path_on_windows = PureWindowsPath(filename)
    onlyfiles = [f for f in listdir(path_on_windows) if isfile(join(path_on_windows, f))]
    filepath_list = ([str(filepath) + s for s in onlyfiles])
    print(filepath_list[1:4])
        

def get_filepath():
    filepath = input("ange sökväg till csv: ")
    filename = Path(filepath) #input file path
    path_on_windows = PureWindowsPath(filename) #make file path python compatible eg / instead of \
    #init_csvfile(path_on_windows)
    return path_on_windows

def init_csvfile(path_on_windows):
    with open(path_on_windows, "r+", encoding="utf-8") as csv_file:
        content = csv_file.read()

    with open(path_on_windows, "w+", encoding="utf-8") as csv_file:
        csv_file.write(content.replace('"', ''))

    with open(path_on_windows) as infile:
        reader = csv.reader(infile, delimiter = ",") #Create a new reader
        next(reader) # Skip the first row
        data = list(reader)
        csv_file.close()
    return data

def split_values_from_csv(data, what_list):
    fnumber_list = [row[3].split(",")[0] for row in data] #splits the out every value in col 3 from data list
    servername_list = [row[2].split(",")[0] for row in data] #splits the out every value in col 2 from data list
    date_list = [row[0].split(",")[0] for row in data] #splits the out every value in col 0 from data list
    system_name = [row[1].split(",")[0] for row in data] #splits the out every value in col 1 from data list 
    date_list = format_datelist(date_list)
    return {
        'flist': fnumber_list,
        'servname': servername_list,
        'datelist': date_list,
        'systemname': system_name,
        'datelist': date_list
    }.get(what_list, "not found")

def format_datelist(date_list):
    date_list_temp = []
    for b in date_list: #replace space and / to - for date row
        j = b.replace(' ', '-')
        j = b.replace("/","-")
        date_list_temp.append(j)
    date_string = str(date_list_temp[0]) #converted one date row to string
    return date_string


def sort_list(csv_list):
    fNumberList = list(map(int, fNumberList)) # convert list from string to int
    fNumberList.sort(reverse=False) # sort biggest first in list
    fNumberList.pop(1)


#init sequence
#init_csvfile(get_filepath()) #data 
#print(split_values_from_csv(init_csvfile(get_filepath()), 'flist'))
read_directory()
