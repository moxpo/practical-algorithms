def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


print(str(factorial(5)))

"""

1b. Is FACTORIAL a tail recursive function? Justify your answer.

    TRUE 
    
    n-1

    Tail recursion is defined as a recursive function in which the recursive call is the last 
    statement that is executed by the function. So basically nothing is left to execute after
    the recursion call. 

1c. Is FACTORIAL a linear recursive function? Justify your answer.

    TRUE
    
    n *
    
    something is being done in the function, its not jus the function itself

    Linear Recursion: A linear recursive function is a function that makes only a single 
    call to itself each time the function runs. 
    
"""