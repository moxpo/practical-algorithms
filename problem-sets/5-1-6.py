test = ("this is a test block of text without punctuation")
dict = {}

# def wordFreq(text):
#     firstList = text.split()
#     for i in range(len(firstList)):
#         if firstList[i] in dict.keys():
#             print
#             "blah"
#         else:
#             print
#             "boo
#             print(firstList[i])
#     return firstList







wordFreq(test)


"""
6) Dictionaries, loops, strings
 6a) Define a function which is given a string and returns a dictionary with words (strings) as keys and numbers as
 values, showing how many times each word occurs in the original string. For example, when given the string:
"The first test of the function."
the function wordFreq() should return
{ "the":2, "first":1, "test":1, "of":1, "function":1 }
Of course, the items above might be in a different order. The function should ignore any non-letters in the string
(so if the string contains "hello1 how are you", the 1 should be ignored), and convert everything to lower case.
Test the function.
The function split from the string module will be very useful for this exercise. It separates a string into blocks,
using a given string to indicate where the blocks begin and end. For example,
"The first test of the function.".split(" ")
(argument is a space) returns
[ "The", "first", "test", "of", "the", "function." ]
Another hint: string.ascii_lowercase will return a string with all lowercase letters from a to z as a string. And,
you can check whether a particular chacter is in a string by using the "in" keyword.
Think about how you are going to attack this exercise, especially how you are going to convert from the original
string into a list of individual words, in lower case, with all the non-letters removed.
You might find it useful to develop some small functions to carry out the individual steps of this process.
"""