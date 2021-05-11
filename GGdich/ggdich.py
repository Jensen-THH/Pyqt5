from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as menu
from googletrans import Translator
import googletrans
from tkinter.filedialog import askopenfilename
import pyaudio
from gtts import gTTS
import playsound
import webbrowser as web
import os
import speech_recognition
from PIL import Image
import pytesseract
from time import sleep
#mo file txt
def openf():
    openfile = Tk()
    openfile.withdraw()
    filename = askopenfilename()
    filename = str(filename)
    if ".txt" not in filename:
    	messagebox.showinfo("CHÚ Ý", "File TÀI LIỆU phải là file đuôi .TXT")
    else:
    	return filename
#doc file txt
def docfiletext():
	file = open(openf())
	data=file.read()
	file.close()
	return data

#in chu txt
def innhapdltxt():
    nhapdl.delete(0,END)
    nhapdl.insert(0,docfiletext())
    return
#ghi am giong noi
def ghiam():
	hear= speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		hear.adjust_for_ambient_noise(mic)
		ai= "đang nghe"
		output = gTTS(ai,lang="vi", slow=False)
		output.save("fileghiam.mp3")
		playsound.playsound('fileghiam.mp3')
		os.remove('fileghiam.mp3')
		audio = hear.record(mic,duration=3)
	try:
		you= hear.recognize_google(audio,language="vi-VN")
	except:
		you=""
	return you
#in chu nhap du lieu
def inchunhapdl():
    nhapdl.delete(0,END)
    nhapdl.insert(0,ghiam())
    return
def ggdich(nn1,nn2):
	data = nhapdl.get()
	trans = Translator()
	text = data
	result= trans.translate(text, scr= nn1, dest= nn2)
	xuat = result.text
	return xuat
def chonngonngu():
    vallang1 =mn1.get()
    vallang2 = mn2.get()
    #get vallang1
    if vallang1 == lang1[0]:
    	nn1 = "en"
    elif vallang1 == lang1[1]:
       	nn1 = "vi" 
    elif vallang1 == lang1[2]:
        nn1 = "ja" 
    elif vallang1 ==lang1[3]:
        nn1 = "ko" 
    elif vallang1 == lang1[4]:
        nn1 = "zh-cn" 
    elif vallang1 == lang1[5]:
        nn1 = "ca" 
    elif vallang1 == lang1[6]:
        nn1 = "fr" 
    else:
        nn1 = "th"
    #get vallang2
    if vallang2 == lang2[0]:
    	nn2 = "en"
    elif vallang2 == lang2[1]:
       	nn2 = "vi" 
    elif vallang2 == lang2[2]:
        nn2 = "ja" 
    elif vallang2 ==lang2[3]:
        nn2 = "ko" 
    elif vallang2 == lang2[4]:
        nn2 = "zh-cn" 
    elif vallang2 == lang2[5]:
        nn2 = "ca" 
    elif vallang2 == lang2[6]:
        nn2 = "fr" 
    else:
        nn2 = "th"
    ggdich(nn1,nn2)
    def inchuxuatdl():
    	xuatchu.delete(0,END)
    	xuatchu.insert(0,ggdich(nn1,nn2))
    	return
    inchuxuatdl()
#return ngon ngu 1
def returnnn1():
    vallang1 =mn1.get()
    #get vallang1
    if vallang1 == lang1[0]:
    	nn1 = "en"
    elif vallang1 == lang1[1]:
       	nn1 = "vi" 
    elif vallang1 == lang1[2]:
        nn1 = "ja" 
    elif vallang1 ==lang1[3]:
        nn1 = "ko" 
    elif vallang1 == lang1[4]:
        nn1 = "zh-cn" 
    elif vallang1 == lang1[5]:
        nn1 = "ca" 
    elif vallang1 == lang1[6]:
        nn1 = "fr" 
    else:
        nn1 = "th"
    return nn1
#return ngon ngu 2
def returnnn2():
    vallang2 = mn2.get()
    #get vallang2
    if vallang2 == lang2[0]:
    	nn2 = "en"
    elif vallang2 == lang2[1]:
       	nn2 = "vi" 
    elif vallang2 == lang2[2]:
        nn2 = "ja" 
    elif vallang2 ==lang2[3]:
        nn2 = "ko" 
    elif vallang2 == lang2[4]:
        nn2 = "zh-cn" 
    elif vallang2 == lang2[5]:
        nn2 = "ca" 
    elif vallang2 == lang2[6]:
        nn2 = "fr" 
    else:
        nn2 = "th"
    return nn2
def soundinput():
	ai=str(nhapdl.get())
	if ai != "":
		output = gTTS(ai,lang=returnnn1(), slow=False)
		output.save("fileinput.mp3")
		playsound.playsound('fileinput.mp3')
		os.remove('fileinput.mp3')
	else:
		ai ="không có dữ liệu"
		output = gTTS(ai,lang="vi", slow=False)
		output.save("fileinput.mp3")
		playsound.playsound('fileinput.mp3')
		os.remove('fileinput.mp3')
