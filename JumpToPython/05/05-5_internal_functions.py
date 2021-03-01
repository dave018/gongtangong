a = chr(65)
print(a) #A
b = ord('9') - 48
print(b + 10) #19

#print(dir({})) #return member var and functions

a,b = divmod(7,3) #return tuple
print("{0}, {1}".format(a,b))
print(a, b)

#enumerate return tuple which has index and value(from list, tuple, string)
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i,name)

#eval : run express. Usually used if python command has come as string
print(eval('divmod(4,3)'))

def positive(x):
    return x>0
#filter(cond_func, Iteratable)
print(list(filter(positive, [1,-3,2,0,-5,6])))
print(list(filter(lambda x: x>0, [1,-3,2,0,-5,6])))

#hex() return string. and int() can't parse 0x99f201 (ValueError)
print(int(3.14))

a=3
print(isinstance(a,int))

#map(func, iteratable)
a = map(lambda a: a*2, [1,2,3,4])
print(list(a))

print(min([1,2,3]))
print(max([1,2,3]))

print(round(5.678), round(5.678,2))

print(sorted((3,1,2))) #return list
print(sorted("zero"))

class myStr:
    def __str__(self):
        return "myStr"
mystr = myStr()
#str call __str__()
print(str(mystr))

#zip union same len iterable objects. each element turns on tuple
print(list(zip([1,2,3],['a','b','c'])))