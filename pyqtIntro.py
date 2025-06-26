# PyQt5 

# boilerplate code
import sys 

from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel 
from PyQt5.QtGui import QIcon , QFont , QPixmap  
from PyQt5.QtCore import Qt  #for alignment

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("hello world")
        self.setGeometry(500 , 500 , 1000 , 500 )
        self.setWindowIcon(QIcon("C:/Users/hp/OneDrive/Desktop/python/1317107.jpeg"))

        label = QLabel("hello world" , self)
        label.setFont(QFont("Airal", 30))
        label.setGeometry(0,0,1000, 500)
        label.setStyleSheet("color:#f7c90f;"
                            "background-color:#fc6f0a;"
                            "font-weight : bold;"
                            "font-Style : italic;"
                            "text-decoration:underline")
        # label.setAlignment(Qt.AlignTop)
       # label.setAlignment(Qt.AlignBottom)
        #label.setAlignment(Qt.Alignvroght)
        #label.setAlignment(Qt.AlignHright)
        #label.setAlignment(Qt.AlignRight)
        #label.setAlignment(Qt.AlignHCenter)
        #label.setAlignment(Qt.AlignHRight |  Qt.AlignVCenter)    # to combine both h and v


        pixmap = QPixmap("C:/Users/hp/OneDrive/Desktop/python/1317107.jpeg")
        
        label.setPixmap(pixmap)
        label.setScaledContents(True)


def main():
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    