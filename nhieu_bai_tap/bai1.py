import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class bai1(QDialog):
    def __init__(self):
        super(bai1, self).__init__()
        self.ui = uic.loadUi('bai1.ui', self)
        self.ui.pushButton.clicked.connect(self.hienthi)
        self.show()
    def hienthi(self):
        self.ui.label.setText("Hello "+self.ui.lineEdit.text())

if __name__=="__main__":
    app=QApplication(sys.argv)
    windowa=bai1()
    sys.exit(app.exec_())