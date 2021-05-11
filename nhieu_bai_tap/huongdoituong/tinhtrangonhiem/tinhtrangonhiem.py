import sys
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5 import uic
class tinhtrang():
    nhamay=0
    khudancu=0
    tttm=0
    def __init__(self,nhamay,khudancu,tttm):
        self.nhamay=nhamay
        self.khudancu=khudancu
        self.tttm=tttm
    def printtt(self):
        tbc=(self.nhamay+self.khudancu+self.tttm)/3
        if tbc>=50:
           return str('Chỉ số ô nhiễm là: '+str(round(tbc,2))+', Tình trạng ô nhiễm: Độc hại !')
        else:
           return 'Chỉ số ô nhiễm là: '+str(round(tbc,2))+', Tình trạng ô nhiễm: An toàn'
class Chiso(QDialog):
    def __init__(self):
        super(Chiso, self).__init__()
        self.ui = uic.loadUi('tinhtrangonhiem.ui', self)
        self.ui.pushButton.clicked.connect(self.hienthi)
        self.ui.pushButton_2.clicked.connect(self.ketthuc)
        self.show()
    def hienthi(self):
        if self.ui.lineEdit.text().isnumeric()==True and self.ui.lineEdit_2.text().isnumeric()==True and self.ui.lineEdit_3.text().isnumeric()==True:
            a=tinhtrang(int(self.ui.lineEdit.text()),int(self.ui.lineEdit_2.text()),int(self.ui.lineEdit_3.text()))
            a1=a.printtt()
            self.ui.label_4.setText(
                a1
            )
        else:
            self.ui.label_4.setText('Nhập chỉ số!')
            self.ui.lineEdit.setFocus()
    def ketthuc(self):
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setFocus()
        self.ui.label_4.setText('')
if __name__=="__main__":
    app=QApplication(sys.argv)
    windowa=Chiso()
    sys.exit(app.exec_())
