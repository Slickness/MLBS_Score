#!/usr/bin/env python
import time
import sys
from PyQt4 import QtGui, QtCore, Qt
import MLB
games = []
game= []
x = 0
class Window(QtGui.QWidget):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,200,100)
        self.setWindowTitle("MLB Scores")
        self.home()
        self.thread = Worker() #to enable the updating of the widget
        self.setFixedSize(200,100)
    def home(self):
        btn =  QtGui.QPushButton("Get Score",self)
        btn.move(65,0)
        #btn.resize(50,20)
        btn.clicked.connect(self.score)
        self.LabelStatus = QtGui.QLabel("Status",self)
        self.LabelStatus.move(10,25)
        self.LabelVis =QtGui.QLabel("Visitor",self)
        self.LabelVis.move(10,50)
        self.LableVScore = QtGui.QLabel("vscore",self)
        self.LableVScore.move(170,50)
        self.LabelHome =QtGui.QLabel("Home",self)
        self.LabelHome.move(10,75)
        self.LableHScore = QtGui.QLabel("hscore",self)
        self.LableHScore.move(170,75)
        self.worker = Worker()
        self.connect(self.worker,QtCore.SIGNAL("ThreadDone()"),self.ShowScores,QtCore.Qt.DirectConnection)
        self.LabelStatus.setFixedWidth(100)
        self.LabelHome.setFixedWidth(200)
        self.LabelVis.setFixedWidth((200))
        self.LableHScore.setFixedWidth(50)
        self.LableVScore.setFixedWidth(50)


        self.show()
    def score(self):
        self.worker.start()
        #self.LabelHome.setText(str("test"))
    def ShowScores(self):
        global x
        global game
        self.palette = QtGui.QPalette()
        self.palette.setColor(QtGui.QPalette.Window,QtCore.Qt.yellow)
        self.LabelStatus.setText(game[4])
        self.LabelStatus.setPalette(self.palette)
        self.LabelHome.setText(game[2])

        self.LabelVis.setText(game[0])

        self.LableHScore.setText(game[3])


        self.LableVScore.setText(game[1])

        Qt.QApplication.processEvents()
class Worker(QtCore.QThread):

    def __init__(self, parent = None):

        QtCore.QThread.__init__(self, parent)


    def run(self):
        global x
        global games
        global game
        url ="http://www.sportsnet.ca/baseball/mlb/scores/"
        while True:
            games = MLB.main(url)
            for game in games:
                time.sleep(5)
                #print  "over with thread"

                self.emit(QtCore.SIGNAL("ThreadDone()"))
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
