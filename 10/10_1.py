class Person():
    def __init__(self, name, s_name, age):
        self.name = name
        self.s_name = s_name
        self.age = age

    def Hi(self):
        print(f'Привет! Меня зовут {self.name} {self.s_name} и мне {self.age} лет ')

person1= Person('Андрей','Ищенко',25)
person1.Hi()
