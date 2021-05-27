import random

list = []
while True:
    x=random.randint(0,100)
    list.append(x)
    if len(list)==10:
        break
print( list, max(list), sep='\n')