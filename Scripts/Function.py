def greet():
    print("Hello! Welcome to my space")
    print("How are you doing today?")

greet()

def greet(name):
    print("hello " +  name)

greet("Boris")
greet("Aranza")

def introduce(name, age):
    print("Hello, my name is " + name + " and my age is " + str(age))

introduce("Boris", 25)
introduce("Aranza", 22)

def add(a,b):
    return a + b

total = add(4, 5)
print(total)

import random
def getAnswer(number):
    if number == 1:
        return "It is safe"
    elif number == 2:
        return "yes"
    elif number == 3:
        return "Ask later"
    else:
        return "I don't thin so"

r = random.randint(1,4)
print(getAnswer(r))
print(getAnswer(random.randint(1,4)))

#If the function is not returning anything, it will return "None" by default
x = print("Hello")
print(x == None)

print("hello", end = " ")
print("World")

print("cats", "dogs", "birds", sep = ", ")

#Local and global scope
def spam():
    eggs = 123

spam()
# print(eggs) # This will raise an error because eggs is not defined in the global scope

def spam()