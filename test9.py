from module1 import *
from turtle import *

print("로또 추첨을 시작합니다")
lottoNumList = getNum()
print("추첨된 로또 번호==>", lottoNumList)      


setList = getSize(500,500)
title('거북이 문자열 활용')
setup(width = setList[0] + 50, height = setList[1] + 50)
screensize(setList[0], setList[1])

inStr = getString()

for i in inStr :
    xyList = getXY(setList[0], setList[1])
    getColor = getRGB()
    tSize = getSize(0,0,20,100)

    shape('turtle')
    color(getColor[0],getColor[1],getColor[2]) # R, G, B
    write(i,font=("",tSize[2]))
    penup()
    goto(xyList[0], xyList[1])

done()    