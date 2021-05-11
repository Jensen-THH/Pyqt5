import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QRect, QPropertyAnimation
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic, QtCore
import random
import time
# class TS:
#     def __init__(self, x_1, y_1, Step):
#         self.x = x_1
#         self.y = y_1
#         self.step = Step
#
#     def X1(self):
#         return self.x
#
#     def Y1(self):
#         return self.y
#
#     def Step(self):
#         return self.step

class MyForm2(QDialog):
    def __init__(self):
        super(MyForm2, self).__init__()
        self.ui = uic.loadUi('Test-3.ui', self)
        self.setWindowTitle("Game Over")
        self.ui.pushButton.clicked.connect(self.PlayAgain)
        self.ui.pushButton_2.clicked.connect(self.Quit)
        self.ui.label.setText("Score: 500")
    def PlayAgain(self):
        print("alo123")
        w2 = MyForm2()
        # w2.exit()
        self.close()
        # w2.closeAllWindows()
    def Quit(self):
        print("Quit")
        sys.exit()

class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = uic.loadUi('Test-2.ui', self)
        self.ui.pushButton.clicked.connect(self.set)

    def set(self):
        w2 = MyForm2()
        w2.show()

    def alo(self):
        print("456a45s")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
