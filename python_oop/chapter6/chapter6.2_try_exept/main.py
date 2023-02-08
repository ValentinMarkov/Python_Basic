
try:
    with open('text2.txt', 'r') as file:
        print(file.read())

except FileNotFoundError as err:
    print('File cannot be found!')
    raise err

