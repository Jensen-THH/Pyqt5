import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic

class btthem(QDialog):
    def __init__(self):
        super(btthem, self).__init__()
        self.ui = uic.loadUi('baitapthem2.ui', self)


        self.show()
