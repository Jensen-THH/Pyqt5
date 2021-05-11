import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class bai1(QDialog):
    pass
    # def __init__(self):
    #     super(bai1, self).__init__()
    #     self.ui = uic.loadUi('chuong2bai1.ui', self)
    #     self.ui.copy.toggled.connect(self.hienthi)
    #     self.ui.past.toggled.connect(self.hienthi)
    #     self.ui.lineEdit.toggled.connect(self.hienthi)
    #     self.ui.lineEdit_2.toggled.connect(self.hienthi)
    #     self.show()
    #
    #
    #
if __name__ == '__main__':
    app=QApplication(sys.argv)
    b=bai1()
    b.show()
    sys.exit(app.exec())