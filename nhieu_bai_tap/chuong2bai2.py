import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class baitapsohai(QDialog):
    def __init__(self):
        super(baitapsohai,self).__init__()
        self.ui = uic.loadUi('chuonghaibai2.ui',self)
        self.ui.cong.clicked.connect(self.congso)
        self.ui.tru.clicked.connect(self.truso)
        self.ui.nhan.clicked.connect(self.nhanso)
        self.ui.chia.clicked.connect(self.chiaso)
        self.show()
    def congso(self):
     try:
        if len(self.ui.lineEdit.text())!=0 and len(self.ui.lineEdit_2.text())!=0:
                a=int(self.ui.lineEdit.text())
                b=int(self.ui.lineEdit_2.text())
                c=a+b
                self.ui.ketqua.setText('Addition:'+str(c))
        else:
            self.ui.ketqua.setText('Nothing')
     except ValueError:
         self.ui.ketqua.setText('Not a number')


    def truso(self):
        try:
            if len(self.ui.lineEdit.text()) != 0 and len(self.ui.lineEdit_2.text()) != 0:
                a = int(self.ui.lineEdit.text())
                b = int(self.ui.lineEdit_2.text())
                c = a - b
                self.ui.ketqua.setText('Addition:' + str(c))
            else:
                self.ui.ketqua.setText('Nothing')
        except ValueError:
            self.ui.ketqua.setText('Not a number')

    def nhanso(self):
        try:
            if len(self.ui.lineEdit.text()) != 0 and len(self.ui.lineEdit_2.text()) != 0:
                a = int(self.ui.lineEdit.text())
                b = int(self.ui.lineEdit_2.text())
                c = a * b
                self.ui.ketqua.setText('Addition:' + str(c))
            else:
                self.ui.ketqua.setText('Nothing')
        except ValueError:
            self.ui.ketqua.setText('Not a number')

    def chiaso(self):
        try:
            if len(self.ui.lineEdit.text()) != 0 and len(self.ui.lineEdit_2.text()) != 0:
                a = int(self.ui.lineEdit.text())
                b = int(self.ui.lineEdit_2.text())
                c = a / b
                self.ui.ketqua.setText('Addition:' + str(c))
            else:
                self.ui.ketqua.setText('Nothing')
        except ValueError:
            self.ui.ketqua.setText('Not a number')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    b=baitapsohai()
    sys.exit(app.exec())