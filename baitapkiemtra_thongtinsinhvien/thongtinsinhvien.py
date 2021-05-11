import sys
from PyQt5.QtWidgets import QDialog,QApplication,QTableWidgetItem
from PyQt5 import uic
class ktttsv():
    mssv = 0
    hotensv=''
    malop=''

    diemlythuyet=0
    diemthuchanh=0


    def __init__(self,mssv=0,hotensv='',malop='',diemlythuyet=0,diemthuchanh=0):
        self.hotensv=hotensv
        self.malop=malop
        self.mssv=mssv
        self.diemlythuyet=diemlythuyet
        self.diemthuchanh=diemthuchanh
    def prthoten(self):

            # if len(self.hotensv)!=0 and self.hotensv.isnumeric == False:
                return self.hotensv

    def prtmssv(self):

            # if len(self.mssv) != 0 and self.mssv.isnumeric()==True:
                return self.mssv

    def prtdth(self):

            # if len(self.diemthuchanh) != 0 and self.diemthuchanh.isnumeric()==True:
                return self.diemthuchanh

    def prtdlt(self):

            # if len(self.diemlythuyet) != 0 and self.diemlythuyet.isnumeric()==True:
                return self.diemlythuyet

    def prtmalop(self):
        return self.malop

    def prtdtb(self):
        try:
            lt=float(self.diemlythuyet)
            th=float(self.diemthuchanh)

            if 0 <= lt <= 10 and 0 <= th <= 10:
                return round(((lt+th) / 2) ,2)
            else:return 'nhập điểm sai !'

        except ValueError:
            return 'nhập sai!'

    def prtkq(self):


                # if float(self.diemthuchanh+self.diemlythuyet)>=10 :
                #     self.ketqua='Đậu'
                #     return self.ketqua
                # else:
                #     self.ketqua= 'rớt'
                #     return self.ketqua
        try:
            lt = float(self.diemlythuyet)
            th = float(self.diemthuchanh)

            if 0 <= lt <= 10 and 0 <= th <= 10:
                tc= round(((lt + th) / 2), 2)
                if tc>=5:
                    return 'đậu'
                else:return 'rớt'
            else:
                return 'nhập điểm sai !'
        except ValueError:
            return 'nhập sai!'






class ttsv(QDialog):
    def __init__(self):
        super(ttsv, self).__init__()
        self.ui = uic.loadUi('thongtinsinhvien.ui', self)
        self.ui.pushButton.clicked.connect(self.hienthi)
        self.ui.pushButton_2.clicked.connect(self.them)
        self.ui.pushButton_3.clicked.connect(self.clearne)
        self.bangthongtin=[]
        lstmalop=['CD22001','CD22002','CD22004','CD22005']
        for i in lstmalop:
            self.ui.comboBox.addItem(i)
        self.show()
    def hienthi(self):
        a=ktttsv(
                 diemlythuyet=(self.ui.lineEdit_4.text()),
                 diemthuchanh=(self.ui.lineEdit_5.text()))
        #mssv,hotensv,malop,diemlythuyet,diemthuchanh)

        dtb=a.prtdtb()
        kq=a.prtkq()
        # hvt=a.prthoten()
        # lop=a.prtmalop()
        # maso=a.prtmssv()
        # dlt=a.prtdlt()
        # dth=a.prtdth()



        self.ui.lineEdit_6.setText(str(dtb))
        self.ui.lineEdit_7.setText(str(kq))

    def them(self):
        ht=self.ui.lineEdit_2.text()
        lop=self.ui.comboBox.currentText()
        maso=self.ui.lineEdit.text()
        dlt=self.ui.lineEdit_4.text()
        dth=self.ui.lineEdit_5.text()
        tb=self.ui.lineEdit_6.text()
        kq=self.ui.lineEdit_7.text()

        sv=ktttsv(maso,ht,lop,dlt,dth)
        self.bangthongtin.append(sv.prtmssv())
        self.bangthongtin.append(sv.prthoten())
        self.bangthongtin.append(sv.prtmalop())
        self.bangthongtin.append(str(sv.prtdlt()))
        self.bangthongtin.append(str(sv.prtdth()))
        self.bangthongtin.append(str(sv.prtdtb()))
        self.bangthongtin.append(sv.prtkq())

        col = 0

        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(row + 1)
        print(self.bangthongtin)
        for item in self.bangthongtin:
            oneItem = QTableWidgetItem(item)
            self.ui.tableWidget.setItem(row, col, oneItem)
            col += 1

        self.bangthongtin=[]
    def clearne(self):
        self.bangthongtin=[]
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        self.ui.tableWidget.setRowCount(0)

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=ttsv()
    sys.exit(app.exec_())