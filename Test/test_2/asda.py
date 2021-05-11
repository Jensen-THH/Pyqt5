import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem
from PyQt5 import uic, QtCore
from datetime import datetime
import random

class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = uic.loadUi('CountDown.ui', self)
        self.time = 30
        self.timer = QtCore.QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.startT)
    def startT(self):
        if self.time >= 0:
            self.ui.label.setText(str(self.time))
            self.time -= 1
        else:
            self.timer.stop()
            self.time = 30


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
