#!/usr/bin/env python
import sys
from PyQt4 import QtGui

class HelloWindow(QtGui.QMainWindow):

    def __init__(self,win_parent = None):
        #init the base class
        QtGui.QMainWindow.__init__(self,win_parent)
    def create_widgets(self):
        central_widget = QtGui.QWidget()
        self.setCentralWidget(central_widget)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #the main window
    main_window = HelloWindow()
    main_window.show()
    app.exec_()
