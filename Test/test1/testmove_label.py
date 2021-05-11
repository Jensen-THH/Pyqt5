import sys
from PyQt5.QtWidgets import QDialog,QApplication,QLabel
from PyQt5 import uic,QtCore
from PyQt5.QtCore import QRect, QPropertyAnimation
import  random
import  time
class ApplWindow(QDialog):
    def __init__(self):
        super(ApplWindow, self).__init__()
        self.ui = uic.loadUi('testmoveLabel.ui', self)
        self.ui.pushButton.clicked.connect(self.runne)
        self.ui.pushButton_2.clicked.connect(self.runne)
        self.count=True


        # self.left = [300,350,400,450]
        # self.top = 0
        # self.width = 20
        # self.height = [170,160,180,190]
        # for i in range(-1,3):
        #     label_8 = QLabel(str("label_"+str(i+1)), self)
        #     label_8.setStyleSheet("background:red")
        #     label_8.setGeometry(self.left[i+1], self.top, self.width, self.height[i+1])

        self.show()
    def runne(self,x):




            # self.lstR = [30, 190, 360]
            # a = random.choice(self.lstR)
            # self.CN = QPropertyAnimation(self.ui.label, b"geometry")
            # self.CN.setDuration(2000)
            # self.CN.setLoopCount(-1)
            # self.CN.setStartValue(QRect(0, 100, 130, 170))
            # self.CN.setEndValue(QRect(400, 100, 130, 170))
            # self.CN.start()
            # print(self.count)
            self.CN = QPropertyAnimation(self.ui.label, b"geometry")
            self.lstR = [-100]
            self.CN.setDuration(4000)
            self.CN.setLoopCount(-1)
            print('a')
            self.CN.setStartValue(QRect(600, 0, 80, 120))
            self.CN.setEndValue(QRect(-100, 0, 80, 120))
            self.CN.start()

            self.CN1 = QPropertyAnimation(self.ui.label_2, b"geometry")
            self.CN1.setDuration(4300)
            self.CN1.setLoopCount(-1)
            self.CN1.setStartValue(QRect(800, 100, 80, 140))
            self.CN1.setEndValue(QRect(-50, 0, 80, 140))
            self.CN1.start()
            print('b')

            self.CN2 = QPropertyAnimation(self.ui.label_3, b"geometry")
            self.CN2.setDuration(4600)
            self.CN2.setLoopCount(-1)
            self.CN2.setStartValue(QRect(1000, 0, 80, 135))
            self.CN2.setEndValue(QRect(0, 0, 80, 135))
            self.CN2.start()
            print('c')





    def stopx(self):
        self.CN.stop()
        self.CN1.stop()
        self.CN2.stop()







if __name__=="__main__":
    app=QApplication(sys.argv)
    window=ApplWindow()
    sys.exit(app.exec_())