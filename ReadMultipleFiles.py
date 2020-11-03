import csv
import operator
import os
from pathlib import Path, PureWindowsPath
from datetime import datetime
from os import listdir
from os.path import isfile, join

def read_directory(file_nr, first_time):
    filepath_list = []
    if(first_time == 1):
        global filepath
        filepath = input("ange sökväg till mapp: ")
        print('\n')
    filename = Path(filepath) #input file path
    path_on_windows = PureWindowsPath(filename)
    onlyfiles = [f for f in listdir(path_on_windows) if isfile(os.path.join(path_on_windows, f))]
    filepath_list = (([filepath+ "\\" + s  for s in onlyfiles]))
    first_time=0
    global initcounter
    initcounter = len(filepath_list)
    global data
    data = []
    pre_init_csvfile(filepath_list[file_nr])
    data += init_csvfile(filepath_list[file_nr])
    return data

def pre_init_csvfile(path_on_windows):
    with open(path_on_windows, 'a', newline='', encoding="utf-8") as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(['2020/07/15 00:13:37 CEST','PLACEHOLDER','xx555533.dd.pppppp.ssss','0'])
        csv_file.close()

def init_csvfile(path_on_windows):
    data = []
    with open(path_on_windows, "r+", encoding="utf-8") as csv_file:
        content = csv_file.read()

    with open(path_on_windows, "w+",encoding="utf-8") as csv_file:
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
    return date_list_temp

def sort_list(csv_list):
    csv_list = list(map(int, csv_list)) # convert list from string to int
    csv_list.sort(reverse=True) # sort biggest first in list
    return csv_list

def calculate_difference_in_list(csv_list, system_name_list): # den här skapar flist_diff dvs diffar 
    csv_list = list(map(int, csv_list))
    csv_list.sort(reverse=True)
    og_csv_list = csv_list
    csv_list = ([j-i for i, j in zip(csv_list[:-1], csv_list[1:])])
    return csv_list

def go_again(loopround):
    loopround += 1
    if(loopround<initcounter):
        data.clear()
        read_directory(loopround,0)
        create_list_per_system(split_values_from_csv(data, 'flist'), split_values_from_csv(data, 'systemname'),calculate_difference_in_list(split_values_from_csv(data, 'flist'),split_values_from_csv(data,'systemname')), loopround, split_values_from_csv(data, 'format_datelist'))
 
def create_list_per_system(flist, system_name_list, flist_diff, loopround, date_list):
    flist = list(map(int, flist)) 
    flist_diff = list(map(int, flist_diff)) 
    flist.sort(reverse=True)

    fnumber_list = [[item_flist] for item_flist,item_system_name,item_flist_diff in zip(flist, system_name_list, flist_diff) if item_flist_diff <-1 and "PLACEHOLDER" not in str(item_system_name) and item_flist_diff >-200]
    list_with_diff = [[item_flist_diff] for item_flist,item_system_name,item_flist_diff in zip(flist, system_name_list, flist_diff) if item_flist_diff <-1 and "PLACEHOLDER" not in str(item_system_name) and item_flist_diff >-200]
    list_system_name = [[item_system_name] for item_flist,item_system_name,item_flist_diff in zip(flist, system_name_list, flist_diff) if item_flist_diff <-1 and "PLACEHOLDER" not in str(item_system_name) and item_flist_diff >-200] 
    list_with_dates = [[item_date_list] for item_flist,item_system_name,item_flist_diff,item_date_list in zip(flist, system_name_list, flist_diff,date_list) if item_flist_diff <-1 and "PLACEHOLDER" not in str(item_system_name) and item_flist_diff >-200]

    flattend_list_with_fnumber = [val for sublist in fnumber_list  for val in sublist] 
    flattened_list_with_diff = [val for sublist in list_with_diff for val in sublist]
    flattend_list_system_name_list = [val for sublist in list_system_name  for val in sublist]
    flattend_list_with_dates = [val for sublist in list_with_dates  for val in sublist]
    first_loop = 1
    for idx,item in enumerate(flattened_list_with_diff):
        amount_to_add_to_subtract = item
        int_flattend_list_with_fnumber = 1
        loopchecker = -2
        list_with_all_fnumbers = []
        list_with_system_names = []
        list_with_current_dates = []
        while item<=loopchecker:
            list_with_all_fnumbers.append(str(flattend_list_with_fnumber[idx]-int_flattend_list_with_fnumber) + "|")
            int_flattend_list_with_fnumber = int_flattend_list_with_fnumber + 1
            amount_to_add_to_subtract = amount_to_add_to_subtract +1
            loopchecker = loopchecker - 1
        list_with_system_names.append(str(flattend_list_system_name_list[idx]))
        list_with_current_dates.append(str(flattend_list_with_dates[idx][0:10]))
        print_result(list_with_all_fnumbers,list_with_system_names,list_with_current_dates,first_loop)
        first_loop = first_loop + 1
    print('\n')
    go_again(loopround)


def print_result(list_with_all_fnumbers,list_with_system_names,list_with_current_dates, first_loop):
    date_time = str(datetime.date(datetime.now()))
    if(first_loop<=1):
        print('##########',*list_with_system_names,'##########')
        print("Kontrollera antal rader: ",'egrep "\|(',*list_with_all_fnumbers,')\|" ',*list_with_system_names,'-',*list_with_current_dates,'.log',' | ','wc -l',sep='')
        print("Skapa fil: ",'egrep "\|(',*list_with_all_fnumbers,')\|" ',*list_with_system_names,'-',*list_with_current_dates,'.log',' | ','grep -iv heartbeat ','> ',*list_with_system_names,'_',date_time,'.log',sep='')
    else:
        print("Skapa fil: ",'egrep "\|(',*list_with_all_fnumbers,')\|" ',*list_with_system_names,'-',*list_with_current_dates,'.log',' | ','grep -iv heartbeat ','>> ',*list_with_system_names,'_',date_time,'.log',sep='')

read_directory(0,1)
create_list_per_system(split_values_from_csv(data, 'flist'), split_values_from_csv(data, 'systemname'),calculate_difference_in_list(split_values_from_csv(data, 'flist'),split_values_from_csv(data,'systemname')), 0, split_values_from_csv(data, 'format_datelist'))

