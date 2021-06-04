def fun(a,b):
    try:
        return a*a/b
    except ZeroDivisionError:
        return 'Нельзя делить на 0!'
try:
    a = int(input())
    b = int(input())
    print(fun(a, b))
except ValueError:
     print('Введите числа!')

