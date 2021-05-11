import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap

class baitapphim(QDialog):
    def __init__(self):
        super(baitapphim, self).__init__()
        self.ui=uic.loadUi('baitapphim.ui',self)

        self.show()
    def keyPressEvent(self,e):
        if e.modifiers() == QtCore.Qt.ShiftModifier and e.key() == QtCore.Qt.Key_B:
            self.ui.label.setPixmap(QPixmap("bo.jpg"))
            print('running')
        elif e.key()==QtCore.Qt.Key_B:
            self.ui.label.setPixmap(QPixmap("bocon.jpg"))
            print('running')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = baitapphim()
    sys.exit(app.exec_())

