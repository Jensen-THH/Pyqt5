import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class baitap4(QDialog):
    def __init__(self):
        super(baitap4, self).__init__()
        self.ui = uic.loadUi('baitapso4.ui', self)
        self.ui.a.stateChanged.connect(self.hienthi)
        self.ui.b.stateChanged.connect(self.hienthi)
        self.ui.c.stateChanged.connect(self.hienthi)
        self.ui.d.stateChanged.connect(self.hienthi)
        self.ui.q.stateChanged.connect(self.hienthi)
        self.ui.w.stateChanged.connect(self.hienthi)
        self.ui.e.stateChanged.connect(self.hienthi)
        self.ui.groupBox.toggled.connect(self.hienthi)
        self.ui.groupBox_2.toggled.connect(self.hienthi)
        self.show()
    def hienthi(self):
        total=0
        if self.ui.groupBox.isChecked() == True:
            if self.ui.a.isChecked()==True:
                total+=4
            if self.ui.b.isChecked()==True:
                total+=2
            if self.ui.c.isChecked()==True:
                total+=1
            if self.ui.d.isChecked()==True:
                total+=3
        if self.ui.groupBox_2.isChecked() == True:
            if self.ui.q.isChecked()==True:
                total+=5
            if self.ui.w.isChecked()==True:
                total+=10
            if self.ui.e.isChecked()==True:
                total+=15
        self.ui.ketqua.setText('Total: '+str(total))
if __name__ == '__main__':
    app=QApplication(sys.argv)
    b=baitap4()
    b.show()
    sys.exit(app.exec())