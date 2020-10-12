import threading
 
def printChar(start, stop):
    str_line = ""
    for i in range(start, stop):
        str_line += str(chr(i))
        if i%100 == 0:
            print(str_line)
            str_line =""

def printNumber(start, stop):
    str_line = ""
    for i in range(start, stop):
        str_line += str(i)
        if i%100 == 0:
            print(str_line)
            str_line =""
        
if __name__ == '__main__':
    
    printChar = threading.Thread(target=printChar, args=(1, 100000))
    printNum = threading.Thread(target=printNumber, args=(1, 100000))

    printChar.start()
    printNum.start()

