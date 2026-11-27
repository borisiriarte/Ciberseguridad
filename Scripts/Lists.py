#Lists: it is a value that contains an ordered sequence of other values(number, texts, booleans and even another lists) closed inbetween brackets and separeted by a coma
ports = [21, 22, 80 ,408, 1004893]
print(ports[0], ports[1], ports[-1], ports[1:4], sep=" - ")

#lists of other list
access_matrix = [
    ["ana", "admin", True],
    ["Luis", "invitado", False]
]

print(access_matrix[0][1])
print(access_matrix[1][2])

eggs = [1,2,3]

del eggs[2]
eggs.append(4)
print(eggs)

#overwrite
eggs = [4,5,6]
print(eggs)

#Modifying a copy of a list changes the original list too.
spam = [0,1,2,3,4,5]
cheese = spam
print(cheese)
cheese[3] = 98

print(spam)
#If you want a independent copy, use copy.copy() o [:]
import copy
original = [1, 2, 3, 4, 5]
independent = copy.copy(original)
independent.append(32)

print(original)
print(independent)

origin = ["hello", "bye", "are you ok?"]
newButIndependent = origin[:]
newButIndependent.append("sdf")
print(origin)
print(newButIndependent)

#Methods
servers = ["web-01", "db-01", "auth-01"]
#search position
idx = servers.index("db-01")
# Add at the end or inserting in an especific position
servers.append("log-01")
servers.insert(1, "proxy-01")

#Delete by value(delete the first coincidence)
servers.remove("proxy-01")

#sort in place
numbers = [73, 23, 1, 54, 100, 14]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#Tuplas y strings

config_const = ("123.0.1.1", 5647)
print(config_const[0])
token = "ABC-123"
print(token[1])
print("123" in token)


#Excercises
print("-------------------------------")
print(len(""))
print("   ".strip())

print("".isspace())
print("asdf".isspace())
print(" sdfs ".strip())
print("SFCSDsdfSD".lower())
numbers = [1, 2, 2, 3, 1, 4]
uniques = list(dict.fromkeys(numbers))
print(uniques)

uniques_1 = []

for number in numbers:
    if number not in uniques_1:
        uniques_1.append(number)

print(uniques_1)

items = [[1, 2], [3, 4], [1, 2]]
unicos = []

for item in items:
    if item not in unicos:
        unicos.append(item)

print(unicos)


listOfEvents = ['  Login_OK ', 'ERROR_AUTH', 'login_ok', '', 'timeout  ', 'ERROR_AUTH']

def cleanLogs(array):
    newListOfEvents = []
    for event in array:
        currentEvent = event.strip().lower()
        if currentEvent:
            newListOfEvents.append(currentEvent)


    return list(dict.fromkeys(newListOfEvents))

print(cleanLogs(listOfEvents))

def clean_logs(events):
    clean_events = []

    for event in events:
        # 1. Limpiamos espacios y pasamos a minúsculas
        cleaned = event.strip().lower()
        # 2. Verificamos que no esté vacío y que no esté repetido
        if cleaned and cleaned not in clean_events:
            clean_events.append(cleaned)

    return clean_events

print(clean_logs(listOfEvents))

# [1,2,3,4,5] --- [1,2,3] [4, 5] --- [4, 5, 1, 2, 3] postive step
# [1,2 3, 4, 5] --- [1,2] [3, 4, 5] --- [3, 4, 5, 1, 2]
print ("------Excersice Two------")
letras = [1,2,3,4,5]
print(letras[0:3])
print(letras[3:])
print(letras[0:1])
print(letras[1:])
print(-2 % len(letras))
print(letras[0:-2])
print(letras[-2:])
print(letras[0:3])
print(letras[3:])
print("-------------")

def rotate_lists(elements, steps):
    steps = steps % len(elements)

    if steps <= 1:
        return elements

    elements[:] = elements[-steps:]+ elements[:-steps]
    return elements

print ("------Excersice Three------")
print(not [])

words = ["a","b", "c", "d"]
words_1= ["a","b", "c", "d", 5]

def format_legible_list(array):
    try:
        if  not isinstance(array, list):
            raise TypeError("Parameter must be a list")

        if not all(isinstance(x, str) for x in array):
            raise TypeError("All elements inside the list must be texts(Strings)")

        if not array:
            return ""
        if len(array) == 1:
            return array[0]
        if len(array) == 2:
            return f"{array[0]} y {array[1]}"


    except TypeError as e:
        print(f"Type error: {e}")
        return None


    return f"{", ".join(array[:-1])} y {array[-1]}"
print(format_legible_list(["s", "a"]))