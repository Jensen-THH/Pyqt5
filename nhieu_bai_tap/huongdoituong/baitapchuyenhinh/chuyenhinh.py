import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

class baitapchuyenhinh(QDialog):
    def __init__(self):
        super(baitapchuyenhinh, self).__init__()
        self.ui=uic.loadUi('chuuyenhinh.ui',self)

        self.pushButton.clicked.connect(self.backimg)
        self.pushButton_2.clicked.connect(self.nextimg)
        self.show()
        self.so=0
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.label.setPixmap(QPixmap('hanquoc.jpg'))
        self.ui.label_2.setPixmap(QPixmap('japan.jpg'))
        self.ui.label_3.setPixmap(QPixmap('thailan.jpg'))
        self.ui.label_4.setPixmap(QPixmap('campuchia.jpg'))
    def backimg(self):


            if self.so <= 0:
                self.so = 3
                self.ui.stackedWidget.setCurrentIndex(self.so)
                print('tra ve 3')

            else:
                self.so -= 1
                self.ui.stackedWidget.setCurrentIndex(self.so)
                print('tru 1')




    def nextimg(self):


            if self.so>=3:
                self.so =0
                self.ui.stackedWidget.setCurrentIndex(self.so)
                print('tra ve 0')
            else:
                self.so +=1
                self.ui.stackedWidget.setCurrentIndex(self.so)
                print(" cong 1")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = baitapchuyenhinh()
    sys.exit(app.exec_())

