def oops():
    raise IndexError ('IndexError')

def fun():
    try:
        oops()
    except IndexError as error_text:
         return f'Ошибка {error_text} не найдена'

print(fun())
