class Animal():
    def __init__(self, name):
        self.name = name

    def Talk(self):
        print('Животные не разговаривают')

class Dog(Animal):
    def Talk(self):
        print('woof woof')

class Cat(Animal):
    def Talk(self):
        print('meow')

def foo(Cat,Dog):
    kot = Cat(input('Введите кличку кота: '))
    kot.Talk()
    sob = Dog(input('Введите кличку собаки: '))
    sob.Talk()
    
foo(Cat,Dog)


