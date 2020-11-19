# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from detection_color import*
def dection_color_ui(self):
    self.Dialog_detection_color = QtWidgets.QDialog()
    self.ui_detection_color = Ui_detecton_clor_Dialog()
    self.ui_detection_color.setupUi(self.Dialog_detection_color)
    self.Dialog_detection_color.show()

class Ui_fuction_Dialog(object):
    def setupUi(self, fuction_Dialog):
        fuction_Dialog.setObjectName("fuction_Dialog")
        fuction_Dialog.resize(400, 300)
        self.funnction_pushButton = QtWidgets.QPushButton(fuction_Dialog)
        self.funnction_pushButton.setGeometry(QtCore.QRect(120, 80, 89, 25))
        self.funnction_pushButton.setObjectName("funnction_pushButton")
        
        self.funnction_pushButton.clicked.connect(self.detection_color_show)
        self.retranslateUi(fuction_Dialog)
        QtCore.QMetaObject.connectSlotsByName(fuction_Dialog)

    def retranslateUi(self, fuction_Dialog):
        _translate = QtCore.QCoreApplication.translate
        fuction_Dialog.setWindowTitle(_translate("fuction_Dialog", "Dialog"))
        self.funnction_pushButton.setText(_translate("fuction_Dialog", "function_1"))
    def detection_color_show(self):
        dection_color_ui(self)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fuction_Dialog = QtWidgets.QDialog()
    ui = Ui_fuction_Dialog()
    ui.setupUi(fuction_Dialog)
    fuction_Dialog.show()
    sys.exit(app.exec_())

