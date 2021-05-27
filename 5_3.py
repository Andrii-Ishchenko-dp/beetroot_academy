#Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

range_list = range(1,101)
i = 0
list1 = []
list2 = []
while i != 100:
    list1.append(range_list[i])
    if list1[i] % 7 == 0 and list1[i] % 5 != 0:
        list2.append(i)
    i += 1
print(list2)
