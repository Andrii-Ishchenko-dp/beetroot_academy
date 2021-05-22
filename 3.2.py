num=input('Введите номер:')
if len(num)!=10:
    print('Введите 10 цифр')
else:
    for i in range(len(num)):
        if num[i].isdigit()!=True:
            print('В номере недопустимый символ')
            break
    else:
        print('Номер введён верно')


