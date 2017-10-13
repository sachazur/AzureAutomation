#Tuple is read only list and only have index and count property
#Tuples and Strings are immutable objects
a = (1,2,3,45,5,6)
print (type(a))
print (a[0])
print (a[-1])
print (len(a))
print (sum(a))
print (min(a))
print (max(a))
print (a[2:5])
print (a[::2])

b = 3,4,5
print (type(b))
print (b[0])
print (b.count(3))
#Error
b[2]=45
b.append(6)
