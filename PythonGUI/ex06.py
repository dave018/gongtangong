### 클래스 메소드를 인스턴스 생성자와 같은 용도로도 사용

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

id_number1 = '991010-1234567'
id_number2 = '040205-4065452'

#주민번호를 parsing해서 클래스 생성자에 인자로 전달하는 함수
def id_parser(id_number):
    front, back = id_number.split('-')
    gender = back[0]

    if gender == '1' or gender == '2':
        year = '19' + front[:2]
    elif gender == '3' or gender == '4':
        year = '20' + front[:2]

    if (int(gender) % 2) == 0 :
        gender = '여성'
    else :
        gender = '남성'

    month = front[2:4]
    day = front[4:6]

    return year, month, day, gender


print(id_parser(id_number1))
print(id_parser(id_number2))
person1 = Person(1999, 10, 10, '남자')
person2 = Person(*id_parser(id_number2)) ##### ?? asterisk를 왜 넣는거지??

print(person1)
print(person2)

person3 = Person.id_constructor(id_number1)
print(person3)