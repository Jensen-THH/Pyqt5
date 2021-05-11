import sys
from PyQt5.QtWidgets import QDialog,QApplication,QInputDialog,QListWidgetItem
from PyQt5 import uic
class baitap(QDialog):
    def __init__(self):
        super(baitap,self).__init__()
        self.ui = uic.loadUi('baitap8_10_11.ui', self)
        self.ui.pushButton.clicked.connect(self.edit)
        self.ui.pushButton_2.clicked.connect(self.dele)
        self.ui.pushButton_3.clicked.connect(self.delall)

        self.ui.listWidget.addItem('Pizza')
        self.ui.listWidget.addItem('Soda')
        self.ui.listWidget.addItem('Coffe')
        self.show()
    def edit(self):
        row=self.ui.listWidget.currentRow()
        newtext,ok=QInputDialog.getText(self,'enter new text','enter new text')
        if ok and len(newtext)!=0:
            self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
            self.ui.listWidget.insertItem(row,QListWidgetItem(newtext))
    def dele(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
    def delall(self):
        self.ui.listWidget.clear()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = baitap()
    sys.exit(app.exec())