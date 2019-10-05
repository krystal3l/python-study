# section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서X, 중복X, 수정O, 삭제O

# Key, Value (json) -> MongoDB
# 선언

a = {'name' : 'Kim', 'Phone' : '010-7777-7777', 'birth' : 870214}
b = {0 : 'Hello Python', 1 : 'Hello Coding'}
c = {'arr' : [1,2,3,4,5]}

# print(type(a))

# 출력
print(a['name'])
print(a.get('name'))
print(a.get('address'))     #값이 없으면 None
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1,3,4]
a['rank2'] = (1,2,3,)
print(a)

# keys, values, items : 아이템은 한쌍을 뜻함 ex) 'name' : 'Kim'
print(a.keys())
print(list(a.keys()))       # 리스트로 형변환

temp = list(a.keys())
print(temp[1:3])

print(a.values())
temp2 = list(a.values())
print(temp2)

print(a.items())
temp3 = list(a.items())
print(temp3)

print(2 in b)
print('name' in a)


# 집합(sets) (순서X, 중복X)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(l)

print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))      # 교집합
print(s1 & s2)

print(s1 | s2)                  # 합집합
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))        # 차집합

# 집합 추가 & 제거 가능
s3 = set([7, 8, 10, 15])
s3.add(18)
# s3.add(7)

print(s3)

s3.remove(15)
print(s3)

print(type(s3))


