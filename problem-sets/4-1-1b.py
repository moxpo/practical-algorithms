import random

name = input("What is your last name?").lower()

firstThree = name[0:3]

randomInt = str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9))

UserId = firstThree + randomInt

print(UserId)

# 1b) Write a program that prompts the user to enter their last name, and then creates a 6
# character user id based on the first three letters of their surname (in lower case), and a
# 3 digit randomly generated number.