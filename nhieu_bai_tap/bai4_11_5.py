import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class bai4_11_5(QDialog):
        def __init__(self):
            super(bai4_11_5, self).__init__()
            self.ui = uic.loadUi('bai4_11_5.ui', self)
            self.ui.checkBox1.stateChanged.connect(self.hienthi)
            self.ui.checkBox2.stateChanged.connect(self.hienthi)
            self.ui.checkBox3.stateChanged.connect(self.hienthi)
            self.show()
        def hienthi(self):
            amount=10
            if self.ui.checkBox1.isChecked()==True:
                amount+=1
            if self.ui.checkBox2.isChecked()==True:
                amount+=1
            if self.ui.checkBox3.isChecked()==True:
                amount+=2
            self.ui.ketqua.setText('Your Total price: $ '+str(amount))
if __name__ == '__main__':
    app=QApplication(sys.argv)
    a=bai4_11_5()
    a.show()
    sys.exit(app.exec())