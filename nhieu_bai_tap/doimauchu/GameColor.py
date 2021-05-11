import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic,QtCore
import random
class choi:
    nam=''
    def __init__(self):
        self.color=['Black','Blue','Red','Yellow','Gray','Green','Pink','purple','Cyan','Peru','Gold','violet']
        self.point=0
    def randomchu(self):
        self.a = random.choice(self.color)
        return self.a
    def randommau(self):
        self.b = random.choice(self.color)
        return self.b
    def check(self,chu,chudung):
        if chudung.lower()==chu.lower():
            self.point+=1
            self.randommau()
            self.randomchu()
            self.n=1
            self.ok()
        else:
            self.n=0
            self.ok()
        return self.point
    def mauchu(self):
        return self.a
    def chu(self):
        return self.b
    def diemng(self):
        return self.point
    def ok(self):
        return self.n
    def reset(self):
        self.point=0
        return self.point
class ApplyWindow(QDialog):
    def __init__(self):
        super(ApplyWindow,self).__init__()
        self.ui=uic.loadUi('GameColor.ui',self)
        self.ui.pushButton.clicked.connect(self.start)
        self.ui.pushButton_2.clicked.connect(self.reset)
        self.ui.lineEdit.returnPressed.connect(self.check)
        self.thoigian=31
        self.nguoichoi = choi()
        self.diemtru=0
        self.show()
    def start(self):
        self.nguoichoi.randommau()
        self.nguoichoi.randomchu()
        self.ui.label_2.setText(self.nguoichoi.chu())
        self.ui.label_2.setStyleSheet("color:"+ self.nguoichoi.mauchu())
        self.myTimer = QtCore.QTimer()
        self.myTimer.timeout.connect(self.NextTimer)
        self.NextTimer()
    def NextTimer(self):
        self.myTimer.start(1000)
        if self.thoigian>0:
            self.thoigian=self.thoigian-1
            self.ui.label_3.setText(str(self.thoigian))
        else:
            self.thoigian =31
            self.diemtru+=1
    def check(self):
        a=self.nguoichoi.mauchu()
        b=self.ui.lineEdit.text()
        self.nguoichoi.check(a,b)
        if self.nguoichoi.ok() ==1:
            self.thoigian =31
        self.diem=self.nguoichoi.diemng() - self.diemtru
        self.ui.label.setText('Score ' + str(self.diem))
    def reset(self):
        self.diem=0
        self.ui.label.setText('Score ' + str(self.diem))
        self.thoigian=31
        self.nguoichoi.reset()
        self.start()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=ApplyWindow()
    sys.exit(app.exec_())