import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox


form_class = uic.loadUiType("omok02.ui")[0]

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
                      [0,0,0,0,0, 0,0,0,0,0],
                      [0,0,0,0,0, 0,0,0,0,0],
                      [0,0,0,0,0, 0,0,0,0,0],
                      [0,0,0,0,0, 0,0,0,0,0],
                      
                      [0,0,0,0,0, 0,0,0,0,0],
                      [0,0,0,0,0, 0,0,0,0,0],
                      [0,0,0,0,0, 0,0,0,0,0],
                      [0,0,0,0,0, 0,0,0,0,0],
                      [0,0,0,0,0, 0,0,0,0,0]
                     ]
        
        self.arr2d = []
        self.flagTurn = True
        self.flagIng = True
        
        
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
        
        if not self.flagIng :
            return
        
        
        a = self.sender().whatsThis()
        b = a.split(",")
        
        ii = int(b[0])
        jj = int(b[1])
        
        if self.int2d[ii][jj] > 0 :
            return
        
        
        cnt_stone = 0
        if self.flagTurn :
            self.int2d[ii][jj] = 1
            cnt_stone = 1
        else :
            self.int2d[ii][jj] = 2
            cnt_stone = 2
    
        self.mydraw()
        
        up_cnt = self.getUp(ii,jj,cnt_stone);
        dw_cnt = self.getDw(ii,jj,cnt_stone);
        le_cnt = self.getLe(ii,jj,cnt_stone);
        ri_cnt = self.getRi(ii,jj,cnt_stone);
        
        uple_cnt = self.getUpLe(ii,jj,cnt_stone);
        upri_cnt = self.getUpRi(ii,jj,cnt_stone);
        dwle_cnt = self.getDwLe(ii,jj,cnt_stone);
        dwri_cnt = self.getDwRi(ii,jj,cnt_stone);
        
        cnt5p = [0,0,0,0]
        
        cnt5p[0] = up_cnt + dw_cnt + 1
        cnt5p[1] = le_cnt + ri_cnt + 1
        cnt5p[2] = uple_cnt + dwri_cnt + 1
        cnt5p[3] = upri_cnt + dwle_cnt + 1
        
        for i in range(4):
            if cnt5p[i] == 5 :
                if self.flagTurn :
                    QMessageBox.about(self, "Omok", "흰돌이 이겼습니다.")
                else :
                    QMessageBox.about(self, "Omok", "검은돌이 이겼습니다.")
                self.flagIng = not self.flagIng
        
        
        
        print("up_cnt : {}" .format(up_cnt))
        print("dw_cnt : {}" .format(dw_cnt))
        print("le_cnt : {}" .format(le_cnt))
        print("ri_cnt : {}" .format(ri_cnt))
        
        print("uple_cnt : {}" .format(uple_cnt))
        print("upri_cnt : {}" .format(upri_cnt))
        print("dwle_cnt : {}" .format(dwle_cnt))
        print("dwri_cnt : {}" .format(dwri_cnt))
        
        self.flagTurn = not self.flagTurn
        
    
    def getDwRi(self, ii, jj, cnt_stone):
        cnt = 0
        while True :
            ii += 1
            jj += 1
            if ii < 0 or ii >= len(self.int2d) :
                return cnt
            if jj < 0 or jj >= len(self.int2d[ii]) :
                return cnt
            if self.int2d[ii][jj] == cnt_stone :
                cnt += 1
            else :
                break
        return cnt

    def getDwLe(self, ii, jj, cnt_stone):
        cnt = 0
        while True :
            ii += 1
            jj -= 1
            if ii < 0 or ii >= len(self.int2d) :
                return cnt
            if jj < 0 or jj >= len(self.int2d[ii]) :
                return cnt            
            if self.int2d[ii][jj] == cnt_stone :
                cnt += 1
            else :
                break
        return cnt
    
    def getUpRi(self, ii, jj, cnt_stone):
        cnt = 0
        while True :
            ii -= 1
            jj += 1
            if ii < 0 or ii >= len(self.int2d) :
                return cnt
            if jj < 0 or jj >= len(self.int2d[ii]) :
                return cnt            
            if self.int2d[ii][jj] == cnt_stone :
                cnt += 1
            else :
                break
        return cnt
    
    def getUpLe(self, ii, jj, cnt_stone):
        cnt = 0
        while True :
            ii -= 1
            jj -= 1
            if ii < 0 or ii >= len(self.int2d) :
                return cnt
            if jj < 0 or jj >= len(self.int2d[ii]) :
                return cnt
            if self.int2d[ii][jj] == cnt_stone :
                cnt += 1
            else :
                break
        return cnt
    
        
    def getRi(self, ii, jj, cnt_stone):
        cnt = 0
        while True :
            jj += 1
            if ii < 0 or ii >= len(self.int2d) :
                return cnt
            if jj < 0 or jj >= len(self.int2d[ii]) :
                return cnt            
            if self.int2d[ii][jj] == cnt_stone :
                cnt += 1
            else :
                break
        return cnt
        
    def getLe(self, ii, jj, cnt_stone):
        cnt = 0
        while True :
            jj -= 1
            if ii < 0 or ii >= len(self.int2d) :
                return cnt
            if jj < 0 or jj >= len(self.int2d[ii]) :
                return cnt
            if self.int2d[ii][jj] == cnt_stone :
                cnt += 1
            else :
                break
        return cnt
        
        
    def getDw(self, ii, jj, cnt_stone):
        cnt = 0
        while True :
            ii += 1
            if ii < 0 or ii >= len(self.int2d) :
                return cnt
            if jj < 0 or jj >= len(self.int2d[ii]) :
                return cnt
            if self.int2d[ii][jj] == cnt_stone :
                cnt += 1
            else :
                break
        return cnt

    def getUp(self, ii, jj, cnt_stone):
        cnt = 0
        while True :
            ii -= 1
            if ii < 0 or ii >= len(self.int2d) :
                return cnt
            if jj < 0 or jj >= len(self.int2d[ii]) :
                return cnt
            if self.int2d[ii][jj] == cnt_stone :
                cnt += 1
            else :
                break
        return cnt
        
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