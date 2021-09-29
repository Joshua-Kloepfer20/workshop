#Joshua Kloepfer
#SoftDev
#K06
#2021-9-28
import csv
import random
finalDict = {}
def randomJob(reader):
        x = random.randint(0, 1000)
        y = 0
        for i in reader:
                y += reader[i] * 10
                if (y > x):
                        print(i)
                        break
with open('occupations.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                finalDict[row['Job Class']] = float(row['Percentage'])
        randomJob(finalDict)
