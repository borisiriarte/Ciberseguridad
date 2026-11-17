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

#why does this expression cause an error? 'spam' + 3?
#print("spam" + 3 + "burritos") #This will cause an error because we are trying to concatenate a string and an integer. We need to convert the integer to a string before concatenating.