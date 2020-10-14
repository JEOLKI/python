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

        options = Options()
        options.headless = False
        self.browser = webdriver.Chrome(executable_path="chromedriver.exe", options=options) #self를 붙이면 전역
        self.browser.get("https://place.map.kakao.com/9772243")
        #self.browser.get("http://localhost/HelloWeb/hello.jsp")
        
        self.pushButton.clicked.connect(self.buttonFunction)
        
    def buttonFunction(self):
        title = self.browser.find_element_by_class_name("inner_place").find_element_by_class_name("tit_location").text
        objs = self.browser.find_element_by_class_name("list_menu").find_elements_by_tag_name("li")
        
        
        conn = cx_Oracle.connect("HJG/java@localhost:1521/xe")
        cursor = conn.cursor() #커서생성
        
        for obj in objs:
            menu_name = obj.find_element_by_class_name("loss_word").text
            menu_price = obj.find_element_by_class_name("price_menu").text
            print(title)
            print(menu_name)
            print(menu_price)
            
            sql = "insert into mymenu values(:1,:2,:3)"
            data=(title, menu_name, menu_price)
    
            cursor.execute(sql,data)
            
        cursor.close()
        conn.commit() #JDBC는 오토 커밋 python은 오토커밋이 아니다.
        conn.close()
        
        

if __name__ == "__main__" :
    
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    




