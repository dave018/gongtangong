s1 = set("Hello")
print(s1) #print {'l', 'e', 'o', 'H'}. But result would be changed if retry
#set : no duplicate element
#      Unordered == dic != list, tuple

l1 = list(s1)
t1 = tuple(s1)
print(l1[0] + ", " + t1[1])

s1 = set([1,2,3,4,5,6])
s2 = set((4,5,6,7,8,9))
print(s1&s2) # same s1.intersection(s2)
print(s1|s2) # same s1.union(s2)
print(s1-s2) # same s1.difference(s2)
print(s2-s1) # same s2.difference(s1)

s1 = s1-s2 #1,2,3
s1.add(4)
print(s1)
s1.add(4) #no effect
print(s1)

s1.update([4,5,6]) #same with add(4); add(5); add(6);
print(s1)

s1.remove(3) #Thers is no multiple remove method
print(s1)