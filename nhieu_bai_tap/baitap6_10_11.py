import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class baitap6_10_11(QDialog):
    def __init__(self):
        super(baitap6_10_11,self).__init__()
        self.ui = uic.loadUi('baitap6_10_11.ui',self)
        self.ui.listWidget.itemSelectionChanged.connect(self.add)
        self.show()
    def add(self):
        self.ui.listWidget_2.clear()
        item = self.ui.listWidget.selectedItems()
        x=[]
        for i in list(item):
            self.ui.listWidget_2.addItem(i.text())
            x.append(str(i.text()))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = baitap6_10_11()
    sys.exit(app.exec())