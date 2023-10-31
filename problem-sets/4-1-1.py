import random

def psa1():
    beforeTax = float(input("What is the price of the item before item?"))
    discount = float(input("What is the discount to be applied, as a percentage?"))
    newPrice = beforeTax - (beforeTax * discount / 100)
    finalPrice = newPrice + (newPrice * 17.5 / 100)
    print (beforeTax)
    print(newPrice)
    print(finalPrice)


def ps1b():
    name = input("What is your last name?").lower()
    firstThree = name[0:3]
    randomInt = str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9))
    UserId = firstThree + randomInt
    print(UserId)

psa1()

ps1b()



"""

1a) Write a Python program that prompts for two inputs: the before tax price of an item,
and the discount offered on it (as a percentage). The program should then calculate and display
the new price, given that the sales tax rate is 17.5%.


1b) Write a program that prompts the user to enter their last name, and then creates a 6
character user id based on the first three letters of their surname (in lower case), and a
3 digit randomly generated number.

"""