def factorial(n):
    result = 1
    for x in range(1,n):
        result = result * n
        n = n-1
    return result

for n in range(1,11):
    print(n, factorial(n))