def soundoutput():
	ai=str(xuatchu.get())
	if ai != "":
		output = gTTS(ai,lang=returnnn2(), slow=False)
		output.save("fileoutput.mp3")
		playsound.playsound('fileoutput.mp3')
		os.remove('fileoutput.mp3')
	else:
		ai="không có dữ liệu"
		output = gTTS(ai,lang="vi", slow=False)
		output.save("fileoutput.mp3")
		playsound.playsound('fileoutput.mp3')
		os.remove('fileoutput.mp3')
#mo file anh
def openfimg():
    openfile = Tk()
    openfile.withdraw()
    filename = askopenfilename()
    filename = str(filename)
    if ".jpg" not in filename and ".png" not in filename and ".JPG" not in filename and ".PNG" not in filename:
    	messagebox.showinfo("CHÚ Ý", "File ẢNH phải là file đuôi .PNG hoặc .JPG")
    else:
    	return filename
#in chu img
def innhapdlimg():
    try:
        f = open("C:\\Program Files\\Tesseract-OCR\\tesseract.exe")
    except:
        messagebox.showinfo("CHÚ Ý", "Bạn chưa cài đặt gói chuyển hình ảnh sang văn bản\nBạn có muốn tải tự động không???")
        web.open("https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v4.1.0-bibtag19.exe", new =1)
    nhapdl.delete(0,END)
    nhapdl.insert(0,outhinhanh())
    return
def outhinhanh():
	pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
	image = Image.open(openfimg()).convert("RGB")
	image_to_text = pytesseract.image_to_string(image,lang='eng')
	if image_to_text =="":
		messagebox.showinfo("CHÚ Ý", "Không phát hiện chữ trong ẢNH!!!")
		return
	else:
		return str(image_to_text)
form = Tk()
form.title("GOOGLE DỊCH")
scrW= form.winfo_screenwidth()
scrH= form.winfo_screenheight()
W = scrW/2-400
H = scrH/2-300
form.geometry('800x570+%d+%d' %(W,H))

#chọn ngôn ngữ 1
mn1= menu.Combobox(form,width=12, font='Times 20', state="readonly")
lang1 = ["    Tiếng Anh","    Tiếng Việt","    Tiếng Nhật","    Tiếng Hàn","   Tiếng Trung"," Tiếng Canada","    Tiếng Pháp","    Tiếng Thái"]
mn1["values"]=(lang1[0],lang1[1],lang1[2],lang1[3],lang1[4],lang1[5],lang1[6],lang1[7])
mn1.current(0)
mn1.place(x=110,y=200)

#chọn ngôn ngữ thứ 2
mn2= menu.Combobox(form,width=12, font='Times 20', state="readonly")
lang2 = ["    Tiếng Anh","    Tiếng Việt","    Tiếng Nhật","    Tiếng Hàn","   Tiếng Trung"," Tiếng Canada","    Tiếng Pháp","    Tiếng Thái"]
mn2["values"]=(lang2[0],lang2[1],lang2[2],lang2[3],lang2[4],lang2[5],lang2[6],lang2[7])
mn2.current(1)
mn2.place(x=500,y=200)

#nhap du lieu
nhapdl = Entry(form,font='Times 30')
nhapdl.place(x=0, y=20, height= 100, width= 800)

#ghi am
btnlt= Button(form, text="Giọng Nói🎙",font='Times 20', fg = "red", bg = "white",command= inchunhapdl)
btnlt.place(x=325,  y=140, height= 35, width= 150)

#click xem ket qua
btn= Button(form, text="DỊCH 🔍",font='Times 20', fg = "white", bg = "black", command = chonngonngu)
btn.place(x=325, y=300, height= 35, width= 150)
#xuat ket qua
xuatchu = Entry(form,font='Times 30', fg = "red")
xuatchu.place(x=0, y=400, height= 100, width= 800)

#phát âm thanh intext
btnit= Button(form, text="🔊",font='Times 20', fg = "blue", bg = "white", command = soundinput)
btnit.place(x=10, y=130, height= 50, width= 50)

#phát âm thanh outtext
btnot= Button(form, text="🔊",font='Times 20', fg = "blue", bg = "white", command = soundoutput)
btnot.place(x=10, y=510, height= 50, width= 50)

#đọc tài liệu
btnoptext= Button(form, text="TÀI LIỆU 📄",font='Times 20', fg = "blue", bg = "white",command=innhapdltxt)
btnoptext.place(x=130, y=140, height= 35, width= 150)

#đọc hình ảnh 
btnopimg= Button(form, text="ẢNH 🎞",font='Times 20', fg = "blue", bg = "white",command=innhapdlimg)
btnopimg.place(x=520, y=140, height= 35, width= 150)
#hiệu ứng load
load = Label(form, text= "◼◼◼◼◼◼▶",font='Times 20' )
load.place(x=325,  y=200, height= 35, width= 155)
form.mainloop()