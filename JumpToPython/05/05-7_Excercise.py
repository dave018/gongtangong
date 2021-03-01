#Q1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self,val):
        self.value +=val

class UpgradeCalculator(Calculator):    
    def sub(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.sub(7)
print(cal.value)

#Q2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if (self.value >100):
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

#Q3
print(all([1,2,abs(-3)-3])) #False
print (chr(ord('a')) == 'a') #True

#Q4
print(list(filter(lambda x: x>=0, [1,-2,3,-5,8,-3])))

#Q5
print(int(hex(234), base=16))

#Q6
print(list(map(lambda x: x*3, [1,2,3,4])))

#Q7
l7 = [-8,2,7,5,-3,5,0,1]
print(max(l7))
print(min(l7))

#Q8
print(round(17/3, 4))

#Q9
import sys
res9 = 0
for i in range(1, len(sys.argv)):
    rest9 += sys.argv[i]
print(res9)

#Q10
import os
#os.chdir("C:\SamsungU\JumpToPython")
#res10 = os.system("dir")
#print(res10)

#Q11
import glob
print(glob.glob(os.getcwd() + "\*.py"))

#Q12
import time
#this is answer. But it doesn't print 21/03/01 14:30:54.
#print Mon Mar  1 14:30:27 2021
print(time.strftime('%c', time.localtime(time.time())))

#Q13
import random
numbers13 = list(range(1,46))
while (len(numbers13) > 39):
    num = random.choice(numbers13)
    print(num)
    numbers13.remove(num)
print(numbers13)