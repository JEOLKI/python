import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QLabel

form_class = uic.loadUiType("tetris.ui")[0]


class WindowClass(QMainWindow, form_class) :

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.block2D = []
        self.stack2D = []
        self.scrin2D = []
        
        self.lbl2D = []
        
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
        
    def initBlock2DStack2DScrin2D(self, arr2D):
        for i in range(20):
            self.block2D.append([0, 0, 0, 0, 0 , 0, 0, 0, 0, 0])
            self.stack2D.append([0, 0, 0, 0, 0 , 0, 0, 0, 0, 0])
            self.scrin2D.append([0, 0, 0, 0, 0 , 0, 0, 0, 0, 0])
            
    
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
