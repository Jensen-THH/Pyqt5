import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class maytinh(QDialog):
    def __init__(self):
        super(maytinh, self).__init__()
        self.ui = uic.loadUi('maytinhne.ui', self)
        self.ui.hai.clicked.connect(lambda :self.hienthi('1'))
        self.show()
    def hienthi(self,a):

        print('hello')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = maytinh()
    b.show()
    sys.exit(app.exec())
