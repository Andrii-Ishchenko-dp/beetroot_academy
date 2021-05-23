import random

y=input('Введите слово: ')
for i in range(5):
    x=random.sample(y,k=len(y))
    string=''.join(x)
    print(string)
