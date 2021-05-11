import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
import random
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
class kbb(QDialog):
    def __init__(self):
        super(kbb, self).__init__()
        self.ui=uic.loadUi('keobuabao.ui',self)
        self.ui.pushButton.clicked.connect(self.rock)
        self.ui.pushButton_2.clicked.connect(self.bao)
        self.ui.pushButton_3.clicked.connect(self.keo)
        self.ui.pushButton_4.clicked.connect(self.reset)
        self.nguoichoi=''
        self.maychon=''
        self.diem=0
        self.timer = QTimer()
        self.show()
        self.lstimg={
            'scissors':'keo.jpg',
            'rock':'bua.jpg',
            'paper':'bao.jpg'
        }

        self.lstmay=['scissors','paper','rock']
    def maychonne(self):
        self.timer.start(5000)
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)
        # máy chọn
        self.maychon = random.choice(self.lstmay)
        for i in self.lstimg:
            if i == self.maychon:
                self.ui.label_2.setPixmap(QPixmap(self.lstimg[i]))
    def nguoichoirock(self):
        self.nguoichoi = 'rock'
        for i in self.lstimg:
            if i == self.nguoichoi:
                self.ui.label.setPixmap(QPixmap(self.lstimg[i]))
    def nguoichoibao(self):
        self.nguoichoi = 'paper'
        for i in self.lstimg:
            if i == self.nguoichoi:
                self.ui.label.setPixmap(QPixmap(self.lstimg[i]))
    def nguoichoikeo(self):
        self.nguoichoi = 'scissors'
        for i in self.lstimg:
            if i == self.nguoichoi:
                self.ui.label.setPixmap(QPixmap(self.lstimg[i]))
    #kiểm tra
    def kiemtra(self):
        if self.maychon == self.nguoichoi:
            self.ui.label_4.setText('Hòa')
        elif (self.maychon == 'scissors' and self.nguoichoi=='rock') or (self.maychon == 'rock' and self.nguoichoi=='paper') or (self.maychon == 'paper' and self.nguoichoi=='scissors'):
            self.ui.label_4.setText('Bạn thắng')
            self.diem += 1
            self.ui.label_6.setText(str(self.diem))
        else:
            self.ui.label_4.setText('Bạn thua')


    #người chọn búa
    def rock(self):
        self.nguoichoirock()
        #máy chọn
        self.maychonne()
        # kết quả
        self.kiemtra()

    # người chọn bao
    def bao(self):
        self.nguoichoibao()
        # máy chọn
        self.maychonne()
        # kết quả
        self.kiemtra()

    # người chọn kéo
    def keo(self):
        self.nguoichoikeo()
        # máy chọn
        self.maychonne()
        # kết quả
        self.kiemtra()

    def reset(self):
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_3.setEnabled(True)
        self.ui.label_4.clear()
        self.ui.label.clear()
        self.ui.label_2.clear()
        self.nguoichoi = ''
        self.maychon = ''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = kbb()
    sys.exit(app.exec())