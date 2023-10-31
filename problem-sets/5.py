import timeit
def forLoop():
    sum = 0
    for n in range(10000000):
        sum += n


def whileLoop():
    n = 0
    sum = 0
    while n < 10000000:
        n += 1
        sum += n

forLoop()
print("For Loop :")
print(timeit.default_timer())

whileLoop()
print("While Loop :")
print(timeit.default_timer())