def linear_sum(A, n):
    if n == 1:
        return A[0]
    else:
        return linear_sum(A, n-1) + A[n-1]


print(linear_sum([3,6,4,8,7,5,2], 7))