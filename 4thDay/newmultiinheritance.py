class Dog:
    def speak (self):   print ("bhou")
    def likes (self):   print ("bones")
    def guard (self):   print ("guarding")
class Cat:
    def speak (self):   print ("meau")
    def likes (self):   print ("milk")
    def hunts (self):   print ("mice")
class Doat(Dog,Cat):
    def speak (self):   print ("bou..meau")
    def hpbby (self):   print ("python")
    def pspeak (self):   super (Doat,self).speak() # super class



print (Doat.__mro__) # get method resolution order


            
                
