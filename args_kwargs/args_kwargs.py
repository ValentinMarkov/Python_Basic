current_year = 2022


def get_age(yob):
    print(current_year - yob)


get_age(1982)


# # Calculate persons ages
def get_ages(yob1, yob2, yob3):
    print([current_year - yob1,
           current_year - yob2,
           current_year - yob3])


get_ages(1985, 1988, 2007)


# Use *argsssssssdsddsdeed    asdddffweasd asdsda
def calc_ages(*years_of_birth):
    for year in years_of_birth:
        print(f'The age for your yob is {current_year - year}')


calc_ages(1989, 2014, 1945, 2011)


# Use **kwargs
def get_ages_kwargs(**kwargs):
    for item in kwargs:
        print(item)


get_ages_kwargs(name='Valio', age=39)


def get_ages_kwargs2(**kwargs):
    for k, v in kwargs.items():
        print(f'The param was "{k}" and the value was "{v}"')


get_ages_kwargs2(name='Silvia', age=36)