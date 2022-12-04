"""The program should have two classes. The first class will be called Person and the second class will be called
Employee. You will need to guess their relationship so you can write the inheritance correctly. The person class will
have the following attributes:
-name
-dob (date of birth)
-id_number

In the person class, you should have the info() method that will print all of the Person details in a new line. The
class Employee should be able to use all of the attributes and methods from the parents class but it should also
have new attributes:
-salary
-position

The employee class will have its own info() method with the same name as from the Person class so it can print the
parent class details plus the new Employee details as well (method overriding). In the end, you need to create an
instance of the class
"""


class Person:
    def __init__(self, name, dob, id_number):
        self.name = name
        self.dob = dob
        self.id_number = id_number

    def info(self):
        print(f"Name: {self.name}\n"
              f"Date of birth: {self.dob}\n"
              f"ID number: {self.id_number}")


class Employee(Person):
    def __init__(self, name, dob, id_number, salary, position):
        Person.__init__(self, name, dob, id_number)
        self.salary = salary
        self.position = position

# super() function
# The super() function needs to be called in the child class and in our case the Employee class. The
# super() function doesn’t even require the ‘self’ keyword The super() is called super because it refers to the
# parent class (Person) and the parent classes are also known as super or abstract classes. This is how we can
# use the super() to link up the parent and child classes

    # def __init__(self, name, dob, id_number, salary, position):
    #     super().__init__(name, dob, id_number)
    #     self.salary = salary
    #     self.position = position


    def info(self):
        Person.info(self)
        print(f'Salary: {self.salary}\n'
              f'Position: {self.position}')


person_obj_1 = Person('Robin Hood', '20/06/1598', 12789)
employee_obj_1 = Employee('Sam Bush', '01/10/1989', 23409, 1500, 'python developer')

print('*** Class Person ***')
person_obj_1.info()

print('*** Class Employee ***')
employee_obj_1.info()