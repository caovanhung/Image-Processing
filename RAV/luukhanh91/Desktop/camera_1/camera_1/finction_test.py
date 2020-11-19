# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fuction_Dialog(object):
    def setupUi(self, fuction_Dialog):
        fuction_Dialog.setObjectName("fuction_Dialog")
        fuction_Dialog.resize(400, 300)
        self.funnction_pushButton = QtWidgets.QPushButton(fuction_Dialog)
        self.funnction_pushButton.setGeometry(QtCore.QRect(60, 80, 111, 25))
        self.funnction_pushButton.setObjectName("funnction_pushButton")
        self.pushButton = QtWidgets.QPushButton(fuction_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 130, 111, 25))
        self.pushButton.setObjectName("pushButton")
        self.Detect_OCR_pushButton = QtWidgets.QPushButton(fuction_Dialog)
        self.Detect_OCR_pushButton.setGeometry(QtCore.QRect(60, 180, 111, 25))
        self.Detect_OCR_pushButton.setObjectName("Detect_OCR_pushButton")

        self.retranslateUi(fuction_Dialog)
        QtCore.QMetaObject.connectSlotsByName(fuction_Dialog)

    def retranslateUi(self, fuction_Dialog):
        _translate = QtCore.QCoreApplication.translate
        fuction_Dialog.setWindowTitle(_translate("fuction_Dialog", "Dialog"))
        self.funnction_pushButton.setText(_translate("fuction_Dialog", "Detect_color"))
        self.pushButton.setText(_translate("fuction_Dialog", "Detect_pixel"))
        self.Detect_OCR_pushButton.setText(_translate("fuction_Dialog", "Detect_OCR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fuction_Dialog = QtWidgets.QDialog()
    ui = Ui_fuction_Dialog()
    ui.setupUi(fuction_Dialog)
    fuction_Dialog.show()
    sys.exit(app.exec_())

