import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
import random

class vesovietlot(QDialog):
    def __init__(self):
        super(vesovietlot, self).__init__()
        self.ui=uic.loadUi('vesovietlot.ui',self)
        self.ui.pushButton.clicked.connect(self.kt)
        self.ui.pushButton_2.clicked.connect(self.clearnb)
        self.sotrung=[]
        self.sodoan=[]


        #số trúng
        for i in range(6):
            st = random.randint(1, 45)
            self.sotrung.append(st)
        print(self.sotrung)


        self.show()
    def clearnb(self):
        self.ui.spinBox.setValue(1)
        self.ui.spinBox_2.setValue(1)
        self.ui.spinBox_3.setValue(1)
        self.ui.spinBox_4.setValue(1)
        self.ui.spinBox_5.setValue(1)
        self.ui.spinBox_6.setValue(1)


    def kt(self):
        #lấy số người chơi đoán:
        self.sodoan.append(self.ui.spinBox.value())
        self.sodoan.append(self.ui.spinBox_2.value())
        self.sodoan.append(self.ui.spinBox_3.value())
        self.sodoan.append(self.ui.spinBox_4.value())
        self.sodoan.append(self.ui.spinBox_5.value())
        self.sodoan.append(self.ui.spinBox_6.value())

        print(self.sodoan)
        kq=6
        for y in self.sotrung:
            if y in self.sodoan:
                kq-=1
        if kq==0:
            self.ui.label.setText('bạn đã trúng giải độc đắc!')
            self.sotrung = []
            self.sodoan=[]
        if kq>3:
            self.ui.label.setText('chúc bạn may mắn lần sau!')
            self.sotrung=[]
            self.sodoan = []
        if kq<=3:
            self.ui.label.setText('bạn đã trúng giải nhì!')
            self.sotrung = []
            self.sodoan = []


        # if self.sotrung!=0:
        #     vs_value = int(self.ui.spinBox.value())
        #     # print(vs_value)
        #
        #     if self.sotrung== vs_value:
        #         self.ui.label.setText('Corect Guess')
        #     else:
        #         self.ui.label.setText('Incorect Guess')
        # else:
        #     self.ui.label.setText('click Start !')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = vesovietlot()
    sys.exit(app.exec_())