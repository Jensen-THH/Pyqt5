import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
from datetime import date,timedelta
from PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QPixmap
class thongtin():
    ten=''
    ngaysinh=''
    diachi=''
    diadiemdi=''
    diadiemden=''
    ngaydi=''
    ngayve=''
    ngaysinh1=''
    def __init__(self,ten,ngaysinh,ngaysinh1,diachi,diadiemdi,diadiemden,ngaydi,ngayve):
        self.ten=ten
        self.ngaysinh=ngaysinh
        self.ngaysinh1=ngaysinh1
        self.diachi=diachi
        self.diadiemdi=diadiemdi
        self.diadiemden=diadiemden
        self.ngaydi=ngaydi
        self.ngayve=ngayve
        self.noidi={
            'HCM':[5000000,300000,20000000,7000000],
            'Hà Nội':[4000000,200000,19000000,6000000],
            'Vũng Tàu': [6000000, 400000, 22000000, 85000000]
        }
        self.img={
            'Hàn Quốc': 'HanQuoc.jpg',
            'Thái Lan': 'ThaiLan.jpg',
            'Nhật': 'NhatBan.jpg',
            'Úc ':'Uc.jpg'
        }
    def printten(self):
        return self.ten
    def printngaysinh(self):
        return self.ngaysinh
    def age(self):
        today=date.today()
        ngaysinh=self.ngaysinh
        age = today - ngaysinh
        return age
    def printdiachi(self):
        return self.diachi
    def printdi(self):
        return self.diadiemdi
    def printden(self):
        return self.diadiemden
    def printngaydi(self):
        ngaydi=self.ngaydi
        ngaydi=ngaydi.toString('dd/MM/yyyy')
        return ngaydi
    def printngayve(self):
        ngayve = self.ngayve
        ngayve = ngayve.toString('dd/MM/yyyy')
        return ngayve
    def totalmoney(self):
        n=self.diadiemdi
        for i in self.noidi:
            if i == n:
                if self.diadiemden =='Hàn Quốc':
                    return self.noidi[i][0]
                if self.diadiemden =='Thái Lan':
                    return self.noidi[i][1]
                if self.diadiemden =='Úc ':
                    return self.noidi[i][2]
                if self.diadiemden =='Nhật':
                    return self.noidi[i][3]
    def hinh(self):
        n=self.diadiemden
        for i in self.img:
            if i == n:
                return self.img[i]
    def tuoi(self):
        b = QDateTime.currentDateTime()
        ngaysinh = self.ngaysinh1
        yearnow = int(b.toString("yyyy"))
        a = int(ngaysinh.toString('yyyy'))
        age = yearnow - a
        return age
    def totalday(self):
        now = self.ngaydi
        diff = self.ngayve
        totalday = now.daysTo(diff)
        return totalday
class ApplyWindow(QDialog):
    def __init__(self):
        super(ApplyWindow,self).__init__()
        self.ui=uic.loadUi('kiemtra.ui',self)
        self.ui.pushButton.clicked.connect(self.hienthi)
        self.ui.pushButton_2.clicked.connect(self.xoa)
        self.ui.comboBox_2.activated.connect(self.hienthi1)
        self.ui.comboBox_2.activated.connect(self.hienthi)
        self.ui.comboBox.activated.connect(self.hienthi)
        self.ui.label_8.setPixmap(QPixmap('HanQuoc.jpg'))
        today = date.today()
        self.ui.dateEdit_2.setDate(today)
        self.ui.dateEdit_3.setDate(today +timedelta(1))
        self.img={
            'Hàn Quốc': 'HanQuoc.jpg',
            'Thái Lan': 'ThaiLan.jpg',
            'Nhật': 'NhatBan.jpg',
            'Úc ':'Uc.jpg'
        }
        self.show()
    def hienthi(self):
        if len(self.ui.lineEdit.text())!=0 and len(self.ui.lineEdit_2.text())!=0:
            now = self.ui.dateEdit_2.date()
            diff =self.ui.dateEdit_3.date()
            totalday = now.daysTo(diff)
            if self.ui.dateEdit.text() != self.ui.dateEdit_2.text() and self.ui.dateEdit.text() != self.ui.dateEdit_3.text() and self.ui.dateEdit_2.text() != self.ui.dateEdit_3.text() and totalday>0 :
                khachhang=thongtin(self.ui.lineEdit.text(),self.ui.dateEdit.text(),self.ui.dateEdit.date(),self.ui.lineEdit_2.text(),self.ui.comboBox.currentText(),self.ui.comboBox_2.currentText(),self.ui.dateEdit_2.date(),self.ui.dateEdit_3.date())
                self.ui.label_8.setPixmap(QPixmap(khachhang.hinh()))
                self.ui.label_9.setText('Tên: ' + khachhang.printten()+'\nNgày sinh: ' + str(khachhang.printngaysinh())+' Tuổi '+str(khachhang.tuoi()) +'\nĐịa chỉ: '+ khachhang.printdiachi()+'\nĐi: ' + khachhang.diadiemdi+ ' - ' + khachhang.diadiemden +'\nNgày đi: '+ str(khachhang.printngaydi())+'\nNgày về: '+str(khachhang.printngayve())+'\nTổng tiền: ' + str(khachhang.totalmoney()*totalday))
                self.ui.label_10.setText('Tổng số ngày đi: '  +str(khachhang.totalday()))
            else: self.ui.label_9.setText('Nhập sai về ngày')
        else:
            self.ui.label_9.setText('Nhập đầy đủ thông tin')
    def xoa(self):
        self.ui.lineEdit.setText('')
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit_2.setText('')
        self.ui.label_9.setText('')
        self.ui.label_10.setText('')
    def hienthi1(self):
        for i in self.img:
            if self.ui.comboBox_2.currentText() == i:
                self.ui.label_8.setPixmap(QPixmap(self.img[i]))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=ApplyWindow()
    sys.exit(app.exec_())