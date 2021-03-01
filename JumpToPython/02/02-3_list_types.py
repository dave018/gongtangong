#list can have element. And element could be any types

a = [1, 2, 3]
print(a[-3]) #print 1
#print(a[-4]) #out of range error

print(a[:2]) #print [1, 2]
print(a*2)
b = [4, 5]
print(a+b)
print(b+a)
a.extend(b) # same with a = a+b
print(a)
a.extend([4,5])
print(a)
a[0]=100 # wow! modify random accessed element!
print(a)
#extend == list+list

print(len(a+b))
print(str(a[-1])+"hi") #without str(), TypeError

print(a)
del a[1] #del means delete OBJECT
print(a)

a = [1, 2, 3, 4, 5]
del a[1:3]
print(a)
a.append(2)
a.append(3)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(a.index(5)) # same str.find(). If it couldn't be found, ValueError
#print(a.find(1)) # list has no .find()

del a[1]
a.insert(1,2)
print(a) #[5, 2, 3, 2, 1]
a.remove(2) # remove first 2. If no exist, ValueError
print(a) # print [5,3,2,1]
print(a.pop()) #pop last one and return.
print(a)
print(a.pop(0)) #pop [0]. and return.
print(a)