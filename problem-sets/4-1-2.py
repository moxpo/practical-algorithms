def ps2a():
    firstNumber = int(input("input a nonzero number"))
    secondNumber = int(input("input a second nonzero number"))
    check = firstNumber % secondNumber

    if check == 0:
        print("True")


def ps2b():
    hourlyRate = float(input("What is your hourly rate?"))
    hoursWorked = float(input("How many hours have you worked?"))


    if hoursWorked <= 40:
        grossPay = hourlyRate * hoursWorked
        print("You have earned £" + str(grossPay))
    else:
        overtimeHours = hoursWorked - 40
        grossPay = (hourlyRate * 40) + ((hourlyRate*1.5)*overtimeHours)
        print("You have earned £" + str(grossPay))




def ps2c():
    seasons = {
        1 : "winter",
        2 : "winter",
        3 : "spring",
        4 : "spring",
        5 : "summer",
        6 : "summer",
        7 : "summer",
        8 : "summer",
        9: "august",
        10: "august",
        11: "winter",
        12: "winter",
    }

    monthNumber = int(input("Tell me a month by number 1-12"))

    if monthNumber in seasons:
        print(seasons[monthNumber])
    else:
        print("only whole numbers between 1-12, try again")


def ps2d():
    seasonsNormal = {
        1: "winter",
        2: "winter",
        3: "spring",
        4: "spring",
        5: "summer",
        6: "summer",
        7: "summer",
        8: "summer",
        9: "august",
        10: "august",
        11: "winter",
        12: "winter",
    }

    seasonsScotland = {
        1: "winter",
        2: "winter",
        3: "winter",
        4: "winter",
        5: "winter",
        6: "June",
        7: "winter",
        8: "winter",
        9: "winter",
        10: "winter",
        11: "winter",
        12: "winter",
    }

    monthNumber = int(input("Tell me a month by number 1-12"))
    question = input("Is this question about Scotland? yes/no?")


    if question.lower() == "yes":
        if monthNumber in seasonsScotland:
            print(seasonsScotland[monthNumber])
        else:
            print("only whole numbers between 1-12, try again")
    elif question.lower() == "no":
       if monthNumber in seasonsNormal:
           print(seasonsNormal[monthNumber])
       else:
           print("only whole numbers between 1-12, try again")




"""

2a) [Single-alternative condition] Draw/write the flowchart or pseudocode, and then write a Python program
that asks the user to input two nonzero integers, and tells you if one is a multiple of the other (so, e.g.,
if you enter 18 and 6, or 6 and -18, it should return "True". If not, nothing displayed) .

2b) [Dual-alternative condition] Draw/write the flowchart or pseudocode, and then write a Python program 
that prompts the user for their hourly pay rate and the number of hours worked in a given week, and then 
returns their gross pay. The hourly rate applies for up to 40 hours of work; any hours worked over 40 
are paid at 1.5 times the given hourly rate. 

2c) [Multiple-alternative conditions] Draw/write the flowchart or pseudocode, and then write a Python program 
that prompts the user for a number between 1 and 12, corresponding to the month order, and then returns the season 
for that month, as per the following:

    Nov, Dec, Jan and Feb: Winter
    Mar and Apr: Spring
    May, Jun, Jul and Aug: Summer
    Sep and Oct: Autumn

2d) [Nested conditions] Modify the program you wrote for 2c to add another prompt to the user which asks them: 
"Is this question about Scotland?". If they answer yes to this question, then the season should be calculated as 
described here:

    Jun: June
    Jul to May: Winter

Otherwise, the season should be calculated as described in 2c  (you know, the way it is "normally" supposed to be...). 


(I'm going to use this image inside problem set chapters to highlight important learning takeaway.)

You can consider a simple guideline (not "rule") when considering the use of multiple alternative 
conditions vs nested conditions:

    When you are making decisions based on different values of a single variable, then you use single/dual/multiple 
    alternative conditions. In flowchart terms, you have a single diamond only.
    When you are making decisions based on different values of two or more variables, then nested conditions is 
    probably what you want to do (though you could use Boolean operators to create compound conditions as well)

And you can have a combination of both as well, as this next problem indicates

"""