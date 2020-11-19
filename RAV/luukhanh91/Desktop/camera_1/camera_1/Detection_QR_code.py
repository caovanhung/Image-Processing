from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtGui import QIcon


from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QRect, Qt

from Detection_QR_code_xulyanh import*
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
    qApp, QFileDialog
import os
import cv2
from pypylon import pylon

#camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

class Detection_QR_code_MyLabel(QLabel):

     x0 = 0
     y0 = 0
     x1 = 0
     y1 = 0
     flag = False
     dk=0
     
 #Mouse click event
     def mousePressEvent(self,event):
        if self.dk:

          self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()
 #Mouse release event
     def mouseReleaseEvent(self,event):
          if self.dk:
             self.flag = False
 #Mouse movement events
     def mouseMoveEvent(self,event):
        if self.flag and self.dk:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()
     def setfdk(self,flag):
          self.dk=flag
     def getdk(self):
          return self.dk;
      #Draw events
     def paintEvent(self, event):
          
     
          super().paintEvent(event)
          rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
       # print(self.x1)
          painter = QPainter(self)
          if self.dk:
             painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
             painter.drawRect(rect)
class Ui_Detection_QR_code_Dialog(object):
    def setupUi(self, Detection_QR_code_Dialog):
        Detection_QR_code_Dialog.setObjectName("Detection_QR_code_Dialog")
        Detection_QR_code_Dialog.resize(1061, 678)
        self.scrollArea = QtWidgets.QScrollArea(Detection_QR_code_Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 10, 751, 591))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 749, 589))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        #self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Detection_QR_code_Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 610, 231, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.detection_QR_OK_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.detection_QR_OK_pushButton.setObjectName("detection_QR_OK_pushButton")
        self.horizontalLayout.addWidget(self.detection_QR_OK_pushButton)
        self.detection_QR_img_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.detection_QR_img_comboBox.setObjectName("detection_QR_img_comboBox")
        self.detection_QR_img_comboBox.addItem("")
        self.detection_QR_img_comboBox.addItem("")
        self.detection_QR_img_comboBox.addItem("")
        self.detection_QR_img_comboBox.addItem("")
        self.detection_QR_img_comboBox.addItem("")
        self.detection_QR_img_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.detection_QR_img_comboBox)
        self.pushButton = QtWidgets.QPushButton(Detection_QR_code_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(510, 610, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(Detection_QR_code_Dialog)
        self.groupBox.setGeometry(QtCore.QRect(760, 50, 301, 441))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 281, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.Detection_QR_Kernel_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.Detection_QR_Kernel_comboBox.setObjectName("Detection_QR_Kernel_comboBox")
        self.Detection_QR_Kernel_comboBox.addItem("")
        self.Detection_QR_Kernel_comboBox.addItem("")
        self.Detection_QR_Kernel_comboBox.addItem("")
        self.Detection_QR_Kernel_comboBox.addItem("")
        self.Detection_QR_Kernel_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.Detection_QR_Kernel_comboBox)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 80, 281, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.Detection_QR_Filter_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.Detection_QR_Filter_comboBox.setObjectName("Detection_QR_Filter_comboBox")
        self.Detection_QR_Filter_comboBox.addItem("")
        self.Detection_QR_Filter_comboBox.addItem("")
        self.Detection_QR_Filter_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.Detection_QR_Filter_comboBox)
        self.Detection_bar_code_tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.Detection_bar_code_tableWidget.setGeometry(QtCore.QRect(10, 150, 281, 81))
        self.Detection_bar_code_tableWidget.setObjectName("Detection_bar_code_tableWidget")
        self.Detection_bar_code_tableWidget.setColumnCount(0)
        self.Detection_bar_code_tableWidget.setRowCount(0)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 250, 281, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Detection_QR_code_SAVE_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Detection_QR_code_SAVE_pushButton.setObjectName("Detection_QR_code_SAVE_pushButton")
        self.horizontalLayout_4.addWidget(self.Detection_QR_code_SAVE_pushButton)
        self.Detection_QR_code_RESET_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Detection_QR_code_RESET_pushButton.setObjectName("Detection_QR_code_RESET_pushButton")
        self.horizontalLayout_4.addWidget(self.Detection_QR_code_RESET_pushButton)

        
        self.img_detection_QR_code=Detection_QR_code_MyLabel(self.scrollAreaWidgetContents)
        self.scrollArea.setBackgroundRole(QPalette.Dark)#THEM DONG
        self.img_detection_QR_code.setWordWrap(True)
        self.img_detection_QR_code.setObjectName("label")
        self.scrollArea.setWidget(self.img_detection_QR_code)# dong quan trong
        self.detection_QR_OK_pushButton.clicked.connect(self.Detection_QR_code_open_img)


        self.retranslateUi(Detection_QR_code_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Detection_QR_code_Dialog)

    def retranslateUi(self, Detection_QR_code_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Detection_QR_code_Dialog.setWindowTitle(_translate("Detection_QR_code_Dialog", "Dialog"))
        self.detection_QR_OK_pushButton.setText(_translate("Detection_QR_code_Dialog", "OK"))
        self.detection_QR_img_comboBox.setItemText(0, _translate("Detection_QR_code_Dialog", "01"))
        self.detection_QR_img_comboBox.setItemText(1, _translate("Detection_QR_code_Dialog", "02"))
        self.detection_QR_img_comboBox.setItemText(2, _translate("Detection_QR_code_Dialog", "03"))
        self.detection_QR_img_comboBox.setItemText(3, _translate("Detection_QR_code_Dialog", "04"))
        self.detection_QR_img_comboBox.setItemText(4, _translate("Detection_QR_code_Dialog", "05"))
        self.detection_QR_img_comboBox.setItemText(5, _translate("Detection_QR_code_Dialog", "06"))
        self.pushButton.setText(_translate("Detection_QR_code_Dialog", "RUN"))
        self.groupBox.setTitle(_translate("Detection_QR_code_Dialog", "SET UP"))
        self.label.setText(_translate("Detection_QR_code_Dialog", "KERNEL"))
        self.Detection_QR_Kernel_comboBox.setItemText(0, _translate("Detection_QR_code_Dialog", "3X3"))
        self.Detection_QR_Kernel_comboBox.setItemText(1, _translate("Detection_QR_code_Dialog", "5X5"))
        self.Detection_QR_Kernel_comboBox.setItemText(2, _translate("Detection_QR_code_Dialog", "7X7"))
        self.Detection_QR_Kernel_comboBox.setItemText(3, _translate("Detection_QR_code_Dialog", "11X11"))
        self.Detection_QR_Kernel_comboBox.setItemText(4, _translate("Detection_QR_code_Dialog", "13x13"))
        self.label_2.setText(_translate("Detection_QR_code_Dialog", "FILTER"))
        self.Detection_QR_Filter_comboBox.setItemText(0, _translate("Detection_QR_code_Dialog", "Averaging"))
        self.Detection_QR_Filter_comboBox.setItemText(1, _translate("Detection_QR_code_Dialog", "Gaussian Filtering"))
        self.Detection_QR_Filter_comboBox.setItemText(2, _translate("Detection_QR_code_Dialog", "Median Filtering"))
        self.Detection_QR_code_SAVE_pushButton.setText(_translate("Detection_QR_code_Dialog", "SAVE"))
        self.Detection_QR_code_RESET_pushButton.setText(_translate("Detection_QR_code_Dialog", "RESET"))

    def Detection_QR_code_open_img(self):
        file_goc=os.getcwd()
        self.ten=self.detection_QR_img_comboBox.currentText()
        file_config=file_goc.replace("/detection_edges","")
        self.file_img=file_config+"/"+self.ten+".jpg"
        self.img=cv2.imread(self.file_img,1)
        self.img_1=cv2.imread(self.file_img,1)

        self.img_0=cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.img_10=cv2.cvtColor(self.img_1, cv2.COLOR_BGR2GRAY)

        height, width,channel = self.img.shape
        step =  width*channel
        qImg = QImage(self.img.data, width, height, step, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.img_detection_QR_code.setPixmap(QPixmap.fromImage(qImg))
        self.img_detection_QR_code.setCursor(QtCore.Qt.CrossCursor)
        self.img_detection_QR_code.setfdk(1)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Detection_QR_code_Dialog = QtWidgets.QDialog()
    ui = Ui_Detection_QR_code_Dialog()
    ui.setupUi(Detection_QR_code_Dialog)
    Detection_QR_code_Dialog.show()
    sys.exit(app.exec_())

