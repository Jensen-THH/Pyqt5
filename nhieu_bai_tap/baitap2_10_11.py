import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class baitap(QDialog):
    def __init__(self):
        super(baitap,self).__init__()
        self.ui = uic.loadUi('baitap2_10_11.ui', self)
        self.ui.horizontalScrollBar.valueChanged.connect(self.hienthi)
        self.ui.horizontalSlider.valueChanged.connect(self.hienthi1)
        self.ui.verticalScrollBar.valueChanged.connect(self.hienthi2)
        self.ui.verticalSlider.valueChanged.connect(self.hienthi3)
        self.show()
    def hienthi(self,a):
        self.ui.lineEdit.setText('Sugar level: '+str(a))
    def hienthi1(self,value):
        self.ui.lineEdit.setText('Sugar level: '+str(value))
    def hienthi2(self,value):
        self.ui.lineEdit.setText('Sugar level: '+str(value))
    def hienthi3(self,value):
        self.ui.lineEdit.setText('Sugar level: '+str(value))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = baitap()
    sys.exit(app.exec())