import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class baitapthemne(QDialog):
    def __init__(self):
        super(baitapthemne,self).__init__()
        self.ui = uic.loadUi('baitapthemngoai.ui',self)
        self.show()
        self.ui.pushButton.clicked.connect(self.thongke)
    def thongke(self):
            pass

if __name__ == '__main__':
    app=QApplication(sys.argv)
    b = baitapthemne()
    sys.exit(app.exec())
