Assignment:

You find the data in python/data/Jiang2013_data.csv . Write a
function that takes as input the desired Taxon , and returns the mean
value of r .

https://www.dropbox.com/s/n92g2x055afvbkp/Jiang2013_data.csv?dl=1

(^link to data)

import csv
import sys

with open('Jiang2013_data.csv', encoding= "ISO-8859-1") as csv_file:
    taxon = sys.argv[1]

#found = {}
    reader=csv.reader(csv_file)
    for i in range(1):
        reader.__next__()
    for line in file:
        split_line = line.split(' ')
        str1=split_line[2]
        r=split_line[3]
    for taxa in taxon:
        if taxa in str1:
            print(r)