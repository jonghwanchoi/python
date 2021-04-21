flag = True
while flag : 
    print("계산기의 숫자 입력 방식을 선택해주세요 : ")
    print("1. 실수")
    print("2. 정수")
    number = int(input())
    if(number==1) :
        print("실수형 숫자 2개를 입력하세요 :")
        a = float(input())
        b = float(input())
        flag = ~(flag)
    elif(number==2) : #else if -> elif
        print("정수형 숫자 2개를 입력하세요 :")
        a = int(input())
        b = int(input())
        flag = ~(flag)
    else : print("잘못된 입력 방식입니다.")
    
result = a + b
print("덧셈 : ", a, "+", b, "=", result)
result = a - b
print("뺄셈 : ", a, "-",b, "=", result)
result = a * b
print("곱셈 : ", a, "*", b, "=", result)
result = a / b
print("나눗셈 : ", a, "/", b, "=", result)

result = a // b 
print("몫 구하기 : ", a, "//", b, "=", result) #몫 구하기
result = a % b 
print("나머지 구하기 : ", a, "%", b, "=", result) #나머지 구하기
result = a ** b 
print("제곱근 구하기 : ", a, "**", b, "=", result) #제곱근 구하기

