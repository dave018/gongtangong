#Q1
def is_odd(a):
    return a%2 == 1
print(is_odd(3))

#Q2
def myAverageFoo(*args):
    avg = 0
    for i in args:
        avg += i
    avg /= len(args)
    return avg
print(myAverageFoo(3, 6, 7, 10))

#Q3
'''
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
'''

#Q4
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python") # , makes ' ' in print()
print("".join(["you", "need", "python"]))

#Q5
with open("04-4_tests.txt", 'w') as f:
    f.write("Life is too short\n")
with open("04-4_tests.txt", 'r') as f:
    print(f.read())
#or f1.close()

#Q6
with open("04-4_tests_Q6.txt", 'a') as f:
    data = input("inputs : ")
    f.write(data + "\n")

#Q7
data = ""
with open("04-4_tests_Q7.txt", 'r+') as f:
    data = f.read()
print(type(data))
print(data.find("java"))
data = data.replace("java", "python")
print(data)
with open("04-4_tests_Q7.txt", 'w') as f:
    f.write(data)