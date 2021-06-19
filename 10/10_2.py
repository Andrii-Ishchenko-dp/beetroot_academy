class Dog():
    age_factor = 7
    def __init__(self,age):
        self.age = int(age)
    def HumanAge(self):
        return self.age * Dog.age_factor
    def init_age(self):
        if self.age <= 0:
            raise TypeError('Возраст должен быть больше 0!')
        else:
            return self.age
try:
    Tommy = Dog(input('Введите возвраст собаки: '))
    Tommy.init_age()
    print(Tommy.HumanAge())
except ValueError:
    print('Возраст должен быть введён числом!')
except TypeError as err_msg:
    print('Возраст должен быть больше 0!')
