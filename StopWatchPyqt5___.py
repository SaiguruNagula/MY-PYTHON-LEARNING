# stop Watch programme

import sys 
from PyQt5.QtWidgets import (QApplication , QMainWindow , QLabel , QHBoxLayout , QVBoxLayout , QGridLayout, QPushButton,QWidget)
from PyQt5.QtGui import QPixmap , QIcon
from PyQt5.QtCore import Qt , QTimer , QTime 

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00:00",self)
        self.start_button = QPushButton("start",self)
        self.stop_button = QPushButton("stop",self)
        self.reset_button = QPushButton("reset",self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("stopwatch")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)
        
        self.setStyleSheet("""
                           QPushButton,QLabel{padding :20px;
                                              font-weight:bold
                                }
                           QPushButton {font-size : 50px;
                                         background-color :#03fce3;
                                         border-radius : 20px }
                           
                           QLabel{
                                  font-size: 100px;
                                color : #2ff728;
                                background-color:black;
                                border-radius : 20px
                                 }
                           """)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)



    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.formate_time(self.time))

    def formate_time(self, time):
        hours = time.hour()
        minute = time.minute()
        sec = time.second()
        millisecond = time.msec()//10
        return f'{hours:02}:{minute:02}:{sec:02}.{millisecond:02}'

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.formate_time(self.time))

        





def main():
    app = QApplication(sys.argv)
    window= Stopwatch()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
