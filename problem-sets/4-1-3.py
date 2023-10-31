userInputStr = input("Give me a 5 digit number to check if it is a palindrome")

## WIP


if userInputStr.isdigit():
    userInputInt = int(userInputStr)
    if userInputInt < 0:
        print("positive numbers only")
else:
    print("Whole integer numbers only")


reverseInputStr = userInputStr[::-1]
reversedInputInt = int(reverseInputStr)

print(userInputInt)
print(userInputStr)
print(reversedInputInt)
print(reverseInputStr)








"""
3) Is a given number a Palindrome?

Palindrome numbers remain the same even when you reverse the order of their digits. 
So e.g. 12321 is a 5-digit palindrome. 

Write a Python program that prompts the user to enter a 5-digit number, and checks if it is a palindrome. 
The program should display error messages if the user enters a floating point number; or a negative integer; 
or a number that has less or more than 5 digits. 

Note: This is not the problem for using exceptions, we want to use conditionals for checking for errors.
(Hint # 1: An outer multiple-alternative conditional can check for the different error types, such that you 
get to the final "else" only if there are no errors. Then you'll need a nested conditional inside that last 
else that checks whether or not the number is a palindrome.)

(Hint  # 2: If you are using the input() function in Python 3, recall what type it returns).
"""