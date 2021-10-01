#Joshua Kloepfer
#The Best Team
#SoftDev
#K06-printing from csv file and choosing random job
#2021-9-28
#We open up the csv file and convert to a dictionary with the keys as the job and the value as the percentage
#we then put the dictionary into a function which picks a random int from 0 to 1000
#the function adds each percentage until it reaches one greater than the random int and pickts that one to print
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
