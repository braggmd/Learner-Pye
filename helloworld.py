import random
import sys
import os

print("hello world")

firstName = "Dillon"
lastName = "Bragg"
password = "1234"

user = firstName + " " + lastName

login = "Username " + user +" Password " + password

print(login)
print("Welcome to Scifo " + firstName)

print("How are ", end="")
print("you doing?")

print('\n' * 2,)
print("Good?")

groceryList = ['apple', 'orange', 'tomato']
toDoList = ['hair', 'teeth', 'clean']

#list+list makes one big list, [list, list] make multiple list in one list

everyList = [groceryList, toDoList]

#list start a 0 and go up
print(everyList)
print(everyList[1][2])
#adds onion to the end of the list
groceryList.append('onions')
print(groceryList)
#puts pepper in 2nd slot sliding over the list to the right
groceryList.insert(1, "pepper")
print(groceryList)
#removes orange from the list
groceryList.remove("orange")
print(groceryList)
#sorts the list alphabeticly
groceryList.sort()
print(groceryList)
#flips the list and puts it in reverse order
groceryList.reverse()
print(groceryList)
#del is delete, delete item from list
del groceryList[1]
print(groceryList)
#prints number of slots in list
print(len(groceryList))
#prints the end of the list
print(max(groceryList))
#prints the first square of list
print(min(groceryList))

pi_tuple = (1,2,3,4,5,6)
print(pi_tuple)

new_tuple = list(pi_tuple)
print(new_tuple)

new_list = tuple(new_tuple)
print(new_list)

print(len(pi_tuple))
print(max(pi_tuple))
print(min(pi_tuple))

#
#
#dictionary
#left is keys, right is values
super_heros = {'batman' : 'bruce wayne',
               'superman' : 'clark kent',
               'flash' : 'wallie white',
               'jak' : 'daxter'}
print(super_heros['batman'])

super_heros['jak'] = 'ripper'

print(super_heros['jak'])

print(super_heros.get('batman'))

print(len(super_heros))

del super_heros['jak']

print(len(super_heros))

print(super_heros.keys())
print(super_heros.values())

#
#
#conditionals

age = 21

if age > 16 :
    print("you are old enough")
else:
    print("you are not old enough")

if age >= 21:
    print("yee old enough doe")
elif age>= 16:
    print("you is good for car")
else:
    print("you is not old enough fool")

if ((age >= 1) and (age <= 18)):
    print('you is young')
elif (age == 21) or (age >= 65):
    print("dang you old")
elif not(age == 30):
    print("you get nothing")
else:
    print("you need a birthday")

for x in range(0,10):
    print(x, '', end="")
print('\n')

for y in groceryList:
    print(y,'',end="")
print('\n')

num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y], '', end="")
print('\n')


#random_num = random.randrange(0,16)
#while(random_num != 15):
#    print(random_num)
#    random_num = random.randrange(0,16)

i = 0;

while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 17):
        break
    else:
        i +=1
        continue
    i += 1


#
#
#Function

def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

print(addNumber(1,4))
string = addNumber(2,2)
print(string)


#Input

#print('What is your name?')

#name = sys.stdin.readline()

#print('Hello', name.capitalize())



#Strings

longString = "i see you have tried "

print(longString.capitalize())

print(longString.find("you"))

print(longString.isalpha())

print(longString.isalnum())

print(len(longString))

print(longString.replace("tried","won"))

quote_list = longString.split(" ")
print(quote_list)
print('\n')


#I/O

test_file = open("test.txt", "ab+")

print(test_file.mode)

print(test_file.name)

test_file.write(bytes("write me to the file\n", 'UTF-8'))

test_file.close()

test_file = open("test.txt", "r+")

text_in_file = test_file.read()
print(text_in_file)

test_file.close()
os.remove("test.txt")



#Classes

class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = ""

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name

    def get_height(self):
        return str(self.__height)

    def get_weight(self):
        return str(self.__weight)

    def get_sound(self):
        return str(self.__sound)

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms, says {}".format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound)
cat = Animal('Skid', 33, 10, 'Meow')

print(cat.toString())


class Dog(Animal):

    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kilograms, says {} His owner {} is proud".format(self.__name,
                                                                   self.__height,
                                                                   self.__weight,
                                                                   self.__sound,
                                                                   self.__owner)

    #def multiple_sounds(self, how_many=None):
     #   if how_many is None:
      #      print(self.get_sound())
       # else:
        #    print(self.get_sound() * how_many)


joe = Dog("Joe", 53, 27, "Ruff", "Dillon")

print(joe.toString())
