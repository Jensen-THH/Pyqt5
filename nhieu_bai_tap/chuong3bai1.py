import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic,QtCore
class chuong3bai1(QDialog):
    def __init__(self):
        super(chuong3bai1, self).__init__()
        self.ui = uic.loadUi('chuong3bai1.ui', self)
        time = QtCore.QTimer(self)
        time.start(1000)
        time.timeout.connect(self.hienthi)
        self.hienthi()
        self.show()

    def hienthi(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.ui.clock.display(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = chuong3bai1()
    b.show()
    sys.exit(app.exec())
