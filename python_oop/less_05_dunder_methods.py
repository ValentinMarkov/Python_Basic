class Car:
    def __init__(self, color, make, year, size):
        self.color = color
        self.make = make
        self.year = year
        self.size = size
        self.engine_dict = {
            'automatic': 'Yes',
            'manual': 'No'
        }

    # def __str__(self):
    #     return f'{self.make}'
    #
    # def __del__(self):
    #     print('Deleted')

    def __getitem__(self, index):
        return self.engine_dict[index]


bmw_car = Car('red', 'bmw', '2021', 'sedan')

# call the dunder __str__ method:
# print(bmw_car.__str__())  # <__main__.Car object at 0x000002161C7C0FD0>

# the exact same as above is the built-in str() function
# print(str(bmw_car))  # <__main__.Car object at 0x000002161C7C0FD0>

# call del method
# del bmw_car  # Deleted. The method is changed

# if we try to access the bmw_car object an error
# print(bmw_car)  # NameError: name 'bmw_car' is not defined

# getitem method
print(bmw_car['manual'])
