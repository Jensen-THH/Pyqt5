import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
import random
class churandom(QDialog):
    def __init__(self):
        super(churandom, self).__init__()
        self.ui=uic.loadUi('xepchu2player.ui',self)
        self.ui.pushButton.clicked.connect(self.kt)
        self.ui.pushButton_2.clicked.connect(self.start)
        self.ui.pushButton_3.clicked.connect(self.reset)
        self.words=['red','green','blue','yellow']
        self.drow=''
        self.word=''
        self.chudaonguoc=''
        self.diem1=0
        self.diem2=0
        self.nguoichoi=0
        self.show()
    def nguoichoine(self):
        if self.nguoichoi==0:
            self.nguoichoi=1
        else:
            self.nguoichoi=0
    # tính điểm:
    def tinhdiemne(self):
        self.nguoichoine()
        if self.nguoichoi==0:
            self.diem1 += 1
            self.ui.label_2.setText(str(self.diem1))
        if self.nguoichoi==1:
            self.diem2+=1
            self.ui.label_6.setText(str(self.diem2))
    def tinhdiemtraloisai(self):
        self.nguoichoine()
        if self.nguoichoi == 0:
            self.diem1 -= 1
            self.ui.label_2.setText(str(self.diem1))
        if self.nguoichoi == 1:
            self.diem2 -= 1
            self.ui.label_6.setText(str(self.diem2))

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
                    self.tinhdiemne()
                    self.ui.lineEdit.clear()
                    self.ui.lineEdit.setFocus()

                else:
                    self.ui.label_3.setText('Incorrect !')
                    self.tinhdiemtraloisai()
                    self.ui.lineEdit.clear()
                    self.ui.lineEdit.setFocus()

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