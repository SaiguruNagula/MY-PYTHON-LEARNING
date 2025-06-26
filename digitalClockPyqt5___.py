# python digital clock 

import sys  
from PyQt5.QtWidgets import (QLabel ,QApplication, QMainWindow, QHBoxLayout , QVBoxLayout , QGridLayout , QWidget )
from PyQt5.QtCore  import  Qt , QTimer , QTime
from PyQt5.QtGui import QPixmap , QIcon , QFont , QFontDatabase

class digitalClock(QWidget):
    def __init__(self):
      super().__init__()
      self.time_label1 = QLabel("12:00:00",self)
      self.Timer = QTimer(self)
      self.initUi()


    def initUi(self):
      self.setWindowTitle("Digital Clock")
      self.setGeometry(600 , 400 , 300 , 100) 

      vbox = QVBoxLayout()
      vbox.addWidget(self.time_label1)
      self.setLayout(vbox)
       

      self.time_label1.setAlignment(Qt.AlignCenter)

      self.time_label1.setStyleSheet("font-size:150px;"
                                      
                                      "color: #77fc03;"
                                      )
      
      self.setStyleSheet("background-color:black;")

      font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
      font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
      my_family = QFont(font_family,150)
      self.time_label1.setFont(my_family)

      self.Timer.timeout.connect(self.update_time)
      self.Timer.start(1000)
      
      self.update_time()
      

    def update_time(self):
       self.currentTime= QTime.currentTime().toString("hh:mm:ss AP")
       self.time_label1.setText(self.currentTime)

      


def main():
    app = QApplication(sys.argv)
    clock = digitalClock()
    clock.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
     main()