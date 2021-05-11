import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class chuong3bai3(QDialog):
    def __init__(self):
        super(chuong3bai3,self).__init__()
        self.ui = uic.loadUi('chuong3bai3.ui',self)
        self.ui.pushButton.clicked.connect(self.hienthi)
        self.show()

    def hienthi(self):
        room={
            'Super Luxury':40,
            'Suite':30,
            'Super Deluve':20,
            'Ordinary':10
        }
        money=0
        self.ui.label.setText(self.ui.calendarWidget.selectedDate().toString('dd/MM/yy')+' Number of days: '
                              +str(self.ui.spinBox.value())+' and room type: '+ self.ui.comboBox.currentText())
        for i in room:
            if self.ui.comboBox.currentText()==i:
                money=room[i]
        self.ui.label_2.setText('Room Rent for single day for '+ self.ui.comboBox.currentText() +' is ' +str(money)+'\nTotal room is: '+str(self.ui.spinBox.value()*money))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = chuong3bai3()
    b.show()
    sys.exit(app.exec())

