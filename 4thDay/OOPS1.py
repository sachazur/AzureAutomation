class Dog:
    __legcount = 4
    __eyecount = 2
    __puppycount = 0
    def __init__(self,color="red",breed="gs"):
        self.color=color
        self.breed=breed
        Dog.__puppycount+=1
        
    def speak(self): #normal method
        print ("Bhow")
    def guard(self):
        print ("I am guarding your house")
    @classmethod #binding method to class,eg.classmethod
    def getpuppycount(cls):
        print(cls.__puppycount)
    @staticmethod
    def simpleinterest (p,t,r):
        print (p*t*r/100)

#tommy.Bite()
#class always starts with Capitalletter
#__init__ is intializer or constructors
        
#_"variablename", adding _ is sign that this is private variable its convention
#"__" sudo underscore for private variable
