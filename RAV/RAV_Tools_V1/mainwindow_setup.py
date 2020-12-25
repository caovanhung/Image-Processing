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


import tkinter as tk
root = tk.Tk()
width_px = int(root.winfo_screenwidth()/2)
height_px = int(root.winfo_screenheight())

#camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())


def open_register_ui(self):
    self.Dialog = QtWidgets.QDialog()
    self.ui_1 = Ui_register_Dialog()
    self.ui_1.setupUi(self.Dialog)
    self.Dialog.show()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(width_px, height_px)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        Dialog.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1021, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_row1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_row1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_row1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_row1.setObjectName("gridLayout_row1")
        self.textEdit_Infor = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_Infor.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEdit_Infor.setObjectName("textEdit_Infor")
        self.gridLayout_row1.addWidget(self.textEdit_Infor, 0, 4, 1, 1)

        self.btn_IO = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_IO.sizePolicy().hasHeightForWidth())
        self.btn_IO.setSizePolicy(sizePolicy)
        self.btn_IO.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_IO.setObjectName("btn_IO")
        self.gridLayout_row1.addWidget(self.btn_IO, 0, 2, 1, 1)

        self.btn_GotoModeRun = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_GotoModeRun.sizePolicy().hasHeightForWidth())
        self.btn_GotoModeRun.setSizePolicy(sizePolicy)
        self.btn_GotoModeRun.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_GotoModeRun.setObjectName("btn_GotoModeRun")
        self.gridLayout_row1.addWidget(self.btn_GotoModeRun, 0, 5, 1, 1)

        self.btn_FILE = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_FILE.sizePolicy().hasHeightForWidth())
        self.btn_FILE.setSizePolicy(sizePolicy)
        self.btn_FILE.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_FILE.setObjectName("btn_FILE")
        self.gridLayout_row1.addWidget(self.btn_FILE, 0, 0, 1, 1)

        self.btn_RefImage = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_RefImage.sizePolicy().hasHeightForWidth())
        self.btn_RefImage.setSizePolicy(sizePolicy)
        self.btn_RefImage.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_RefImage.setObjectName("btn_RefImage")
        self.gridLayout_row1.addWidget(self.btn_RefImage, 0, 1, 1, 1)

        self.btn_CameraSetting = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_CameraSetting.sizePolicy().hasHeightForWidth())
        self.btn_CameraSetting.setSizePolicy(sizePolicy)
        self.btn_CameraSetting.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_CameraSetting.setObjectName("btn_CameraSetting")
        self.gridLayout_row1.addWidget(self.btn_CameraSetting, 0, 3, 1, 1)

        self.textEdit_OK_NG = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_OK_NG.sizePolicy().hasHeightForWidth())
        self.textEdit_OK_NG.setSizePolicy(sizePolicy)
        self.textEdit_OK_NG.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_OK_NG.setFont(font)
        self.textEdit_OK_NG.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textEdit_OK_NG.setObjectName("textEdit_OK_NG")
        self.gridLayout_row1.addWidget(self.textEdit_OK_NG, 0, 6, 1, 1)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 1021, 111))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_row2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_row2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_row2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_row2.setObjectName("gridLayout_row2")

        self.btn_CAM2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_CAM2.sizePolicy().hasHeightForWidth())
        self.btn_CAM2.setSizePolicy(sizePolicy)
        self.btn_CAM2.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_CAM2.setObjectName("btn_CAM2")
        self.gridLayout_row2.addWidget(self.btn_CAM2, 0, 1, 1, 1)

        self.textEdit_listTool = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_listTool.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEdit_listTool.setObjectName("textEdit_listTool")
        self.gridLayout_row2.addWidget(self.textEdit_listTool, 0, 3, 1, 1)

        self.btn_CAM1 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_CAM1.sizePolicy().hasHeightForWidth())
        self.btn_CAM1.setSizePolicy(sizePolicy)
        self.btn_CAM1.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_CAM1.setObjectName("btn_CAM1")
        self.gridLayout_row2.addWidget(self.btn_CAM1, 0, 0, 1, 1)

        self.btn_AddTool = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_AddTool.sizePolicy().hasHeightForWidth())
        self.btn_AddTool.setSizePolicy(sizePolicy)
        self.btn_AddTool.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_AddTool.setObjectName("btn_AddTool")
        self.gridLayout_row2.addWidget(self.btn_AddTool, 0, 2, 1, 1)

        self.btn_STOP = QtWidgets.QPushButton(Dialog)
        self.btn_STOP.setGeometry(QtCore.QRect(840, 730, 95, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_STOP.sizePolicy().hasHeightForWidth())
        self.btn_STOP.setSizePolicy(sizePolicy)
        self.btn_STOP.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_STOP.setObjectName("btn_STOP")

        self.btn_Run = QtWidgets.QPushButton(Dialog)
        self.btn_Run.setGeometry(QtCore.QRect(940, 730, 95, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Run.sizePolicy().hasHeightForWidth())
        self.btn_Run.setSizePolicy(sizePolicy)
        self.btn_Run.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_Run.setObjectName("btn_Run")

        self.scrollArea_CAM = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_CAM.setGeometry(QtCore.QRect(10, 259, 821, 581))
        self.scrollArea_CAM.setWidgetResizable(True)
        self.scrollArea_CAM.setObjectName("scrollArea_CAM")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 819, 579))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_ShowCam = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_ShowCam.setGeometry(QtCore.QRect(5, 7, 811, 571))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ShowCam.sizePolicy().hasHeightForWidth())
        self.label_ShowCam.setSizePolicy(sizePolicy)
        self.label_ShowCam.setObjectName("label_ShowCam")
        self.scrollArea_CAM.setWidget(self.scrollAreaWidgetContents)

        self.gridLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(840, 260, 191, 461))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_setup = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_setup.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_setup.setObjectName("gridLayout_setup")
        self.textEdit_setup = QtWidgets.QTextEdit(self.gridLayoutWidget_3)
        self.textEdit_setup.setObjectName("textEdit_setup")
        self.gridLayout_setup.addWidget(self.textEdit_setup, 0, 0, 1, 1)


#####################################################################################
        self.btn_RefImage.clicked.connect(self.open_register)
        self.textEdit_Infor.setText("information")


















        #self.timer = QTimer()
        #self.timer.timeout.connect(self.viewCam)
        #self.controlTimer()
#####################################################################################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_IO.setText(_translate("Dialog", "I/O"))
        self.btn_GotoModeRun.setText(_translate("Dialog", "GO TO MODE RUN"))
        self.btn_FILE.setText(_translate("Dialog", "FILE"))
        self.btn_RefImage.setText(_translate("Dialog", "REF IMAGE"))
        self.btn_CameraSetting.setText(_translate("Dialog", "CAMERA SETTING"))
        self.textEdit_OK_NG.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:400; color:#000000;\">OK</span></p></body></html>"))
        self.btn_CAM2.setText(_translate("Dialog", "CAM 2"))
        self.btn_CAM1.setText(_translate("Dialog", "CAM 1"))
        self.btn_AddTool.setText(_translate("Dialog", "ADD TOOL"))
        self.btn_STOP.setText(_translate("Dialog", "STOP"))
        self.btn_Run.setText(_translate("Dialog", "RUN"))
        self.label_ShowCam.setText(_translate("Dialog", "TextLabel"))

#####################################################################################


    def open_register(self):
        self.timer.stop()
        camera.StopGrabbing()
        open_register_ui(self)

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
#####################################################################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
