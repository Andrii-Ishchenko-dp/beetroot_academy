x=input()
if len(x)==2:
    print(x*2)
elif len(x)<2:
    print('Empty String')
else:
    print(x[:2]+x[-2:])

