import sys
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5 import uic
class bmi():
    cao=0
    nang=0
    def __init__(self,cao,nang):
        self.cao=cao
        self.nang=nang
    def printcao(self):
        return self.cao
    def printnang(self):
        return self.nang


class tinhbmi(QDialog):

        def __init__(self):
            super(tinhbmi,self).__init__()
            self.ui =uic.loadUi('tinhBMI.ui',self)
            self.ui.pushButton.clicked.connect(self.hienthi)
            self.show()
        def hienthi(self):
            if len(self.ui.lineEdit.text()) != 0 and len(self.ui.lineEdit_2.text()) != 0:
                a=bmi(self.ui.lineEdit.text(),self.ui.lineEdit_2.text())
                k=round((float(a.printnang())/(float(a.printcao())*float(a.printcao()))),2)
                self.ui.ketqua_2.setText('Ket qua: ' + str(k))

            else:
                self.ui.ketqua_2.setText(' vui long Nhap thong tin !')

if __name__=="__main__":
    app=QApplication(sys.argv)
    windowa=tinhbmi()
    sys.exit(app.exec_())