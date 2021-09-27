import random

list1 = ["Rayat", "William", "Michelle", "Lucas", "Ivan"];
list2 = ["Yoonah", "Joshua", "Alif", "Josephine", "Andrew"];

def printName():
    print("period 1: " + list1[random.randint(0, len(list1) - 1)])
    print("period 2: " + list2[random.randint(0, len(list2) - 1)])
printName()