from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
    qApp, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import cv2
import os
from pypylon import pylon
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
class Ui_register_Dialog(object):
    def setupUi(self, register_Dialog):
        register_Dialog.setObjectName("register_Dialog")
        register_Dialog.resize(749, 598)
        self.re_Save_pushButton = QtWidgets.QPushButton(register_Dialog)
        self.re_Save_pushButton.setGeometry(QtCore.QRect(30, 560, 89, 25))
        self.re_Save_pushButton.setObjectName("re_Save_pushButton")
        self.comboBox = QtWidgets.QComboBox(register_Dialog)
        self.comboBox.setGeometry(QtCore.QRect(260, 560, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
      #  self.Close_pushButton = QtWidgets.QPushButton(register_Dialog)
     ##   self.Close_pushButton.setGeometry(QtCore.QRect(390, 560, 89, 25))
      #  self.Close_pushButton.setObjectName("Close_pushButton")
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
        file_goc=os.getcwd()
       # self.ten=self.Image_comboBox.currentText()
        file_config=file_goc.replace("/detection_edges","")
        file_config_incon_zoom_in=file_config+"/resources/icons/zoom-in.png"
        file_config_incon_zoom_out=file_config+"/resources/icons/zoom-out.png"
        file_config_incon_zoom_fit=file_config+"/resources/icons/zoom.png"
        self.Register_Zoom_In_pushButton.setIcon(QtGui.QIcon(file_config_incon_zoom_in))
        self.Register_Zoom_out_pushButton.setIcon(QtGui.QIcon(file_config_incon_zoom_out))
        self.Register_Zoom_fit_pushButton.setIcon(QtGui.QIcon(file_config_incon_zoom_fit))



        self.re_img_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)#THEM DONG
        self.scrollArea.setBackgroundRole(QPalette.Dark)#THEM DONG
        self.re_img_label.setWordWrap(True)
        self.re_img_label.setObjectName("label")
        self.scrollArea.setWidget(self.re_img_label)

        self.timer = QTimer()
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
        self.comboBox.setItemText(0, _translate("register_Dialog", "01"))
        self.comboBox.setItemText(1, _translate("register_Dialog", "02"))
        self.comboBox.setItemText(2, _translate("register_Dialog", "03"))
        self.comboBox.setItemText(3, _translate("register_Dialog", "04"))
        self.comboBox.setItemText(4, _translate("register_Dialog", "05"))
        self.comboBox.setItemText(5, _translate("register_Dialog", "06"))
        self.comboBox.setItemText(6, _translate("register_Dialog", "07"))
        self.comboBox.setItemText(7, _translate("register_Dialog", "08"))
        self.comboBox.setItemText(8, _translate("register_Dialog", "09"))
        self.comboBox.setItemText(9, _translate("register_Dialog", "10"))
     #  self.Close_pushButton.setText(_translate("register_Dialog", "Close"))
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
            
           # image=cv2.resize(image,(1117, 710))
        # get image infos
            height, width, channel = self.image.shape
            step = channel * width
        # create QImage from image
            qImg = QImage(self.image.data, width, height, step, QImage.Format_RGB888)
           # pixmapQPixmap.fromImage(qImg)
        # show image in img_label
           # pixmap_resized = pixmap.scaled(720, 405, QtCore.Qt.KeepAspectRatio)
            self.re_img_label.setPixmap(QPixmap.fromImage(qImg))
            #self.ui.img_label.setScaledContents(True)

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():

            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            # start timer
            self.timer.start(20)
            # update control_bt text
          #  self.ui.OpenCamera_pushButton.setText("Stop")
        # if timer is started
    def save_img(self):
        ten=self.comboBox.currentText()
      #  ret, image = self.cap.read()
        file_img=ten+".jpg"
        
        cv2.imwrite(file_img,self.image)
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

