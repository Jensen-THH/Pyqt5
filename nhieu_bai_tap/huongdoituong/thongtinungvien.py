import sys
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5 import uic
class tt():
    ten=''
    gioitinh=''
    diachi=''
    qualification=''
    assets=''
    def __init__(self,ten,gioitinh,diachi,qualification,assets):
        self.ten=ten
        self.gioitinh=gioitinh
        self.diachi=diachi
        self.qualification=qualification
        self.assets=assets
    def printten(self):
        return self.ten
    def printgt(self):
        return self.gioitinh
    def printdc(self):
        return self.diachi
    def printqlf(self):
        return self.qualification
    def printast(self):
        return self.assets
class thongtinungvien(QDialog):
    def __init__(self):
        super(thongtinungvien, self).__init__()
        self.ui = uic.loadUi('thongtinungvien.ui', self)
        self.ui.pushButton_2.clicked.connect(self.hienthi)
        self.show()
        self.gt=''
    def hienthi(self):
        if self.ui.radioButton.isChecked() == True:
            self.gt = ('Nam')
        else:
            self.gt = ('Nu')
        a=tt(self.ui.lineEdit.text(),self.gt,self.ui.lineEdit_2.text(),self.ui.comboBox.currentText(),'')
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('Ten khach hang:'+a.printten()+'\n Gioi tinh:'+self.gt+'\n Qualification:'+a.printqlf())
        msg.setInformativeText('{}\n{}\n{}'.format(
            'Home ' if self.ui.checkBox.isChecked()==True else '',
            'car ' if self.ui.checkBox_2.isChecked() == True else '',
            'bike ' if self.ui.checkBox_3.isChecked()==True else '')
        )
        msg.exec()
if __name__=="__main__":
    app=QApplication(sys.argv)
    windowa=thongtinungvien()
    sys.exit(app.exec_())