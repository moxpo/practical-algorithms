beforeTax = float(input("What is the price of the item before item?"))
discount = float(input("What is the discount to be applied, as a percentage?"))

newPrice = beforeTax - (beforeTax * discount / 100)

finalPrice = newPrice + (newPrice * 17.5 / 100)

print (beforeTax)

print(newPrice)

print(finalPrice)





# 1a) Write a Python program that prompts for two inputs: the before tax price of an item,
# and the discount offered on it (as a percentage). The program should then calculate and display
# the new price, given that the sales tax rate is 17.5%.

