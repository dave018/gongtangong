# Actually, print doesn't need + between "" or '' strings
print("a" "b" "c") #abc
print('a' 'b' 'c')
print("a", "b", "c")#a b c
a = "asdf"
#print(a "a") #SyntaxError

#there is no start keyword in print()
for i in range(1,11):
    print(i, end=' ')