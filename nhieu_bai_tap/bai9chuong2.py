import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic

class baitap9(QDialog):
    def __init__(self):
        super(baitap9, self).__init__()
        self.ui = uic.loadUi('bai9chuong2.ui', self)
        self.ui.pushButton.clicked.connect(self.chon)
        self.ui.pushButton_2.clicked.connect(self.xoa)
        self.items = []
        self.show()

    def chon(self):
        a=[]
        item=''
        if self.ui.radioButton.isChecked()==True:
            item='Bò'
        if self.ui.radioButton_2.isChecked() == True:
            item = 'Gà'
        if self.ui.radioButton_3.isChecked() == True:
            item = 'Cá'
        if self.ui.checkBox.isChecked()==True:
            d=self.ui.checkBox.text()
            a.append(d)
        if self.ui.checkBox_2.isChecked()==True:
            d = self.ui.checkBox_2.text()
            a.append(d)
        if self.ui.checkBox_3.isChecked()==True:
            d = self.ui.checkBox_3.text()
            a.append(d)
        for m in a :
            i = item+ ' ' + m
            if i not in self.items:
                self.ui.listWidget.addItem(i)
                self.items.append(i)
    def xoa(self):
        lisitem=self.ui.listWidget.selectedItems()
        if not lisitem:
            return
        for it in lisitem:
            self.ui.listWidget.takeItem(self.ui.listWidget.row(it))
            self.items.remove(it.text())
if __name__ == '__main__':

    app=QApplication(sys.argv)
    b = baitap9()
    sys.exit(app.exec())
