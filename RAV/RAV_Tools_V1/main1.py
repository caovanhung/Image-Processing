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

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

def open_register_ui(self):
    self.Dialog = QtWidgets.QDialog()
    self.ui_1 = Ui_register_Dialog()
    self.ui_1.setupUi(self.Dialog)
    self.Dialog.show()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui =  Ui_Form_camera()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        self.ui.btn_RUN.clicked.connect(self.controlTimer)
        self.ui.btn_SET_RUN.clicked.connect(self.open_register)

        self.controlTimer()





    def open_register(self):
        self.timer.stop()
        camera.StopGrabbing()
        self.ui.btn_RUN.setText("RUN")
        open_register_ui(self)

    def viewCam(self):
        converter = pylon.ImageFormatConverter()
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

            # create video capture
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
        # Access the image data
            image = converter.Convert(grabResult)
            self.img = image.GetArray()
            image = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            
           # image=cv2.resize(image,(1117, 710))
        # get image infos
            height, width, channel = image.shape
            step = channel * width
        # create QImage from image
            qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
           # pixmapQPixmap.fromImage(qImg)
        # show image in img_label
           # pixmap_resized = pixmap.scaled(720, 405, QtCore.Qt.KeepAspectRatio)
            self.ui.img_label.setPixmap(QPixmap.fromImage(qImg))
            #self.ui.img_label.setScaledContents(True)

        # start/stop timer
    def controlTimer(self):
        # if timer is stopped
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
