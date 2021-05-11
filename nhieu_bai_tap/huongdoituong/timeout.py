import sys
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5 import uic
import time
from PyQt5.QtCore import QBasicTimer
class timeoutne(QDialog):
    def __init__(self):
        super(timeoutne, self).__init__()
        self.ui = uic.loadUi('TIMEOUT.ui', self)
        self.ui.pushButton.clicked.connect(self.chay)
        self.ui.pushButton_2.clicked.connect(self.stopne)
        self.count=0
        self.running=True
        self.show()
    def chay(self):
        if self.ui.lineEdit.text().isnumeric()==True and self.running:
                a=int(self.ui.lineEdit.text())
                self.ui.progressBar.setMaximum(a)
                self.ui.progressBar_2.setMaximum(a)
                while self.running==True and self.count<a:
                    self.count+=1
                    # slowing down the loop
                    time.sleep(0.05)

                    # setting value to progress bar
                    self.ui.progressBar.setValue(self.count)
                    self.ui.progressBar_2.setValue(self.count)

        else:
            self.ui.lineEdit.setFocus()
    def stopne(self):
                    self.running = False


if __name__=="__main__":
    app=QApplication(sys.argv)
    windowa=timeoutne()
    sys.exit(app.exec_())