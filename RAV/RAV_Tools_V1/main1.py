import sys
import os
from PyQt5 import QtWidgets 
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

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())


def open_setup_ui(self):
    self.setup_Dialog = QtWidgets.QDialog()
    self.ui_2 = Ui_Dialog()
    self.ui_2.setupUi(self.setup_Dialog)
    self.setup_Dialog.show()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui =  Ui_Form_camera()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        self.ui.btn_RUN.clicked.connect(self.controlTimer)
        self.ui.btn_SET_RUN.clicked.connect(self.open_setup)

  

        self.controlTimer()


    def open_setup(self):
        self.timer.stop()
        camera.StopGrabbing()
        self.ui.btn_RUN.setText("RUN")
        open_setup_ui(self)

    def viewCam(self):
        converter = pylon.ImageFormatConverter()
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
            image = converter.Convert(grabResult)
            self.img = image.GetArray()
            image = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            height, width, channel = image.shape
            step = channel * width
            qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
            self.ui.img_label.setPixmap(QPixmap.fromImage(qImg))
    def controlTimer(self):
        if not self.timer.isActive():
            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            self.timer.start(20)
            self.ui.btn_RUN.setText("Stop")
        else:
            self.timer.stop()
            camera.StopGrabbing()
            self.ui.btn_RUN.setText("Run")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    sys.exit(app.exec_())
