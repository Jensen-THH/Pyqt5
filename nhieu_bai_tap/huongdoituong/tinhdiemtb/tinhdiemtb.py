import sys
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5 import uic
class dtb():
    toan=0
    van=0
    def __init__(self,toan,van):
        self.toan=toan
        self.van=van
    def printdtb(self):
        try:
            self.van=float(self.van)
            self.toan = float(self.toan)
            if 0<= self.toan<=10 and 0<= self.van<=10:
                tb = round((self.toan + self.van) / 2,2)
                if tb>=8 and self.toan>=7 and self.van>=7:
                    return str('Điểm trung bình: '+str(tb)+'\n Xếp loại: Giỏi')
                elif tb>=6 and self.toan>=6 and self.van>=6:
                    return str('Điểm trung   bình: ' + str(tb) + '\n Xếp loại: Khá')
                elif tb>=5 and self.toan>=5 and self.van>=5:
                    return str('Điểm trung bình: ' + str(tb) + '\n Xếp loại: Trung bình')
                else:
                    return str('Điểm trung bình: ' + str(tb) + '\n Xếp loại: Yếu')
            else:
                return 'Hãy nhập đúng  !'
        except ValueError:
          return 'Nhập số đầy đủ và đúng'
class tinhtbne(QDialog):
    def __init__(self):
        super(tinhtbne, self).__init__()
        self.ui = uic.loadUi('tinhdiemtb.ui', self)
        self.ui.pushButton.clicked.connect(self.hienthi)
        self.ui.lineEdit.textChanged.connect(self.openclick)
        self.ui.lineEdit_2.textChanged.connect(self.openclick)
        self.show()
    def openclick(self):
        self.ui.pushButton.setEnabled(True)
    def hienthi(self):
        self.ui.pushButton.setEnabled(False)
        a=dtb(self.ui.lineEdit.text(),self.ui.lineEdit_2.text())
        a1=a.printdtb()
        self.ui.label_3.setText(a1)

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=tinhtbne()
    sys.exit(app.exec_())
