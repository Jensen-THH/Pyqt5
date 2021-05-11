import sys
from PyQt5.QtWidgets import QDialog,QApplication,QLabel
from PyQt5 import uic,QtCore
from PyQt5.QtCore import QRect, QPropertyAnimation
import  random
import  time
class ApplWindow(QDialog):
    def __init__(self):
        super(ApplWindow, self).__init__()
        self.ui = uic.loadUi('testmoveLabel.ui', self)
        self.ui.pushButton.clicked.connect(self.runne)
        self.ui.pushButton_2.clicked.connect(self.checkne)


        self.show()
    def runne(self,x):





            self.CN = QPropertyAnimation(self.ui.label, b"geometry")
            self.CN.setDuration(4000)
            self.CN.setLoopCount(1)
            print('a')
            self.CN.setKeyValueAt(0,QRect(600, 0, 80, 120))
            self.CN.setKeyValueAt(0.5,QRect(0, 0, 80, 120))
            self.CN.setKeyValueAt(1,QRect(70, 200, 80, 120))
            self.CN.start()
    def checkne(self):
        x=self.ui.label.x()
        x2=self.ui.label_2.x()
        print(x)
        print(x2)










    def stopx(self):
        self.CN.stop()








if __name__=="__main__":
    app=QApplication(sys.argv)
    window=ApplWindow()
    sys.exit(app.exec_())