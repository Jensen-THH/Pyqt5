import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class baitap10_11(QDialog):
    def __init__(self):
        super(baitap10_11,self).__init__()
        self.ui = uic.loadUi('baitap10_11.ui',self)
        self.ui.spinBox.editingFinished.connect(self.tinh)
        self.ui.soluongsugar.editingFinished.connect(self.tinh1)
        self.show()
    def tinh(self):

            if len(self.ui.book.text())!=0:
                a=int(self.ui.book.text())
                b=int(self.ui.spinBox.value())
                c= a * b
                self.ui.pricebook.setText(str(c))
                self.ui.total.setText(float(round(self.ui.pricesugar.text()+c,2)))
            else :
                c=0
                self.ui.pricebook.setText(c)

    def tinh1(self):
            if len(self.ui.sugar.text())!=0:
                e=float(self.ui.sugar.text())
                f=float(self.ui.soluongsugar.value())
                g= e * f
                self.ui.pricesugar.setText(str(round(g,2)))
                self.ui.total.setText(int(self.ui.pricebook.text()) + g)
            else :
                self.ui.pricesugar.setText('0')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = baitap10_11()
    sys.exit(app.exec())