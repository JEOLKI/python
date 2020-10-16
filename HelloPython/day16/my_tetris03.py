import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QLabel
from sqlalchemy.sql.expression import except_

form_class = uic.loadUiType("tetris.ui")[0]

class Block:
    def __init__(self):
        self.kind = 3
        self.status = 1
        self.i = 1
        self.j = 5
        
    def __str__(self):
        return str(self.kind)+" "+str(self.status)+" "+ str(self.i)+" "+str(self.j)


class WindowClass(QMainWindow, form_class) :

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.block2D = []
        self.stack2D = []
        self.scrin2D = []
        self.lbl2D = []
        self.block = Block()
        
        self.initBlock2DStack2DScrin2D(self)
        
        self.scrin2D[0][0] = 1
        self.scrin2D[0][1] = 1
        self.scrin2D[1][1] = 1
        self.scrin2D[2][1] = 1
        
        for i in range(20) :
            arr = []
            for j in range(10) :
                label = QLabel(self)
                label.setGeometry(25*j, 25*i, 24, 24)
                arr.append(label)
            self.lbl2D.append(arr)

        self.myrender()
        self.print2D(self.scrin2D)
        print(self.block)
        
    def initBlock2DStack2DScrin2D(self, arr2D):
        for i in range(20):
            self.block2D.append([0, 0, 0, 0, 0 , 0, 0, 0, 0, 0])
            self.stack2D.append([0, 0, 0, 0, 0 , 0, 0, 0, 0, 0])
            self.scrin2D.append([0, 0, 0, 0, 0 , 0, 0, 0, 0, 0])
            
    def keyPressEvent(self, e):
        #16777234 좌, 16777235 위, 16777236 우, 16777237 아래
        mykeycode = e.key()
        
        if(mykeycode == 16777234):
            self.block.j -= 1
        if(mykeycode == 16777236):
            self.block.j += 1
        if(mykeycode == 16777235):
            self.changeBlockStatus()
        if(mykeycode == 16777237):
            self.block.i += 1
            
        try:
            self.setBlock2DWithBlock()
        except:
            print("예외")
        self.moveStackBlock2Scrin()
        self.myrender()
        self.print2D(self.scrin2D)
        
    def changeBlockStatus(self):
        if self.block.kind == 1:
            pass
            
        if self.block.kind == 2 or self.block.kind == 3 or self.block.kind == 4 :
            if self.block.status == 1 :
                self.block.status = 2
            elif self.block.status == 2 :
                self.block.status = 1
        
        if self.block.kind == 5 or self.block.kind == 6 or self.block.kind == 7 :
            if self.block.status == 1 :
                self.block.status = 2
            elif self.block.status == 2 :
                self.block.status = 3
            elif self.block.status == 3 :
                self.block.status = 4
            elif self.block.status == 4 :
                self.block.status = 1
            
        
        
            
    def setBlock2DWithBlock(self):
        for i in range(20):
            for j in range(10):
                self.block2D[i][j] = 0
                
        if self.block.kind == 1:
            self.block2D[self.block.i]      [self.block.j]        = self.block.kind
            self.block2D[self.block.i]      [self.block.j+1]      = self.block.kind
            self.block2D[self.block.i + 1]  [self.block.j]        = self.block.kind
            self.block2D[self.block.i + 1]  [self.block.j + 1]    = self.block.kind
        if self.block.kind == 2:
            if self.block.status == 1:
                self.block2D[self.block.i - 1]  [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j]        = self.block.kind
                self.block2D[self.block.i + 2]  [self.block.j]        = self.block.kind
            if self.block.status == 2:
                self.block2D[self.block.i]      [self.block.j - 2]    = self.block.kind
                self.block2D[self.block.i]      [self.block.j - 1]    = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j + 1]    = self.block.kind
        if self.block.kind == 3:
            if self.block.status == 1:
                self.block2D[self.block.i]      [self.block.j - 1]    = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j]        = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j + 1]    = self.block.kind
            if self.block.status == 2:
                self.block2D[self.block.i - 1]  [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j - 1]    = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j - 1]    = self.block.kind
        if self.block.kind == 4:
            if self.block.status == 1:
                self.block2D[self.block.i]      [self.block.j + 1]    = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j]        = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j - 1]    = self.block.kind
            if self.block.status == 2:
                self.block2D[self.block.i - 1]  [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j + 1]    = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j + 1]    = self.block.kind
        if self.block.kind == 5:
            if self.block.status == 1:
                self.block2D[self.block.i - 1]  [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j - 1]    = self.block.kind
                self.block2D[self.block.i]      [self.block.j + 1]    = self.block.kind
            if self.block.status == 2:
                self.block2D[self.block.i - 1]  [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j + 1]    = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j]        = self.block.kind
            if self.block.status == 3:
                self.block2D[self.block.i]      [self.block.j - 1]    = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j + 1]    = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j]        = self.block.kind
            if self.block.status == 4:
                self.block2D[self.block.i - 1]  [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j - 1]    = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j]        = self.block.kind
        if self.block.kind == 6:
            if self.block.status == 1:
                self.block2D[self.block.i - 1]  [self.block.j - 1]    = self.block.kind
                self.block2D[self.block.i - 1]  [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j]    = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j]        = self.block.kind
            if self.block.status == 2:
                self.block2D[self.block.i - 1]  [self.block.j + 1]    = self.block.kind
                self.block2D[self.block.i]      [self.block.j - 1]    = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j + 1]    = self.block.kind
            if self.block.status == 3:
                self.block2D[self.block.i - 1]  [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j]        = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j + 1]    = self.block.kind
            if self.block.status == 4:
                self.block2D[self.block.i]      [self.block.j - 1]    = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j + 1]    = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j - 1]    = self.block.kind
        if self.block.kind == 7:
            if self.block.status == 1:
                self.block2D[self.block.i - 1]  [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j]        = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j - 1]    = self.block.kind
            if self.block.status == 2:
                self.block2D[self.block.i]      [self.block.j - 1]    = self.block.kind
                self.block2D[self.block.i - 1]  [self.block.j - 1]    = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j + 1]    = self.block.kind
            if self.block.status == 3:
                self.block2D[self.block.i - 1]  [self.block.j + 1]    = self.block.kind
                self.block2D[self.block.i - 1]  [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j]        = self.block.kind
            if self.block.status == 4:
                self.block2D[self.block.i]      [self.block.j - 1]    = self.block.kind
                self.block2D[self.block.i]      [self.block.j]        = self.block.kind
                self.block2D[self.block.i]      [self.block.j + 1]    = self.block.kind
                self.block2D[self.block.i + 1]  [self.block.j + 1]    = self.block.kind
            
    def moveStackBlock2Scrin(self):
        for i in range(20):
            for j in range(10):
                    self.scrin2D[i][j] = self.stack2D[i][j] + self.block2D[i][j]

                
    def print2D(self, arr2D):
        print("--------------------------------------")
        for line in arr2D:
            print(line)

    
    def myrender(self):
        for i in range(20) :
            for j in range(10) :
                if self.scrin2D[i][j] == 0 :
                    self.lbl2D[i][j].setStyleSheet("background-color : #353535")
                    
                if self.scrin2D[i][j] == 1 :
                    self.lbl2D[i][j].setStyleSheet("background-color : #FFA7A7")
                if self.scrin2D[i][j] == 2 :
                    self.lbl2D[i][j].setStyleSheet("background-color : #FFC19E")
                if self.scrin2D[i][j] == 3 :
                    self.lbl2D[i][j].setStyleSheet("background-color : #FAED7D")
                if self.scrin2D[i][j] == 4 :
                    self.lbl2D[i][j].setStyleSheet("background-color : #B7F0B1")
                if self.scrin2D[i][j] == 5 :
                    self.lbl2D[i][j].setStyleSheet("background-color : #B2CCFF")
                if self.scrin2D[i][j] == 6 :
                    self.lbl2D[i][j].setStyleSheet("background-color : #B5B2FF")
                if self.scrin2D[i][j] == 7 :
                    self.lbl2D[i][j].setStyleSheet("background-color : #D1B2FF")
                    
                if self.scrin2D[i][j] == 11 :
                    self.lbl2D[i][j].setStyleSheet("background-color : #FFD8D8")
                if self.scrin2D[i][j] == 12 :
                    self.lbl2D[i][j].setStyleSheet("background-color : #FAE0D4")
                if self.scrin2D[i][j] == 13 :
                    self.lbl2D[i][j].setStyleSheet("background-color : #FAF4C0")
                if self.scrin2D[i][j] == 14 :
                    self.lbl2D[i][j].setStyleSheet("background-color : #CEFBC9")
                if self.scrin2D[i][j] == 15 :
                    self.lbl2D[i][j].setStyleSheet("background-color : #D9E5FF")
                if self.scrin2D[i][j] == 16 :
                    self.lbl2D[i][j].setStyleSheet("background-color : #DAD9FF")
                if self.scrin2D[i][j] == 17 :
                    self.lbl2D[i][j].setStyleSheet("background-color : #E8D9FF")
                    
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
