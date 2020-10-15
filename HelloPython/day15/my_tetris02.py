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
            for j in range(20) :
                label = QLabel(self)
                label.setGeometry(25*j, 25*i, 24, 24)
                arr.append(label)
            self.lbl2D.append(arr)

        self.print2D(self.scrin2D)
        self.myrender()
        
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
        ii = 0
        for line in self.scrin2D :
            jj = 0
            for item in line :
                if self.scrin2D[ii][jj] == 0 :
                    self.lbl2D[ii][jj].setStyleSheet("background-color : #FFFFFF")
                elif self.scrin2D[ii][jj] == 1 :
                    self.lbl2D[ii][jj].setStyleSheet("background-color : #00FF00")
                jj += 1
            ii += 1 

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
