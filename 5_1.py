#Write a Python program to get the largest number from a list of random numbers with the length of 10
#Constraints: use only while loop and random module to generate numbers


import random

list = []
while True:
    x=random.randint(0,100)
    list.append(x)
    if len(list)==10:
        break
print( list, max(list), sep='\n')
