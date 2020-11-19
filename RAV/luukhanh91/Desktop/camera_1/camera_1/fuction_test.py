# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_function_Dialog(object):
    def setupUi(self, function_Dialog):
        function_Dialog.setObjectName("function_Dialog")
        function_Dialog.resize(828, 459)
        self.verticalLayoutWidget = QtWidgets.QWidget(function_Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 401, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Detect_edges_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Detect_edges_pushButton.setObjectName("Detect_edges_pushButton")
        self.verticalLayout.addWidget(self.Detect_edges_pushButton)
        self.Detect_pixel_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Detect_pixel_pushButton.setObjectName("Detect_pixel_pushButton")
        self.verticalLayout.addWidget(self.Detect_pixel_pushButton)
        self.Detect_color_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Detect_color_pushButton.setObjectName("Detect_color_pushButton")
        self.verticalLayout.addWidget(self.Detect_color_pushButton)
        self.Detect_OCR_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Detect_OCR_pushButton.setObjectName("Detect_OCR_pushButton")
        self.verticalLayout.addWidget(self.Detect_OCR_pushButton)
        self.Detect_QR_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Detect_QR_pushButton.setObjectName("Detect_QR_pushButton")
        self.verticalLayout.addWidget(self.Detect_QR_pushButton)
        self.Edges_width_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Edges_width_pushButton.setObjectName("Edges_width_pushButton")
        self.verticalLayout.addWidget(self.Edges_width_pushButton)

        self.retranslateUi(function_Dialog)
        QtCore.QMetaObject.connectSlotsByName(function_Dialog)

    def retranslateUi(self, function_Dialog):
        _translate = QtCore.QCoreApplication.translate
        function_Dialog.setWindowTitle(_translate("function_Dialog", "Dialog"))
        self.Detect_edges_pushButton.setText(_translate("function_Dialog", "Detect_edges"))
        self.Detect_pixel_pushButton.setText(_translate("function_Dialog", "Detect_pixel"))
        self.Detect_color_pushButton.setText(_translate("function_Dialog", "Detect_color"))
        self.Detect_OCR_pushButton.setText(_translate("function_Dialog", "Detect_OCR"))
        self.Detect_QR_pushButton.setText(_translate("function_Dialog", "Detect_QR"))
        self.Edges_width_pushButton.setText(_translate("function_Dialog", "Edges_width"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    function_Dialog = QtWidgets.QDialog()
    ui = Ui_function_Dialog()
    ui.setupUi(function_Dialog)
    function_Dialog.show()
    sys.exit(app.exec_())

