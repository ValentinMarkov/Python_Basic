# inheritance

class Mammal:
    def __init__(self, name):
        self.name = name

    # eat method
    def eat(self):
        print(f'{self.name} eats different types of foods!')

    # walk method
    def walk(self):
        if self.name != 'bat':
            print(f'{self.name} can walk!')
        else:
            print(f'The {self.name} is the only mammal that can fly!')


print('******** Mammal class instances output! ********')
mammal_obj1 = Mammal('Elephant')
mammal_obj1.eat()
mammal_obj1.walk()
mammal_obj2 = Mammal('bat')
mammal_obj2.eat()
mammal_obj2.walk()


class Dog(Mammal):
    def __init__(self, name, breed, legs):
        Mammal.__init__(self, name)
        self.breed = breed
        self.legs = legs

    # eat method overriding
    def eat(self):
        print(f'{self.name} eats only dog food!')

    # details method - unique for the class Dog

    def details(self):
        print(f'The {self.name} is a {self.breed} \n'
              f'and like all dogs have {self.legs}-legs!')


print('******** Dog class instances output! ********')
dog_obj1 = Dog('Benn', 'labrador', 4)
dog_obj1.eat()
dog_obj1.walk()
