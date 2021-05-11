import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic,QtCore
from datetime import *
class chuong3bai1(QDialog):
    def __init__(self):
        super(chuong3bai1,self).__init__()
        self.ui = uic.loadUi('lichvannien.ui',self)
        time= QtCore.QTimer(self)
        time.start(1000)
        time.timeout.connect(self.hienthi)
        self.hienthi()
        self.hienthingaytn()
        self.show()



        self.hinh = {
            0: './huongdoituong/12congiap/than.jpg',
            1: './huongdoituong/12congiap/u.jpg',
            2: './huongdoituong/12congiap/tuat.jpg',
            3: './huongdoituong/12congiap/hoi.jpg',
            4: './huongdoituong/12congiap/ty.jpg',
            5: './huongdoituong/12congiap/suu.jpg',
            6: './huongdoituong/12congiap/dan.jpg',
            7: './huongdoituong/12congiap/mao.jpg',
            8: './huongdoituong/12congiap/thin.jpg',
            9: './huongdoituong/12congiap/ran.jpg',
            10: './huongdoituong/12congiap/gno.jpg',
            11: './huongdoituong/12congiap/mui.jpg'
        }
    def hienthi(self):
        time=QtCore.QTime.currentTime()
        text=time.toString('hh:mm:ss')
        self.ui.clock.display(text)
    def hienthingaytn(self):
        today=date.today()
        ngay=today.day
        thang=today.month
        thu=today.weekday()
        nam=today.year
        self.ui.label.setText('Tháng: '+str(thang))
        self.ui.label_2.setText(str(nam))
        self.ui.label_3.setText('Ngày: ' + str(ngay))

        self.ui.label_8.setText( str(ngay))
        lstthu={0:'Thứ hai',1:'Thứ ba',2:'Thứ tư',3:'Thứ năm',4:'Thứ sáu',5:'Thứ bảy',6:'Chủ nhật'}
        lstthuen=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        self.ui.label_9.setText(lstthuen[thu])
        for i in lstthu:
            if i==thu:
                td=lstthu[i]
                self.ui.label_5.setText(str(td))
###################################################
        n=int(self.ui.label_2.text())

        can = n % 10
        schi = n % 12
        tc = ''
        tchi = ''
        socan = {0: 'Canh', 1: 'Tân', 2: 'Nhâm', 3: 'Quý', 4: 'Giáp', 5: 'Ất', 6: 'Binh', 7: 'Đinh', 8: 'Mậu', 9: 'Kỷ'}
        for i in socan:
            if can == i:
                tc = socan[i]

        chi = {0: 'Thân', 1: 'Dậu', 2: 'Tuất', 3: 'Hợi', 4: 'Tý', 5: 'Sửu', 6: 'Dần', 7: 'Mẹo', 8: 'Thìn', 9: 'Tị',
               10: 'Ngọ', 11: 'Mùi'}
        for i in chi:
            if schi == i:
                tchi = chi[i]

        self.ui.label_7.setText('Năm: '+tc + ' ' + tchi)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = chuong3bai1()
    b.show()
    sys.exit(app.exec())
