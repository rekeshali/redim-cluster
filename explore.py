#!/usr/bin/ python

# macro to check for data format
def is_num(string): # returns true if number, false otherwise
    try:
        float(string)
        return True
    except ValueError:
        return False# open, get, close data files

# begin data exploration
import csv
dbraw = {}
filename = 'data/UTK-peers.csv'
# filename = 'data/IPEDS-big-trimmed.csv'
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            row[0] = 'N'
            keyraw = row
        for idx,item in enumerate(row):
            if line_count == 0:
                dbraw[item] = []
            else:
                dbraw[keyraw[idx]].append(item)
        line_count += 1


db = {}
key = []
for tooth in keyraw[4:]:
    db[tooth] = []
    key.append(tooth)
    for item in dbraw[tooth]:
        item = item.replace(',','').replace('$','')
        if is_num(item):
            db[tooth].append(float(item))
        else:
            del db[tooth]
            del key[-1]
            break
for tooth in key:
    if len(db[tooth]) > len(dbraw['N']):
        for idx in range(0, len(db[tooth]), 2):
            mean = (db[tooth][idx] + db[tooth][idx+1])/2
            db[tooth][int(idx/2)] = mean
        del db[tooth][int(len(db[tooth])/2):]
