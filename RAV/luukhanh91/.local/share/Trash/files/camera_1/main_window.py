"""
In this example, we demonstrate how to create simple camera viewer using Opencv3 and PyQt5

Author: Berrouba.A
Last edited: 21 Feb 2018
"""

# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from pypylon import pylon

# import Opencv module
import cv2

from test import *
#from register import *
from test_1 import *
from function import *

# conecting to the first available camera
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

# Grabing Continusely (video) with minimal delay



# converting to opencv bgr format


def open_register_ui(self):
    self.Dialog = QtWidgets.QDialog()
    self.ui_1 = Ui_register_Dialog()
    self.ui_1.setupUi(self.Dialog)
    self.Dialog.show()
def open_function_ui(self):
    self.function_Dialog= QtWidgets.QDialog()
    self.ui_function=Ui_fuction_Dialog()
    self.ui_function.setupUi(self.function_Dialog)
    self.function_Dialog.show()
    

class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui =  Ui_Form_camera()
        self.ui.setupUi(self)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.OpenCamera_pushButton.clicked.connect(self.controlTimer)
        self.ui.Register_pushButton.clicked.connect(self.open_register)
        self.ui.fuction_pushButton.clicked.connect(self.open_function)

    # view camera
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
        # get image infos
            height, width, channel = image.shape
            step = channel * width
        # create QImage from image
            qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
            self.ui.img_label.setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():

            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 

            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.OpenCamera_pushButton.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            camera.StopGrabbing()
            # update control_bt text
            self.ui.OpenCamera_pushButton.setText("Start")
    def open_register(self):
        self.timer.stop()
        camera.StopGrabbing()
        open_register_ui(self)
        print (step)
    def open_function(self):
        open_function_ui(self)
        
    
        
            


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    #open_register_ui()
    #register_1=register_dialog()
    #register_1.show()
    sys.exit(app.exec_())
