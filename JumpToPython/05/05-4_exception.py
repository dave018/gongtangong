'''
f = open("not_exist.txt", 'r') #FileNotFoundError: [Errno 2] No such file or directory: 'not_exist.txt'
f.close()
'''
'''
print(4/0) #ZeroDivisionError : division by zero
'''
'''
a=[1,2,3]
print(a[3]) #IndexError: list index out of range
'''

try:
    4/0
except ZeroDivisionError as e:
    print(e)

try:
    a=[1,2,3]
    print(a[3])
    4/0 # never running
except ZeroDivisionError as e:
    print(e)
except IndexError:
    print("out of range")
finally:
    print("ERROR!")

#catch multi exceptions
try:
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
finally:
    print("ERROR!")

#try-else
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')
finally: #if no error, final clause run
    print("final")

'''
class Bird:
    def fly(self): raise NotImplementedError
class Eagle(Birt):
    pass
eagle = Eagle()
eagle.fly() #NotImplementedError
'''

try:
    raise NotImplementedError #This is like pure virtual function

except NotImplementedError as e:
    print(e) #nothing...?
    print("ERROR")

#custom exception
class MyError(Exception):
    def __str__(self):
        return "[HS] My Error"

def say_nick(nick):
    if nick == 'fool':
        raise MyError()
    print(nick)

try:
    say_nick("fool") #__main__.MyError
except MyError as e:
    print(e) #print __str__
    print("custom error raised")

