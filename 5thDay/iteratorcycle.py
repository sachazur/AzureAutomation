class Week:
    def __init__(self):
        self.days="SMTWtFs"
    def __iter__(self):
        self.count = 0
        return self
    def __next__(self):
        output=self.days[self.count % 7]
        self.count +=1
        return output

import time
for weekday in Week():
    print (weekday)
    time.sleep(1)
import itertools

for x in zip(range(1,32),Week()):
    print (x)
