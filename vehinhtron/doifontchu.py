
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QFont,QPainter
from PyQt5 import uic


class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('font.ui', self)

        self.show()
    def paintEvent(self):
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())