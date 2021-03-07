# [ 클래스의 상속 ]
# 기존에 만들어진 클래스를 확장하는 개념

# 상속(부모로부터 물려 받는 것)의 활용
# 다수의 기능을 하는 함수(메소드)를 한데 묶어 하나의 클래스를 만들어두고
# 이 클래스가 가지고 있는 모든 기능을 그대로 가져오면서,
# 거기에 더해 기능을 첨가하여 더 나은 클래스를 만들어 사용하는 것

# 클래스 옆에 소괄호를 해도되고 안해도 된다.
class Parent():
    def print_last_name(self):
        print('김')

class Parent2:
    def print_middle_name(self):
        print('수한무')

# 다중 상속도 된다.
class Child(Parent, Parent2):
    def __init__(self, name):
            self.name = name
    def print_first_name(self):
        print('말똥')
        
    def print_last_name(self):
        print('이')

child = Child("거북이")
child.print_last_name()
child.print_middle_name()
child.print_first_name()

# 상속을 받은 클래스(Child 클래스)는 기존에 부모로부터 물려받은 함수를 덮어쓰기(Overwrite)할 수 있다.
# 즉, 부모격에 해당하는 클래스에 있는 함수(메소드)를 같은 이름의 함수로 정의하면서
# 그 기능(함수의 내용)을 바꿀 수 있다.
# => Overriding

class Person:
    def greeting(self):
        print('안녕하세요')

class Student(Person):
    #오버라이딩
    def greeting(self):
        # print('안녕하세요. 저는 파이썬을 배우는 학생입니다.')
        super().greeting() # 기반 클래스의 메소드를 호출하여 중복을 줄인다.
        print('저는 파이썬을 배우는 학생입니다.')


# 여기서 Person 클래스를 부모클래스(기반 클래스)라고 한다.
# Student 클래스는 자식클래스(파생클래스, 서브클래스, 하위클래스)

kim = Student()
kim.greeting()
person = Person()
person.greeting()