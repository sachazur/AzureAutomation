class Car(object):
    def __init__(self,reg_no=None):
        self.reg_no=reg_no
    def __bool__(self):
        if self.reg_no:
            return True
        else:
            return False

zen=Car("MH05BJ203")
alto=Car()
print (bool(zen))
print (bool(alto))
if zen:
    print ("registered")
            
