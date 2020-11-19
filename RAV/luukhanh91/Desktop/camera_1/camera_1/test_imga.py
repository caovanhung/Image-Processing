# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_imga.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtGui import QIcon
#from detection_edges_xulyanh import*
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QRect, Qt
import os
import cv2
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(487, 348)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(120, 140, 120, 80))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 150, 200))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 150, 200))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.label.setScaledContents(1)
        self.Detection_edges_open_img()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
    def Detection_edges_open_img(self):
        file_goc=os.getcwd()
       # self.ten=self.Image_comboBox.currentText()
        file_config=file_goc.replace("/detection_edges","")
        self.file_img=file_config+"/"+"01.jpg"
      #  print(file_img)
        self.img=cv2.imread(self.file_img,1)
       # self.img_1=cv2.imread(self.file_img,1)
       # self.img=cv2.resize(self.img,(601, 531))
       # self.img_1=cv2.resize(self.img_1,(601, 531))
       # self.img_0=cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
       # self.img_10=cv2.cvtColor(self.img_1, cv2.COLOR_BGR2GRAY)

        height, width,channel = self.img.shape
        step =  width*channel
        qImg = QImage(self.img.data, width, height, step, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.label.setPixmap(QPixmap.fromImage(qImg))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

