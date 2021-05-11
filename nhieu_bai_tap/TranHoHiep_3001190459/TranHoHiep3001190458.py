import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from datetime import date
class travel():
    name=''
    age=0
    diachi=''
    daybegin=''
    dayback=''
    diadiemdi=''
    diadiemden=''
    def __init__(self,name,age,diachi,daybegin,dayback,diadiemdi,diadiemden):
        self.name=name
        self.age=age
        self.diachi=diachi
        self.dayback=dayback
        self.daybegin=daybegin
        self.diadiemdi=diadiemdi
        self.diadiemden=diadiemden

    def showName(self):
        return self.name
    def showAge(self):
        return self.age
    def showDiachi(self):
        return self.diachi
    def showBegin(self):
        return self.daybegin
    def showBack(self):
        return self.dayback

    def showdiadiemdi(self):
        return self.diadiemdi
    def showdiadiemden(self):
        return self.diadiemden

class baikt(QDialog):
    def __init__(self):
        super(baikt, self).__init__()
        self.ui = uic.loadUi('baikiemtra.ui', self)
        self.ui.comboBox_2.currentIndexChanged.connect(self.showImg)
        self.ui.pushButton.clicked.connect(self.showAll)
        self.ui.dateEdit_2.setDate(date.today())
        self.ui.dateEdit_3.setDate(date.today())

        self.ui.pushButton_2.clicked.connect(self.clearAll)
        self.show()
        self.tv=0
        self.travels = {
            'Hồ Chí Minh':[5000000,300000,20000000,7000000],
            'Hà Nội':[4000000,200000,19000000,6000000],
            'Vũng Tàu': [6000000, 400000, 22000000, 85000000]
        }
        # self.travels = {
        #     'Hàn Quốc':100,
        #     'Nhật Bản': 200,
        #     'Thái Lan': 300,
        #     'Campuchia': 400
        # }
        self.img = {
            'Hàn Quốc': 'hanquoc.jpg',
            'Nhật Bản': 'japan.jpg',
            'Thái Lan': 'thailan.jpg',
            'Campuchia': 'campuchia.jpg'
        }


        for i in self.img:
            if self.ui.comboBox_2.currentText() == i:
                images = self.img[i]

        self.ui.label_11.setPixmap(QPixmap(images))
    #hiển thị hình
    def showImg(self):
        for i in self.img:
            if self.ui.comboBox_2.currentText() == i:
                images = self.img[i]
        self.ui.label_11.setPixmap(QPixmap(images))
    #hien thi
    def showAll(self):
        for i in self.travels:
            if self.ui.comboBox.currentText() == i:
                if self.ui.comboBox_2.currentText()=='Hàn Quốc':
                    self.tv = self.travels[i][0]
                if self.ui.comboBox_2.currentText() == 'Nhật Bản':
                    self.tv = self.travels[i][1]
                if self.ui.comboBox_2.currentText() == 'Thái Lan':
                    self.tv = self.travels[i][2]
                if self.ui.comboBox_2.currentText() == 'Campuchia':
                    self.tv = self.travels[i][3]

        # print(str(int(date.today().year)-int(self.ui.dateEdit.date().year())))
        hienthi=travel(
                   self.ui.lineEdit.text(),
                   int(date.today().year)-int(self.ui.dateEdit.date().year()),
                   self.ui.lineEdit_2.text(),
                   str(self.ui.dateEdit_2.text()),
                   str(self.ui.dateEdit_3.text()),
                   self.ui.comboBox.currentText(),
                   self.ui.comboBox_2.currentText(),
                 )
        ten=hienthi.showName()
        tuoi=hienthi.showAge()
        diachila=hienthi.showDiachi()
        ngaydi=hienthi.showBegin()
        ngayve=hienthi.showBack()
        diadiemdi=hienthi.showdiadiemdi()
        diadiemden=hienthi.showdiadiemden()

        if len(self.ui.lineEdit.text()) != 0 and self.ui.lineEdit.text().isnumeric() == False and len(self.ui.lineEdit_2.text()) != 0 and self.ui.lineEdit_2.text().isnumeric() == False:
            self.ui.label_10.setText(
                                     'Tên: '+ten+'\nTuổi '+str(tuoi)+'\nĐịa Chỉ: '
                                     +diachila+'\nNgày đi: '+ngaydi+'\nNgày về: '+ngayve
                                     +'\n\nTừ: '+diadiemdi+' tới '+diadiemden
                                        +'\nTổng tiền: '+str(int(self.tv)*(int(self.ui.dateEdit_3.date().day())-int(self.ui.dateEdit_2.date().day())))
                                        )
            if self.ui.dateEdit_3.date()>self.ui.dateEdit_2.date():
                snd = int(self.ui.dateEdit_3.date().day()) - int(self.ui.dateEdit_2.date().day())
                self.ui.label_9.setText('TỔNG SỐ NGÀY ĐI:'+str(snd))

            else:
                self.ui.label_9.setText('Thời gian đi ít nhất là 1 ngày')
                self.ui.label_10.setText(' ')
        else:
            self.ui.label_10.setText('Xin mời nhập đầy đủ thông tin !')
            self.ui.lineEdit.setFocus()
    def clearAll(self):
        self.ui.label_9.setText('')
        self.ui.label_10.setText('')
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit.setText('')
        self.ui.lineEdit.setFocus()
        self.tv = 0
if __name__=="__main__":
    app=QApplication(sys.argv)
    windowa=baikt()
    sys.exit(app.exec_())