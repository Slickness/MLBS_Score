__author__ = 'randy'        
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton
import MLB

class Scores(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn =  QPushButton("Get Score",self)
        btn.move(65,0)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GameSCores = Scores()
    sys,exit(app.exec_())
    
