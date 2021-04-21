ss, rss= [], []
ss = input("문자열을 입력하세요 : ")
ssLen = len(ss)

for i in range(ssLen-1,-1,-1):
        rss.append(ss[i])
print("문자열 거꾸로 출력 --> ",' '.join(rss))

# import turtle
# import random
# from tkinter.simpledialog import * 

# tX, tY, tColor, tSize = 0,0,0,0
# swidth, sheight=500, 500

# turtle.title('거북이 문자열 활용')
# turtle.setup(width = swidth + 50, height = sheight + 50)
# turtle.screensize(swidth, sheight)

# inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')

# for i in inStr :
#     tX = random.randrange(-swidth / 2, swidth / 2)
#     tY = random.randrange(-sheight / 2, sheight / 2)

#     r = random.random(); g = random.random(); b = random.random()

#     tSize = random.randrange(20, 100)
#     turtle.shape('turtle')
#     turtle.color(r,g,b)
#     turtle.write(i,font=("",tSize))
#     turtle.penup() #default값이 pendown
#     turtle.goto(tX, tY)

# turtle.done()    