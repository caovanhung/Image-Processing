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
class Ui_Form_camera(object):
    def setupUi(self, Form_camera):
        Form_camera.setObjectName("Form_camera")
        Form_camera.resize(1061, 708)
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
        self.scrollArea_2 = QtWidgets.QScrollArea(Form_camera)
        self.scrollArea_2.setGeometry(QtCore.QRect(250, 30, 799, 129))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 797, 127))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.Update_function_pushButton = QtWidgets.QPushButton(Form_camera)
        self.Update_function_pushButton.setGeometry(QtCore.QRect(380, 670, 91, 31))
        self.Update_function_pushButton.setObjectName("Update_function_pushButton")
        self.scrollArea = QtWidgets.QScrollArea(Form_camera)
        self.scrollArea.setGeometry(QtCore.QRect(20, 180, 871, 471))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 869, 469))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        #self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.img_label=QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.scrollArea.setBackgroundRole(QPalette.Dark)#THEM DONG
        self.img_label.setWordWrap(True)
        self.img_label.setObjectName("label")


        
        self.scrollArea.setWidget(self.img_label)# dong quan trong
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

