import sys
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5 import uic
class songay():
    thang=0
    nam=0
    def __init__(self,thang,nam):
        self.thang=thang
        self.nam=nam
    def printnam(self):
        return self.nam
    def printthang(self):
        namethang={
            1:'Tháng Một',
            2:'Tháng Hai',
            3:'Tháng Ba',
            4: 'Tháng Bốn',
            5: 'Tháng Năm',
            6: 'Tháng Sáu',
            7: 'Tháng Bảy',
            3: 'Tháng Tám',
            8: 'Tháng Tám',
            9: 'Tháng Chín',
            10: 'Tháng Mười',
            11: 'Tháng Mười một',
            12: 'Tháng Mười hai',
        }
        for i in namethang:
            if self.thang==i:
                tenthang=namethang[i]
                return  tenthang
    def dayy(self):
        month31=[1,3,5,7,8,10,12]
        month30 = [4,6,7,11]
        for i in month31:
            if self.thang==i:
                return '31 ngày'
        for i in month30:
            if self.thang == i:
                return '30 ngày'
        if self.thang==2:
            if self.nam % 4 == 0 and self.nam % 100 != 0 or self.nam%400==0:
                    return '29 ngày'

            else:
                    return '28 ngày'

class songayne(QDialog):
    def __init__(self):
        super(songayne, self).__init__()
        self.ui = uic.loadUi('tinhsongay.ui', self)
        self.ui.pushButton.clicked.connect(self.hienthi)
        self.show()
    def hienthi(self):
        a=songay(int(self.ui.lineEdit_2.text()),int(self.ui.lineEdit.text()))
        a1=a.printthang()
        a3=a.printnam()
        a2=a.dayy()
        self.ui.label_3.setText(
            str(a1)+', năm '+ str(a3)+ ' có '+a2
        )
if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = songayne()
    sys.exit(app.exec())




