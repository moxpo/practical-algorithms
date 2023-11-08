# 1b) Implement the above algorithm in Python, and measure the time taken to sort lists of size 100, 1000, 10_000,
# and 20_000 (updated). The lists should initially be populated randomly with positive integers in the range 0-1000.
# Compare your empirical observations with the big-O complexity analysis you did in 1a)


import random
import time

one_hundred = 100
one_thousand = 1000
ten_thousand = 10000
twenty_thousand = 20000

totalListTime=0

new_list=[]

def random_list(size):
    for i in range(0, size):
        n = random.randint(1, 1000)
        new_list.append(n)
    return new_list





def bubble_sort(list):
    for outer in range(len(list) -1, 0, -1):
        for i in range(0, outer -1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp






random_list(one_hundred)
startListTime = time.time()
bubble_sort(new_list)
endListTime = time.time()
totalListTime = endListTime-startListTime
print("100 = " + str(totalListTime))

random_list(one_thousand)
startListTime = time.time()
bubble_sort(new_list)
endListTime = time.time()
totalListTime = endListTime-startListTime
print("1 000 = " + str(totalListTime))

random_list(ten_thousand)
startListTime = time.time()
bubble_sort(new_list)
endListTime = time.time()
totalListTime = endListTime-startListTime
print("10 000 = " + str(totalListTime))

random_list(twenty_thousand)
startListTime = time.time()
bubble_sort(new_list)
endListTime = time.time()
totalListTime = endListTime-startListTime
print("20 000 = " + str(totalListTime))




