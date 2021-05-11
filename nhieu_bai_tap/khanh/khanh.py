import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class khambenh(QDialog):
    def __init__(self):
        super(khambenh,self).__init__()
        self.ui = uic.loadUi('khanh.ui',self)
        self.ui.listWidget.itemSelectionChanged.connect(self.add)
        self.ui.pushButton_2.clicked.connect(self.delitem)
        self.ui.pushButton.clicked.connect(self.showall)
        self.x=[]
        self.ui.listWidget.addItem("1")

        self.ui.listWidget.addItem("2")
        self.ui.listWidget.addItem("3")
        self.ui.listWidget.addItem("4")
        self.x=[]
        self.show()
    def add(self):

        self.x=[]
        self.ui.listWidget_2.clear()
        item = self.ui.listWidget.selectedItems()

        for i in list(item):
            self.ui.listWidget_2.addItem(i.text())
            self.x.append(str(i.text()))
    def delitem(self):
        self.ui.listWidget_2.clear()
        self.ui.label_7.clear()
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setFocus()
    def showall(self):
        a=''
        for i in self.x:
           a+=i+';'
        if len(self.ui.lineEdit.text())!=0:
            if self.ui.lineEdit_2.isnumeric()==True and self.ui.lineEdit_3.isnumeric()==True and self.ui.lineEdit_4.isnumeric()==True:
             self.ui.label_7.setText(
                'Họ tên:'+str(self.ui.lineEdit.text())
                +'\n Ngày sinh: '+str(self.ui.lineEdit_2.text())+' '+str(self.ui.lineEdit_3.text())+' '+str(self.ui.lineEdit_4.text())+' '
                +'\n Dịch vụ đã chọn: '+str(a)
             )
            else:self.ui.label_7.setText('Vui lòng nhập đúng ngày tháng năm sinh')
        else:self.ui.lineEdit.setFocus()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = khambenh()
    sys.exit(app.exec())