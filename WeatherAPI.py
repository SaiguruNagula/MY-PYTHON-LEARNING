# weather api  app

import sys
import requests

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__ (self ):
        super().__init__()
        
        self.city_label = QLabel("Enter the city Name :", self)
        self.city_input = QLineEdit(self)
        self.get_Weather_button = QPushButton("get Weather",self)
        self.temperature_Label= QLabel(self)
        self.emoji_label= QLabel(self)
        self.Description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        # window properties
        self.setWindowTitle("Weather API App")
        self.setGeometry(100, 100, 400, 200)
        
        #set Labels and input
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_Weather_button)
        vbox.addWidget(self.temperature_Label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.Description_label)

        self.setLayout(vbox)


        # set Alignments
        self.city_label.setAlignment(Qt.AlignCenter)
        self.temperature_Label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.Description_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)

        # set css 
        # first set object then set css
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temperature_Label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.Description_label.setObjectName("description_label")
        self.get_Weather_button.setObjectName("get_weather_button")

        self.setStyleSheet("""
                          QLabel, QPushButton {
                                font-family : calibri;
                           }
                           QLabel#city_label {
                                font-size: 40px;
                                font-style : italic;
                            }
                           QLineEdit#city_input {
                                font-size: 40px;
                                padding: 10px;
                                border: 2px solid #ccc;
                                border-radius: 5px;
                            }  
                           QPushButton#get_weather_button {
                                font-size: 40px;
                                padding: 10px;
                                background-color: #4CAF50;
                                color: white;
                                border: none;
                                border-radius: 5px;
                            }
                           QLabel#temperature_label {
                                font-size: 75px;
                                
                            }
                            QLabel#emoji_label {
                                font-size: 100px;
                                font-family : segoe UI emoji;
                            } 
                            QLabel#description_label {
                                font-size: 50px;
                                font-style: italic;
                            }

                           """)
        
        # connect button to function
        self.get_Weather_button.clicked.connect(self.get_weather)
        
    def get_weather(self):
        
        api_key = "94d51a77a4fb399ffe09ccf4e519f568"
        city = self.city_input.text()    # get text from city input lineedit
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
           response = requests.get(url)
           response.raise_for_status()
           data = response.json()

           if data["cod"]==200 : # check if the response is successful
              self.display_weather(data)
          
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 404:
                    self.display_error("City not found. Please enter a valid city name.")
                case 401:
                    self.display_error("Invalid API key. Please check your API key.")
                case 403:
                    self.display_error("Access forbidden. Please check your API key and permissions.")
                case 400:
                    self.display_error("Bad request. Please check the city name and try again.")
                case 500:
                    self.display_error("Internal server error. Please try again later.")
                case 502:
                    self.display_error("Bad gateway. The server is currently unavailable.") 
                case 503:
                    self.display_error("Service unavailable. The server is currently overloaded or down for maintenance.")
                case 504:
                    self.display_error("Gateway timeout. The server took too long to respond.")
                case _:
                    self.display_error("An error occurred while fetching the weather data.")
        except requests.exceptions.ConnectionError:
             self.display_error("Network error. Please check your internet connection.")

        except requests.exceptions.Timeout:
             self.display_error("The request timed out. Please try again later.")

        except requests.exceptions.TooManyRedirects:
             self.display_error("Too many redirects. Please check the URL and try again.")

        except requests.exceptions.RequestException as req :
             self.display_error(f"An error occurred while making the request: {req}. Please try again later.")


    def display_error(self, message):
        self.temperature_Label.setStyleSheet("color: red; font-size: 30px;")
        self.temperature_Label.setText(message)

    def display_weather(self, data):
        temp_c = data["main"]['temp']
        temp_c = temp_c - 273.15
        weather_description = data["weather"][0]["description"]
        weather_id = data["weather"][0]['id']

        self.emoji_label.setText(self.set_emoji(weather_id))
        self.temperature_Label.setText(f'Temperature: {temp_c:.2f}°C')
        self.Description_label.setText(f'{weather_description}')

    @staticmethod
    def set_emoji(weather_id):
        if 200 <= weather_id < 300:
            return "🌩️" 
        if 300 <= weather_id < 400:
            return "🌧"
        if 500 <= weather_id < 600:
            return "🌧️"
        if 600 <= weather_id < 700:
            return "❄️"
        if 700 <= weather_id < 800:
            return "🌫️"
        if weather_id == 800:
            return "☀️"
        if 801 <= weather_id < 900:
            return "🌤️" 
        if 900 <= weather_id < 1000:
            return "🌪️"
        if weather_id >= 1000:
            return "🌩️"
        if weather_id < 200:
            return "🌩️"
        if weather_id < 0:
            return "invalid"
        if weather_id == 0:
            return "invalid"

        else :
            return ""

def main():
    app = QApplication(sys.argv)
    weatherapp = WeatherApp()
    weatherapp.show()
    sys.exit(app.exec_())




if __name__ == "__main__":
    main()