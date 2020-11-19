# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from main_window import *
from pypylon import pylon

import cv2
class xulyanh:
    def __init__(self,img):
        self.img=img
    def getData(self):
        return self.img
    def setdata(self,img):
        self.img=img
    
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

class Ui_register_Dialog(object):
    
    def setupUi(self, register_Dialog):
        register_Dialog.setObjectName("register_Dialog")
        register_Dialog.resize(749, 598)
        self.verticalLayoutWidget = QtWidgets.QWidget(register_Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 581, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.re_img_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.re_img_label.setText("")
        self.re_img_label.setObjectName("re_img_label")
        self.verticalLayout.addWidget(self.re_img_label)
        self.re_Save_pushButton = QtWidgets.QPushButton(register_Dialog)
        self.re_Save_pushButton.setGeometry(QtCore.QRect(0, 530, 89, 25))
        self.re_Save_pushButton.setObjectName("re_Save_pushButton")
        self.comboBox = QtWidgets.QComboBox(register_Dialog)
        self.comboBox.setGeometry(QtCore.QRect(240, 530, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
      
        self.Test_textEdit = QtWidgets.QTextEdit(register_Dialog)
        self.Test_textEdit.setGeometry(QtCore.QRect(590, 340, 151, 70))
        self.Test_textEdit.setObjectName("Test_textEdit")
        self.Close_pushButton = QtWidgets.QPushButton(register_Dialog)
        self.Close_pushButton.setGeometry(QtCore.QRect(470, 530, 89, 25))
        self.Close_pushButton.setObjectName("Close_pushButton")
        register_Dialog.closeEvent = self.CloseEvent
        self.retranslateUi(register_Dialog)

        QtCore.QMetaObject.connectSlotsByName(register_Dialog)
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.timer = QTimer()
        self.re_Save_pushButton.clicked.connect(self.save_img)

        self.timer.timeout.connect(self.viewCam_1)
        self.anh=xulyanh(0)
        self.controlTimer()


    def viewCam_1(self):
        converter = pylon.ImageFormatConverter()
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

            # create video capture
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
        # Access the image data
            image = converter.Convert(grabResult)
            self.img = image.GetArray()

            self.image = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            self.image=cv2.resize(self.image ,(581, 491))
         #   print(self.image.shape)
            self.anh.setdata(self.image)
        # get image infos
            image=self.anh.getData()
            height, width, channel = image.shape
            step = channel * width
            #self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 700, 700))
        # create QImage from image
            qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
            self.re_img_label.setPixmap(QPixmap.fromImage(qImg))

    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            # start timer
            self.timer.start(20)
    def save_img(self):
        ten=self.comboBox.currentText()
        img_2=self.anh.getData()
        file_img=ten+".jpg"
        cv2.imwrite(file_img,img_2)
        self.re_Save_pushButton.setEnabled(0)
 

    def retranslateUi(self, register_Dialog):
        _translate = QtCore.QCoreApplication.translate
        register_Dialog.setWindowTitle(_translate("register_Dialog", "Dialog"))
        self.re_Save_pushButton.setText(_translate("register_Dialog", "Save"))
        self.comboBox.setItemText(0, _translate("register_Dialog", "01"))
        self.comboBox.setItemText(1, _translate("register_Dialog", "02"))
        self.comboBox.setItemText(2, _translate("register_Dialog", "03"))
        self.comboBox.setItemText(3, _translate("register_Dialog", "04"))
 
               # self.Close_pushButton.setText(_translate("register_Dialog", "Close"))
    def CloseEvent(self, event):
        self.timer.stop()
     # release video capture
        camera.StopGrabbing()
        # update control_bt text
    def selectionchange(self):
        self.re_Save_pushButton.setEnabled(1)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_Dialog = QtWidgets.QDialog()
    ui = Ui_register_Dialog()
    ui.setupUi(register_Dialog)
    register_Dialog.show()
    sys.exit(app.exec_())

