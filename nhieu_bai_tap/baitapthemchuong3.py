import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
class baitapthem3(QDialog):
    def __init__(self):
        super(baitapthem3,self).__init__()
        self.ui = uic.loadUi('baitapthemchuong.ui',self)
        self.ui.comboBox.currentIndexChanged.connect(self.hienthi)
        self.ui.pushButton.clicked.connect(self.all)
        self.show()
        self.travel={
            'Hàn Quốc':100,
            'Nhật Bản':200,
            'Thái Lan':50,
            'Campuchia':50
        }
        self.img={
            'Hàn Quốc': 'hanquoc.jpg',
            'Nhật Bản': 'japan.jpg',
            'Thái Lan': 'thailan.jpg',
            'Campuchia': 'campuchia.jpg'
        }
        self.tienphong={
            'Hàn Quốc': 100,
            'Nhật Bản': 500,
            'Thái Lan': 100,
            'Campuchia': 100
        }
        tien = 0
        phong=0
        for i in self.travel:
            if self.ui.comboBox.currentText() == i:
                tien = self.travel[i]
                image = self.img[i]
                phong=self.tienphong[i]

        self.ui.label_10.setPixmap(QPixmap(image))
        self.ui.label_8.setText(str(tien))
        self.giaphong = int(phong) * int((self.ui.spinBox.value()))

    def hienthi(self):
        tien = 0
        phong=0
        for i in self.travel:
            if self.ui.comboBox.currentText() == i:
                tien = self.travel[i]
                image = self.img[i]
                phong = self.tienphong[i]

        self.ui.label_10.setPixmap(QPixmap(image))
        self.ui.label_8.setText(str(tien))

    def all(self):
        if len(self.ui.lineEdit.text())!=0 and self.ui.lineEdit.text().isnumeric()==False:
            self.ui.label_9.setText(
                'Khách hàng:{}\nNơi đi: {}\nSố ngày đi: {}\nSố người đi: {}'
                '\nNgày Khởi Hành: {}\nTổng tiền: {}'.format(self.ui.lineEdit.text(),
                                                            self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()),
                                                            str(self.ui.spinBox.value()),
                                                            str(self.ui.spinBox_2.value()),
                                                            self.ui.calendarWidget.selectedDate().toString('dd/MM/yy'),
                                                            str(
                                                                (int(self.ui.label_8.text()) * int((self.ui.spinBox.value())))* int(self.ui.spinBox_2.value())

                                                                )

                                                             ))
        else :
            self.ui.label_9.setText('Nhập tên !')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = baitapthem3()
    sys.exit(app.exec())
