# import turtle
# import random

# ## 전역 변수 선언 부분 ##
# myTurtle , tX, tY, tColor, tSize, tShape= [None] * 6
# shapeList = []
# playerTurtles = []      # 거북 2차원 리스트
# swidth, sheight=500, 500

# ## 메인 코드 부분 ##
# if __name__ == "__main__" :
#     turtle.title('거북 리스트 활용')
#     turtle.setup(width = swidth + 50, height = sheight + 50)
#     turtle.screensize(swidth, sheight)

#     shapeList = turtle.getshapes()
#     for i in range(0, 100) :
#         random.shuffle(shapeList)
       myTurtle = turtle.Turtle(shapeList[0])
#         tX = random.randrange(-swidth / 2, swidth / 2)
#         tY = random.randrange(-sheight / 2, sheight / 2)
#         r = random.random(); g = random.random(); b = random.random()
#         tSize = random.randrange(1, 3)
#         playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])

#     for tList in playerTurtles :
#         myTurtle = tList[0]
#         myTurtle.color((tList[4], tList[5], tList[6]))
#         myTurtle.pencolor((tList[4], tList[5], tList[6]))
#         myTurtle.turtlesize(tList[3])
#         myTurtle.penup() 
#         myTurtle.setpos(tList[1], tList[2])
#         myTurtle.pendown()
#         myTurtle.goto(0,0)
        
#     turtle.done()

# aa = [1,2,3]
# tt1 = (1,2,3)
# print(aa[1:3])
# print(tt1[0:2])

# bb=[]
# dic1 = {1:'a', 2:'b', 3:'c'}
# dic1[1] = 'd'
# bb=dic1[1]
# print(bb)

# student1 = {'학번':1000, '이름':'최종환', '학과':'컴공'}
# student1['연락처'] = '01094663460'
# student1['학과'] = '전자공'
# del(student1['연락처'])

# print(student1.get('')) # ''썼을때 none이라고 반환해줌
# print(student1['학과']) # 위와 동일하게 설정한 경우 오류

# print(student1.keys()) # 키에 대해서만 출력
# print(student1.values()) # 키 값에 대해서 출력

# print('이름' in student1)

# ## 변수 선언 부분 ##
# animals = {"개":"강아지", 
#             "곰":"능소니",
#             "말":"망아지",
#             "소":"송아지",
#             "호랑이":"개호주",
#             "치킨": "꺼벙이",
#             "매":"초고리" };
# while (True) :
#     animal = input("동물의 어미 이름을 입력하세요 : ")
#     if animal in animals :
#         print("%s의 새끼 이름은 %s 입니다." % (animal, animals.get(animal)))
#     elif animal == 'end' :
#         break
#     else :
       # print("리스트에 없는 동물 이름입니다.")

# mySet1 = {1, 2, 3}
# print(mySet1)

# salesList=['삼각김밥','삼각김밥', '바나나', '도시락']
# print(set(salesList))
# num=[1,2,3]
# numList = [num for num in range(1,21) if range (num % 3) == 0]

# foods=['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삽겹살']
# sides=['오뎅', '단무지', '김치']
# appetizes = ['콜라', '커피', '사이다']
# for food, side, appetize in zip(foods, sides,appetizes):
# 	print(food, '--->', side, '-->', appetize)

# dic = dict(zip(foods,sides))

# oldList = ['짜장면', '탕수육', '군만두']
# newList = oldList[:]
# oldList[0]='짬뽕' 

parking = []
top = 0

parking.append("자동차A")
top += 1 # 현재 위치

parking.append("자동차B")
top += 1

parking.append("자동차C")
top += 1

outCar = parking.pop()
top -= 1