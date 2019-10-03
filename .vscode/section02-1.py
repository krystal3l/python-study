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
