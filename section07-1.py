# section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스를 생성해서 인스터스화(변수에 할당하는 것)된 변수들은 서로 독립적인 네임스페이스 라는 공간에 저장하고 있음
# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공강
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명:
#     함수
#     함수
#     함수


# 예제1 클래스: 붕어빵 틀을 만듬
class UserInfo:      # 클래스명 맨 앞은 대문자
    # 속성(나이, 성별..), 메소드(걷다, 뛰다, 움직이다..)
    def __init__(self, name):
        self.name = name

    def user_info_p(self):
        print("Name : ", self.name)
    
# 네임스페이스
user1 = UserInfo("Kim")     # 인스턴스화
user1.user_info_p()
user2 = UserInfo("Pack")
user2.user_info_p()

# id : 메모리의 주소값을 찍어줌
print(id(user1))        
print(id(user2))

# 네임스페이스 출력
print(user1.__dict__)
print(user2.__dict__)


# 예제 2
# self의 이해
class SelfTest:
    def function1():        # 클래스 메소드
        print('function1 called!')
    def function2(self):    # 인스턴스 메소드
        print(id(self))
        print('function2 called!')


self_test = SelfTest()
# self_test.function1()
SelfTest.function1()        # self인자가 없어서 function1은 클래스에서 호출해야함.
self_test.function2()

print(id(self_test))
SelfTest.function2(self_test)

# 예제 3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

print(WareHouse.__dict__)   # 클래스 네임스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)


print(user1.stock_num)      # 인스턴스 네임스페이스에 stock_num이 없을 경우 클래스 네임스페이스에서 값을 확인하여 값을 가져옴
print(user2.stock_num)
print(user3.stock_num)

del user1

print(user2.stock_num)
print(user3.stock_num)