import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
class hoadon():
    def __init__(self,name='',somay='',giovao=0,giora=0,tienkhac=0):
        self.name=name
        self.somay=somay
        self.giovao=giovao
        self.giora=giora
        self.tienkhac=tienkhac
    def rt_name(self):
        return self.name
    def rt_somay(self):
        return self.somay
    def rt_giovao(self):
        return self.giovao
    def rt_giora(self):
        return self.giora
    def tinhtienchoi(self):
        total=0
        self.giora=int(self.giora)
        self.giovao=int(self.giovao)
        if self.giora > self.giovao:
            a=self.giora-self.giovao
            if a<=1:
                total=8
            elif a<=3:
                total=8+((a-1)*7)
            else:
                total=8+14+((a-3)*5)
            return total
        else:
            return 'nhap sai!'
    def alltotal(self,x):
        self.tienkhac=int(self.tienkhac)
        c = x+self.tienkhac
        return c


class ApplyWindow(QDialog):
    def __init__(self):
        super(ApplyWindow,self).__init__()
        self.ui=uic.loadUi('quannet.ui',self)
        self.ui.pushButton.clicked.connect(self.tt)
        self.ui.pushButton_2.clicked.connect(self.showall)
        self.show()


    def tt(self):
        ten = self.ui.lineEdit.text()
        somay = self.ui.lineEdit_2.text()
        giovao = self.ui.lineEdit_3.text()
        giora = self.ui.lineEdit_4.text()
        tienkhac = self.ui.lineEdit_6.text()

        qln = hoadon(ten, somay, giovao, giora, tienkhac)
        x=qln.tinhtienchoi()
        self.ui.lineEdit_5.setText(str(x))
    def showall(self):
        ten = self.ui.lineEdit.text()
        somay = self.ui.lineEdit_2.text()
        giovao = self.ui.lineEdit_3.text()
        giora = self.ui.lineEdit_4.text()
        tienkhac = self.ui.lineEdit_6.text()
        qln = hoadon(ten, somay, giovao, giora, tienkhac)
        xx=qln.alltotal(int(self.ui.lineEdit_5.text()))
        ten=qln.rt_name()
        gv=qln.rt_giovao()
        gr=qln.rt_giora()
        sm=qln.rt_somay()
        self.ui.lineEdit_7.setText(str(xx))
        self.ui.label_7.setText(str(ten)+'\n gio vao:'+str(gv)
                              + '\n gio ra:' + str(gr)
                              + '\n so may:' + str(sm)
                              + '\n tong cong:' + str(xx)

        )


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=ApplyWindow()
    sys.exit(app.exec_())




