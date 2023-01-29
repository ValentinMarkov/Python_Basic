
try:
    with open('text1.txt', 'r') as file:
        print(file.readline())

except FileNotFoundError as err:
    print(err)

# BOOKMARK: As you can see, whatever we put in the except block was printed because there was an error opening and reading this file