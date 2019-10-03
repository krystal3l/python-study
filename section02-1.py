#Section02-1
#파이썬 기초 코딩
#Print 구문의 이해
#  -print를 사용하면 기본 엔터값(줄바꿈)이 존재함
#  -seperator 옵션
#  -end 옵션

#기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

#seperator 옵션 사용
print('t','e','s','t', sep='')
print('2019','02','19', sep = '-')
print('niceman','google.com',sep='@')


#end 옵션 사용 (print의 엔터 역할을 빼버림)
print('welcome To', end='')
print(' the black', end ='')
print (' piano notes')


#format 사용
print('{} and {}'.format('You','Me'))
print("{0} and {1} and {0}".format('You','Me'))
print("{a} are {b}".format(a='You', b='Me'))

print("%s's favorite number is %d" % ('Eunki',7)) # %s : 문자, %d : 정수 , %f : 실수(소수점)

print("Test1 : %5d, Price: %4.2f" % (776, 6534.123))
print("Test1 : {0: 5d}, Price : {1:4.2f}".format(776,6534.123))
print("Test1 : {a:5d}, Price : {b:4.2f}".format(a=776,b=6534.123))

print("'you'")
print('\'you\'')
print('\t test')