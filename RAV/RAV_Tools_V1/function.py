# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from dection_pixel.Threshold import*
#from detection_OCR.detection_OCR import*
#from detection_edges.detection_edges import*
#from Detection_QR_Code.Detection_QR_code import*
#from Edges_width.Edges_width import*
#from Edges_width.Edges_width_xulyanh import*

def dection_color_ui(self):
    self.Dialog_detection_color = QtWidgets.QDialog()
    self.ui_detection_color = Ui_detecton_clor_Dialog(0,'a')
    self.ui_detection_color.setupUi(self.Dialog_detection_color)
    self.Dialog_detection_color.show()
def dection_pixel_ui(self):
    self.Dialog_detection_pixel = QtWidgets.QDialog()
    self.ui_detection_pixel = Ui_Threshold_Dialog(0,'a')
    self.ui_detection_pixel.setupUi(self.Dialog_detection_pixel)
    self.Dialog_detection_pixel.show()
def detection_OCR_ui(self):
    self.Dialog_detection_OCR=QtWidgets.QDialog()
    self.ui_detection_OCR=Ui_Dialog_OCR(0,'a')
    self.ui_detection_OCR.setupUi(self.Dialog_detection_OCR)
    self.Dialog_detection_OCR.show()
def detection_edges_ui(self):
    self.detction_edges_Dialog=QtWidgets.QDialog()
    self.ui_detction_edges=Ui_Detection_edges_Dialog()
    self.ui_detction_edges.setupUi(self.detction_edges_Dialog)
    self.detction_edges_Dialog.show()
def detection_QR_ui(self):
    self.detection_QR_Dialog=QtWidgets.QDialog()
    self.ui_detection_QR=Ui_Detection_QR_code_Dialog()
    self.ui_detection_QR.setupUi(self.detection_QR_Dialog)
    self.detection_QR_Dialog.show()
def Edges_width_ui(self):
    self.Edges_width_Dialog=QtWidgets.QDialog()
    self.ui_Edges_width=Ui_Edges_width_Dialog()
    self.ui_Edges_width.setupUi(self.Edges_width_Dialog)
    self.Edges_width_Dialog.show()
    


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

        self.Detect_edges_pushButton.clicked.connect(self.detection_edges_show)
        self.Detect_pixel_pushButton.clicked.connect(self.detection_pixel_show)
        self.Detect_color_pushButton.clicked.connect(self.detection_color_show)        
        self.Detect_OCR_pushButton.clicked.connect(self.detection_OCR_show)   
        self.Detect_QR_pushButton.clicked.connect(self.detection_QR_show)
        self.Edges_width_pushButton.clicked.connect(self.Edges_width_show)
  #      self.Edges_width_pushButton.clicked.connect(self.detection_QR_show)

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

    def detection_color_show(self):
        dection_color_ui(self)
    def detection_pixel_show(self):
        dection_pixel_ui(self)
    def detection_OCR_show(self):
        detection_OCR_ui(self)
    def detection_edges_show(self):
        detection_edges_ui(self)
    def detection_QR_show(self):
        detection_QR_ui(self)
    def Edges_width_show(self):
        Edges_width_ui(self)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    function_Dialog = QtWidgets.QDialog()
    ui = Ui_function_Dialog()
    ui.setupUi(function_Dialog)
    function_Dialog.show()
    sys.exit(app.exec_())

