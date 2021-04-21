
sel = int(input("입력 진수 결정 (16/10/8/2) : "))

num = input("값 입력 : ")

if sel == 16 :
    num10 = int(num, 16)
if sel == 10 :
    num10 == int(num, 10)

print(hex(num10))
# %%
