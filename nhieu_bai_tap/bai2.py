import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class myforma(QDialog):
    def __init__(self):
        super(myforma,self).__init__()
        self.ui =uic.loadUi('bai2.ui',self)
        self.ui.radioButton_1.toggled.connect(self.hienthi)
        self.ui.radioButton_2.toggled.connect(self.hienthi)
        self.ui.radioButton_3.toggled.connect(self.hienthi)
        self.show()
    def hienthi(self):
        farea = 0
        if self.ui.radioButton_1.isChecked()==True:
            farea=150
        if self.ui.radioButton_2.isChecked()==True:
            farea=125
        if self.ui.radioButton_3.isChecked()==True:
            farea=100
        self.ui.labelResult.setText('do la : ' + str(farea))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    a=myforma()
    a.show()
    sys.exit(app.exec())