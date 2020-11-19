# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_camera(object):
    def setupUi(self, Form_camera):
        Form_camera.setObjectName("Form_camera")
        Form_camera.resize(718, 566)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form_camera)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 511, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.img_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.img_label.setText("")
        self.img_label.setObjectName("img_label")
        self.verticalLayout.addWidget(self.img_label)
        self.OpenCamera_pushButton = QtWidgets.QPushButton(Form_camera)
        self.OpenCamera_pushButton.setGeometry(QtCore.QRect(50, 520, 89, 25))
        self.OpenCamera_pushButton.setObjectName("OpenCamera_pushButton")
        self.Register_pushButton = QtWidgets.QPushButton(Form_camera)
        self.Register_pushButton.setGeometry(QtCore.QRect(330, 520, 89, 25))
        self.Register_pushButton.setObjectName("Register_pushButton")
        self.fuction_pushButton = QtWidgets.QPushButton(Form_camera)
        self.fuction_pushButton.setGeometry(QtCore.QRect(30, 70, 89, 25))
        self.fuction_pushButton.setObjectName("fuction_pushButton")

        self.retranslateUi(Form_camera)
        QtCore.QMetaObject.connectSlotsByName(Form_camera)
      
        
    def retranslateUi(self, Form_camera):
        _translate = QtCore.QCoreApplication.translate
        Form_camera.setWindowTitle(_translate("Form_camera", "Form"))
        self.OpenCamera_pushButton.setText(_translate("Form_camera", "Open"))
        self.Register_pushButton.setText(_translate("Form_camera", "Register"))
        self.fuction_pushButton.setText(_translate("Form_camera", "Function"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_camera = QtWidgets.QWidget()
    ui = Ui_Form_camera()
    ui.setupUi(Form_camera)
    Form_camera.show()
    sys.exit(app.exec_())

