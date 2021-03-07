'''
class Employee:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def empInfo(self):
		return '{}, {}'.format(self.name, self.age)

emp1 = Employee("김개똥", 22)
emp2 = Employee("홍길동", 33)

#인스턴스의 메소드 접근 방법
print(emp1.empInfo())
print(emp2.empInfo())
'''
'''
##클래스변수 vs 인스턴스 변수

# 인스턴스 변수 : 각각의 인스턴스마다 가지고 있는 고유한 ㅔㄷ이터
# 클래스 변수 : 같은 클래스로 만들어진 모든 인스턴스가 공유하는 데이터 

class Employee:
	employeeCnt = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age
		Employee.employeeCnt += 1


	def empInfo(self):
		print("Name : ", self.name, ", Age : ", self.age)

	def empCount(self):
		print("전체 종업원 수 : %d" %self.employeeCnt)

emp1 = Employee("김개똥", 22)
emp2 = Employee("홍길동", 33)

emp1.empInfo()
emp2.empInfo()

emp1.empCount();
emp2.empCount();


'''

### Namespace
# 인스턴스 namespace -> Class namespace -> SuperClass namespace
# 위와 같은 구조에서, 멤버 변수를 찾는 순서는 반드시 인스턴스->Class->SuperClass 순서이다.