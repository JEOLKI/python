import time

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

import cx_Oracle

form_class = uic.loadUiType("hello.ui")[0]

class WindowClass(QMainWindow, form_class) :

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonFunction)

        options = Options()
        options.headless = False
        self.browser = webdriver.Chrome(executable_path="chromedriver.exe", options=options)  # self를 붙이면 전역
        self.browser.get("https://place.map.kakao.com/9772243")
        # self.browser.get("http://localhost/HelloWeb/hello.jsp")
        
        self.conn = cx_Oracle.connect("HJG/java@localhost:1521/xe")
        self.cursor = self.conn.cursor()  # 커서생성
        
    def buttonFunction(self):
        try:
            title = self.browser.find_elements_by_class_name("tit_location")[1].text
            objs = self.browser.find_element_by_class_name("list_menu").find_elements_by_tag_name("li")
        
            for obj in objs:
                menu_name = obj.find_element_by_class_name("loss_word") .text
                menu_price = obj.find_element_by_class_name("price_menu").text

                sql = "insert into mymenu values(:1,:2,:3)"
                data = (title, menu_name, menu_price)
                self.cursor.execute(sql, data)

                print(title, menu_name, menu_price)

        except:
            print("예외발생")

        self.cursor.close()
        self.conn.commit()  # JDBC는 오토 커밋 python은 오토커밋이 아니다.
        self.conn.close()
        
    def __del__(self):
        pass
        

if __name__ == "__main__" :
    
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()

