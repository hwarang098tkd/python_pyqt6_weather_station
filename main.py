# An API pogram which retrieve weather info about a cite that you select
import sys

import requests
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon


def get_city_info(city_name):
    data = 'error'
    if city_name != '':
        # API key
        API_key = 'put_your_api'
        # Url construction
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
        response = requests.get(url)

        # Check if the response is successfully formed
        if response.status_code == 200:
            data = response.json()
            print("Success")
        else:  # if the response failed
            print("Something went wrong. Please try again.")
    return data


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle("Weather Station")
        self.setWindowIcon(QIcon("icon.jpg"))

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.city_name = QLabel(text='City Name')
        layout.addWidget(self.city_name)
        self.city_name = QLineEdit()

        layout.addWidget(self.city_name)
        self.confirm_btn = QPushButton()
        self.confirm_btn.setText("Get Info")
        layout.addWidget(self.confirm_btn)
        self.confirm_btn.clicked.connect(self.button_press)
        # info widgets
        self.weather = QLabel(text='Weather condition')
        layout.addWidget(self.weather)

        self.description = QLabel(text='Weather description')
        layout.addWidget(self.description)

        self.temperature = QLabel(text='Temperature')
        layout.addWidget(self.temperature)

        self.feels_like = QLabel(text='Feels like')
        layout.addWidget(self.feels_like)

        self.humidity = QLabel(text='Humidity')
        layout.addWidget(self.humidity)

        self.wind_speed = QLabel(text='Wind speed')
        layout.addWidget(self.wind_speed)

        self.status = QLabel(text='Status')
        layout.addWidget(self.status)

    def button_press(self):
        if self.city_name == '':  # if the user press the button without set the city name
            self.status.setText('Status: Failed')
        else:
            weather_info = get_city_info(self.city_name.text())
            if weather_info != 'error':  # if data is filled with values
                print(weather_info)
                self.weather.setText('Weather condition' + ' : ' + weather_info['weather'][0]['main'])
                self.description.setText('Weather description' + ' : ' + weather_info['weather'][0]['description'])
                self.temperature.setText('Temperature' + ' : ' + str(round(weather_info['main']['temp'] - 273.15, 2)))
                self.feels_like.setText(
                    'Feels like' + ' : ' + str(round(weather_info['main']['feels_like'] - 273.15, 2)))
                self.humidity.setText('Humidity' + ' : ' + str(weather_info['main']['humidity']))
                self.wind_speed.setText('Wind speed' + ' : ' + str(weather_info['wind']['speed']))
                self.status.setText('Status: Success')
            else:  # on failed
                self.status.setText('Status: Failed')
                # reset textboxes
                self.weather.setText('Weather condition' + ' : ')
                self.description.setText('Weather description' + ' : ')
                self.temperature.setText('Temperature' + ' : ')
                self.feels_like.setText('Feels like' + ' : ')
                self.humidity.setText('Humidity' + ' : ')
                self.wind_speed.setText('Wind speed' + ' : ')


def main():  # call the main window
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
