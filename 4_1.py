import random

print('Компьютер выберет число от 1 до 10, угадай его!')
computer=random.randint(1,10)
num=int(input('Введите число:'))
if computer==num:
    print('Ты угадал!')
else:
    print(f'Ты не угадал, компьютер загадал {computer}')