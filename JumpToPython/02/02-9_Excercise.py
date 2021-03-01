#Q1
Korean = 80
English = 75
Math = 55
result = (Korean + English + Math) / 3
print(result)

#Q2
num = 13
if num%2 == 1 :
    print("odd number")
else:
    print('even number')

#Q3
PersonalId = "881120-1068234"
date = "19" + PersonalId[:6]
UniqueId = PersonalId[7:]
print("date : " + date + ", UniqId : " + UniqueId)

#Q4
print(UniqueId[0])
print(PersonalId[7:8])

#Q5
a = "a:b:c:d"
print('#'.join(a.split(':')))

#Q6
l6 = [1,3,5,4,2]
l6.sort()
l6.reverse()
print(l6)

#Q7
l7 = ['Life', 'is', 'too', 'short']
print(' '.join(l7))

#Q8
t8 = 1,2,3
t8_2 = (4,)
print(t8 + t8_2)

#Q9
#a['name'] = 'python'
#a[('a',)] = 'python'
#a[[1]] = 'python' # => Dictionary's key couldn't be list
#a[250] = 'python'

#Q10
d10 = {'A':90, 'B':80, 'C':70}
print(d10['B'])
print(d10.pop('B'))
print(d10)

#Q11
l10 = [1,1,1,2,2,3,3,3,4,4,5]
s10 = set(l10)
print(s10)

#Q12
l12 = l12_2 = [1,2,3]
l12[1]=4
print(l12_2)
print(id(l12) == id(l12_2))