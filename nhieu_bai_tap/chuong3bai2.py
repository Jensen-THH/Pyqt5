import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic,QtCore

class chuong3bai2(QDialog):
    def __init__(self):
        super(chuong3bai2,self).__init__()
        self.ui = uic.loadUi('chuong3bai2.ui',self)
        self.ui.calendarWidget.selectionChanged.connect(self.hienthi)
        self.show()
    def hienthi(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = chuong3bai2()
    sys.exit(app.exec())