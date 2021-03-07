### 클래스 메소드와 스태틱 메소드의 구분

#인스턴스 메소드와 클래스 메소드, 스태틱 메소드느 모두클래스 메소드 안에서 정의된다.

    # 인스턴스 메소드는 인스턴스를 통해서 호출되고, 첫번째 인자로 인스턴스 자신을 전달한다(self)

    #클래스 메소드는 클래스를 통해서 호출되고, @classmethod 데코레이터로 정의한다.
    #첫번째 인자로 클래스 자신이 자동으로 전달된다(cls)

    #스태틱 메소드는 위의 두 메소드와는 다르게 인자를 받지 않는다!!
    #클래스 네임스페이스 안에만 있을 뿐, 일반 함수와 똑같다.
    #클래스 안에 정의되어 있다는 것은, 클래스와 연관성이 있는 메소드를 의미한다.
    #따라서, 인스턴스나 클래스를 통해서 호출할 수 있다.
    # @staticmethod 데코레이터를 사용하여 정의한다.

'''
class Demon:
    num = 10

    @staticmethod
    def add(x,y):
        return x+y+Demon.num

d = Demon()

print(d.add(1,2))

print(Demon.add(2,2))
'''

class Person:
    def __init__(self, year, month, day, gender):
        self.year = year
        self.month= month
        self.day = day
        self.gender = gender

    def __str__(self):
        return '{}년 {}월 {}일 {}입니다'.format(self.year, self.month, self.day, self.gender)

    # 아래 id_parser함수를 클래스메소드로 추가해놓는 게 좋다. Person과 관련된 함수니까.
    @classmethod
    def id_constructor(cls, id_number):
        front, back = id_number.split('-')
        gender = back[0]

        if gender == '1' or gender == '2':
            year = '19' + front[:2]
        elif gender == '3' or gender == '4':
            year = '20' + front[:2]

        if (int(gender) % 2) == 0:
            gender = '여성'
        else:
            gender = '남성'

        month = front[2:4]
        day = front[4:6]

        return cls(year, month, day, gender) #return Person(...) 도 되는데, cls가 common한 코드다.

    @staticmethod
    def work_day(day):
        #weekday() 함수의 리턴값은 0,1,2...6 이다. (월~일)
        if day.weekday() == 5 or day.weekday() == 6:
            return '휴무'
        return '근무'

id_number1 = "881212-1292821"
id_number2 = "031010-4202022"

person1 = Person.id_constructor(id_number1)
print(person1)

person2 = Person.id_constructor(id_number2)
print(person2)

import datetime as dt
my_date = dt.date(2018, 10, 10)

print(person1.work_day(my_date))
print(Person.work_day(my_date))