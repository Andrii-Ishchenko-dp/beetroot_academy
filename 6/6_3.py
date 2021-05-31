i = []
j = []
for o in range(1,11):
    i.append(o)
for p in range(len(i)):
    j.append(i[p]*i[p])
i = tuple(i)
j = tuple(j)
s = [i, j]
print(s)