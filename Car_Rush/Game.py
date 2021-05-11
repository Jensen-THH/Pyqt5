import sys
# pip install python-vlc
import vlc
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QRect, QPropertyAnimation
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic, QtCore
import random


class MyForm3(QDialog):
    def __init__(self):
        super(MyForm3, self).__init__()
        self.ui = uic.loadUi('file_ui/CountDown.ui', self)
        self.setWindowTitle("Count Down")
        self.count = 3
        self.timecount = QtCore.QTimer()
        self.timecount.start(900)
        self.timecount.timeout.connect(self.set)

    def set(self):
        self.lstcount = ["Go", 1, 2, 3]
        if self.count >= 0:
            self.ui.label.setText(str(self.lstcount[self.count]))
            self.count -= 1
        else:
            self.close()

class MyForm2(QDialog):
    def __init__(self):
        super(MyForm2, self).__init__()
        self.ui = uic.loadUi('file_ui/GameOver.ui', self)
        self.setWindowTitle("Game Over")
        self.ui.pushButton_2.clicked.connect(self.Quit)
        self.ui.label.setText("SCORE: ")

    def Quit(self):
        print("Quit")
        MyForm().stopall()

    def closeDialog(self):
        self.close()
class hd(QDialog):
    def __init__(self):
        super(hd, self).__init__()
        self.ui = uic.loadUi('file_ui/TUTORIOL.ui', self)
        self.setWindowTitle("TUTORIAL")
        self.ui.CLOSE.clicked.connect(self.closeDialog)
    def closeDialog(self):
        self.close()
