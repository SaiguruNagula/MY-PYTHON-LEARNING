# layout

import sys

from PyQt5.QtWidgets import (QApplication , QMainWindow , QHBoxLayout , QVBoxLayout , QGridLayout , QWidget , QLabel)
from PyQt5.QtGui import QPixmap , QIcon , QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Manager")
        self.setGeometry(700,300,500,500)
        self.initUi()
        
    def initUi(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        label1= QLabel('#1',self)
        label2= QLabel('#2',self)
        label3= QLabel('#3',self)
        label4= QLabel('#4',self)

        label4.setStyleSheet("background-color:blue;")
        label3.setStyleSheet("background-color:red;")
        label2.setStyleSheet("background-color:yellow;")
        label1.setStyleSheet("background-color:orange;")



        vbox = QGridLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        self.central_widget.setLayout(vbox)

        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())




if __name__ == '__main__':
    main()
