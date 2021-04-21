#함수 모음 => 모듈화
import random
from tkinter.simpledialog import *

def getNum():
    randnumList = []
    for i in range(0,6):   
        lottoNum= random.randrange(1,46) #중복 방지 설정 해줘야함
        randnumList.append(lottoNum)
        if i>0 :
            for j in range(0,i):
                if randnumList[i]==randnumList[j] :
                    del randnumList[i]
                    i-=1
    return randnumList


def getXY(swidth, sheight):
    xyList = []
    tx = random.randrange(-swidth / 2, swidth / 2)
    ty = random.randrange(-sheight / 2, sheight / 2)
    xyList.append(tx)
    xyList.append(ty)
    return xyList

def getRGB():
    RGBlist = []
    for i in range(0,3):
        RGBlist.append(random.random())
    return RGBlist

def getString():
    getStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')
    return getStr

def getSize(swidth, sheight, a=0, b=1):
    tSize = 0
    sizeList = [swidth, sheight]
    tSize = random.randrange(a, b)
    sizeList.append(tSize)
    return sizeList



