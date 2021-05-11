import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
import random
from PyQt5.QtGui import QPixmap

class boituonlai(QDialog):
    def __init__(self):
        super(boituonlai, self).__init__()
        self.ui=uic.loadUi('tuonglai.ui',self)
        self.ui.pushButton.clicked.connect(self.hienthi)
        self.show()
        self.socan={
            0:'canh',
            1:'tan',
            2:'nham',
            3:'quy',
            4:'giap',
            5:'at',
            6:'binh',
            7:'dinh',
            8:'mau',
            9:'ky'
        }
        self.chi={
            0: 'than',
            1: 'dau',
            2: 'tuat',
            3: 'hoi',
            4: 'ty',
            5: 'suu',
            6: 'dan',
            7: 'meo',
            8: 'thin',
            9: 'ty',
            10:'ngo',
            11:'mui'
        }
        self.hinh = {
            0: '12congiap/than.jpg',
            1: '12congiap/u.jpg',
            2: '12congiap/tuat.jpg',
            3: '12congiap/hoi.jpg',
            4: '12congiap/ty.jpg',
            5: '12congiap/suu.jpg',
            6: '12congiap/dan.jpg',
            7: '12congiap/mao.jpg',
            8: '12congiap/thin.jpg',
            9: '12congiap/ran.jpg',
            10: '12congiap/gno.jpg',
            11: '12congiap/mui.jpg'
        }
        self.lstchuc=['Hành trình sống của con người phụ thuộc vào quá khứ, hiện tại và tương lai.\n Nếu hiện tại có thể biết thì quá khứ đã đi qua\n không thể níu kéo và tương lai chưa tới lại càng không thể nắm bắt.\n Bởi quá khứ đã rơi vào quên lãng nên ta không thể trở với nó,\n còn tương lại thì chưa tới nên cũng sẽ không biết nó xảy ra.',
              'Dòng thời gian cứ trôi không ngừng nghỉ. \nCuộc sống cứ bám chặt lấy thời gian mà tồn tại.\n Ngày nào thời gian đứng lại thì ngày đó cuộc sống tiêu tan. \nHiện hữu của con người cũng vậy, một đời người so với vòng quay của thời gian chẳng đáng chi,\n một kiếp nhân sinh so với dòng chảy của cuộc sống có nghĩa gì',
                      ' Đừng đếm những gì bạn đã mất,\n hãy quý trọng những gì bạn đang có và lên kế hoạch \n cho những gì sẽ đạt được bởi quá khứ không bao giờ trở lại,\n nhưng tương lai có thể bù đắp cho mất mát.',
                      'Tương lai có rất nhiều tên: \nVới kẻ yếu, nó là Điều không thể đạt được.\n Đối với người hay sợ hãi, nó là Điều chưa biết.\n Với ai dũng cảm, nó là Cơ hội.',
                'Tương lai của bạn phụ thuộc vào rất nhiều điều,\n nhưng chủ yếu là vào bạn.',
                      'Sự kiên nhẫn của ngày hôm nay có thể\n biến những nản lòng của ngày hôm qua thành khám phá của ngày mai.\n Những mục đích của ngày hôm nay có thể biến những thất bại \ncủa ngày hôm qua thành quyết tâm của ngày mai.']
        self.hinhne=''

    def hienthi(self):
        if len(self.ui.lineEdit.text()) != 0 :

            n = self.ui.dateEdit.date().year()
            can = n % 10
            chi = n % 12
            tc = ''
            tchi = ''
            for i in self.socan:
                if can == i:
                    tc = self.socan[i]
            for i in self.chi:
                if chi == i:
                    tchi = self.chi[i]
                    self.hinhne = self.hinh[i]
            a=random.choice(self.lstchuc)
            print(a)
            self.ui.label_4.setPixmap(QPixmap(self.hinhne))
            self.ui.label_5.setText('Tên: '+str(self.ui.lineEdit.text())+'\n'+
                tc + ' ' + tchi+' \n'+
                                    'Tương lai: '+
                        str(a)
                                    )

        else:
            self.ui.lineEdit.setText('')
            self.ui.lineEdit.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = boituonlai()
    sys.exit(app.exec())
