import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QRect, QPropertyAnimation
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic, QtCore
import random
import time
class TS:
    def __init__(self):
        pass
    def setPoint(self,p):
        self.point = p
        return self.point
    def getPoint(self):
        return self.point

class MyForm2(QDialog):
    def __init__(self):
        super(MyForm2, self).__init__()
        self.ui = uic.loadUi('Test-3.ui', self)
        self.setWindowTitle("Game Over")
        self.ui.pushButton.clicked.connect(self.PlayAgain)
        self.ui.pushButton_2.clicked.connect(self.Quit)
        self.Ts = TS()
        self.ui.label.setText("SCORE: " + str(self.Ts.getPoint()))
    def PlayAgain(self):
        print("PlayAgain")
        self.close()
        MF = MyForm()
        MF.Go()

    def Quit(self):
        print("Quit")
        sys.exit()
class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = uic.loadUi('TestGeometry.ui', self)
        self.ui.frame.setStyleSheet('background-image:url("Artboard 1.png")')
        self.ui.pushButton_2.clicked.connect(self.Go)
        self.ui.pushButton_3.clicked.connect(self.stop)
        self.ui.pushButton_4.clicked.connect(self.Go)
        self.ui.pushButton_5.clicked.connect(self.resume)
        self.setWindowTitle('Car Rush')
        self.setWindowIcon(QIcon('Supercar.png'))
        # TS(200, 600, 15)
        self.p = 0
        self.x = 190
        self.y = 400
        self.settime = 5100
        self.speed = 5000

    def Go(self):
        print("Start")
        self.ui.labelXe1.setGeometry(180, -200, 100, 150)
        self.ui.label_10.setGeometry(190, 400, 100, 150)
        self.timmer = QtCore.QTimer()
        self.timmer.start(self.settime)
        self.timmer.timeout.connect(self.create)
        self.timmer2 = QtCore.QTimer()
        self.timmer2.start(100)
        self.timmer2.timeout.connect(self.check)
        self.timmer3 = QtCore.QTimer()
        self.timmer3.start(5000)
        self.timmer3.timeout.connect(self.calculate)


    def check(self):
        w_car = self.ui.labelXe1.width()
        h_car = self.ui.labelXe1.height()
        X_car = self.ui.labelXe1.x()
        Y_car = self.ui.labelXe1.y()
        w_car2 = self.ui.label_10.width()
        h_car2 = self.ui.label_10.height()

        print(X_car, Y_car, "|", self.x, self.y, "|", h_car, w_car)

        if ((self.x <= (X_car + w_car) and self.x >= X_car) or (self.x + w_car2 >= X_car and self.x + w_car2 <= X_car + w_car)) \
                and ((h_car + Y_car >= self.y) and (h_car2 + Y_car <= self.y + h_car2) or ((Y_car >= self.y) and (Y_car <= self.y + w_car2))):
            self.timmer.stop()
            self.CN.stop()
            self.timmer2.stop()
            print("Game Over")
            w2 = MyForm2()
            w2.show()

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
    def calculate(self):
        if self.ui.labelXe1.y() >= 700:
            self.p += 10
            Ts = TS()
            Ts.setPoint(self.p)
            print(Ts.getPoint())
            self.ui.label.setText(str(Ts.getPoint()))



    def create(self):
        self.image = ["Car-Blue.png", "Car-Green.png", "Car-Oranges.png", "Car-Pink.png"]
        image = random.choice(self.image)
        self.labelXe1.setPixmap(QPixmap(image))
        self.lstR = [30, 190, 360]
        a = random.choice(self.lstR)
        self.CN = QPropertyAnimation(self.ui.labelXe1, b"geometry")
        self.CN.setDuration(self.speed)
        self.CN.setStartValue(QRect(a, -50, 100, 150))
        self.CN.setEndValue(QRect(a, 800, 100, 150))
        self.CN.start()


    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_W or e.key() == QtCore.Qt.Key_Up:
            if self.y > 250:
                self.y -= 30
                self.x += 0
        elif e.key() == QtCore.Qt.Key_S or e.key() == QtCore.Qt.Key_Down:
            if self.y < 420:
                self.y += 30
                self.x += 0
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
