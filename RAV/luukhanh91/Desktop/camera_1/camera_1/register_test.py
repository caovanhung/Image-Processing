# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_register_Dialog(object):
    def setupUi(self, register_Dialog):
        register_Dialog.setObjectName("register_Dialog")
        register_Dialog.resize(749, 598)
        self.verticalLayoutWidget = QtWidgets.QWidget(register_Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 581, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.re_img_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.re_img_label.setText("")
        self.re_img_label.setObjectName("re_img_label")
        self.verticalLayout.addWidget(self.re_img_label)
        self.re_Save_pushButton = QtWidgets.QPushButton(register_Dialog)
        self.re_Save_pushButton.setGeometry(QtCore.QRect(0, 530, 89, 25))
        self.re_Save_pushButton.setObjectName("re_Save_pushButton")
        self.comboBox = QtWidgets.QComboBox(register_Dialog)
        self.comboBox.setGeometry(QtCore.QRect(240, 530, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.Test_textEdit = QtWidgets.QTextEdit(register_Dialog)
        self.Test_textEdit.setGeometry(QtCore.QRect(590, 340, 151, 70))
        self.Test_textEdit.setObjectName("Test_textEdit")
        self.Close_pushButton = QtWidgets.QPushButton(register_Dialog)
        self.Close_pushButton.setGeometry(QtCore.QRect(470, 530, 89, 25))
        self.Close_pushButton.setObjectName("Close_pushButton")

        self.retranslateUi(register_Dialog)
        QtCore.QMetaObject.connectSlotsByName(register_Dialog)

    def retranslateUi(self, register_Dialog):
        _translate = QtCore.QCoreApplication.translate
        register_Dialog.setWindowTitle(_translate("register_Dialog", "Dialog"))
        self.re_Save_pushButton.setText(_translate("register_Dialog", "Save"))
        self.comboBox.setItemText(0, _translate("register_Dialog", "01"))
        self.comboBox.setItemText(1, _translate("register_Dialog", "02"))
        self.comboBox.setItemText(2, _translate("register_Dialog", "03"))
        self.comboBox.setItemText(3, _translate("register_Dialog", "04"))
        self.Close_pushButton.setText(_translate("register_Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_Dialog = QtWidgets.QDialog()
    ui = Ui_register_Dialog()
    ui.setupUi(register_Dialog)
    register_Dialog.show()
    sys.exit(app.exec_())

