from datetime import datetime
d=datetime.now()
print (d)
print (d.year)
print  (d.month)
print (d.day)
print (d.hour)
print (d.minute)
print (d.second)

print (d.strftime("%A %d. %B %Y"))
print (d.strftime("%d %m %y"))




#performance measurement

import time
starttime=time.time()

for x in range(1000):
     x**x


endtime=time.time()

print(endtime-starttime)

time.sleep(1)
