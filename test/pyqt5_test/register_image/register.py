from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
    qApp, QFileDialog,QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import cv2
import os
from pypylon import pylon

import tkinter as tk

#Lay kich thuoc man hinh thuc te
root = tk.Tk()
width_px = root.winfo_screenwidth()
height_px = root.winfo_screenheight() 

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
class Ui_register_Dialog(QDialog):
    def setupUi(self, register_Dialog):
        register_Dialog.setObjectName("register_Dialog")
        register_Dialog.resize(width_px, height_px)
        self.re_Save_pushButton = QtWidgets.QPushButton(register_Dialog)
        self.re_Save_pushButton.setGeometry(QtCore.QRect(30, 560, 89, 25))
        self.re_Save_pushButton.setObjectName("re_Save_pushButton")

        #self.Close_pushButton = QtWidgets.QPushButton(register_Dialog)
        #self.Close_pushButton.setGeometry(QtCore.QRect(390, 560, 89, 25))
        #self.Close_pushButton.setObjectName("Close_pushButton")

        self.horizontalLayoutWidget = QtWidgets.QWidget(register_Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 351, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.register_Camera_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.register_Camera_comboBox.setObjectName("register_Camera_comboBox")
        self.horizontalLayout.addWidget(self.register_Camera_comboBox)
        self.Register_Zoom_In_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Register_Zoom_In_pushButton.setText("")
        self.Register_Zoom_In_pushButton.setIconSize(QtCore.QSize(25, 25))
        self.Register_Zoom_In_pushButton.setObjectName("Register_Zoom_In_pushButton")
        self.horizontalLayout.addWidget(self.Register_Zoom_In_pushButton)
        self.Register_Zoom_out_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Register_Zoom_out_pushButton.setText("")
        self.Register_Zoom_out_pushButton.setIconSize(QtCore.QSize(25, 25))
        self.Register_Zoom_out_pushButton.setObjectName("Register_Zoom_out_pushButton")
        self.horizontalLayout.addWidget(self.Register_Zoom_out_pushButton)
        self.Register_Zoom_fit_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Register_Zoom_fit_pushButton.setText("")
        self.Register_Zoom_fit_pushButton.setIconSize(QtCore.QSize(25, 25))
        self.Register_Zoom_fit_pushButton.setObjectName("Register_Zoom_fit_pushButton")
        self.horizontalLayout.addWidget(self.Register_Zoom_fit_pushButton)

        self.scrollArea = QtWidgets.QScrollArea(register_Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 701, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 699, 489))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")





       # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        register_Dialog.closeEvent = self.CloseEvent
        dir_file_goc=os.getcwd()
       # self.ten=self.Image_comboBox.currentText()
        #file_config=file_goc.replace("/detection_edges","")

        file_config_incon_zoom_in=dir_file_goc+"/resources/icons/zoom-in.png"
        file_config_incon_zoom_out=dir_file_goc+"/resources/icons/zoom-out.png"
        file_config_incon_zoom_fit=dir_file_goc+"/resources/icons/zoom.png"
        self.Register_Zoom_In_pushButton.setIcon(QtGui.QIcon(file_config_incon_zoom_in))
        self.Register_Zoom_out_pushButton.setIcon(QtGui.QIcon(file_config_incon_zoom_out))
        self.Register_Zoom_fit_pushButton.setIcon(QtGui.QIcon(file_config_incon_zoom_fit))



        self.re_img_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)#THEM DONG
        self.scrollArea.setBackgroundRole(QPalette.Dark)#THEM DONG
        self.re_img_label.setWordWrap(True)
        self.re_img_label.setObjectName("label")
        self.scrollArea.setWidget(self.re_img_label)

        self.timer = QTimer()
        #self.Close_pushButton.clicked.connect()
        self.re_Save_pushButton.clicked.connect(self.save_img)
        self.timer.timeout.connect(self.viewCam_1)
        self.controlTimer()
        
        self.retranslateUi(register_Dialog)
        QtCore.QMetaObject.connectSlotsByName(register_Dialog)
       # self.close_event()

    def retranslateUi(self, register_Dialog):
        _translate = QtCore.QCoreApplication.translate
        register_Dialog.setWindowTitle(_translate("register_Dialog", "Dialog"))
        self.re_Save_pushButton.setText(_translate("register_Dialog", "Save"))
        #self.Close_pushButton.setText(_translate("register_Dialog", "Close"))
        self.label.setText(_translate("register_Dialog", "Camera"))

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
            height, width, channel = self.image.shape
            step = channel * width
            qImg = QImage(self.image.data, width, height, step, QImage.Format_RGB888)
            self.re_img_label.setPixmap(QPixmap.fromImage(qImg))

    def controlTimer(self):
        if not self.timer.isActive():
            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            self.timer.start(20)

    def save_img(self):
        dir_image_raw = os.getcwd()+"/image_raw"
        dir_image_raw = dir_image_raw.rstrip()
        count_img_raw_saved = len(os.listdir(dir_image_raw))
        count_img_raw_saved = count_img_raw_saved + 1
        length=len (str(count_img_raw_saved))
        self.name = "image_raw_"+str(count_img_raw_saved)
        name_save = dir_image_raw+"/"+self.name+".jpg"
        cv2.imwrite(name_save,self.image)

    def CloseEvent(self, event):
        self.timer.stop()
        camera.StopGrabbing()
        print("dong")
      
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_Dialog = QtWidgets.QDialog()
    ui = Ui_register_Dialog()
    ui.setupUi(register_Dialog)
    register_Dialog.show()
    sys.exit(app.exec_())

