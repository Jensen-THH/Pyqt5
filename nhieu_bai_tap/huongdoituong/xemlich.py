import sys
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
class namamlich():
    nam=0
    def __init__(self,nam):
        self.nam=nam
    def printnam(self):
        return self.nam
class tinhnam(QDialog):
    def __init__(self):
        super(tinhnam, self).__init__()
        self.ui = uic.loadUi('xemlich.ui', self)
        self.ui.pushButton.clicked.connect(self.hienthi)
        self.show()
        self.socan={
            0:'canh',
            1:'tan',
            2:'nham',
            3:'quy',
            4:'giap',
            5:'at',
            6:'binh',
            7:'dinh',
            8:'mau',
            9:'ky'
        }
        self.chi={
            0: 'than',
            1: 'dau',
            2: 'tuat',
            3: 'hoi',
            4: 'ty',
            5: 'suu',
            6: 'dan',
            7: 'meo',
            8: 'thin',
            9: 'ty',
            10:'ngo',
            11:'mui'
        }
        self.hinh={
            0: '12congiap/than.jpg',
            1: '12congiap/u.jpg',
            2: '12congiap/tuat.jpg',
            3: '12congiap/hoi.jpg',
            4: '12congiap/ty.jpg',
            5: '12congiap/suu.jpg',
            6: '12congiap/dan.jpg',
            7: '12congiap/mao.jpg',
            8: '12congiap/thin.jpg',
            9: '12congiap/ran.jpg',
            10: '12congiap/gno.jpg',
            11: '12congiap/mui.jpg'
        }
    def hienthi(self):
        if len(self.ui.lineEdit.text())!=0 and self.ui.lineEdit.text().isnumeric()==True:
            a=namamlich(int(self.ui.lineEdit.text()))
            n=int(a.printnam())
            can=n%10
            chi=n%12
            tc=''
            tchi=''
            for i in self.socan:
                if can==i:
                    tc=self.socan[i]
            for i in self.chi:
                if chi==i:
                    tchi=self.chi[i]
            for i in self.hinh:
                if chi==i:
                    tchi=self.chi[i]
                    hinh=self.hinh[i]

            self.ui.label_2.setText(tc + ' ' + tchi)
            self.ui.label_3.setPixmap(QPixmap(hinh))

        else:
            self.ui.lineEdit.setText('')
            self.ui.lineEdit.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = tinhnam()
    sys.exit(app.exec())
