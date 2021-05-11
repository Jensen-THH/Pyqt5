import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
import random
import time
from PyQt5.QtCore import QTimer
class test():
    def __init__(self):
        self.lstcolor = ['red', 'green', 'blue', 'black', 'yellow', 'white', 'grey', 'violet', 'purple']
        self.diem = 0
    def mauauto(self):
        self.maurd=random.choice(self.lstcolor)
        return self.maurd
    def mauchuanne(self):
        self.kqmau=random.choice(self.lstcolor)
        return self.kqmau
    def diemne(self,b,c):
        maumaychon=b
        maunguoichon=c
        if maunguoichon==maumaychon:
            self.diem=1

        else:
            self.diem=-1
        return self.diem
    def reset(self):
        return 0


class doimauchu(QDialog):
    def __init__(self):
        super(doimauchu, self).__init__()
        self.ui=uic.loadUi('doimauchu.ui',self)
        self.ui.pushButton.clicked.connect(self.hienthi)
        self.ui.lineEdit.returnPressed.connect(self.hienthikq)
        self.lstchu=[]
        self.diemso=0

        # QTimer

        self.thoigian=31
        self.timer=QTimer()
        self.timer.timeout.connect(self.updatetimetion)
        self.show()


    def updatetimetion(self):

            self.timer.start(1000)
            if self.thoigian>0:
                self.thoigian-=1
                self.ui.label_4.setText(str(self.thoigian))

                print(self.thoigian)
            else:
                self.thoigian = 31
    def hienthi(self):

        a=test()

        a1 =a.mauauto()
        mauchuankq=a.mauchuanne()

        self.lstchu.append(mauchuankq)
        self.ui.label_3.setText(a1)
        self.ui.label_3.setStyleSheet("color:"+mauchuankq)



    def hienthikq(self):

        a=test()
        mau=self.lstchu[-1]
        nguoichoi=self.ui.lineEdit.text()
        a3= a.diemne(mau,nguoichoi)
        self.diemso+=a3

        self.ui.label_2.setText(str(self.diemso))
        self.ui.lineEdit.clear()
        #chữ khác
        a1 = a.mauauto()
        mauchuankq = a.mauchuanne()
        self.lstchu.append(mauchuankq)
        self.ui.label_3.setText(a1)
        self.ui.label_3.setStyleSheet("color:" + mauchuankq)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = doimauchu()
    sys.exit(app.exec())
