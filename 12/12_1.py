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

Animals=[Cat('Bars'),Dog('Kroha'),Cat('Simon')]

for x in Animals:
    x.Talk()


