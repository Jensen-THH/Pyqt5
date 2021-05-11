

import sys
from PyQt5.QtWidgets import QDialog,QApplication,QInputDialog
from PyQt5 import uic
import requests
import json
class ApplWindow(QDialog):
    def __init__(self):
        super(ApplWindow, self).__init__()
        self.ui = uic.loadUi('weather.ui', self)
        self.country = ["saigon,vn", "london,uk"]
        self.addcontent()
        self.comboBox.activated.connect(self.get_cases)
        self.show()
    def addcontent(self):
        for i in self.country:
            i = i.upper()
            self.comboBox.addItem(i)

    def get_cases(self):
        url = "https://community-open-weather-map.p.rapidapi.com/weather"
        city=self.ui.comboBox.currentText()
        querystring = {"q": city, "lat": "0", "lon": "0", "callback": "test", "id": "2172797", "lang": "null",
                       "units": "\"metric\" or \"imperial\"", "mode": "xml, html"}

        headers = {
            'x-rapidapi-key': "e800f09e48mshdcbf31ffe6e7e12p131605jsn2a98bfdc4ec7",
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data=json.loads(response.text[5:-1])
        print(data["weather"])
        lat=data["coord"]["lat"]
        clouds=data["weather"][0]["main"]


        self.label.setText("vi do: " + str(lat))
        self.label_2.setText("Thoi tiet: " + str(clouds))



if __name__=="__main__":
    app=QApplication(sys.argv)
    window=ApplWindow()
    sys.exit(app.exec_())