import random
import sys
import os

#Hello, Python
#This is the print command
print("Hello World")

#Setting up some basic quick comment blocks
word = ' word '
sentence = " this is a sentence "
paragraph = """ this is a paragraph """
print(word,sentence,paragraph)

#Basic math functions
# Addition +, Subtraction -, Multiplication *, Division /,   Remainder %,   Square **,    Division no-re //
print(1+0);   print(3-1);    print(3*1);       print(8/2);   print(5%10);   print(6**1);  print(14//2)

print("1 + 2 - 3 * 2 = ", (1 + 2 - 3) * 2)

#Strings
motto = "\"Plus Ultra\""
print('\n' * 3, motto)

firstName = "Dillon"
lastName = "Bragg"

fullName = firstName + " " + lastName
print("Welcome ", fullName, end=" ")
print(motto)

#List
#Lists start at 0, exm. [0], [1], [2], [3]
fruitList = ['apple', 'orange', 'tomato']


print(fruitList)

#If else is a set that does this or that
if True:
    print("True")
else:
    print("False")

input("Enter apple, then press enter.")
if input is "apple":
    print("true")
else:
    print("wrong")
print(input)


input ("\n\nPress the enter key to exit.")
