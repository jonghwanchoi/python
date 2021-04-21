# intNum = int(input("지폐로 교환할 돈은 얼마? "))
num_list = list(map(int, input("지폐 종류 입력 : ").split()))
# strVal_1 = "%d원짜리 ==> %d장"
# strVal_2 = "지폐로 바꾸지 못한 잔돈 : %d원"

# for i in num_list :
#     result = intNum / i
#     intNum %= i
#     print(strVal_1 % (i,result))
# print(strVal_2 % intNum)

from turtle import * 
from random import  * 
s_width, s_height, pSize, exitCount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY, lastX, lastY = [0] * 9

title('거북이가 맘대로 다니기')

shape('turtle')
pensize(pSize)
setup(width = s_width + 30, height = s_height + 30)
screeensize = (s_width, s_height)

while True :

    r= random()
    g= random()
    b= random()
    pencolor((r, g, b))

    angle = randrange(0,360)
    dist = randrange(1, 100)

    # left(angle)
    # forward(dist)
    # circle(dist,)

    curX = xcor() #현재 x좌표 대입
    curY = ycor() #현재 y좌표 대입

    if(-s_width / 2 <= curX and curX <= s_width/2) and (-s_height / 2 <= curY and curY <= s_height / 2) :
        # x좌표 -150~150 , y좌표 -150~150 안에 있을때만 움직임 수행
        lastX = curX
        lastY = curY
    else :
        penup()
        left(45)
        goto(lastX, lastY) # 조건을 벗어나면 원점(0, 0)으로 되돌아오기
        pendown()

        # exitCount += 1 # 원점으로 되돌아오는 것을 5번 카운트 후
        # if exitCount >= 5 :
        #     break # while문 빠져나가기
done()