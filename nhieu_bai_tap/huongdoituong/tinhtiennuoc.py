import sys
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5 import uic
class tinhtiennuoc(QDialog):
    def __init__(self):
        super(tinhtiennuoc, self).__init__()
        self.ui = uic.loadUi('tinhtiennuoc.ui', self)
        self.ui.spinBox.valueChanged.connect(self.tinhdinhmuc)
        self.ui.pushButton.clicked.connect(self.tinh)
        self.ui.pushButton_2.clicked.connect(self.inhd)
        self.show()

    def tinhdinhmuc(self):

        # if  self.ui.lineEdit_2.text().isnumeric() == True and len(self.ui.lineEdit_2.text())!=0:
            dm=int(self.ui.spinBox.value())
            if dm==3:
                self.ui.lineEdit_6.setText(str(12))
            else:
                tdm=dm*4
                self.ui.lineEdit_6.setText(str(tdm))
        # else:
        #     self.ui.lineEdit_6.setText('')
    def tinh(self):
        try:
            socu=int(self.ui.lineEdit_3.text())
            somoi = int(self.ui.lineEdit_4.text())
            if socu<somoi:
                soht= somoi-socu

                self.ui.lineEdit_5.setText(str(soht))
                self.ui.label_17.setText('')
            else:
                self.ui.lineEdit_5.setText('')
                self.ui.label_17.setText('nhập sai !')

            sott = int(self.ui.lineEdit_5.text())
            sotdm = int(self.ui.lineEdit_6.text())
            sovdm=sott-sotdm
            if sovdm>=0:
                self.ui.lineEdit_7.setText(str(sovdm))
            else:
                self.ui.lineEdit_7.setText(str(0))
            ttsd=int(self.ui.lineEdit_6.text())*4000+int(self.ui.lineEdit_7.text())*8000
            self.ui.label_14.setText(str(ttsd)+' Vnđ')
            self.ui.label_15.setText(str(ttsd*0.05)+' Vnđ')
            self.ui.label_16.setText(str(int(ttsd * 0.05+ttsd)) + ' Vnđ')
        except ValueError:
            self.ui.label_17.setText('Vui lòng nhập đầy đủ thông tin !')
    def inhd(self):
        try:
            if len(self.ui.lineEdit.text())!=0:
                self.ui.label_17.setText(
                                        'Họ tên: '+self.ui.lineEdit.text()+
                                        '\n Số nhân khẩu: '+str(self.spinBox.value())+
                                        '\n Mét khối tiêu thụ: '+str(self.ui.lineEdit_5.text())+
                                        '\n Tổng số tiền phải trả: ' + str(self.ui.label_16.text())
                                    )
            else:
                self.ui.label_17.setText(' !')
        except ValueError:
            self.ui.label_17.setText('Nhập đầy đủ !')

if __name__=="__main__":
    app=QApplication(sys.argv)
    windowa=tinhtiennuoc()
    sys.exit(app.exec_())