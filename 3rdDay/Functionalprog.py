#lambda Function:
square = lambda a:a*a
print (type(square))
print (square(4))

def abc(myfun,x):
    return myfun(x)

def cube(x):
    return x**3

print (abc(cube,5))

print (abc(square,6))

print (abc(lambda d:d*d*d,60))
