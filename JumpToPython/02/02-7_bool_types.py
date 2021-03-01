a=True
b=False
print(str(a) + " " + str(b) + " type(a) : " + str(type(a)))
print(1==1)
print(2<1)

#  value   | T or F
# "Python" | T
# ""       | F
# [1,2,3]  | T
# []       | F
# ()       | F
# {}       | F
# 1        | T
# 0        | F
# None     | F

a = [1,2,3,4]
while a:
    print(a.pop(0))

print(bool("Python")) # True
print(bool([])) # False
