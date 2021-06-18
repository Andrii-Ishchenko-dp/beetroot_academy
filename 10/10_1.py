class Person():
    def __init__(self, name, s_name, age):
        self.name = name
        self.s_name = s_name
        self.age =  int(age)

    def Hi(self):
        print(f'Привет! Меня зовут {self.name} {self.s_name} и мне {self.age} лет ')

try:
    person1 = Person(name=input('Name: '), s_name=input('Surname: '), age=input('Age: '))
    person1.Hi()
except ValueError:
    print('Возраст должен быть введён числом!')
