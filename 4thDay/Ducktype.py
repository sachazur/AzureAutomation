class Car:
    def __init__(self,seats):
        self.seats=seats
    def __str__(self): #duck typing is to make a object behave like some other object
        return "I am a {} seater car".format(self.seats)
    def __len__(self):return self.seats
    def __add__(self,other):
        return len(self) + len(other)
    def __sub__(self,other):#"__sub__"duck typing is to make a object behave like some other object
        return len(other) - len(self)
    

alto=Car(5)
innova=Car(7)

print (alto)
print (innova)

print (len(alto))
print (len(innova))

print (alto + innova)

print (str.upper("print there are {} extra seats in innova".format(alto-innova)))
       
