#Q1
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
#shirt printed

#Q2
i2 = 0
sum2 = 0
while i2<1000:
    i2 += 1
    if (i2%3 ==0):
        sum2+=i2
print(sum2)

#Q3
i3 = 0
while i3<5:
    i3 += 1
    print('*'*i3)

#Q4
for i4 in range(1,101):
    print(i4)

#Q5
l5 = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum5 = 0
for i5 in l5:
    sum5+=i5
print(sum5/len(l5))

#Q6
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

result6 = [n*2 for n in numbers if n%2==1]
print(result6)