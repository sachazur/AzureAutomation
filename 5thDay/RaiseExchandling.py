def factorial(n):
    f=1
    if n < 0 :
        raise ValueError("no factorial for -ve num")
    for x in range(2,n+1):
        f*=x
    return f

print(factorial(0))
print(factorial(-4))
print(factorial(4))
print(factorial('s'))
