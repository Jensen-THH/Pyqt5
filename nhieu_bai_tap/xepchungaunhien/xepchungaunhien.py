import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
import random
class churandom(QDialog):
    def __init__(self):
        super(churandom, self).__init__()
        self.ui=uic.loadUi('xepchu.ui',self)
        self.ui.pushButton.clicked.connect(self.kt)
        self.ui.pushButton_2.clicked.connect(self.start)
        self.ui.pushButton_3.clicked.connect(self.reset)
        self.words=['red','green','blue','yellow']
        self.drow=''
        self.word=''
        self.chudaonguoc=''
        self.diem=0
        self.show()

    def kt(self):

        if len(self.word) != 0:

            a=self.ui.lineEdit.text()
            if len(self.ui.lineEdit.text())!=0:
                if self.word==a:
                    self.ui.label_3.setText('Correct !')
                    self.word = random.choice(self.words)
                    # print(self.word)
                    self.drow = random.sample(self.word, len(self.word))
                    self.chudaonguoc = ''.join(self.drow)
                    self.ui.label.setText(self.chudaonguoc)
                    self.ui.lineEdit.clear()
                    self.ui.lineEdit.setFocus()
                    self.diem+=1
                    self.ui.label_2.setText(str(self.diem))
                else:
                    self.ui.label_3.setText('Incorrect !')

            else:
                self.ui.label_3.setText('fill in the blank !')
        else:
            self.ui.label_3.setText('button Start !')

    def start(self):
        self.word =''
        self.word = random.choice(self.words)
        # print(self.word)
        self.drow=random.sample(self.word,len(self.word))
        self.chudaonguoc=''.join(self.drow)
        self.ui.label.setText(self.chudaonguoc)
        self.ui.label_3.clear()
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setFocus()
    def reset(self):
        self.word = ''
        self.ui.label_3.clear()
        self.ui.label.clear()
        self.diem = 0
        self.ui.label_2.clear()
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setFocus()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = churandom()
    sys.exit(app.exec_())