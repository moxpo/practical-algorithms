
def ps4a():
    numberChoice = int(input("How many numbers will you give?"))
    sum=0
    for x in range(numberChoice):
        userNumber = int(input("Give me number " + str(x + 1)))
        sum += int(userNumber)
    print("Absolute Sum " + str(sum))