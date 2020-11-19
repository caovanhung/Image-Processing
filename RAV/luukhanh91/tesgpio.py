# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_gpio.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


import RPi.GPIO as GPIO
import time

output_dc01 =17
output_dc02 =27
output_dc03 =22
output_dc04 =5


output_dc11 =6
output_dc12 =13
output_dc13 =19
output_dc14 =26


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(517, 416)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 80, 160, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_01 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_01.setObjectName("pushButton_01")
        self.verticalLayout.addWidget(self.pushButton_01)
        self.pushButton_02 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_02.setObjectName("pushButton_02")
        self.verticalLayout.addWidget(self.pushButton_02)
        self.pushButton_03 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_03.setObjectName("pushButton_03")
        self.verticalLayout.addWidget(self.pushButton_03)
        self.pushButton_04 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_04.setObjectName("pushButton_04")
        self.verticalLayout.addWidget(self.pushButton_04)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(280, 80, 160, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_2.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_2.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_2.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_2.addWidget(self.pushButton_14)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(output_dc01, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(output_dc02, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(output_dc03, GPIO.OUT, initial=GPIO.HIGH) 
        GPIO.setup(output_dc04, GPIO.OUT, initial=GPIO.HIGH) 
          


        GPIO.setup(output_dc11, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(output_dc12, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(output_dc13, GPIO.OUT, initial=GPIO.HIGH) 
        GPIO.setup(output_dc14, GPIO.OUT, initial=GPIO.HIGH)
        self.pushButton_01.clicked.connect(self.DC_1_E)
        self.pushButton_02.clicked.connect(self.DC_1_W)
        self.pushButton_03.clicked.connect(self.DC_1_N)
        self.pushButton_14.clicked.connect(self.DC_1_S)

        self.pushButton_11.clicked.connect(self.DC_2_E)
        self.pushButton_12.clicked.connect(self.DC_2_W)
        self.pushButton_13.clicked.connect(self.DC_2_N)
        self.pushButton_14.clicked.connect(self.DC_2_S)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_01.setText(_translate("Form", "01"))
        self.pushButton_02.setText(_translate("Form", "02"))
        self.pushButton_03.setText(_translate("Form", "03"))
        self.pushButton_04.setText(_translate("Form", "04"))
        self.pushButton_11.setText(_translate("Form", "11"))
        self.pushButton_12.setText(_translate("Form", "12"))
        self.pushButton_13.setText(_translate("Form", "13"))
        self.pushButton_14.setText(_translate("Form", "14"))
    
    def DC_1_E(self):
        GPIO.output(output_dc01,GPIO.LOW)
        GPIO.output(output_dc02,GPIO.HIGH)
        GPIO.output(output_dc03,GPIO.HIGH)
        GPIO.output(output_dc04,GPIO.HIGH)


    def DC_1_W(self):
        GPIO.output(output_dc01, GPIO.HIGH)
        GPIO.output(output_dc02,GPIO.LOW)
        GPIO.output(output_dc03,GPIO.HIGH)
        GPIO.output(output_dc04,GPIO.HIGH)


    def DC_1_N(self):
        GPIO.output(output_dc01, GPIO.HIGH)
        GPIO.output(output_dc02,GPIO.HIGH)
        GPIO.output(output_dc03,GPIO.LOW)
        GPIO.output(output_dc04,GPIO.HIGH)
    def DC_1_S(self):
        GPIO.output(output_dc01, GPIO.HIGH)
        GPIO.output(output_dc02,GPIO.HIGH)
        GPIO.output(output_dc03,GPIO.HIGH)
        GPIO.output(output_dc04,GPIO.LOW)



    def DC_2_E(self):
        GPIO.output(output_dc11, GPIO.LOW)
        GPIO.output(output_dc12,GPIO.HIGH)
        GPIO.output(output_dc13,GPIO.HIGH)
        GPIO.output(output_dc14,GPIO.HIGH)


    def DC_2_W(self):
        GPIO.output(output_dc11, GPIO.HIGH)
        GPIO.output(output_dc12,GPIO.LOW)
        GPIO.output(output_dc13,GPIO.HIGH)
        GPIO.output(output_dc14,GPIO.HIGH)


    def DC_2_N(self):
        GPIO.output(output_dc11, GPIO.HIGH)
        GPIO.output(output_dc12,GPIO.HIGH)
        GPIO.output(output_dc13,GPIO.LOW)
        GPIO.output(output_dc14,GPIO.HIGH)
    def DC_2_S(self):
        GPIO.output(output_dc11, GPIO.HIGH)
        GPIO.output(output_dc12,GPIO.HIGH)
        GPIO.output(output_dc13,GPIO.HIGH)
        GPIO.output(output_dc14,GPIO.LOW)     
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

