import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic

class baitapcombobox(QDialog):
    def __init__(self):
        super(baitapcombobox, self).__init__()
        self.ui = uic.loadUi('baitap_combobox.ui', self)
        self.ui.comboBox.currentIndexChanged.connect(self.hienthi)
        self.show()
    def hienthi(self):
        self.ui.label_2.setText('You have select: '+self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = baitapcombobox()
    sys.exit(app.exec())