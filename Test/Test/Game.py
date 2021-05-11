import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QRect, QPropertyAnimation
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic, QtCore
import random


class MyForm3(QDialog):
    def __init__(self):
        super(MyForm3, self).__init__()
        self.ui = uic.loadUi('CountDown.ui', self)
        self.setWindowTitle("Count Down")
        self.count = 3
        self.timecount = QtCore.QTimer()
        self.timecount.start(1000)
        self.timecount.timeout.connect(self.set)
        # MF = MyForm()
        # MF.Disable()
    def set(self):
        self.lstcount = ["Alo", "Go", 1, 2, 3]
        if self.count > 0:
            self.ui.label.setText(str(self.lstcount[self.count]))
            self.count -= 1
        else:
            self.close()


class MyForm2(QDialog):
    def __init__(self):
        super(MyForm2, self).__init__()
        self.ui = uic.loadUi('GameOver.ui', self)
        self.setWindowTitle("Game Over")
        # self.ui.pushButton.clicked.connect(self.)
        self.ui.pushButton_2.clicked.connect(self.Quit)
        self.ui.label.setText("SCORE: " )
    # def PlayAgain(self):
    #     print("PlayAgain")
    #     self.close()
    #     MyForm().close()
    #     MF = MyForm()
    # 
    #     MF.create()
    #     MF.Go()
    #     MyForm().show()
    #     # MyForm().Go()
    #     # MyForm().Enabled()

    def Quit(self):
        print("Quit")
        sys.exit()
    def closeDialog(self):
        self.close()


