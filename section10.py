# section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크


# SyntxaError : 잘못된 문법
# print('Test)
# if True 
#     pass
# x => y


# nameError : 참조변수 없음
# a = 10
# b = 15
# print(c)


# ZeroDivisionError : 0 나누기 에러
# print(10/0)


# IndexError : 인덱스 범위 오버
x = [10, 20, 30]
print(x[0])
# print(x[3]) # 예외 발생


# KeyError
dic = {'name':'Kim', 'Age' : 33, 'City':'Seoul'}
#print(dic['hobby'])
print(dic.get('hobby')) # hobby라는 키 값이 있는지 get 메소드 이용하기


# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
import time
print(time.time())
# print(time.month())


# ValueError : 참조 값이 없을 때 발생
x = [1, 5, 9]
# x.remove(10)
# x.index(10)


# FileNotFoundError 
# f = open('test.txt', 'r') # 예외 발생


# TypeError
x = [1, 2]
y = (1, 2)
z = 'test'
# print(x + y) # 예외
# print(x + z)

#print(x + list(y)) # 예외


# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩하기
# 그 후에 런타임 예외 발생시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본. try문에서 에러가 발생하면 except로 빠짐
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행


# 예제1
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim' # cho 예외 발생
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occutted ValueError!')
else:
    print('Ok! else!')


# 예제2
try:
    z = 'Jin'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:
    print('Not found it! - Occutted Error!')
else:
    print('Ok! else!')


# 예제3
try:
    z = 'Jin'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:
    print('Not found it! - Occutted Error!')
else:
    print('Ok! else!')
finally:
    print('finally ok!')


# 예제4
# 예제 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('Try')
finally:
    print('ok Finally!!')

print()


# 예제5
try:
    z = 'Jin'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError as l:
    print(l)
except IndexError:
    print('Not found it! - IndexError Error!')
except Exception:
    print('Not found it! - Occutted Error!')
else:
    print('Ok! else!')
finally:
    print('finally ok!')


# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Kim'
    if a == 'Kim':
        print('Ok 허가!')
    else:
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('ok!')

