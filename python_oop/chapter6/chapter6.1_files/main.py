import random

if __name__ == "__main__":
    with open('text1.txt', 'r') as fb:
        content = fb.readline()  # return only first line in file. content-> str
        content1 = fb.readlines()  # return list with all content separate by \n. content-> lst
        content2 = fb.read()  # return only first line in file. content-> str

    # read and writhe
    # with open('text.txt', 'r+') as file:
    #     file.write('Hello readers')

    # append text
    with open('text.txt', 'a') as file:
        file.write(f'\nMy number: {random.randint(0, 2000)}')

