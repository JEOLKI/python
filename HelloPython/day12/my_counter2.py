import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import threading
import time

form_class = uic.loadUiType("my_counter2.ui")[0]


class WindowClass(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.on_click)
        
    def on_click(self):
        print("on_click")
        t1 = threading.Thread(target=self.on_increase, args=(1, 10))
        t1.start()
            
    def on_increase(self, start, end):
        for i in range(start, end):
            num = self.label.text()
            self.label.setText(str(int(num)+1))
            time.sleep(1)
        
            
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
    global count
    
