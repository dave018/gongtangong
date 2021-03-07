#클래스 만들기
	#class 키워드를 이용해서 선언

class BusinessCard:

	#생성자. __init__()
	def __init__(self, name, email, addr):
		self.name = name
		self.email = email
		self.addr = addr

	def display(self):
		print('----------------------------------')
		print('name : %s' % self.name)
		print('E-mail : %s' % self.email)
		print('Office : %s' % self.addr)
		print('----------------------------------')

member1 = BusinessCard("홍길동", "hong@naver.com", "Seoul")
member1.display()