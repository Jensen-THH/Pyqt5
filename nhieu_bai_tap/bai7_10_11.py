import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class baitap(QDialog):
    def __init__(self):
        super(baitap,self).__init__()
        self.ui = uic.loadUi('baitap7_10_11.ui', self)
        self.ui.pushButton.clicked.connect(self.addlist)
        self.show()
    def addlist(self):
        self.ui.listWidget.addItem( self.ui.lineEdit.text())
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setFocus()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = baitap()
    sys.exit(app.exec())