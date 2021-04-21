# 참 / 거짓 -->boolean 
# print(5 < 10)
# print(not (5>10))

# station = "사당"
# print(station + "행 열차가 들어오고 있습니다")

# print(1+1)
# print(2**3) #2^3 = 8
# print(5%3) # 나머지 구하기 2
# print(5/3) #소수점까지 나옴
# print(5//3) # 몫 =1
# print(10>3) #True
# print(4 >= 7) #False
# print(5 <= 5) #True
# print(3 == 3) #True
# print(3 != 4) #True
# print(not(1 != 3)) #False
# print((3>0)and(3<5)) #True
# print((3>0) & (3<5)) #True
# print((3>0) or (3>5)) #True
# print((3>0) | (3>5)) #True
# print(5>4>3) #True

# print(2+3*4)
# number = 2 + 3 * 4
# print(number)
# number = number+2
# print(number)
# number += 2
# print(number)

# print(abs(-5))
# print(pow(4, 2)) #4^2 = 16
# print(max(5, 12))
# print(round(3.14)) # 3 반올림

# from math import *
# print(floor(4.99)) #내림, 4
# print(ceil(3.14)) #올림, 4
# print(sqrt(16)) #제곱근, 4

# from random import * # #include랑 비슷한 역할

# day = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월"+ str(day) + "일로 선정되었습니다. ")

# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)

# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# jumin = "990120-1234567" #배열과 같다
# print("성별 : " + jumin[7])
# print("연 : "+ jumin[0:2]) #0부터 2번째자리 직전까지..0,1
# print("월 : "+ jumin[2:4])
# print("일 : "+ jumin[4:6])

# print("생년월일 : "+ jumin[:6]) #처음부터 6 직전까지
# print("뒤 7자리 : "+jumin[7:]) #7부터 끝까지
# print("뒤 7자리 : " + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

# python = "Python is Amazing"
# print(python.lower()) #소문자로 출력
# print(python.upper())
# print(python[0].isupper()) #문자열 0번째 값이 대문자인지? True or False
# print(len(python)) #문자열 길이 구하기
# print(python.replace("Python", "Java")) #원하는 글자로 대체

# index = python.index("n") #해당 문자 첫 위치(index) 찾기




# index = python.index("n", index+1) #해당 문자의 두번째 위치
# print(index)

# print(python.find("Java")) #원하는 값이 없을때 -1반
# # print(python.index("Java")) #원하는 값이 없을때 오류 및 종료
# print(python.count("n")) #해당 문자 개수
# print(index)

# print("hello world")