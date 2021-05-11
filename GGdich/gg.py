import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic

#--------#
from googletrans import Translator
import googletrans
import os
#---am thanh---#
import pyaudio
from gtts import gTTS
import playsound

#-------giong noi-------#
import speech_recognition
import pyttsx3

#-----------hinh anh-----#
from PIL import Image
import pytesseract
from time import sleep

class ggdich(QDialog):
    def __init__(self):
        super(ggdich,self).__init__()
        self.ui = uic.loadUi('ggdichtest.ui',self)
        #ghi am
        self.ui.pushButton_2.clicked.connect(self.ghiam)
        self.ui.pushButton_3.clicked.connect(self.noi1)
        self.ui.pushButton.clicked.connect(self.dich)
        self.show()

    # ghi am giong noi
    def ghiam(self):
        hear = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as mic:
            hear.adjust_for_ambient_noise(mic)
            ai = "đang nghe"
            output = gTTS(ai, lang="vi", slow=False)
            output.save("fileghiam.mp3")
            playsound.playsound('fileghiam.mp3')
            os.remove('fileghiam.mp3')
            audio = hear.record(mic, duration=5)

        try:
            you = hear.recognize_google(audio, language="vi-VN")
        except:
            you = ""
        self.ui.lineEdit.setText(str(you))
        #---noi----#
    def noi1(self):
        ai = self.ui.lineEdit.text()
        if ai != "":
            output = gTTS(ai, lang="en", slow=False)
            output.save("fileghiamnoi.mp3")
            playsound.playsound('fileghiamnoi.mp3')
            os.remove('fileghiamnoi.mp3')
        else:
            ai = "không có dữ liệu"
            output = gTTS(ai, lang="vi", slow=False)
            output.save("fileghiamnoi.mp3")
            playsound.playsound('fileghiamnoi.mp3')
            os.remove('fileghiamnoi.mp3')
        #-----dich-----#
    def dich(self):
        self.ui.lineEdit_2.setText('')
        datas = str(self.ui.lineEdit.text())
        trans = Translator()

        result = trans.translate(datas, scr="en", dest="vi")
        a=result.text
        print(a)
        return  self.ui.lineEdit_2.setText(str(a))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowa = ggdich()
    sys.exit(app.exec_())
