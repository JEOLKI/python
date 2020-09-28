from random import *

com = ""
mine = ""
result = ""

i = randint(1,3)

if i == 1:
    com = "가위"
elif i == 2:
    com = "바위"
else:
    com = "보"
    
mine = input("가위/바위/보를 입력하세요\n")

if (com == "가위" and mine == "바위") or (com == "바위" and mine == "보") or (com == "보" and mine == "가위"):
    result = "내가 이겼습니다."
elif (com == "가위" and mine == "보") or (com == "바위" and mine == "가위") or (com == "보" and mine == "바위"):
    result = "컴퓨터가 이겼습니다."
else:
    result = "비겼습니다."
    
print("컴퓨터  : {}" .format(com))    
print("나 : {}" .format(mine))    
print("결과 : {}" .format(result))