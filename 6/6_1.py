str1=input().split()
str2=set(str1)
str3=list(str2)
d={str3[a]:str1.count(str3[a]) for a in range(len(str3))}
print(d)
