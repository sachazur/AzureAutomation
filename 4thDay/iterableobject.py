class Car:
    def __init__(self):
        self.seats=5
        self.space=[]
    def board(self,x):
        if len (self.space) < 5:
            self.space.append(x)
        else:
            print("your car is full")
    def list(self):print(self.space)
    def __iter__(self):
        self.count=0
        return self
    def __next__(self):
        if self.count < len(self.space):
            passenger=self.space[self.count]
            self.count += 1
            return passenger
        else:
            raise StopIteration  # inbuilt method to stop iteration


alto=Car()
alto.board("raj")
alto.board("Yat")
alto.board("Ram")
alto.board("Lax")
alto.board("Sur")
alto.board("tej")
alto.list()

for i in alto:
    print (i)
    
