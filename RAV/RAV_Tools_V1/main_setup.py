import sys
import os
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from pypylon import pylon
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication

import cv2
from mainwindow_run import *
from register_image import Ui_register_Dialog
from mainwindow_setup import Ui_MainWindow_Setup

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

def RegisterImage(self):
    self.setup_Dialog1 = QtWidgets.QDialog()
    self.ui_4 = Ui_register_Dialog()
    self.ui_4.setupUi(self.setup_Dialog1)
    self.setup_Dialog1.show()



class Setup_Window(Ui_MainWindow_Setup):
    def __init__(self):
        super().__init__()
        self.ui3 =  Ui_MainWindow_Setup() 
        self.ui3.setupUi(self)
        self.ui3.btn_RefImage.clicked.connect(self.aa)
        print("wellcomeSetup_UI")
    def aa(self):
        RegisterImage(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow_1 = Setup_Window()
    mainWindow_1.showMaximized()

    sys.exit(app.exec_())