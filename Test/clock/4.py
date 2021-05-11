from PyQt5.QtWidgets import*
from PyQt5 import QtCore, QtGui,uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
# tạo một lớp đồng hồ
class Clock(QDialog):
    # Hàm tạo
    def __init__(self):
        super(Clock,self).__init__()
        # tạo một đối tượng hẹn giờ
        self.ui = uic.loadUi('bai4.ui', self)
        timer = QTimer(self)
        # thêm hành động vào bộ hẹn giờ0
        # cập nhật toàn bộ mã
        timer.timeout.connect(self.update)
        # cài đặt thời gian bắt đầu của bộ hẹn 4giờ
        timer.start(1000)
        # thiết lập hình học cửa sổ
        self.setGeometry(240,240,240,240)
        # đặt màu nền cho cửa sổ
        self.setStyleSheet("background : url(44.jpg);")

        # tạo kim giờ
        self.hPointer = QtGui.QPolygon([QPoint(6, 7),
                                        QPoint(-6, 7),
                                        QPoint(0, -50)])
        # tạo kim phút
        self.mPointer = QPolygon([QPoint(6, 7),
                                  QPoint(-6, 7),
                                  QPoint(0, -70)])
        # tạo kim giây
        self.sPointer = QPolygon([QPoint(1, 1),
                                  QPoint(-1, 1),
                                  QPoint(0, -90)])
        # màu cho kim phút và kim giờ
        self.bColor = Qt.white
        # màu cho kim giâylabel
        self.sColor = Qt.red
        # self.ui.label.setPixmap(QPixmap("44.jpg"))
        # phương pháp cho sự kiện sơnlabel
        self.show()
    def paintEvent(self, event):
        tik = QTime.currentTime()
        painter = QPainter(self)
        def drawPointer(color, rotation, pointer):
            # thiết lập kim

            painter.setBrush(QBrush(color))
            painter.save()
            painter.rotate(rotation)
            painter.drawConvexPolygon(pointer)
            painter.restore()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(QtCore.Qt.NoPen)
        drawPointer(self.bColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
        drawPointer(self.bColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
        drawPointer(self.sColor, (6 * tik.second()), self.sPointer)
        # Vạch phút
        painter.setPen(QPen(self.bColor))
        for i in range(0, 60):
            # vẽ đường nền
            if (i % 5) == 0:
                painter.drawLine(87, 0, 97, 0)
            painter.rotate(1)
        painter.end()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Clock()
    win.show()
    exit(app.exec_())