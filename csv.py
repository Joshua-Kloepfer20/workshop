#Joshua Kloepfer
#SoftDev
#K06
#2021-9-28
import csv

with open('occupations.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
for k, v in finalDict.items():
        print(k, v)
