current_year = 2022


class Person:
    def __init__(self, name, **kwargs):
        self.name = name
        self.yob = kwargs.get('yob')  # Returns None if not provided

    def get_age(self):
        if self.yob:  # help to evade None if not provided
            return current_year - self.yob


person1 = Person(name='Valentin', yob=1982)
print(person1.get_age())
