import time as t 
timestart = t.clock()
for i in range(0,1000):
    for j in range(0,1000):
        n = float(i) *float(j)
stop = t.clock()
print('it take\'s ',str(stop-timestart),'to run 1000000 times')
