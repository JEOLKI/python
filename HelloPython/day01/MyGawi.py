from random import *


com = ""
mine = ""
result = ""

i = randint(1,2)
if i == 1:
    com = "홀"
else:
    com = "짝"

mine = input("홀/짝을 입력하세요\n")

if com == mine :
    result = "이겼습니다"
else:
    result = "졌습니다."
    
print("컴 : {}" .format(com))
print("나 : {}" .format(mine))
print("결과 : {}" .format(result))


