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

def spam():
    eggs = "spam local"
    print(eggs)  # This will print "spam local"

def bacon():
    eggs = "bacon local"
    print(eggs)  # This will print "bacon local"
    spam()  # This will call the spam function and print "spam local
    print(eggs)  # This will print "bacon local"

eggs = "global"
bacon()
print(eggs)  # This will print "global"

#The "global" statement allows you to modify a variable outside of the current scope
def spam():
    global eggs
    eggs = "spam"

eggs = "global"
spam()
print(eggs)

#Unbound local error occurs when a local variable is referenced before it has been assigned a value. This can happen if you try to modify a global variable inside a function without declaring it as global.
def spam():
    print(eggs)
    eggs = "spam local"

egss = "global"
#spam()  # This will raise an UnboundLocalError because eggs is referenced before assignment

#Try and Except
def divide(byNum):
    return  42/byNum

print(divide(2))
print(divide(12))
#print(divide(0))  #! This will raise a ZeroDivisionError

def divide(byNum):
    try:
        return 42/byNum
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

print(divide(2))
print(divide(12))
print(divide(0))  #! This will print an error message instead of raising an exception