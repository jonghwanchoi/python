from tkinter import *
from tkinter import messagebox
from time import *
from random import *

# window.title("윈도 창 연습")
# window.geometry("400x100")
# window.resizable(width = FALSE, height = FALSE) #사이즈 고정

# label1 = Label(window, text = "COOKBOOK~~ Python을")
# label2 = Label(window, text = "열심히", font = ("궁서체", 30), fg = "blue")
# label3 = Label(window, text = "공부 중입니다.", bg = "magenta", width = 20, height = 5, anchor = SE)

# label1.pack();
# label2.pack();
# label3.pack();

# button1 = Button(window, text = "파이썬 종료", fg = "red", command = quit)

# button1.pack()

# def  myFunc() :
#     if chk.get() == 0 :
#         messagebox.showinfo("", "체크버튼이 꺼졌어요.")
#     else :
#         messagebox.showinfo("", "체크버튼이 켜졌어요.")
    
# ## 메인 코드 부분 ##
# chk = IntVar()
# cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)

# cb1.pack()


## 전역  변수 선언 부분 ## 
# fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
# photoList = [None] * 9
# num = 0

# ## 함수 선언 부분 ## 
# def clickNext() :
#     global num
#     num += 1
#     if num > 8 :
#         num = 0
#     photo = PhotoImage(file = "gif/" + fnameList[num])
#     pLabel.configure(image = photo)
#     pLabel.image = photo
    
# def clickPrev() :
#     global num
#     num -= 1
#     if num < 0 :
#         num = 8
#     photo = PhotoImage(file = "gif/" + fnameList[num])
#     pLabel.configure(image = photo)
#     pLabel.image=photo
    
# ## 메인 코드 부분(## 이 부분에서 화면을 구성하고 처리 ## )
# window = Tk()

# window.geometry("700x500")
# window.title("사진 앨범 보기")

# btnPrev = Button(window, text = "<< 이전", command = clickPrev)
# btnNext = Button(window, text = "다음 >>", command = clickNext)

# photo = PhotoImage(file = "gif/" + fnameList[0])
# pLabel = Label(window, image = photo)  

# btnPrev.place(x = 250, y = 10)
# btnNext.place(x = 400, y = 10)
# pLabel.place(x = 15, y = 50)

# window.mainloop()

## 변수 선언 부분 ##
# btnList = [""] * 9
# fnameList = ["honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif", "oreo.gif", "pie.gif"]
# photoList=[None] * 9
# i, k = 0, 0
# xPos, yPos = 0, 0
# num = 0

# ## 메인 코드 부분 ##
# window = Tk()
# window.geometry("210x210")

# for i in range(0, 9) :
#     photoList[i] = PhotoImage(file = "gif/" + fnameList[i])
#     btnList[i] = Button(window, image = photoList[i])  # 이미지 자체를 버튼으로 만들기

# for i in range(0, 3) :
#     for k in range(0, 3) :
#         btnList[num].place(x = xPos, y = yPos)
#         num += 1
#         xPos += 70
#     xPos = 0
#     yPos += 70
# window.mainloop()

## 함수 선언 부분 ##
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
#         txt += "마우스 오른쪽버튼이 더블 클릭됨"
#     messagebox.showinfo("마우스", txt)  
   
# ## 메인 코드 부분 ##
# window = Tk()
# eventName = ["<Button>", "<Double-Button>"]
# mouseClick = [clickMouse, DclickMouse]

# select = int(input("마우스 이벤트 선택 : 0.클릭 1.더블 클릭 ==>"))
# if select < 3 :
#     ch=eventName[select]
#     for i in range(0,2) :
#         if ch == eventName[i] :
#             window.bind(eventName[i], mouseClick[i])
   
# window.mainloop()

# from tkinter import *
# from tkinter.filedialog import *

# ## 함수 정의 부분 ##
# from tkinter.filedialog import *

# ## 함수 선언 부분 ##
# def func_open() :
#     filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
#     photo = PhotoImage(file = filename)
#     pLabel.configure(image = photo)
#     pLabel.image = photo

# def func_exit() :
#     window.quit()
#     window.destroy()

# ## 메인 코드  부분 ##
# window = Tk()
# window.geometry("400x400")
# window.title("명화 감상하기")

# photo = PhotoImage()
# pLabel = Label(window, image = photo)
# pLabel.pack(expand=1, anchor = CENTER)

# mainMenu = Menu(window)
# window.config(menu = mainMenu)
# fileMenu = Menu(mainMenu)
# mainMenu.add_cascade(label = "파일", menu = fileMenu)
# fileMenu.add_command(label = "파일 열기", command = func_open)
# fileMenu.add_separator()
# fileMenu.add_command(label = "프로그램 종료", command = func_exit)

# window.mainloop()


def movekey():
    x,y=0,0
    Button.place(x = x+70, y = y+70 ,width =70, height=70)

## 변수 선언 부분 ##
btnList = [""] * 9
fnameList = ["honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif", "oreo.gif", "pie.gif"]
photoList=[None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0


## 메인 코드 부분 ##
window = Tk()
window.geometry("210x210")

for i in range(0, 8) :
    photoList[i] = randrange(1,9)
    btnList[i] = Button(window, text = photoList[i], command=movekey)  


btnList[0].place(x = 0, y = 0 ,width =70, height=70)

num = int(input("숫자를 입력하시오:"))

btnList[0].place(x = num, y = num ,width =70, height=70)
  




window.mainloop()