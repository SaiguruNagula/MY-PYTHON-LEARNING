# push button 

import sys 
from PyQt5.QtWidgets import (QApplication  , QMainWindow , QLayout , QHBoxLayout , QVBoxLayout , QGridLayout , QPushButton)


class MainWindow(QMainWindow):
     def __init__(self):
          super().__init__()
          self.setWindowTitle("Pushbutton")
          self.setGeometry(0,0,500, 500)
          self.button= QPushButton("click me ", self)
          self.initGui()
          

     def initGui(self):
        
          self.button.setGeometry(150,200,200,100)
          self.button.setStyleSheet("Font-Style:30px;")
          self.button.clicked.connect(self.on_click)

     def on_click(self):
          print("button clicked")
          self.button.setText("Clicked!")
          self.setDisabled(True)


def main():
     app = QApplication(sys.argv)
     Window = MainWindow()
     Window.show()
     sys.exit(app.exec_())

if __name__ == '__main__' :
     main()  

          


                 