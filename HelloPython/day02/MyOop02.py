
class Animal:
    def __init__(self):
        self.age = 0
        
    def getOlder(self):
        self.age += 1

class Bird:
    def __init__(self):
        self.mydist = 0
    def fly(self, distance):    
        self.mydist = distance
        
class Human(Animal, Bird):
    def __init__(self):
        Animal.__init__(self)
        Bird.__init__(self)
        self.name = "홍길동"
    
    def changeName(self, name):
        self.name = name

if __name__ == '__main__':
    
    hum = Human()
    print(hum.age)
    print(hum.name)
    print(hum.mydist)

    hum.getOlder()
    hum.changeName("이순신")
    hum.fly(10)
    print(hum.age)
    print(hum.name)
    print(hum.mydist)
    
    