# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형


# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
print("4-1. ", int("30"))
print("4-2. ", float("30"))
print("4-3. ", complex("30"))
print("4-4. ", str(30))


# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
a = 'Niceman'
print("5. ", a[4:])

a_idx = a.index('man')
print(a_idx)
print("5. ", a[a_idx : ])

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
#  list = str.split() : 문자열 => 리스트, 공백시 스페이스 기준
# ''.join( list ) : 리스트에서 문자열으로

a6 = 'Strawberry'
print(''.join(reversed(a6)))

a61 = 'Strawberry'
# print(list(reversed(a61)))
print(a61[::-1])


# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
a7 = '010-7777-9999'
print(a7.replace('-', ''))

# 정규표현식
import re
print(re.sub('[^0-9]','',a7))       # 숫자가 아닌 데이터를 찾아서 ''로 대체하라


# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
a9 = "NiceMan"
print(a9.upper())
print(a9.lower())



# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
a11 = ["Banana", "Apple", "Orange"]
del a11[1]
print(a11)


# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
t12 = (1,2,3,4)
l12 = list(t12)
print(type(l12))


# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
dict1 = {
    "성인" : 100000, 
    "청소년" : 70000, 
    "아동" : 30000
    }
print(dict1)


# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
dict1["소아"] = 0
print(dict1)


# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print(list(dict1.keys()))

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print(list(dict1.values()))

