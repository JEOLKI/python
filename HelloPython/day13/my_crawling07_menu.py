import time

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


form_class = uic.loadUiType("hello.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonFunction)

        options = Options()
        options.headless = False
        self.browser = webdriver.Chrome(executable_path="chromedriver.exe", options=options) #self를 붙이면 전역
        #browser.get("https://map.naver.com/v5/search/%EB%A7%9B%EC%A7%91/place/16069633?c=14184621.1804079,4345586.5859474,16,0,0,0,dh")
        self.browser.get("http://localhost/HelloWeb/hello.jsp")
        
        
    def buttonFunction(self):
        self.label.setText("good Morning")
        tag_names = self.browser.find_element_by_css_selector(".rank_top1000_list").find_elements_by_tag_name("li")
        for tag in tag_names:
            print(tag.text.split("\n"))
            

if __name__ == "__main__" :
    
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
    