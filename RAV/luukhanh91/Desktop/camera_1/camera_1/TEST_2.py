# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TEST_2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
    qApp, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(574, 537)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(20, 60, 531, 431))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 529, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.scrollArea.setBackgroundRole(QPalette.Dark)


        self.Zoom_in_pushButton = QtWidgets.QPushButton(Dialog)
        self.Zoom_in_pushButton.setGeometry(QtCore.QRect(30, 10, 89, 25))
        self.Zoom_in_pushButton.setObjectName("Zoom_in_pushButton")
        self.Zoom_out_pushButton = QtWidgets.QPushButton(Dialog)
        self.Zoom_out_pushButton.setGeometry(QtCore.QRect(150, 10, 89, 25))
        self.Zoom_out_pushButton.setObjectName("Zoom_out_pushButton")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 10, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.scale_textEdit = QtWidgets.QTextEdit(Dialog)
        self.scale_textEdit.setGeometry(QtCore.QRect(360, 9, 104, 31))
        self.scale_textEdit.setObjectName("scale_textEdit")




        self.label.setGeometry(QtCore.QRect(15, 10, 151, 101))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")


        self.scrollArea.setWidget(self.label)
        self.Detection_edges_open_img()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def Detection_edges_open_img(self):
        file_goc=os.getcwd()
       # self.ten=self.Image_comboBox.currentText()
        file_config=file_goc.replace("/detection_edges","")
        self.file_img=file_config+"/"+"Image__2020-09-18__10-32-43.bmp"
      #  print(file_img)
        self.img=cv2.imread(self.file_img,1)

        print (self.img)
        height, width,channel = self.img.shape
        step =  width*channel
        qImg = QImage(self.img.data, width, height, step, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.label.setPixmap(QPixmap.fromImage(qImg))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

