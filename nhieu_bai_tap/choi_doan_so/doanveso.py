import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
import random

class doanso(QDialog):
    def __init__(self):
        super(doanso, self).__init__()
        self.ui=uic.loadUi('doanso.ui',self)
        self.ui.pushButton.clicked.connect(self.kt)
        self.ui.pushButton_2.clicked.connect(self.star)
        self.sotrung=0
        self.show()
    def star(self):
        self.sotrung= random.randint(1, 45)

        # print(self.sotrung)
    def kt(self):
        if self.sotrung!=0:
            vs_value = int(self.ui.spinBox.value())
            # print(vs_value)

            if self.sotrung== vs_value:
                self.ui.label.setText('Corect Guess')
            else:
                self.ui.label.setText('Incorect Guess')
        else:
            self.ui.label.setText('click Start !')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = doanso()
    sys.exit(app.exec_())