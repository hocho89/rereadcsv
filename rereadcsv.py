import csv
import operator
import re

reader = csv.DictReader(open('C:/Users/Loco/Desktop/Git project/rereadcsv/Data/rereaddata.csv', 'r'))
result = sorted(reader, key=lambda d: float(d['appnumber']))

#with open('C:/Users/Loco/Desktop/Git project/rereadcsv/Data/rereaddata.csv', 'r', newline='') as f_input:
    #csv_input = csv.DictReader(f_input)
    #data = sorted(csv_input, key=lambda row: (row['appnumber'], row['servernamn']))

#with open('C:/Users/Loco/Desktop/Git project/rereadcsv/Data/output.csv', 'w', newline='') as f_output:    
#   csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
#    csv_output.writeheader()
#   csv_output.writerows(data)

print('\n'.join(map(str, result)))

