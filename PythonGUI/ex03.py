'''
employee1 = {'name':'김말똥', 'addr':'서울'}
employee2 = {'name':'홍길동', 'addr':'인천'}

print('{},{}'.format(employee1['name'], employee1['addr']))
print('{},{}'.format(employee2['name'], employee2['addr']))
'''
'''
#import할 때 ex03-employee1 하면 syntax 에러가 발생한다.
import ex03employee1 as emp1
import ex03employee2 as emp2

print('{}, {}'.format(emp1.name, emp1.age))
print('{}, {}'.format(emp2.name, emp2.age))
'''

class Employee():
	pass

emp1 = Employee()
emp2 = Employee()

# 메모리가 서로 다름.
print(id(emp1))
print(id(emp2))

#같은 클래스의 인스턴스인지 확인
emp1_class = emp1.__class__
emp2_class = emp2.__class__
print(id(emp1_class))
print(id(emp2_class))

emp1.name = "홍길동"
emp1.age = 43

emp2.name = "강길동"
emp2.age = 44

#인스턴스 변수에 접근하기 위해서는 인스턴스 이름을 사용
print("----종업원 이름----")
print(emp1.name)
print(emp2.name)
print("----종업원 나이----")
print(emp1.age)
print(emp2.age)