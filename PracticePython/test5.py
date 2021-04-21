# from turtle import * 
# from random import  * 

# pSize = 3

# title('원 그리기')
# shape('turtle')

# pensize(pSize)
# screensize(300,300)

# for radians in range(1,250) :

#     if radians%6 == 0 :
#         pencolor('red')
#     elif radians%5 == 0 :
#         pencolor('orange')
#     elif radians%4 == 0 :
#         pencolor('yellow')
#     elif radians%3 == 0 :
#         pencolor('green')
#     elif radians%2 == 0 :
#         pencolor('blue')
#     else :
#         pencolor('purple')      
#     circle(radians)  

select, answer, numStr, num1, num2, num3 = 0, 0,"", 0, 0, 0

select = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 :"))

if select == 1 :
    numStr = input(" *** 수식을 입력하세요 : ")
    answer = eval(numStr)
    print(" %s 결과는 %5.1f입니다." % (numStr, answer))

elif select == 2 :
    num1 = int(input(" *** 첫 번째 숫자를 입력하세요 : "))
    num2 = int(input(" *** 두 번째 숫자를 입력하세요 : "))
    num3 = int(input(" *** 더할 숫자를 입력하세요 : "))
    for i in range(num1, num2+1, num3) :
        answer = answer + i
    print("%d+%d+...+%d는 %d입니다. " %(num1, num3, num2, answer))
else :
    print("1 또는 2만 입력해야 합니다.")
        


