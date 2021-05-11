import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class student():
    code=''
    name=''
    def __init__(self,code,name):
        self.code=code
        self.name=name
    def printName(self):
        return self.name
    def printCode(self):
        return  self.code
class Mark(student):
    historymarks=0
    geographymarks=0
    def __init__(self,code,name,historymarks,geographymarks):
        student.__init__(self,code,name)
        self.historymarks=historymarks
        self.geographymarks=geographymarks
    def diemls(self):
        return self.historymarks
    def diemdl(self):
        return self.geographymarks
class myform(QDialog):
    def __init__(self):
        super(myform,self).__init__()
        self.ui = uic.loadUi('bai2.ui',self)
        self.ui.pushButton.clicked.connect(self.hienthi)
        self.show()
    def hienthi(self):
        a=Mark(self.ui.lineEdit.text(),self.ui.lineEdit_2.text(),self.ui.lineEdit_3.text(),self.ui.lineEdit_4.text())
        a1=a.printCode()
        a2=a.printName()

        
        a3=a.diemls()
        a4=a.diemdl()
        self.ui.label_5.setText(str('code: '+a1+'\nName:'+a2+'\nHistoryMark: '+a3+'\nGeographyMark: '+a4))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = myform()
    sys.exit(app.exec())
