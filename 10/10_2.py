#Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age. Then create a method `human_age` which returns the dog’s age in human equivalent.

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
