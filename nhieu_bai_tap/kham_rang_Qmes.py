import sys
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5 import uic

class baitapthem(QDialog):
    def __init__(self):
        super(baitapthem, self).__init__()
        self.ui = uic.loadUi('baitapthemlan2.ui', self)
        self.ui.pushButton.clicked.connect(self.tong)
        self.ui.pushButton_2.clicked.connect(self.thanhtoan)
        self.show()
    def tong(self):
        total=0
        if self.ui.checkBox.isChecked()==True:
            total+=100
        if self.ui.checkBox_2.isChecked()==True:
            total+=500
        if self.ui.spinBox.value()!=0:
            total=total+self.ui.spinBox.value()*10
        if self.ui.spinBox_2.value()!=0:
            total=total+self.ui.spinBox.value()*15
        self.ui.lineEdit_2.setText(str(total))

    def thanhtoan(self):

        msg =QMessageBox()
        # msg.setWindowTitle('Chi Phí')
        msg.setIcon(QMessageBox.Information)
        msg.setText("chào {} {}".format('Ông'if self.ui.comboBox.currentText()=='Nam' else 'Bà',self.ui.lineEdit.text()))
        msg.setInformativeText('Tổng chi phí là: '+self.ui.lineEdit_2.text())
        msg.exec()
if __name__ == '__main__':

    app=QApplication(sys.argv)
    b = baitapthem()
    sys.exit(app.exec())
