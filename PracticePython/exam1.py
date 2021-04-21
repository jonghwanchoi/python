from tkinter import *
from tkinter import messagebox
import random

btnList = [""]*9
NumList = [1,2,3,4,5,6,7,8,None]
random.shuffle(NumList) # 숫자 섞기

def moveButton(button_1, button_2, index) :
    if button_1["text"] != str(index+1) :
        temp=NumList[index]
        NumList[index]=NumList[index+1]
        NumList[index+1] =temp
    else :
        pass

window = Tk()
window.title("3X3 Puzzle")
window.geometry("300x300")
window.resizable(False, False)

for i in range(0, 9) :
    btnList[i] = Button(window, text = NumList[i], width =13, height=6, command = lambda: moveButton(btnList[i], btnList[i+1], i)) 

btnList[0].grid(row=0, column =0)
btnList[1].grid(row=0, column =1)
btnList[2].grid(row=0, column =2)

btnList[3].grid(row=1, column =0)
btnList[4].grid(row=1, column =1)
btnList[5].grid(row=1, column =2)

btnList[6].grid(row=2, column =0)
btnList[7].grid(row=2, column =1)
btnList[8].grid(row=2, column =2)



# for i in range(0, 3) :
#     for k in range(0, 3) :
#         if num<8 :
#             btnList[num].place(x = xPos, y = yPos, width =100, height=100)
#             num += 1
#             xPos += 100
#     xPos = 0
#     yPos += 100

window.mainloop()

# # 함수 선언 부분 ##
# def clickMouse(event) :
#     txt =""
#     if event.num == 1 :
#         txt += "마우스 왼쪽 버튼이 클릭됨"
#     elif event.num == 2 :
#         txt += "마우스 가운데 버튼이 클릭됨"
#     elif event.num == 3 :
#         txt += "마우스 오른쪽버튼이 클릭됨"
#     messagebox.showinfo("마우스", txt)

# def DclickMouse(event) :
#     txt =""
#     if event.num == 1 :
#         txt += "마우스 왼쪽 버튼이 더블 클릭됨"
#     elif event.num == 2 :
#         txt += "마우스 가운데 버튼이 더블 클릭됨"
#     elif event.num == 3 :
#         txt += "마우스 오른쪽 버튼이 더블 클릭됨"
#     messagebox.showinfo("마우스", txt)

# def DragLeft(event) :
#     messagebox.showinfo("마우스", "마우스 왼쪽 버튼이 드래그됨")
# def DragCenter(event) :
#     messagebox.showinfo("마우스", "마우스 가운데 버튼이 드래그됨")
# def DragRight(event) :
#     messagebox.showinfo("마우스", "마우스 오른쪽 버튼이 드래그됨")    
   
# ## 메인 코드 부분 ##
# window = Tk()
# eventName = ["<Button>", "<Double-Button>", "<B1-Motion>", "<B2-Motion>", "<B3-Motion>"]
# mouseClick = [clickMouse, DclickMouse, DragLeft, DragCenter, DragRight]

# select = int(input("마우스 이벤트 선택 : 0.클릭 1.더블 클릭 2.드래그 ..4==>"))
# if select < 5 :
#     ch=eventName[select]
#     for i in range(0,5) :
#         if ch == eventName[i] :
#             window.bind(eventName[i], mouseClick[i])

# window.mainloop()