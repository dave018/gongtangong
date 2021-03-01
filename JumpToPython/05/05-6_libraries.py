#.py arguments like C's char *argv[], argc
import sys
print(len(sys.argv), ",", sys.argv)

# pickle requires open byte mode
import pickle
with open("test.txt", 'wb') as f:
    data = {1: 'python', 2: 'you need'}
    pickle.dump(data, f)
with open("test.txt", 'rb') as f:
    data = pickle.load(f)
    print(data)

import os
#os.environ is dict
print(os.environ['PATH'])

myDir = os.getcwd()
os.chdir("C:\WINDOWS")
print(os.getcwd())
os.chdir(myDir)
print(os.getcwd())

print("====================")
print(os.system("dir Modules05"))
osRet = os.popen("dir Modules05")
print("[from Python]\n", osRet.read())
#remove file: os.unlink()
#os.mkdir
#os.rmdir
#os.rename(src, dst)

import shutil
#shutil.copy("src.txt", "dst.txt")

import glob
#read all file names in directory
#meta character *, ? can be used
print(glob.glob(os.getcwd() + "\Modules05\*"))
print(glob.glob(os.getcwd() + "\\03*"))

import tempfile
#filename = tempfile.mkstemp() #real create tmp file at C:\Users\nhyunseok\AppData\Local\Temp
#print(filename)
f = tempfile.TemporaryFile() #default open mode is 'wb'
print(f.name)
f.close() #delete this file

import time
time.time()
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime()) #same with above line
print(time.strftime('%c', time.localtime(time.time()))) #with localtime(),(only time.time()) TypeError: Tuple or struct_time argument required

for i in range(3):
    print(i)
    time.sleep(1)

import calendar
#print(calendar.calendar(2021))
#print(calendar.prcal(2021))
print(calendar.prmonth(2021, 12)) # ? why print "None" end of result?
print("hi")

print(calendar.monthrange(2021,3)) #(1,31).. but real return (2,31). BUG!
#monday : 0, sunday: 6
#if (calendar.weekday(2021,12,25) == (5 or 6)):
if (calendar.weekday(2021,12,25) in (5,6)):
    print("T^T")

import random
print(random.random())
print(random.randint(1,10))

def random_pop(data):
    #indexNum = random.randint(0, len(data)-1)
    #return data.pop(indexNum)
    ele = random.choice(data)
    data.remove(ele)
    return ele

data = [10,20,30,40,50]
#random.shuffle should use list
random.shuffle(data)
print(data)
while data:
    print(random_pop(data))
