x = 1
y = 3

if (x==y) :
    print("YES")
else :
    print("NO")

y = 1
if (x>y) or (y<x) :
    print("YES")
else :
    print("NO")

if (x>y) | (y<x) :
    print("YES")
else :
    print("NO")

if (x>y) and (y<x) :
    print("YES")
else :
    print("NO")

if (x>y) & (y<x) : # && is SyntaxError
    print("YES")
else :
    print("NO")

l = [1,2,3] #tuple is okay
if (1 in l):
    print("YES")
if (100 not in l):
    print("YES")

s = "Hello World"
if ("Hell" in s): #string is okay. not only character
    print("string in YES")

# in if clause, empty code is SyntaxError. pass is needed.
if (2<3): pass #one line could be same line with if clause
else: print("pass NO")

x = 3
if (x>5): x = 500
elif (x > 3): x = 300
else: x = 100

x = 3
x = 500 if x>5 else 100  #Same in C : "x = c ? 500 : 100;" But elif is SyntaxError
print(x)
