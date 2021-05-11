import sys
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5 import uic
class sv():
    ten=''
    ngaybd=''
    def __init__(self):
        self.namesv=['Tín','Danh','Toàn','Trâm','Hưng','Huy','Bảo']
        self.svdk={
            'Tín': ['CSDL', 'HƯỚNG ĐỐI TƯỢNG', 'LẬP TRÌNH NÂNG CAO', 'GDTC'],
            'Danh': ['CSDL', 'LẬP TRÌNH NÂNG CAO', 'HƯỚNG ĐỐI TƯỢNG', 'TIẾNG ANH'],
            'Toàn': ['CSDL', 'TIẾNG ANH', 'LẬP TRÌNH NÂNG CAO', 'HƯỚNG ĐỐI TƯỢNG'],
            'Hưng': ['CSDL', 'LẬP TRÌNH NÂNG CAO', 'TIẾNG ANH', 'HƯỚNG ĐỐI TƯỢNG', 'GDTC'],
            'Bảo': ['LẬP TRÌNH NÂNG CAO', 'CSDL', 'GDTC', 'HƯỚNG ĐỐI TƯỢNG'],
            'Huy': ['CSDL', 'LẬP TRÌNH NÂNG CAO', 'HƯỚNG ĐỐI TƯỢNG', 'ÂM NHẠC'],
            'Trâm': ['LẬP TRÌNH NÂNG CAO', 'CSDL', 'HƯỚNG ĐỐI TƯỢNG', 'GDTC']
        }
    def rtname(self):
      return self.namesv
    def rtmh(self,name):
        for i in self.svdk:
            if i == name:
               return self.svdk[i]



class danhsachmon(QDialog):
    def __init__(self):
        super(danhsachmon, self).__init__()
        self.ui = uic.loadUi('danhsachmon.ui', self)
        self.show()
        self.ui.comboBox.currentTextChanged.connect(self.showmonhoc)
        self.ui.pushButton.clicked.connect(self.showall)
        self.ui.pushButton_3.clicked.connect(self.moveall)
        self.ui.pushButton_5.clicked.connect(self.showmonhoc)



        self.sinhvien=sv()
        self.namesvis=self.sinhvien.rtname()
        print(self.namesvis)
        for _ in self.namesvis:
            self.ui.comboBox.addItem(_)
    def moveall(self):

        name = self.ui.comboBox.currentText()
        a=sv()
        a1 = a.rtmh(name)
        self.ui.listWidget_2.clear()
        for i in a1:
            self.ui.listWidget_2.addItem(i)
        self.ui.listWidget.clear()

    def showmonhoc(self):
        name = self.ui.comboBox.currentText()
        a=sv()

        a1=a.rtmh(name)
        print(name)
        print(a1)
        self.ui.listWidget.clear()
        for i in a1:
            self.ui.listWidget.addItem(i)
        self.ui.listWidget_2.clear()
    def showall(self):
        name = self.ui.comboBox.currentText()
        a = sv()
        print(self.ui.comboBox.currentText())

        timer=self.ui.dateEdit.text()

        a1 = a.rtmh(name)
        c=''
        for i in a1:
            c+=i+' ;\n \t'
        print(c)
        self.ui.label_7.setText(
            ' Tên SV: '+name+'\n Thời gian: '+timer+'\n Môn đăng kí: '+c
        )
if __name__=="__main__":
    app=QApplication(sys.argv)
    windowa=danhsachmon()
    sys.exit(app.exec_())