import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class khachhang():
    makh=0
    tenkh=''
    soluong=0
    dongia=0
    def __init__(self,makh,tenkh,soluong,dongia):
        self.makh=makh
        self.tenkh=tenkh
        self.soluong=soluong
        self.dongia=dongia

    def printmakh(self):
            return self.makh

    def printtenkh(self):
        return  self.tenkh
    def printsol(self):
        return  self.soluong
    def printdg(self):
        return  self.dongia
class myform(QDialog):
    def __init__(self):
        super(myform,self).__init__()
        self.ui = uic.loadUi('baitapthem.ui',self)
        self.ui.pushButton_2.clicked.connect(self.hienthi)
        self.ui.pushButton.clicked.connect(self.hienthi2)
        self.ui.radioButton_2.toggled.connect(self.hienthi3)
        self.ui.radioButton.toggled.connect(self.hienthi3)
        self.show()
        self.item=[]
    def hienthi(self):
        x=[]
        a=khachhang(int(self.ui.lineEdit.text()),self.ui.lineEdit_2.text(),int(self.ui.lineEdit_3.text()),int(self.ui.lineEdit_4.text()))
        a1=a.printmakh()
        x.append(a1)
        a2 = a.printtenkh()
        x.append(a2)
        a3 = a.printsol()
        x.append(a3)
        a4 = a.printdg()
        x.append(a4)
        for i in x:
            if i not in self.item:
                self.ui.listWidget.addItem(str(i))
                self.item.append(i)
        self.ui.lineEdit_6.setText(str(self.ui.lineEdit_3.text()))
        # self.ui.listWidget.addItem(str(a1))
        # self.ui.listWidget.addItem(str(a2))
        # self.ui.listWidget.addItem(str(a3))
        # self.ui.listWidget.addItem(str(a4))

    def hienthi3(self):
         if len(self.ui.lineEdit_3.text)!=0 and len(self.ui.lineEdit_4.text)!=0:
            if self.ui.radioButton_2.isChecked()==True:
                self.ui.lineEdit_6.setText(str(self.ui.lineEdit_3.text()))
                tongtang=(int(self.ui.lineEdit_3.text())*int(self.ui.lineEdit_4.text()))*0.05
                self.ui.lineEdit_5.setText(str(
                                                int(self.ui.lineEdit_3.text())
                                               *int(self.ui.lineEdit_4.text())
                                               +int(tongtang)
                                               )
                                          )
            if self.ui.radioButton.isChecked()==True:
                self.ui.lineEdit_6.setText(str(self.ui.lineEdit_3.text()))
                thaydoi = (int(self.ui.lineEdit_3.text()) * int(self.ui.lineEdit_4.text())) * 0.05
                self.ui.lineEdit_5.setText(str(
                                                int(self.ui.lineEdit_3.text())
                                               *int(self.ui.lineEdit_4.text())
                                               -int(thaydoi)
                                               )
                                          )
    def hienthi2(self):
        x=[]
        self.item=[]
        self.ui.listWidget.clear()
        self.ui.lineEdit.setText(' ')
        self.ui.lineEdit_2.setText(' ')
        self.ui.lineEdit_3.setText(' ')
        self.ui.lineEdit_4.setText(' ')
        self.ui.lineEdit_6.setText(' ')
        self.ui.lineEdit_5.setText(' ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = myform()
    sys.exit(app.exec())
