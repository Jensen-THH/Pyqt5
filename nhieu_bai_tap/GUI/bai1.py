import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class pheptinh():
    a=0
    b=0
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def printA(self):
        return self.a
    def printB(self):
        return self.b
class myform(QDialog):
    def __init__(self):
        super(myform,self).__init__()
        self.ui = uic.loadUi('bai1.ui',self)
        self.ui.pushButton.clicked.connect(self.cong)
        self.ui.pushButton_2.clicked.connect(self.tru)
        self.ui.pushButton_3.clicked.connect(self.nhan)
        self.ui.pushButton_4.clicked.connect(self.chia)
        self.show()
    def cong(self):
       try:
        c=pheptinh(int(self.ui.lineEdit.text()),int(self.ui.lineEdit_2.text()))
        a1=c.printA()
        b2=c.printB()
        kq=a1+b2
        self.ui.label_2.setText('ketqua a+b: '+str(kq))
       except ValueError:
           self.ui.label_2.setText('Nhap so !')
    def tru(self):
       try:
        c=pheptinh(int(self.ui.lineEdit.text()),int(self.ui.lineEdit_2.text()))
        a1=c.printA()
        b2=c.printB()
        kq=a1-b2
        self.ui.label_2.setText('ketqua a-b: '+str(kq))
       except ValueError:
           self.ui.label_2.setText('Nhap so !')
    def nhan(self):
       try:
        c=pheptinh(int(self.ui.lineEdit.text()),int(self.ui.lineEdit_2.text()))
        a1=c.printA()
        b2=c.printB()
        kq=a1*b2
        self.ui.label_2.setText('ketqua a*b: '+str(kq))
       except ValueError:
           self.ui.label_2.setText('Nhap so !')
    def chia(self):
       try:
        c=pheptinh(int(self.ui.lineEdit.text()),int(self.ui.lineEdit_2.text()))
        a1=c.printA()
        b2=c.printB()
        kq=a1/b2
        self.ui.label_2.setText('ketqua a:c: '+str(kq))
       except ValueError:
           self.ui.label_2.setText('Nhap so !')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = myform()
    sys.exit(app.exec())
