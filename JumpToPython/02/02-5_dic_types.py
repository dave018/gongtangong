#dic has key & value. value could be any types
# ? how about key's types?

a= {1:'a'}
a[2] = 'b'
print(a)
a[4] = 'd'
a[3] = 'c'
print(a)
del a[4] # dic has no remove()
print(a)

myFruit = {"apple":10, "banana":20}
print(myFruit["apple"])
print(myFruit['apple'])
print(len(myFruit))

myDic = {1:'a', 1:'b'}
print(len(myDic)) # print 1. same key couldn't be exist in one dic
#myDic = {[1,2]:'a'} #key couldn't be list
myDic = {(1,2):'a'} #But key can be tuple
print(myDic[(1,2)])

print(a.keys()) #return dict_keys
print(a.values()) #return dict_values
#dict_keys & dict_values should not be list(dict_keys)
# But they can use iterator but NOT random access like dict_keys[0]
# + NOT append(), insert(), pop(), remove(), sort().
for i in a.keys():
    print("[In for-loop] " + str(i))

print(a.items()) #dict_items
#a.clear() #remove all items.
print(a.get(1)) # same a[1]
#print(a[100]) #KeyError
print(a.get(100)) #return None. None means false
print(a.get(100, "No Element")) #get() has default value
print(100 in a) #print "False"
print(3 in a) #print "True"

myDic = {'a':'A', 'b':'B', 'c':'C'}
myDic.pop('b')
print(myDic)