"""
import random
list1 = []
for i in range(7):
    num = random.randint(1,49)
    list1.append(num)
print('special:',list1.pop())
print(list1)
"""
import random
num = random.sample(range(1,50),7)
special = int(num.pop())
num.sort()
print('this period\'s number is :',num)
print('the special number is:',special)