class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = uic.loadUi('Test.ui', self)
        self.ui.frame.setStyleSheet('background-image:url("Lane.png")')
        self.ui.pushButton_2.clicked.connect(self.Go)
        self.ui.pushButton_3.clicked.connect(self.stop)
        self.ui.pushButton_4.clicked.connect(self.Go)
        self.ui.pushButton_5.clicked.connect(self.resume)
        self.setWindowTitle('Car Rush')
        self.setWindowIcon(QIcon('Supercar.png'))
        self.point = 0
        self.x = 190
        self.y = 400
        self.settime2 = 7100
        self.speed2 = 7000
        self.settime = 5100
        self.speed = 5000

    def Go(self):
        print("Go")
        MF3 = MyForm3()
        MF3.show()
        self.resetpoint()
        self.setPos()
        self.Enabled()
        # Xe1
        self.timmer = QtCore.QTimer()
        self.timmer.start(self.settime)
        self.timmer.timeout.connect(self.create)
        # Xe2
        self.timmerXe2 = QtCore.QTimer()
        self.timmerXe2.start(self.settime2)
        self.timmerXe2.timeout.connect(self.create2)
        # Check
        self.timmerXe2 = QtCore.QTimer()
        self.timmerXe2.start(self.speed2)
        self.timmerXe2.timeout.connect(self.calculatePoint2)
        self.timmer2 = QtCore.QTimer()
        self.timmer2.start(100)
        self.timmer2.timeout.connect(self.check)
        self.timmer3 = QtCore.QTimer()
        self.timmer3.start(self.speed)
        self.timmer3.timeout.connect(self.calculatePoint)

    def create(self):
        self.image = ["Car-Blue.png", "Car-Green.png", "Car-Oranges.png", "Car-Pink.png"]
        image = random.choice(self.image)
        self.labelXe1.setPixmap(QPixmap(image))
        self.lstR = [30, 190, 360]
        self.a = random.choice(self.lstR)
        self.CN = QPropertyAnimation(self.ui.labelXe1, b"geometry")
        self.CN.setDuration(self.speed)
        self.CN.setStartValue(QRect(self.a, -50, 100, 150))
        self.CN.setEndValue(QRect(self.a, 800, 100, 150))
        self.CN.start()

    def create2(self):
        if self.a == 30:
            self.lstR2 = [190, 360]
            r2 = random.choice(self.lstR2)
            self.labelXe2.setPixmap(QPixmap(random.choice(self.image)))
            self.CN2 = QPropertyAnimation(self.ui.labelXe2, b"geometry")
            self.CN2.setDuration(self.speed)
            self.CN2.setStartValue(QRect(r2, -50, 100, 150))
            self.CN2.setEndValue(QRect(r2, 800, 100, 150))
            self.CN2.start()
        elif self.a == 190:
            self.lstR2 = [30, 360]
            r2 = random.choice(self.lstR2)
            self.labelXe2.setPixmap(QPixmap(random.choice(self.image)))
            self.CN2 = QPropertyAnimation(self.ui.labelXe2, b"geometry")
            self.CN2.setDuration(self.speed)
            self.CN2.setStartValue(QRect(r2, -50, 100, 150))
            self.CN2.setEndValue(QRect(r2, 800, 100, 150))
            self.CN2.start()
        elif self.a == 360:
            self.lstR2 = [30, 190]
            r2 = random.choice(self.lstR2)
            self.labelXe2.setPixmap(QPixmap(random.choice(self.image)))
            self.CN2 = QPropertyAnimation(self.ui.labelXe2, b"geometry")
            self.CN2.setDuration(self.speed)
            self.CN2.setStartValue(QRect(r2, -50, 100, 150))
            self.CN2.setEndValue(QRect(r2, 800, 100, 150))
            self.CN2.start()


    def Disable(self):
        print("Disable")
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)

    def Enabled(self):
        print("Enabled")
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_5.setEnabled(True)


    def setPos(self):
        self.ui.labelXe1.setGeometry(180, -200, 100, 150)
        self.ui.label_10.setGeometry(190, 400, 100, 150)
        self.x = 190
        self.y = 400

    def check(self):
        # tọa độ xe 1
        w_car = self.ui.labelXe1.width()
        h_car = self.ui.labelXe1.height()
        X_car = self.ui.labelXe1.x()
        Y_car = self.ui.labelXe1.y()
        # tọa độ xe 2
        w_car2 = self.ui.labelXe2.width()
        h_car2 = self.ui.labelXe2.height()
        X_car2 = self.ui.labelXe2.x()
        Y_car2 = self.ui.labelXe2.y()
        # chiều cao xe đỏ
        w_card = self.ui.label_10.width()
        h_card = self.ui.label_10.height()

        print("Xe 1 ", X_car, Y_car, "|","Xe 2 ", X_car2, Y_car2,"|", self.x, self.y)

        if ((self.x <= (X_car + w_car) and self.x >= X_car) or (self.x + w_card >= X_car and self.x + w_card <= X_car + w_car)) \
                and ((h_car + Y_car >= self.y) and (h_card + Y_car <= self.y + h_card) or ((Y_car >= self.y) and (Y_car <= self.y + w_card))):
            self.timmer.stop()
            self.CN.stop()
            self.timmer2.stop()
            self.Disable()
            print("Game Over")
            self.MF2 = MyForm2()
            self.MF2.ui.pushButton.clicked.connect(self.PlayAgain)
            self.MF2.ui.label.setText('SCORE: ' + str(self.point))
            self.MF2.show()
        if ((self.x <= (X_car2 + w_car2) and self.x >= X_car2) or (self.x + w_card >= X_car2 and self.x + w_card <= X_car2 + w_car2)) \
                and ((h_car2 + Y_car2 >= self.y) and (h_card + Y_car2 <= self.y + h_card) or ((Y_car2 >= self.y) and (Y_car2 <= self.y + w_card))):
            self.timmer.stop()
            self.CN.stop()
            self.CN2.stop()
            self.timmer2.stop()
            self.timmerXe2.stop()
            self.Disable()
            print("Game Over")
            self.MF2 = MyForm2()
            self.MF2.ui.pushButton.clicked.connect(self.PlayAgain)
            self.MF2.ui.label.setText('SCORE: ' + str(self.point))
            self.MF2.show()

    def PlayAgain(self):
        self.Go()
        self.MF2.close()

    def move(self):
        self.anim = QPropertyAnimation(self.ui.label_10, b"geometry")
        self.anim.setDuration(-10)
        self.anim.setStartValue(QRect(self.x, self.y, 100, 150))
        self.anim.setEndValue(QRect(self.x, self.y, 100, 150))
        self.anim.start()

    def stop(self):
        self.timmer.stop()
        self.timmer2.stop()
        self.timmer3.stop()
        self.CN.pause()
        print("End")

    def resume(self):
        self.timmer.start()
        self.timmer2.start()
        self.timmer3.start()
        self.CN.resume()

    def calculatePoint2(self):
        if self.ui.labelXe2.y() >= 700:
            self.point += 10
            print(self.point)
            self.ui.label.setText(str(self.point))

    def calculatePoint(self):
        if self.ui.labelXe1.y() >= 700:
            self.point += 10
            self.ui.label.setText(str(self.point))
            if self.point == 20:
                self.settime = self.settime - 500
                self.speed = self.speed - 500
                print(self.settime, self.speed)
                print(self.point)
            if self.point == 50:
                self.settime = self.settime - 500
                self.speed = self.speed - 500
                print(self.settime, self.speed)
            if self.point == 70:
                self.settime = self.settime - 500
                self.speed = self.speed - 500
                print(self.settime, self.speed)
            if self.point == 100:
                self.settime = self.settime - 500
                self.speed = self.speed - 500
                print(self.settime, self.speed)
            if self.point == 150:
                self.settime = self.settime - 500
                self.speed = self.speed - 500
                print(self.settime, self.speed)
            if self.point == 200:
                self.settime = self.settime - 500
                self.speed = self.speed - 500
                print(self.settime, self.speed)

    def resetpoint(self):
        self.point = 0
        self.ui.label.setText(str(0))

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_W or e.key() == QtCore.Qt.Key_Up:
            if self.y > 250:
                self.y -= 30
                self.x += 0
        elif e.key() == QtCore.Qt.Key_S or e.key() == QtCore.Qt.Key_Down:
            if self.y < 420:
                self.y += 30
                # self.x += 0
        elif e.key() == QtCore.Qt.Key_A or e.key() == QtCore.Qt.Key_Right:
            if self.x > 10:
                self.y += 0
                self.x -= 30
        elif e.key() == QtCore.Qt.Key_D or e.key() == QtCore.Qt.Key_Left:
            if self.x < 350:
                self.y += 0
                self.x += 30
        self.move()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
