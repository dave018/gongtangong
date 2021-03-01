a = [1,2,3]
b = a
print(id(a))
print(id(b))
print(id(a) == id(b))
b[2] = 100
print(a)

b = a[:] # Copy_1 a to b
print(id(b))
print(id(a) == id(b)) # False

from copy import copy
b = copy(a) # Copy_2 a to b
print(id(b))

'''
----------------------------------
'''

(a, b) = ("Hello", 'world')
print(a + " " + b)
print(str(id(a)) + " " + str(id(b)))
a,b = b,a
print(a + " " + b)
print(str(id(a)) + " " + str(id(b))) # id also swapped a <-> b