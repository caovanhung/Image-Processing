# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detection_color.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_detecton_clor_Dialog(object):
    def setupUi(self, detecton_clor_Dialog):
        detecton_clor_Dialog.setObjectName("detecton_clor_Dialog")
        detecton_clor_Dialog.resize(886, 581)
        detecton_clor_Dialog.setBaseSize(QtCore.QSize(3, 3))
        self.pushButton = QtWidgets.QPushButton(detecton_clor_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 510, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(detecton_clor_Dialog)
        self.comboBox.setGeometry(QtCore.QRect(170, 510, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox = QtWidgets.QCheckBox(detecton_clor_Dialog)
        self.checkBox.setGeometry(QtCore.QRect(630, 170, 92, 23))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(detecton_clor_Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(750, 170, 92, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.tableWidget = QtWidgets.QTableWidget(detecton_clor_Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(610, 230, 256, 192))
        self.tableWidget.setBaseSize(QtCore.QSize(3, 3))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.xulyanh_pushButton = QtWidgets.QPushButton(detecton_clor_Dialog)
        self.xulyanh_pushButton.setGeometry(QtCore.QRect(320, 510, 89, 25))
        self.xulyanh_pushButton.setObjectName("xulyanh_pushButton")
        self.detect_color_run_pushButton = QtWidgets.QPushButton(detecton_clor_Dialog)
        self.detect_color_run_pushButton.setGeometry(QtCore.QRect(510, 510, 89, 25))
        self.detect_color_run_pushButton.setObjectName("detect_color_run_pushButton")
        self.scrollArea = QtWidgets.QScrollArea(detecton_clor_Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 591, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 589, 489))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(detecton_clor_Dialog)
        QtCore.QMetaObject.connectSlotsByName(detecton_clor_Dialog)

    def retranslateUi(self, detecton_clor_Dialog):
        _translate = QtCore.QCoreApplication.translate
        detecton_clor_Dialog.setWindowTitle(_translate("detecton_clor_Dialog", "Dialog"))
        self.pushButton.setText(_translate("detecton_clor_Dialog", "OK"))
        self.comboBox.setItemText(0, _translate("detecton_clor_Dialog", "01"))
        self.comboBox.setItemText(1, _translate("detecton_clor_Dialog", "02"))
        self.comboBox.setItemText(2, _translate("detecton_clor_Dialog", "03"))
        self.comboBox.setItemText(3, _translate("detecton_clor_Dialog", "04"))
        self.checkBox.setText(_translate("detecton_clor_Dialog", "GRB"))
        self.checkBox_2.setText(_translate("detecton_clor_Dialog", "HSV"))
        self.xulyanh_pushButton.setText(_translate("detecton_clor_Dialog", "Xuly"))
        self.detect_color_run_pushButton.setText(_translate("detecton_clor_Dialog", "RUN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    detecton_clor_Dialog = QtWidgets.QDialog()
    ui = Ui_detecton_clor_Dialog()
    ui.setupUi(detecton_clor_Dialog)
    detecton_clor_Dialog.show()
    sys.exit(app.exec_())

