import timeit
def ps5a():
    sum = 0
    for n in range(10000001):
        sum += n
    print("For Loop :")
    print(sum)
    print(timeit.default_timer())


def ps5b():
    n = 0
    sum = 0
    while n < 10000000:
        n += 1
        sum += n
    print("While Loop :")
    print(sum)
    print(timeit.default_timer())


def ps5c():
    n = 10000000
    sum = n * (n + 1) // 2
    print("Using Formula :")
    print(sum)
    print(timeit.default_timer())


# ps5a()
# ps5b()
ps5c()


"""
5) Time it!
We are going to execute a few small timing experiments, sneaking in some advanced preparatory work for a key concept 
that we cover in this course: Algorithmic Analysis. But let's not let these terminologies get in the way for now. 
We are just writing some code involving loops, and measuring how long they take.

5a) Write a Python program using a for loop that sums up the first n positive integers, where n=10,000,000
(10 million). Use a timer function to record how long it takes. 

5b) Now write the same program, but this time use a while loop. How long does this this version take?

5c) Finally, write this program using this formula for the sum of the first n
positive integers: 
1+2+⋯+n=n(n+1)2.

 

How long did this version take?"""