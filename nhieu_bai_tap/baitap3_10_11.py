import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class baitap10_11(QDialog):
    def __init__(self):
        super(baitap10_11,self).__init__()
        self.ui = uic.loadUi('baitap3_10_11.ui',self)
        self.ui.listWidget.itemClicked.connect(self.hienthi)
        self.show()
    def hienthi(self):
        self.ui.label_2.setText("You are select:" + self.ui.listWidget.currentItem().text())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = baitap10_11()
    sys.exit(app.exec())