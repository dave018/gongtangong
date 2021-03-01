l = ['one', 'two', 'three']
for num in l:
    print(num)

l2 = [(1,2), (3,4), (5,6)]
for (x,y) in l2:
    print(str(x) + "," + str(y))

print(range(10))
print(range(1,11))

for i in range(10):
    print(i) #0~9
for i in range(1,11):
    print(i) #1~10

marks = [90, 25, 67, 45, 80]
for num in marks:
    if (num <60):
        continue
    print("PASS : {0}".format(num))

for i in range(len(marks)): # range can used for loop arrays
    if (marks[i] <60):
        continue
    print("PASS! : {0}".format(marks[i]), end="-[HS] ") # line "end" is instead of new line
print('')

# imply for-loop in list
l3 = [1,2,3,4]
l3_2 = [num * 3 for num in l3]
print(l3_2)
l3_2 = [num * 3 for num in l3 if num%2 == 0]
print(l3_2)

# 9x9
print([x*y for x in range(2,10) for y in range(1,10)])