import sys
from PyQt5.QtWidgets import QDialog,QApplication,QInputDialog,QListWidgetItem
from PyQt5 import uic
class ApplyWindow(QDialog):
    def __init__(self):
        super(ApplyWindow,self).__init__()
        self.ui=uic.loadUi('baitapthem7.ui',self)
        self.ui.pushButton.clicked.connect(self.thongke)
        self.ui.pushButton_2.clicked.connect(self.removeitemdangchon)
        self.ui.pushButton_3.clicked.connect(self.removealldachon)
        self.ui.pushButton_4.clicked.connect(self.removeall)
        self.dangchon=[]
        self.ui.checkBox.stateChanged.connect(lambda: self.additem('1'))
        self.ui.checkBox_2.stateChanged.connect(lambda: self.additem('2'))
        self.ui.checkBox_3.stateChanged.connect(lambda: self.additem('3'))
        self.ui.checkBox_4.stateChanged.connect(lambda: self.additem('4'))
        self.ui.checkBox_5.stateChanged.connect(lambda: self.additem('5'))
        self.ui.checkBox_6.stateChanged.connect(lambda: self.additem('6'))
        self.ui.checkBox_7.stateChanged.connect(lambda: self.additem('7'))
        self.ui.checkBox_8.stateChanged.connect(lambda: self.additem('8'))
        self.ui.checkBox_9.stateChanged.connect(lambda: self.additem('9'))
        self.ui.checkBox_10.stateChanged.connect(lambda: self.additem('10'))
        self.ui.checkBox_11.stateChanged.connect(lambda: self.additem('11'))
        self.ui.checkBox_12.stateChanged.connect(lambda: self.additem('12'))
        self.ui.checkBox_13.stateChanged.connect(lambda: self.additem('13'))
        self.ui.checkBox_14.stateChanged.connect(lambda: self.additem('14'))
        self.ui.checkBox_15.stateChanged.connect(lambda: self.additem('15'))

        self.show()
    def thongke(self):
        self.dachon=[]
        for i in self.dangchon:
            if i not in self.dachon:
                self.dachon.append(i)
                self.ui.listWidget.addItem(i)
    def removeall(self):
        self.removeitemdangchon()
        self.removealldachon()
    def removeitemdangchon(self):
        self.ui.listWidget_2.clear()
        self.ui.checkBox.setChecked(False)
        self.ui.checkBox_2.setChecked(False)
        self.ui.checkBox_3.setChecked(False)
        self.ui.checkBox_4.setChecked(False)
        self.ui.checkBox_5.setChecked(False)
        self.ui.checkBox_6.setChecked(False)
        self.ui.checkBox_7.setChecked(False)
        self.ui.checkBox_8.setChecked(False)
        self.ui.checkBox_9.setChecked(False)
        self.ui.checkBox_10.setChecked(False)
        self.ui.checkBox_11.setChecked(False)
        self.ui.checkBox_12.setChecked(False)
        self.ui.checkBox_13.setChecked(False)
        self.ui.checkBox_14.setChecked(False)
        self.ui.checkBox_15.setChecked(False)
        self.dangchon=[]
    def removealldachon(self):
        self.ui.listWidget.clear()
        #takeItem=remove
    def additem(self,i):
        if i not in self.dangchon:
            self.dangchon.append(i)
            self.hienthi()
        else:
            self.dangchon.remove(i)
            self.hienthi()
    def hienthi(self):
        self.ui.listWidget_2.clear()
        for y in self.dangchon:
            self.ui.listWidget_2.addItem(y)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=ApplyWindow()
    sys.exit(app.exec_())