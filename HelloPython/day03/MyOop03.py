
class Human:
    def __init__(self):
        self.name = "홍길동"
        print("constructor")

    def __del__(self):
        print("destructor")


if __name__ == '__main__':
    a = Human() #변수에 담아 주었기 때문에 주소지가 있기때문에 프로그램이 끝날때까지 있다.
    b = Human()
    