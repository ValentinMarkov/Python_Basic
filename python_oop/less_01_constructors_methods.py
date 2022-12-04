class Person:
    # Class Object Attribute
    is_person = True

    # Constructor
    def __init__(self, name, last_name, age):
        if age > 18:
            self.name = name  # name attribute
            self.last_name = last_name  # last_name attribute
            self.age = age  # age attribute

    # Method
    def greet(self):
        print(f"{self.name}, {self.last_name}, old: {self.age}, "
              f"Called by class itself {Person.is_person}."
              f"Called by self keyword {self.is_person}")

    # Class method
    @classmethod
    def date_created(cls, today_date, year):
        print(today_date, year)

    # Static Method
    @staticmethod
    def is_adult(age):
        return age >= 18


person_1 = Person('ValMar', 'Markov', 41)

person_1.greet()
person_1.date_created('04/12', 2022)

# Class method -> @classmethod
# Class method belongs to the class itself so you are not required to instantiate the class in order to use it
Person.date_created('12/12', 2023)

# Static Method -> @staticmethod
# The static method does not have access to the Class state and therefore cannot modify the Class. These methods
# can be used as utility-type methods that can take parameters and perform some action.
print(Person.is_adult(19))
