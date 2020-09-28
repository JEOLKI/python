import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("plus.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.pushButton_clicked)
        
        
    def pushButton_clicked(self):
        num1 = self.le1.text()
        x = int(num1)
        num2 = self.le2.text()
        y = int(num2)
        
        num = x + y
        
        self.le3.setText(str(num))
        

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
