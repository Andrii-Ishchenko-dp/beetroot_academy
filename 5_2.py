import random

list1 = []
list2 = []
while True:
    x=random.randint(1, 10)
    list1.append(x)
    y=random.randint(1, 10)
    list2.append(y)
    if len(list1) == 10:
        break
gen = set(list1+list2)
list3 = list(gen)
print(list3)