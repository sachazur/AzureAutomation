#genreate random number
def genrandom():
    import random #import genral or you can do from random import 
    i = random.randrange(10,1000)
    return i

# store random numbers in list
lis=[]
for i in range(10001):
    lis.append(genrandom())
print (lis)

# find how many times each number is repeated:

uniq=[]

for x in lis:
    if x not in uniq:
        uniq.append(x)

for x in uniq:
    print(x,lis.count(x))


# find how many times each number is repeated or

for x in set(lis):
    print(x,lis.count(x))
#how to create set,sets don't have order
myfriends = {"hari","Sita","Ram","Laxman"}
mywifesfriends = {"hari","ajay","Rahul","ramya"}
myfriends.union(mywifesfriends)
myfriends - mywifesfriends # or myfriends.difference(mywifesfriends)
myfriends.intersection(mywifesfriends)
