# variables
user_name = "Hans"
user_age = "18"
user_town = "Stara_Zagora"

# string concatenations
print("Hello I'm " + user_name)
print(user_name + " is " + user_age + " years old")
print(user_town + " is a biggest city in Bulgaria")
print("Valentin\nMarkov")

# work with strings
phrase = "HedgeServe"
print(phrase + " is my job")
print(phrase.lower())
print(phrase.islower())
print(phrase.isupper())
print(phrase.upper().isupper())

# length of variable
print(len(user_town))

# get character number from string
print(user_town[6])

# return index of specified character
hero_name = "Ajax the Greek"
print(hero_name.index("x"))

# replace variable function
print(hero_name.replace("Ajax", "Timon"))