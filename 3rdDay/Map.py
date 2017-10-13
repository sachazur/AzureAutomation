a=[1,2,3,4,5,6,7]
b=[]
for x in a:
    b.append(x*x)

print (b)

#map statement work on iterable elements and if you want to take same action
# on all elements in array

c=map(lambda c:c*c,a)
print (list(c))

print (list(map (lambda x:x+1,a) ) )


#find  factorial
from math import factorial
print (list (map (lambda x:factorial(x),a) ) )

#filter
print (list(filter(lambda x:x%2 == 1,a )))

#reduce always return only a single value
from functools import reduce
print (reduce(lambda d,c:d+c,a))


#exc1, return integers only from list
b=["hello","world","a",2,4,56,1,"sachin"]
print (list(filter(lambda x:type(x)==int,b)))

#exc1, return strings only from list
b=["hello","world","a",2,4,56,1,"sachin"]
print (list(filter(lambda x:type(x)==str,b)))

print (list(filter(lambda x:isinstance(x,str),b)))

a=["ooty","kulu","shimla","lnl"]
print (sorted(a))
print (sorted(a,reverse=True))
print (sorted(a,key=lambda x:len(x)))

d={"name"="sachin";"city"="Pune"}
