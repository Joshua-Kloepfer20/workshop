import random
students = {
"list1": ["Rayat", "William", "Michelle", "Lucas", "Ivan"],
"list2": ["Yoonah", "Joshua", "Alif", "Josephine", "Andrew"]
}

def printName():
    print("period 1: " + students["list1"][random.randint(0, len(students) - 1)])
    print("period 2: " + students["list2"][random.randint(0, len(students) - 1)])
printName()
