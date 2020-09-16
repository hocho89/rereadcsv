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
    onlyfiles = [f for f in listdir(path_on_windows) if isfile(os.path.join(path_on_windows, f))]
    filepath_list = (([filepath+ "\\" + s  for s in onlyfiles]))
    counter = 0
    global data
    data = []
    for i in filepath_list:
        pre_init_csvfile(filepath_list[counter])
        data += init_csvfile(filepath_list[counter])
        counter += 1
    return data

def pre_init_csvfile(path_on_windows):
    with open(path_on_windows, 'a', newline='', encoding="utf-8") as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(['2020/07/15 00:13:37 CEST','KUKSYSTEM','lx555533.dd.pppppp.ssss','0'])
        csv_file.close()

def init_csvfile(path_on_windows):
    data = []
    with open(path_on_windows, "r+", encoding="utf-8") as csv_file:
        content = csv_file.read()

    with open(path_on_windows, "w+", newline='',encoding="utf-8") as csv_file:
        csv_file.write(content.replace('"', ''))

    with open(path_on_windows) as infile:
        reader = csv.reader(infile, delimiter = ",") #Create a new reader
        next(reader) # Skip the first row
        data += list(reader)
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
        'format_datelist': format_datelist(date_list),
        'systemname': system_name,
        'datelist': date_list,
        #'sorted_list': sort_list(fnumber_list)
    }.get(what_list, "not found")

def format_datelist(date_list):
    date_list_temp = []
    for b in date_list: #replace space and / to - for date row
        j = b.replace(' ', '-')
        j = b.replace("/","-")
        date_list_temp.append(j)
    date_string = str(date_list_temp) #converted one date row to string
    return date_string

def sort_list(csv_list):
    csv_list = list(map(int, csv_list)) # convert list from string to int
    csv_list.sort(reverse=True) # sort biggest first in list
    return csv_list

def calculate_difference_in_list(csv_list):
    csv_list = list(map(int, csv_list)) 
    csv_list = ([j-i for i, j in zip(csv_list[:-1], csv_list[1:])])
    return csv_list

def create_list_per_system(flist, system_name_list, flist_diff):
    flist = list(map(int, flist)) 
    flist_diff = list(map(int, flist_diff)) 
    for item_flist, item_system_name, item_flist_diff in zip(flist, system_name_list, flist_diff):
        print(item_flist, item_system_name, item_flist_diff, (item_flist-item_flist_diff))


read_directory()
#print(calculate_difference_in_list(split_values_from_csv(data, 'flist')))
#print(split_values_from_csv(data, 'systemname'))



create_list_per_system(split_values_from_csv(data, 'flist'),split_values_from_csv(data, 'systemname'),calculate_difference_in_list(split_values_from_csv(data, 'flist')))