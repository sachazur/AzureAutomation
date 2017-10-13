class Squares:          #Generator example 
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        self.count=0
        return self
    def __next__(self):
        if self.count <= self.n:
            output=self.count * self.count
            self.count += 1
            return output
        else:
            raise StopIteration

for i in Squares(100):
    print (i)
            
#list comprehension:
a = [1,2,3,4,5,6]
b=[]
for x in a:
    b.append(x*2)
print(b)

c = [x*2 for x in a] #list comprehension
e=[x*x  for x in a if x%2 ==1] #list comprehension

print (type([x*x for x in range(1,10000,2)])) # list type

print (type((x*x for x in range(1,10000,2)))) # generator type, change square bracketsto round brackets

sys.getsizeof(([x*x for x in range(1,10000,2)])) 
sys.getsizeof((x*x for x in range(1,10000,2))) # observe the memory consumption difference





