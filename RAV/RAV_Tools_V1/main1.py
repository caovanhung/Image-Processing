import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication
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
from register_image import *
from mainwindow_setup import *


class Controller:
    def __init__(self):
        pass

    def show_WindowRUN(self):
        self.window_RUN = Ui_Form_camera()
        self.window_RUN.switch_window.connect(self.show_WindowSETUP)
        self.window_RUN.show()


    def show_WindowSETUP(self):
        self.window_SETUP = Ui_Form_camera()
        self.window_SETUP.switch_window.connect(self.show_WindowRUN)
        self.window_SETUP.show()




def main():
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_WindowRUN()
    sys.exit(app.exec_())


if __name__ == '__main__':
	main()
