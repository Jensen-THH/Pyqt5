import sys
from PyQt5.QtWidgets import QDialog,QApplication,QInputDialog
from PyQt5 import uic
import requests
# from PyQt5_GUI.BaiTapLamThem.BMI.CBMI import BMI
# giúp lấy thông tin các trang web 1 cách dễ dàng
# Nó nằm trên cùng một trình phân tích cú pháp HTML hoặc XML, cung cấp các thành ngữ Pythonic để lặp lại, tìm kiếm và sửa đổi cây phân tích cú pháp.
from bs4 import BeautifulSoup as BS

class ApplWindow(QDialog):
    def __init__(self):
        super(ApplWindow, self).__init__()
        self.ui = uic.loadUi('corona.ui', self)
        self.country = ["india", "us", "spain", "china", "russia",
                        "pakistan", "nepal", "italy", "spain",
                        "uk", "brazil"]
        self.addcontent()
        self.comboBox.activated.connect(self.get_cases)
        self.show()
    def addcontent(self):
        for i in self.country:
            i = i.upper()
            self.comboBox.addItem(i)

    def get_cases(self):
        # getting country name
        index = self.comboBox.currentIndex()
        country_name = self.country[index]

        # creating url using country name
        url = "https://www.worldometers.info/coronavirus/country/" + country_name + "/"

        # getting the request from url
        data = requests.get(url)

        # converting the text
        soup = BS(data.text, 'html.parser')

        # finding meta info for cases
        cases = soup.find_all("div", class_="maincounter-number")

        # getting total cases number
        total = cases[0].text

        # filtering it
        total = total[1: len(total) - 2]

        # getting recovered cases number
        recovered = cases[2].text

        # filtering it
        recovered = recovered[1: len(recovered) - 1]

        # getting death cases number
        deaths = cases[1].text

        # filtering it
        deaths = deaths[1: len(deaths) - 1]

        # show data through labels
        self.label.setText("Total Cases : " + total)
        self.label_2.setText("Recovered Cases : " + recovered)
        self.label_3.setText("Total Deaths : " + deaths)



if __name__=="__main__":
    app=QApplication(sys.argv)
    window=ApplWindow()
    sys.exit(app.exec_())