class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = uic.loadUi('file_ui/Game.ui', self)
        self.ui.frame.setStyleSheet('background-image:url("image/Lane.png")')
        self.label_10.setPixmap(QPixmap('image/Super-car.png'))
        self.image = ["image/Car-Blue.png", "image/Car-Green.png", "image/Car-Oranges.png", "image/Car-Pink.png"]
        self.setWindowTitle('Car Rush')
        self.setWindowIcon(QIcon('image/Supercar.png'))

        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)

        self.ui.pushButton_3.clicked.connect(self.stop)
        self.ui.pushButton_4.clicked.connect(self.Go)
        self.ui.pushButton_5.clicked.connect(self.resume)
        self.ui.TUTORIAL.clicked.connect(self.huongdan)

        self.step=10
        self.point = 0
        self.x = 190
        self.y = 400
        self.settime2 = 6000
        self.speed2 = 6000
        self.settime = 5000
        self.speed = 5000
        self.xea=0
        self.lstR2 = [30, 190, 360]
    def huongdan(self):
        hd().show()

    def Go(self):
        self.p = vlc.MediaPlayer("music/divenha.mp3")
        self.p.play()
        print("Go")

        MF3 = MyForm3()
        MF3.show()
        self.resetpoint()
        self.setPos()
        # self.Disable()

        # Xe1
        self.timexe1 = QtCore.QTimer()
        self.timexe1.start(self.settime)
        self.timexe1.timeout.connect(self.create)

        # Xe2
        self.timexe2 = QtCore.QTimer()
        self.timexe2.start(self.settime2)
        self.timexe2.timeout.connect(self.create2)

        # point
        self.time_point = QtCore.QTimer()
        self.time_point.start(self.speed)
        self.time_point.timeout.connect(self.calculatePoint)

        #point 2
        self.time_point2 = QtCore.QTimer()
        self.time_point2.start(self.speed2)
        self.time_point2.timeout.connect(self.calculatePoint2)

        # check
        self.timeCheck = QtCore.QTimer()
        self.timeCheck.start(100)
        self.timeCheck.timeout.connect(self.check)

        # time Disable
        self.timeDisable = QtCore.QTimer()
        self.timeDisable.start(4000)
        self.timeDisable.timeout.connect(self.Enabled)

    def create(self):
        self.xebot1 = vlc.MediaPlayer("music/xebot.wav")
        self.xebot1.play()
        self.lstR2=[30,190,360]
        image = random.choice(self.image)
        self.labelXe1.setPixmap(QPixmap(image))

        self.xea = random.choice(self.lstR2)
        self.CN = QPropertyAnimation(self.ui.labelXe1, b"geometry")
        self.CN.setDuration(self.speed)
        self.CN.setStartValue(QRect(self.xea, -50, 100, 150))
        self.CN.setEndValue(QRect(self.xea, 800, 100, 150))
        self.CN.start()



    def create2(self):
        self.xebot2 = vlc.MediaPlayer("music/xebot.wav")
        self.xebot2.play()
        r2 = random.choice(self.lstR2)
        print(self.xea)

        if r2 != self.xea:
            print("run r2 "+str(r2))
            self.labelXe2.setPixmap(QPixmap(random.choice(self.image)))
            self.CN2 = QPropertyAnimation(self.ui.labelXe2, b"geometry")
            self.CN2.setDuration(self.speed)
            self.CN2.setStartValue(QRect(r2, -50, 100, 150))
            self.CN2.setEndValue(QRect(r2, 800, 100, 150))
            self.CN2.start()
        else:
            self.lstR2.remove(self.xea)
            print(self.lstR2)
            r_again = random.choice(self.lstR2)
            print("run r_again "+str(r_again))
            self.labelXe2.setPixmap(QPixmap(random.choice(self.image)))
            self.CN2 = QPropertyAnimation(self.ui.labelXe2, b"geometry")
            self.CN2.setDuration(self.speed)
            self.CN2.setStartValue(QRect(r_again, -50, 100, 150))
            self.CN2.setEndValue(QRect(r_again, 800, 100, 150))
            self.CN2.start()

    def Enabled2(self,f):
        self.ui.pushButton_3.setEnabled(f)
        print("done")
    def Enabled(self):
        print("Enabled")
        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(True)
        self.timeDisable.stop()
    def Disable(self):
        print("Disable")
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)

    def setPos(self):
        self.ui.labelXe1.setGeometry(180, -200, 100, 150)
        self.ui.label_10.setGeometry(190, 400, 100, 150)
        self.x = 190
        self.y = 400

    def check(self):
        self.a = None
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
        # chiều cao, rộng xe đỏ
        w_card = self.ui.label_10.width()
        h_card = self.ui.label_10.height()

        # print("Xe 1 ", X_car, Y_car, "|","Xe 2 ", X_car2, Y_car2,"|", self.x, self.y)

        if ((self.x <= (X_car + w_car) and self.x >= X_car) or (self.x + w_card >= X_car and self.x + w_card <= X_car + w_car)) \
                and ((h_car + Y_car >= self.y) and (h_card + Y_car <= self.y + h_card) or ((Y_car >= self.y) and (Y_car <= self.y + w_card))):
            self.time_point.stop()
            self.time_point2.stop()
            self.timeCheck.stop()
            self.timexe1.stop()
            self.timexe2.stop()
            self.CN.stop()
            self.CN2.stop()
            self.p.stop()
            self.ui.labelXe1.move(-200, -200)
            self.ui.labelXe2.move(-200, -200)
            #dừng âm thanh
            self.xebot1.stop()
            self.xebot2.stop()
            #âm thanh đụng xe
            self.crash = vlc.MediaPlayer("music/BOOM.mp3")
            self.crash.play()
            self.crash = vlc.MediaPlayer("music/HEAVENLY.mp3")
            self.crash.play()


            self.Disable()
            print("Game Over")
            self.MF2 = MyForm2()
            self.MF2.ui.pushButton.clicked.connect(self.PlayAgain)
            self.MF2.ui.label.setText('SCORE: ' + str(self.point))
            self.MF2.show()
        if ((self.x <= (X_car2 + w_car2) and self.x >= X_car2) or (self.x + w_card >= X_car2 and self.x + w_card <= X_car2 + w_car2)) \
                and ((h_car2 + Y_car2 >= self.y) and (h_card + Y_car2 <= self.y + h_card) or ((Y_car2 >= self.y) and (Y_car2 <= self.y + w_card))):
            self.time_point.stop()
            self.time_point2.stop()
            self.timexe1.stop()
            self.timexe2.stop()
            self.timeCheck.stop()
            self.CN.stop()
            self.CN2.stop()
            self.p.stop()
            self.ui.labelXe1.move(-200, -200)
            self.ui.labelXe2.move(-200, -200)
            # dừng âm thanh
            self.xebot1.stop()
            self.xebot2.stop()
            # âm thanh đụng xe
            self.crash = vlc.MediaPlayer("music/BOOM.mp3")
            self.crash.play()
            self.crash = vlc.MediaPlayer("music/HEAVENLY.mp3")
            self.crash.play()
            self.Disable()
            print("Game Over")
            self.MF2 = MyForm2()
            self.MF2.ui.pushButton.clicked.connect(self.PlayAgain)
            self.MF2.ui.label.setText('SCORE: ' + str(self.point))
            self.MF2.show()

    def PlayAgain(self):
        self.a = None
        self.crash.stop()
        self.settime2 = 7000
        self.speed2 = 7000
        self.settime = 5000
        self.speed = 5000
        self.Go()
        self.MF2.close()

    def move(self):


        self.anim = QPropertyAnimation(self.ui.label_10, b"geometry")
        self.anim.setDuration(-10)
        self.anim.setStartValue(QRect(self.x, self.y, 100, 150))
        self.anim.setEndValue(QRect(self.x, self.y, 100, 150))
        self.anim.start()

    def stop(self):
        self.timexe1.stop()
        self.timexe2.stop()
        self.time_point.stop()
        self.time_point2.stop()
        self.timeCheck.stop()
        self.CN.pause()
        self.CN2.pause()
        self.ui.pushButton_3.setEnabled(False)
        self.step=0
        self.p.pause()
        self.xebot2.pause()
        self.xebot1.pause()
        print("Stop")

    def resume(self):
        self.timexe1.start()
        self.timexe2.start()
        self.time_point.start()
        self.time_point2.start()
        self.timeCheck.start()
        self.CN.resume()
        self.CN2.resume()
        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton_5.setEnabled(True)
        self.step=10
        self.p.play()
        self.xebot2.play()
        self.xebot1.play()
        print("Resume")



    def calculatePoint(self):
        if self.ui.labelXe1.y() > 700:
            self.point += 10
            self.ui.label.setText(str(self.point))
            print("Calculate Point 1")
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

    def calculatePoint2(self):
        if self.ui.labelXe2.y() > 700:
            self.point += 10
            print(self.point)
            self.ui.label.setText(str(self.point))
            print("Calculate Point 2")
            if self.point == 30:
                self.settime2 = self.settime2 - 500
                self.speed2 = self.speed2 - 500
                print(self.settime2, self.speed2)
                print(self.point)
            if self.point == 60:
                self.settime2 = self.settime2 - 500
                self.speed2 = self.speed2 - 500
                print(self.settime2, self.speed2)
            if self.point == 80:
                self.settime2 = self.settime2 - 500
                self.speed2 = self.speed2 - 500
                print(self.settime2, self.speed2)
            if self.point == 110:
                self.settime2 = self.settime2 - 500
                self.speed2 = self.speed2 - 500
                print(self.settime2, self.speed2)
            if self.point == 160:
                self.settime2 = self.settime2 - 500
                self.speed2 = self.speed2 - 500
                print(self.settime2, self.speed2)
            if self.point == 210:
                self.settime2 = self.settime2 - 500
                self.speed2 = self.speed2 - 500
                print(self.settime2, self.speed2)

    def resetpoint(self):
        self.point = 0
        self.ui.label.setText(str(0))
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_W or e.key() == QtCore.Qt.Key_Up:

            if self.y > 250:
                self.y -= self.step
                self.x += 0

        elif e.key() == QtCore.Qt.Key_S or e.key() == QtCore.Qt.Key_Down:

            if self.y < 420:
                self.y += self.step
                # self.x += 0

        elif e.key() == QtCore.Qt.Key_A or e.key() == QtCore.Qt.Key_Right:

            if self.x > 10:
                self.y += 0
                self.x -= self.step

        elif e.key() == QtCore.Qt.Key_D or e.key() == QtCore.Qt.Key_Left:

            if self.x < 350:
                self.y += 0
                self.x += self.step

        self.move()
    def stopall(self):
        sys.exit()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
