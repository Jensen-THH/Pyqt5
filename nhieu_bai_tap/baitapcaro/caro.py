import sys
from PyQt5.QtWidgets import QDialog,QApplication,QTableWidgetItem
from PyQt5 import uic
class myform(QDialog):
    def __init__(self):
        super(myform,self).__init__()
        self.ui = uic.loadUi('caro.ui',self)

        self.show()
        self.ui.tableWidget.clicked.connect(self.process)
        self.item='x'
    def process(self):
        selected_cell = self.ui.tableWidget.selectedIndexes()
        if len(selected_cell) > 0:
            row = selected_cell[0].row()
            column = selected_cell[0].column()

            if self.item=='x':
                self.item='o'
            else:
                self.item='x'
            self.ui.tableWidget.setItem(row, column,QTableWidgetItem(self.item))










if __name__ == '__main__':
    app = QApplication(sys.argv)
    a=myform()
    a.show()
    sys.exit(app.exec())
#selectedIndexes