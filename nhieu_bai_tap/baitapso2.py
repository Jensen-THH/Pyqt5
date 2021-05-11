import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class baitap2(QDialog):
    def __init__(self):
        super(baitap2, self).__init__()
        self.ui = uic.loadUi('baitapso2.ui', self)
        self.ui.m.toggled.connect(self.hienthi)
        self.ui.l.toggled.connect(self.hienthi)
        self.ui.xl.toggled.connect(self.hienthi)
        self.ui.xxl.toggled.connect(self.hienthi)
        self.ui.debit.toggled.connect(self.hienthi)
        self.ui.netbanking.toggled.connect(self.hienthi)
        self.ui.cash.toggled.connect(self.hienthi)
        self.show()
    def hienthi(self):
        size='not'
        payment='no'
        if self.ui.m.isChecked() == True:
            size = 'Medium'
        if self.ui.l.isChecked() == True:
            size = 'Large'
        if self.ui.xl.isChecked() == True:
            size = 'Extra Large'
        if self.ui.xxl.isChecked() == True:
            size = 'Extra Extra Large'
        if self.ui.debit.isChecked()==True:
            payment='Debit'
        if self.ui.netbanking.isChecked()==True:
            payment='NetBanking'
        if self.ui.cash.isChecked()==True:
            payment='Cash on delivery'
        self.ui.ketqua.setText('Choose your size is:'+size +' payment method is: '+payment)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    b=baitap2()
    b.show()
    sys.exit(app.exec())