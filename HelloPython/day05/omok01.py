import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtCore

form_class = uic.loadUiType("omok01.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.resize(750 ,750)
        
        self.ie = QIcon("0.jpg")
        self.iw = QIcon("1.jpg")
        self.ib = QIcon("2.jpg")
        self.int2d = [
                      [0,0,0,0,0, 0,0,0,0,0],
                      [0,1,0,0,0, 0,0,0,0,0],
                      [0,0,2,0,0, 0,0,0,0,0],
                      [0,0,0,2,0, 0,0,0,0,0],
                      [0,0,0,0,0, 0,0,0,0,0],
                      
                      [0,0,0,0,0, 0,0,0,0,0],
                      [0,0,0,0,0, 0,0,0,0,0],
                      [0,0,0,0,0, 0,0,0,0,0],
                      [0,0,0,0,0, 0,0,0,0,0],
                      [0,0,0,0,0, 0,0,0,0,0]
                     ]
        
        self.arr2d = []
        
        for i in range(10) :
            arr = []
            for j in range(10) :
                pb = QPushButton(self)
                pb.setGeometry(75*j, 75*i, 75, 75)
                pb.setIconSize(QtCore.QSize(75,75))
                pb.setIcon(self.ie)
                pb.setWhatsThis("{},{}".format(i,j))
                pb.clicked.connect(self.myclick)
                arr.append(pb)
            self.arr2d.append(arr)
            
        self.mydraw()
            
    def myclick(self) :
        print(self.sender().whatsThis())
        self.myshow2d()
        self.mydraw()
        
    def myshow2d(self):
        for arr in self.int2d :
            print(arr)
    
    def mydraw(self):
        ii = 0
        for line in self.arr2d :
            jj = 0
            for item in line :
                if self.int2d[ii][jj] == 0 :
                    item.setIcon(self.ie);
                elif self.int2d[ii][jj] == 1 :
                    item.setIcon(self.iw);
                else :
                    item.setIcon(self.ib);
            
                jj += 1
            ii += 1        
                
        

if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()