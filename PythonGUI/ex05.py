### 클래스 메소드

# 인스턴스 메소드는 self인 인스턴스를 인자로 받고 인스턴스에만 한정된 데이터를 생성 또는 변경 또는 참조한다.
# 클래스 메소드는 cls인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수처럼 데이터를 생성 또는 변경 또는 참조한다.

class Employee(object):
    raise_amount = 1.1 #연봉 인상률 클래스 변수

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.'+last.lower() + '@naver.com'

    def apply_raise(self):
        print('before "{}", after "{}"'.format(self.pay, self.pay * self.raise_amount))
        self.pay = int(self.pay * self.raise_amount)

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def get_pay(self):
        return '현재 "{}"의 연봉은 "{}" 입니다.'.format(self.full_name(), self.pay)

    #클래스 메소드 데코레이터를 이용한 클래스 메소드 정의
    @classmethod
    def set_raise_amount(cls, amount):
        # 인상률이 1 보다 작으면 재입력 하도록 한다.
        while amount <= 1:
            print('인상률은 1보다 커야합니다')
            amount = input("인상률을 다시 입력해주세요\n =>")
            amount = float(amount)

        cls.raise_amount = amount
        print("인상률 '{}'가 적용되었습니다".format(amount))

employee1 = Employee('gildong', 'Hong', 4000)
employee2 = Employee('maldong', 'Kim', 5000)

#인상 전 연봉
print(employee1.get_pay())
print(employee2.get_pay())

#연봉 인상률 변경하기(클래스 메소드 호출은 클래스 이름을 사용)
Employee.set_raise_amount(0.9)

#연봉 인상하기
employee1.apply_raise()
employee2.apply_raise()

#인상 후 연봉
print(employee1.get_pay())
print(employee2.get_pay())