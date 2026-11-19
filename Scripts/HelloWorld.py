# print("Hello world") #Pythono si tiene un scope que se maneja mediante el indentado
mensaje = "Soy global"

def saludar():
    mensaje_local = "Soy local"
    print(mensaje)
    print(mensaje_local)

# saludar()

# Primeros ejercicios basicos de python

# print(2**3)
# print(22%8)
# print(22//8)
# print(22/8)
# print(3*5)
# print(5-2)
# print(4+9)

# print(45+5+*2) como en la mayoria de los lenguajes esto es incorrecto, no se puede hacer una operacion de suma y multiplicacion sin parentesis
# En python no es necesario poner el tipo de dato, ya que es un lenguaje de tipado dinamico, es decir, que el tipo de dato se asigna en tiempo de ejecucion y no en tiempo de compilacion

# Las varibles solo pueden ser nombradas con letras, numeros y guion bajo, y no pueden empezar con un numero, ni contener espacios, ni caracteres especiales, ni palabras reservadas del lenguaje

balance = 32
currentBalance = 42
current_balance = 52
_spam = "This is a message for all my fellow friends"
SPAM = "This is a message for all my fellow friends"
account4 = 42

# Variable names are case-sensitive, so balance and Balance are different variables
# This program says hello and asks for my name

# print("Hello world")
# print("What is your name?")
# myName = input()  #ask for user input and store it in a variable
# print("It is good to meet you, " + myName)
# print("The length of your name is: " + str(len(myName)))  #len() is a built-in function that returns the length of a string
# #len() is a built-in function that returns the length of a string
# print("What is your age?")
# myAge = input()
# print("You will be " + str(int(myAge) + 1) + " in a year.")  #int() is a built-in function that converts a string to an integer

one = str(29) #int() is a built-in function that converts a string to an integer
int("42") #int() is a built-in function that converts a string to an integer
float("3.14") #float() is a built-in function that converts a string to a float
print(one)

bacon = 20
bacon + 1
print(bacon) #This will print 20, because the value of bacon has not changed. To change the value of bacon, we need to assign the new value to the variable bacon.

#What should the following two expressions evaluate to?
print('spam' + 'spamspam')
print('spam' *3)
print("Hello my fellow friends")

print(59)

#why does this expression cause an error? 'spam' + 3?
#print("spam" + 3 + "burritos") #This will cause an error because we are trying to concatenate a string and an integer. We need to convert the integer to a string before concatenating.

spam = True
print(spam)

print(42 == 42, 42 ==99, 42 < 100, 42 > 100, 42 <= 100, 42 >= 100, 10 != 10, 42 == "42") #This will print True, False, True, False, True, False
eggCount = 42
print(eggCount == 42) #This will print True, because the value of egg


print(True and True) #This will print True, because both values are True
print(False and True) #This will print False, because one of the values is False
print(True or False) #This will print True, because one of the values is True
print(False or False) #This will print False, because both values are False
print(not True) #This will print False, because the value is True and we are negating it

print((4 < 5) and (5 < 6)) #This will print True, because both values are True
print((4 < 5) and (5 > 6)) #This will print False, because one of the values is False
print(not(1==2)or (2==1))

name = input("What is your name? ")
password = input("What is your password? ")

if name == "Mary":
    print("Hello Mary")
elif password == "swordfish":
    print("Access granted.")
else:
    print("Wrong password.")


spam = 0
print(spam)
while spam < 5:
    print("Hello world.")
    spam = spam + 1

print(spam)

print("My name is")
for i in range(5):
    print(" Jimmy Five Times (" + str(i)+ ")") #This will print "Jimmy Five Times (0)" "Jimmy Five Times (1)" "Jimmy Five Times (2)" "Jimmy Five Times (3)" "Jimmy Five Times (4)" "Jimmy Five Times (5)"

import random
randomNumber = random.randint(1, 10) #This will generate a random number between 1 and 10
print(randomNumber)
print(randomNumber)

for i in range(5): #This will generate a random number between 1 and 10
    print(random.randint(1, 10)) #This will generate a random number between 1 and 10

import random, sys, os, math #This will import the random, sys, os, and math modules.

from random import * #This will import all the functions from the random module.

print(randint(1, 100)) #This will generate a random number between 1 and 10



print("hello world")

def hello(name):
    print("Hello, " + name)

hello("Alice")

print(len("Borisasd"))