def greet():
    print("Hello! Welcome to my space")
    print("How are you doing today?")

greet()

def greet_1(name):
    print("hello " +  name)

greet_1("Boris")
greet_1("Aranza")

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

def spam_1():
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
def spam_2():
    global eggs
    eggs = "spam"

eggs = "global"
spam_2()
print(eggs)

#Unbound local error occurs when a local variable is referenced before it has been assigned a value. This can happen if you try to modify a global variable inside a function without declaring it as global.
# def spam():
#     print(eggs)
#     eggs = "spam local"

egss = "global"
#spam()  # This will raise an UnboundLocalError because eggs is referenced before assignment

#Try and Except
def divide(byNum):
    return  42/byNum

print(divide(2))
print(divide(12))
#print(divide(0))  #! This will raise a ZeroDivisionError

def divide_1(byNum):
    try:
        return 42/byNum
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

print(divide_1(2))
print(divide_1(12))
print(divide_1(0))  #! This will print an error message instead of raising an exception

#Let''s say you want to handle multiple types of exceptions. You can do this by adding more except blocks:
def divide_2(byNum):
    try:
        return 42/byNum
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid input type. Please provide a number.")

#Practice game
import random

def gamePractice():
    secretNumber = random.randint(1, 20)
    print("I am thinking of a number between 1 and 20.")

    for guessesTaken in range(1, 7): #You have 6 attempts to guess the number
        print("Take a guess.")
        guess = int(input())

        if guess < secretNumber:
            print("So low.")
        elif(guess > secretNumber):
            print("So high.")
        else:
            break # This condition is the correct guess! So you can exit the loop.

    if guess == secretNumber:
        print("Yeap, you have made a really good job guessing the number in " + str(guessesTaken) + " attempts!")
    else:
        print("Nope. The number I was thinking of was " + str(secretNumber) + ". Better luck next time!")

#gamePractice()


def collatzSequence(number):
    while number != 1:
        if number % 2 != 0:
            number = (3 * number) + 1
        else:
            number = number  / 2
        print(number)

    return number

collatzSequence(4)
collatzSequence(20)


def nextStep(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = (3 * number) + 1

    return number

def countSteps(input):
    count = 0
    try:
        number = int(input)
    except ValueError, TypeError:
        return

    if number >= 1:
        while number != 1:
            number = nextStep(number)
            count += 1
    else:
        return
    
    return count

countSteps(24)

result = countSteps(6)
print(result)

def duplicate(x):
    return x * 2

def addTen(x):
    return x +10

def formatResult(label, value):
    print(label, value, sep=": ", end=".")
    return f"[{label}] Final Value = {value}"

# message1= formatResult("Combined sum", duplicate(addTen(10)))


# def modifyTry():
#     print(count)
#     count += 1

# modifyTry()

# count = 5

# def modifyTry():
#     global count
#     print(count)
#     count += 1

# modifyTry()
# print(count)


count = 5

def modify(value):
    print(value)
    return value + 14

count = modify(count)
print(count)


history = 0

def registerEvent(name):
    global history
    history += 1
    print(f"Registered event #{history}: {name}")

registerEvent("Inicio de sesión")
registerEvent("Descargar Reporte")
print("Total acumulado: ", history)

def registerPureEvent(currentTotal, name):
    newTotal = currentTotal + 1
    message =  f"Registered event #{newTotal}: {name}"
    return (newTotal, message)

total = 0
total, msg = registerPureEvent(total, "First Commit")

print(msg)

total, msg = registerPureEvent(total, "Download report")
print(msg)
print("Total acumulado:", total)

def readPositiveInteger(message):
    while True:
        try:
            number = int(input(message))
        except ValueError:
            print("Invalid input: write an integer number.")
            continue
        except EOFError:
            print("\n interrupted input")
            return None

        if number > 0:
            return number

        print("Number must be higher than zero")


# readPositiveInteger("Please, enter a positive number: ")

def printMultiplicationTable(n: int):
    one = 1 * n
    two = 2 * n
    three = 3 * n
    four = 4 * n
    print(f"Its multiplication table goes:{one}, {two}, {three}, {four}")

def getMultiplicationInline(n: int, i: int):
    result = n * i
    return f"Well. this time multiplier = {n} times multiplicand = {i} is equal to: {result}"

def isNone(result):

    if result is None:
        return "This function has no return statement, so just None as result"

    return "This funcion has a return statement"

print(isNone(getMultiplicationInline(2,6)))
print(isNone(printMultiplicationTable(6)))


def draw_row(symbol, quantity, separator):
    if quantity <= 0:
        print()
        return

    for i in range(quantity):
        if i < quantity - 1:
            print(symbol, end = separator)
        else:
            print(symbol, sep= "", end = "\n")

draw_row("x", 9, ", ")
draw_row("*", 20 , "-")

def calculate(operation, a, b):
    try:
        one, two = float(a), float(b)
        match operation:
            case "addition":
                return one + two
            case "subtraction":
                return one - two
            case "multiplication":
                return one * two
            case "division":
                return one / two
            case _:
                print(f"Unkonw operation: '{operation}'")
                return "try again"

    except TypeError as e:
        print (f"Type error: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    except ZeroDivisionError:
        print("Error: you can't divide by zero")
    except Exception as e:
        print(f"Error inesperado: {e}")

    return "Try again"


calculate("addition", "a", 2)
print(calculate("division", 4, 0))
print(calculate("division", 4, 2))
print(calculate("don", 4, 2))
print(calculate("addition", list , 2))

def isValidQualification(grade):
    if 0 < grade <= 100:
       if grade >= 60:
           return True
    return False

def evaluateStudents(name, grade):
    if isValidQualification(grade):
        return f"The student: {name} has aproved"

    return f"The student: {name} has reproved"

student1 = evaluateStudents("Juan", 34)
student2 = evaluateStudents("Belinda", 67)

print(student1)
print(student2)

import random

def rollTheDice(faces):
    try:
        faces = int(faces)
        if faces < 2:
            return None

        return random.randint(1, faces)
    except (TypeError, ValueError) as e:
        return f"Error: {e}"

print(rollTheDice("asdf"))
print(rollTheDice(list))
print(rollTheDice(1))