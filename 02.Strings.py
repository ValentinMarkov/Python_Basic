# region variables
user_name = "Hans"
user_age = "18"
user_town = "Stara_Zagora"
# endregion

#  region string concatenations
print("Hello I'm " + user_name)
print(user_name + " is " + user_age + " years old")
print(user_town + " is a biggest city in Bulgaria")
print("Valentin\nMarkov")
# endregion

# region work with strings
phrase = "HedgeServe"
print(phrase + " is my job")
print(phrase.lower())
print(phrase.islower())
print(phrase.isupper())
print(phrase.upper().isupper())
# endregion

# region length of variable
print(len(user_town))
# endregion

# region get character number from string
print(user_town[6])
# endregion

# region return index of specified character
hero_name = "Ajax the Greek"
print(hero_name.index("x"))
# endregion

# region replace variable function
print(hero_name.replace("Ajax", "Timon"))
# endregion
