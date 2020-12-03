from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtGui import QIcon

from detection_circle_xuluanh import*
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QRect, Qt


from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
    qApp, QFileDialog

import tkinter as tk
root = tk.Tk()
width_px = int(root.winfo_screenwidth())
height_px = int(root.winfo_screenheight())

space_X = int(width_px/10)
space_Y = int(height_px/10)
space = 10
class Ui_Form_camera(object):
    def setupUi(self, Form_camera):
        Form_camera.setObjectName("Form_camera")
        #Form_camera.resize(1344, 905)
        Form_camera.resize(width_px, height_px)
        font = QtGui.QFont()
        font.setPointSize(30)
        Form_camera.setFont(font)

        #self.space_X = width_px/10
        #self.space_Y = height_px/10

        self.btn_RUN = QtWidgets.QPushButton(Form_camera)
        self.btn_RUN.setGeometry(QtCore.QRect((width_px-space_X*2), height_px-space_Y*2, space_X, space_Y))
        self.btn_RUN.setObjectName("btn_RUN")

        self.horizontalLayoutWidget = QtWidgets.QWidget(Form_camera)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(space_X,space_Y+space*3, space_X*6, space_Y))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.scrollArea_FUN = QtWidgets.QScrollArea(self.horizontalLayoutWidget)
        self.scrollArea_FUN.setWidgetResizable(True)
        self.scrollArea_FUN.setObjectName("scrollArea_FUN")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, space_X*6, space_Y))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_FUN.setBackgroundRole(QPalette.Dark)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_FUN.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.addWidget(self.scrollArea_FUN)

        self.scrollArea_show_cam = QtWidgets.QScrollArea(Form_camera)
        self.scrollArea_show_cam.setGeometry(QtCore.QRect(space, space_Y*3, space_X*7-space, space_Y*6))
        self.scrollArea_show_cam.setWidgetResizable(True)
        self.scrollArea_show_cam.setObjectName("scrollArea_show_cam")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, space_X*7-space, space_Y*6))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        #self.scrollArea_show_cam.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_show_cam.setBackgroundRole(QPalette.Dark)

        self.img_label=QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.img_label.setWordWrap(True)
        self.img_label.setObjectName("label")
        self.scrollArea_show_cam.setWidget(self.img_label)

        self.gridLayoutWidget = QtWidgets.QWidget(Form_camera)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(space_X*7+space, space_Y*3, 301, space_Y*3))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.btn_SET_RUN = QtWidgets.QPushButton(Form_camera)
        self.btn_SET_RUN.setGeometry(QtCore.QRect(width_px-space_X*3, space, space_X, space_Y))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_SET_RUN.setFont(font)
        self.btn_SET_RUN.setObjectName("btn_SET_RUN")

        self.label_stt_OK_NG = QtWidgets.QLabel(Form_camera)
        self.label_stt_OK_NG.setGeometry(QtCore.QRect(width_px-space_X*2, space, space_X, space_Y))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)

        self.label_stt_OK_NG.setFont(font)
        self.label_stt_OK_NG.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stt_OK_NG.setObjectName("label_stt_OK_NG")

        self.retranslateUi(Form_camera)
        QtCore.QMetaObject.connectSlotsByName(Form_camera)

    def retranslateUi(self, Form_camera):
        _translate = QtCore.QCoreApplication.translate
        Form_camera.setWindowTitle(_translate("Form_camera", "Form"))
        self.btn_RUN.setText(_translate("Form_camera", "RUN"))
        self.btn_SET_RUN.setText(_translate("Form_camera", "SET/RUN"))
        self.label_stt_OK_NG.setText(_translate("Form_camera", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_camera = QtWidgets.QWidget()
    ui = Ui_Form_camera()
    ui.setupUi(Form_camera)
    Form_camera.show()
    sys.exit(app.exec_())
