import sys
import PyQt5.QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from PyQt5 import uic
# from PyQt5_GUI.BaiTapLamThem.Caro.BaiTap04.c_Caro
from tranhohiep.baitapcaro.carone import c_Caro
# from Caro.BaiTap04.c_Caro import c_Caro

class App_Caro(QDialog):
    """Xây dựng chương trình Caro."""
    def __init__(self):
        """Khoi tao."""
        super(App_Caro, self).__init__()
        self.ui = uic.loadUi("App_Caro.ui", self)

        ROW = 200
        COLUMN = 200
        self.ui.tableWidget.setRowCount(ROW)
        self.ui.tableWidget.setColumnCount(COLUMN)
        for i in range(COLUMN):
            self.ui.tableWidget.setColumnWidth(i, 1)

        #Khi click vào table kết nối đến hàm xử lý.
        self.ui.tableWidget.clicked.connect(self.process)
        self.count = 0
        #Khỏi tạo bàn cờ Caro
        self.caro = c_Caro(ROW, COLUMN)

    def process(self):
        #Xác định ô đang được chọn trên table
        selected_cell = self.ui.tableWidget.selectedIndexes()
        if len(selected_cell) > 0:
            row = selected_cell[0].row()
            column = selected_cell[0].column()
            if self.count % 2 == 0:
                player = 1
                marker = '    X'
            else:
                player = 2
                marker = '    O'
            self.count += 1

            #Đánh dấu lên bàn cờ caro (ma trận trong c_caro)
            self.caro.mark(player, row, column)
            # Danh dau lên table.
            item = QTableWidgetItem(marker)
            self.ui.tableWidget.setItem(row, column, item)
            # Vo hieu hoa o da danh dau.
            item.setFlags(PyQt5.QtCore.Qt.NoItemFlags)

            # Kiem tra thang.
            if self.caro.isWinner(player, row, column)==True:
                self.ui.tableWidget.setEnabled(False)
                self.ui.win_label.setText('The winner is Player %d' % player)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Caro = App_Caro()
    Caro.show()
    sys.exit(app.exec_())