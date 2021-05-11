import sys
from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow,QFileDialog
from PyQt5 import uic
class openfile(QMainWindow):
    def __init__(self):
        super(openfile, self).__init__()
        self.ui = uic.loadUi('hopthoatopenfile.ui', self)
        self.ui.actionOpen.triggered.connect(self.openfile)
        self.ui.actionCopy.triggered.connect(self.openfile)
        self.ui.actionPast.triggered.connect(self.openfile)
        self.ui.actionSave.triggered.connect(self.Savefile)
        self.show()
    def openfile(self):
        fname=QFileDialog.getOpenFileName(self,'Open file','/home')

        if fname[0]:
            f=open(fname[0],'r')
            with f:
                data=f.read()
                self.ui.textEdit.setText(data)
    def Savefile(self):
        options=QFileDialog.Options()
        options|=QFileDialog.DontUseNativeDialog
        filename,_=QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName","","All file(*);;Text Files(*.txt)",options=options)
        f=open(filename,'w')
        text=self.ui.textEdit.toPlainText()
        f.write(text)
        f.close()


if __name__=="__main__":
    app=QApplication(sys.argv)
    window=openfile()
    sys.exit(app.exec_())