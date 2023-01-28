# Inheritance

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


class Student(Person):
    def __init__(self, name, last_name, age, job, address):
        Person.__init__(self, name, last_name, age)
        self.job = job
        self.address = address

    def greet(self):
        Person.greet(self)
        print(f'My job is: {self.job}\n'
              f'My address is: {self.address}')


student_obj_1 = Student('Jabba', 'The Hutt', 123, 'Pirate gang leader', 'Naboo')

student_obj_1.greet()

# Method overriding


class GoodStudent(Student):
    def __init__(self, name, last_name, age, job, address, graduation_score, gender):
        Student.__init__(self, name, last_name, age, job, address)
        self.graduation_score = graduation_score
        self.gender = gender

    def greet(self):
        Student.greet(self)
        print(f'I am a {self.gender}\nMy graduation score is: {self.graduation_score} points')


good_student_obj1 = GoodStudent('Pinko', 'Panther', 35, 'cartoon hero','Hollywood', 98, 'male')
good_student_obj1.greet()