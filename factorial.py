def factorial(n):
    result = 1
    for i in range(n):
        result = result*n
        n=n-1
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120
