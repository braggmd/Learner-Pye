import random
import sys
import os

house_list = [['House 1','$45,000', 'Old, Well kept'],['House 2', '$110,000', 'New, Middle Class'],['House3', '$85,000', 'New, Trashed']]

#Welcomes Player and gets them involved form the start.
print('Welcome to The House Simulator\n')
input("Press enter to continue\n")

#Beginning tutorial/introduction.
print("""
Welcome to the Market.
Here you can buy and sell houses.
Type market to see the local listings.
""")

#This will be the main menu to get to different areas in the game.
while True:
    user_key = input ('|')

    if user_key == 'market':
        print('you did it')
        break


    if user_key == 'home':
       print("now in houses")
       break

    else:
        print('foo')
        break
