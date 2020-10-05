with open("D:/A_TeachingMaterial/8.Python/HelloPython/day08/myfile","r") as f :
    lines = f.readlines()
    for line in lines:
        print(line)
    
    #close를 자동으로 해준다.