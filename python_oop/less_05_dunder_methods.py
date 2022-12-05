class Car:
    def __init__(self, color, make, year, size):
        self.color = color
        self.make = make
        self.year = year
        self.size = size

    def __str__(self):
        print(f'{self.make}')


bmw_car = Car('red', 'bmw', '2021', 'sedan')

# Call default string method
print(bmw_car.__str__())  # <__main__.Car object at 0x0000024910480FD0>

# After introduce new str method
bmw_car.__str__()  # bmw
