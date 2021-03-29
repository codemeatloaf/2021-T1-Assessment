#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

year = datetime.datetime.now().year
name = input("Input your name here! : ")
age1 = int(input("Input your age here! : "))
final = str((year - age1) + 100)

print(name, " will be 100 in the year", final)
