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
        Form_camera.resize(1117, 710)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form_camera)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 180, 811, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.img_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.img_label.setText("")
        self.img_label.setObjectName("img_label")
        self.verticalLayout.addWidget(self.img_label)
        self.OpenCamera_pushButton = QtWidgets.QPushButton(Form_camera)
        self.OpenCamera_pushButton.setGeometry(QtCore.QRect(60, 670, 91, 31))
        self.OpenCamera_pushButton.setObjectName("OpenCamera_pushButton")
        self.Register_pushButton = QtWidgets.QPushButton(Form_camera)
        self.Register_pushButton.setGeometry(QtCore.QRect(730, 670, 91, 31))
        self.Register_pushButton.setObjectName("Register_pushButton")
        self.fuction_pushButton = QtWidgets.QPushButton(Form_camera)
        self.fuction_pushButton.setGeometry(QtCore.QRect(20, 30, 191, 131))
        self.fuction_pushButton.setObjectName("fuction_pushButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form_camera)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(230, 30, 801, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(Form_camera)
        self.scrollArea.setGeometry(QtCore.QRect(250, 30, 799, 129))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 797, 127))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.Update_function_pushButton = QtWidgets.QPushButton(Form_camera)
        self.Update_function_pushButton.setGeometry(QtCore.QRect(380, 670, 91, 31))
        self.Update_function_pushButton.setObjectName("Update_function_pushButton")

        self.retranslateUi(Form_camera)
        QtCore.QMetaObject.connectSlotsByName(Form_camera)

    def retranslateUi(self, Form_camera):
        _translate = QtCore.QCoreApplication.translate
        Form_camera.setWindowTitle(_translate("Form_camera", "Form"))
        self.OpenCamera_pushButton.setText(_translate("Form_camera", "Open"))
        self.Register_pushButton.setText(_translate("Form_camera", "Register"))
        self.fuction_pushButton.setText(_translate("Form_camera", "Function"))
        self.Update_function_pushButton.setText(_translate("Form_camera", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_camera = QtWidgets.QWidget()
    ui = Ui_Form_camera()
    ui.setupUi(Form_camera)
    Form_camera.show()
    sys.exit(app.exec_())

