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
        
        for i in range(10) :
            for j in range(10) :
                pb = QPushButton(self)
                pb.setGeometry(75*j, 75*i, 75, 75)
                pb.setIconSize(QtCore.QSize(75,75))
                pb.setIcon(self.ie)
                pb.clicked.connect(self.myclick)
                pb.setWhatisThis("1,2")
        
        
    def myclick(self):
        print("ss")
        

if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()