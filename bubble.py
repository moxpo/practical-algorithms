import random

randomlist = []
for i in range(0, 99):
    n = random.randint(1, 100)
    randomlist.append(n)



def bubble_sort(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp




print(randomlist)
bubble_sort(randomlist)
print(randomlist)

