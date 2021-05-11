import sys
from PyQt5.QtWidgets import QDialog,QApplication,QTableWidgetItem
from PyQt5 import uic
class myform(QDialog):
    def __init__(self,data):
        super(myform,self).__init__()
        self.ui = uic.loadUi('baitaptest.ui',self)
        self.data=data
        self.addcontent()
        self.show()
        self.ui.tableWidget.clicked.connect(self.process)

    def addcontent(self):
        row = 0
        for tup in self.data:
            col = 0
            for item in tup:
                oneitem = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, col, oneitem)
                col += 1
            row += 1

    def process(self):
        selected_cell = self.ui.tableWidget.selectedIndexes()
        if len(selected_cell) > 0:
            row = selected_cell[0].row()
            column = selected_cell[0].column()
            s = "Dòng: " + str(row) + "\nCột: " + str(column)
            s += "\nGiá trị: " + self.ui.tableWidget.item(row, column).text()
            self.ui.lb_Chon.setText(s)

data = []
data.append(('Suite', '40$'))
data.append(('Super Luxury', '30$'))
data.append(('Super Deluxe', '20$'))
data.append(('Ordinary', '10$'))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    a=myform(data)
    a.show()
    sys.exit(app.exec())
#selectedIndexes