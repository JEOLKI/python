from random import *

# random값 만들기 (시작, 끝)
com = randint(1,2)

# 스캐너와 같은역할
mine = input("홀/짝을 입력하세요\n")

if com == 1:
    if mine == "짝":
        print("이겼습니다.")
    else:
        print("졌습니다.")
else:
    if mine == "홀":
        print("이겼습니다.")
    else:
        print("졌습니다.")
    
