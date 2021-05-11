import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
import random
from PyQt5.QtGui import QPixmap

class boitinhyeu(QDialog):
    def __init__(self):
        super(boitinhyeu, self).__init__()
        self.ui=uic.loadUi('boitinhyeu.ui',self)
        self.ui.pushButton.clicked.connect(self.hienthi)
        self.lstimg = {
            'chiatay': 'heartbroke.png',
            'hopnhau': 'doubleheart.png',
            'kethon': 'muiten.jpg'
        }
        self.lstrandom=['chiatay','hopnhau','kethon']
        self.lstcolor={'chiatay':'green',
                       'hopnhau':'pink',
                       'kethon':'red'}
        self.show()
        self.kq=''
    def kqne(self):
        self.kq = random.choice(self.lstrandom)
        for i in self.lstimg:
            if i == self.kq:
                self.ui.label_6.setPixmap(QPixmap(self.lstimg[i]))
                # self.ui.label_6.setStyleSheet("background-image:"+self.lstimg[i]+";background-size:cover")
                self.ui.label_5.setStyleSheet("background-color:"+self.lstcolor[i])
    def hienthi(self):

        a=self.ui.lineEdit.text()
        b=self.ui.lineEdit_2.text()
        if len(a)!=0 and len(b)!=0 :
            if  self.ui.lineEdit.text().isnumeric()==False and self.ui.lineEdit_2.text().isnumeric()==False:
                self.kqne()
                if self.kq=='chiatay':
                    self.ui.label_5.setText('xin lỗi '+str(a)+' '+ str(b) +' ở trên tình bạn dưới tình yêu ! :(')
                if self.kq == 'hopnhau':
                    self.ui.label_5.setText(str(a)+' like '+str(b)+' ! :))')
                if self.kq == 'kethon':
                    self.ui.label_5.setText('we will be married ! <3 ')
            else:self.ui.label_5.setText('không nhập số!')

        else:
            self.ui.label_5.setText('Nhập tên đã nào !')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = boitinhyeu()
    sys.exit(app.exec_())

# lst=[1]
# print(lst[-1])