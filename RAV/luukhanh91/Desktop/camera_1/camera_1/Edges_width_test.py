from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtGui import QIcon


from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QRect, Qt

from Edges_width_xulyanh import*
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
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
import os
class Edges_width_MyLabel(QLabel):

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


class Ui_Edges_width_Dialog(object):
    def setupUi(self, Edges_width_Dialog):
        Edges_width_Dialog.setObjectName("Edges_width_Dialog")
        Edges_width_Dialog.resize(1060, 662)
        self.scrollArea = QtWidgets.QScrollArea(Edges_width_Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 10, 691, 571))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 689, 569))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
      #  self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.Edges_width_OK_pushButton = QtWidgets.QPushButton(Edges_width_Dialog)
        self.Edges_width_OK_pushButton.setGeometry(QtCore.QRect(10, 600, 89, 25))
        self.Edges_width_OK_pushButton.setObjectName("Edges_width_OK_pushButton")
        self.Edges_with_img_comboBox = QtWidgets.QComboBox(Edges_width_Dialog)
        self.Edges_with_img_comboBox.setGeometry(QtCore.QRect(160, 600, 86, 25))
        self.Edges_with_img_comboBox.setObjectName("Edges_with_img_comboBox")
        self.Edges_with_img_comboBox.addItem("")
        self.Edges_with_img_comboBox.addItem("")
        self.Edges_with_img_comboBox.addItem("")
        self.Edges_with_img_comboBox.addItem("")
        self.Edges_with_img_comboBox.addItem("")
        self.Edges_with_img_comboBox.addItem("")
        self.Edges_width_RUN_pushButton = QtWidgets.QPushButton(Edges_width_Dialog)
        self.Edges_width_RUN_pushButton.setGeometry(QtCore.QRect(420, 590, 151, 61))
        self.Edges_width_RUN_pushButton.setObjectName("Edges_width_RUN_pushButton")
        self.SET_UP_groupBox = QtWidgets.QGroupBox(Edges_width_Dialog)
        self.SET_UP_groupBox.setGeometry(QtCore.QRect(700, 0, 331, 651))
        self.SET_UP_groupBox.setObjectName("SET_UP_groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.SET_UP_groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 331, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Edges_width_KERNEL_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.Edges_width_KERNEL_comboBox.setObjectName("Edges_width_KERNEL_comboBox")
        self.Edges_width_KERNEL_comboBox.addItem("")
        self.Edges_width_KERNEL_comboBox.addItem("")
        self.Edges_width_KERNEL_comboBox.addItem("")
        self.Edges_width_KERNEL_comboBox.addItem("")
        self.Edges_width_KERNEL_comboBox.addItem("")
        self.Edges_width_KERNEL_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.Edges_width_KERNEL_comboBox)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.SET_UP_groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 80, 331, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Edges_width_FILTER_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.Edges_width_FILTER_comboBox.setObjectName("Edges_width_FILTER_comboBox")
        self.Edges_width_FILTER_comboBox.addItem("")
        self.Edges_width_FILTER_comboBox.addItem("")
        self.Edges_width_FILTER_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.Edges_width_FILTER_comboBox)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.SET_UP_groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 110, 331, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.Edges_width_high_level_horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.Edges_width_high_level_horizontalSlider.setMaximum(255)
        self.Edges_width_high_level_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Edges_width_high_level_horizontalSlider.setObjectName("Edges_width_high_level_horizontalSlider")
        self.verticalLayout.addWidget(self.Edges_width_high_level_horizontalSlider)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.SET_UP_groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 160, 331, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.Edges_with_LOW_LEVEL_horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.Edges_with_LOW_LEVEL_horizontalSlider.setMaximum(255)
        self.Edges_with_LOW_LEVEL_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Edges_with_LOW_LEVEL_horizontalSlider.setObjectName("Edges_with_LOW_LEVEL_horizontalSlider")
        self.verticalLayout_2.addWidget(self.Edges_with_LOW_LEVEL_horizontalSlider)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.SET_UP_groupBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 210, 331, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.Edges_width_DERECTION_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.Edges_width_DERECTION_comboBox.setObjectName("Edges_width_DERECTION_comboBox")
        self.Edges_width_DERECTION_comboBox.addItem("")
        self.Edges_width_DERECTION_comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.Edges_width_DERECTION_comboBox)
        self.Edges_width_tableWidget = QtWidgets.QTableWidget(self.SET_UP_groupBox)
        self.Edges_width_tableWidget.setGeometry(QtCore.QRect(0, 490, 331, 111))
        self.Edges_width_tableWidget.setObjectName("Edges_width_tableWidget")
        self.Edges_width_tableWidget.setColumnCount(0)
        self.Edges_width_tableWidget.setRowCount(0)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.SET_UP_groupBox)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(40, 600, 261, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Edges_width_SAVE_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.Edges_width_SAVE_pushButton.setObjectName("Edges_width_SAVE_pushButton")
        self.horizontalLayout_6.addWidget(self.Edges_width_SAVE_pushButton)
        self.Edges_width_RESET_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.Edges_width_RESET_pushButton.setObjectName("Edges_width_RESET_pushButton")
        self.horizontalLayout_6.addWidget(self.Edges_width_RESET_pushButton)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.SET_UP_groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 260, 331, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.Edges_width_number_pixel_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.Edges_width_number_pixel_spinBox.setObjectName("Edges_width_number_pixel_spinBox")
        self.horizontalLayout_3.addWidget(self.Edges_width_number_pixel_spinBox)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.SET_UP_groupBox)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(0, 360, 331, 41))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.Edges_width_Sensitivity_horizontalSlider = QtWidgets.QSlider(self.horizontalLayoutWidget_7)
        self.Edges_width_Sensitivity_horizontalSlider.setMaximum(100)
        self.Edges_width_Sensitivity_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Edges_width_Sensitivity_horizontalSlider.setObjectName("Edges_width_Sensitivity_horizontalSlider")
        self.horizontalLayout_7.addWidget(self.Edges_width_Sensitivity_horizontalSlider)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.SET_UP_groupBox)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 310, 331, 41))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.Edge_width_threshold_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_8)
        self.Edge_width_threshold_spinBox.setObjectName("Edge_width_threshold_spinBox")
        self.horizontalLayout_8.addWidget(self.Edge_width_threshold_spinBox)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.SET_UP_groupBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 450, 331, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.Edges_width_Position_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.Edges_width_Position_comboBox.setObjectName("Edges_width_Position_comboBox")
        self.Edges_width_Position_comboBox.addItem("")
        self.Edges_width_Position_comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.Edges_width_Position_comboBox)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.SET_UP_groupBox)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(0, 400, 331, 41))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.Edge_width_Edge_1_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_9)
        self.Edge_width_Edge_1_spinBox.setObjectName("Edge_width_Edge_1_spinBox")
        self.horizontalLayout_9.addWidget(self.Edge_width_Edge_1_spinBox)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.Edge_width_Edge_2spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_9)
        self.Edge_width_Edge_2spinBox.setObjectName("Edge_width_Edge_2spinBox")
        self.horizontalLayout_9.addWidget(self.Edge_width_Edge_2spinBox)



        self.img_Edges_width_label=Edges_width_MyLabel(self.scrollAreaWidgetContents)
        self.scrollArea.setBackgroundRole(QPalette.Dark)#THEM DONG
        self.img_Edges_width_label.setWordWrap(True)
        self.img_Edges_width_label.setObjectName("label")
        self.scrollArea.setWidget(self.img_Edges_width_label)
        self.timer = QTimer()
        self.timer.timeout.connect(self.Edges_width_viewCam)
        self.Edges_width_RUN_pushButton.clicked.connect(self.Edges_width_controlTimer)

        self.Edges_width_OK_pushButton.clicked.connect(self.Edges_width_open_img)
        self.Edges_with_LOW_LEVEL_horizontalSlider.valueChanged.connect(self.Edges_width_bar)
        self.Edges_width_high_level_horizontalSlider.valueChanged.connect(self.Edges_width_bar)

        self.Edges_width_SAVE_pushButton.clicked.connect(self.find_counter)



        self.retranslateUi(Edges_width_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Edges_width_Dialog)

    def retranslateUi(self, Edges_width_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Edges_width_Dialog.setWindowTitle(_translate("Edges_width_Dialog", "Dialog"))
        self.Edges_width_OK_pushButton.setText(_translate("Edges_width_Dialog", "OK"))
        self.Edges_with_img_comboBox.setItemText(0, _translate("Edges_width_Dialog", "01"))
        self.Edges_with_img_comboBox.setItemText(1, _translate("Edges_width_Dialog", "02"))
        self.Edges_with_img_comboBox.setItemText(2, _translate("Edges_width_Dialog", "03"))
        self.Edges_with_img_comboBox.setItemText(3, _translate("Edges_width_Dialog", "04"))
        self.Edges_with_img_comboBox.setItemText(4, _translate("Edges_width_Dialog", "05"))
        self.Edges_with_img_comboBox.setItemText(5, _translate("Edges_width_Dialog", "05"))
        self.Edges_width_RUN_pushButton.setText(_translate("Edges_width_Dialog", "RUN"))
        self.SET_UP_groupBox.setTitle(_translate("Edges_width_Dialog", "SET UP"))
        self.label.setText(_translate("Edges_width_Dialog", "KERNEL"))
        self.Edges_width_KERNEL_comboBox.setItemText(0, _translate("Edges_width_Dialog", "3X3"))
        self.Edges_width_KERNEL_comboBox.setItemText(1, _translate("Edges_width_Dialog", "5X5"))
        self.Edges_width_KERNEL_comboBox.setItemText(2, _translate("Edges_width_Dialog", "7X7"))
        self.Edges_width_KERNEL_comboBox.setItemText(3, _translate("Edges_width_Dialog", "9X9"))
        self.Edges_width_KERNEL_comboBox.setItemText(4, _translate("Edges_width_Dialog", "11X11"))
        self.Edges_width_KERNEL_comboBox.setItemText(5, _translate("Edges_width_Dialog", "13X13"))
        self.label_2.setText(_translate("Edges_width_Dialog", "FILTER"))
        self.Edges_width_FILTER_comboBox.setItemText(0, _translate("Edges_width_Dialog", "Averaging"))
        self.Edges_width_FILTER_comboBox.setItemText(1, _translate("Edges_width_Dialog", "Gaussian Filtering"))
        self.Edges_width_FILTER_comboBox.setItemText(2, _translate("Edges_width_Dialog", "Median Filtering"))
        self.label_3.setText(_translate("Edges_width_Dialog", "                                    HIGH LEVEL"))
        self.label_5.setText(_translate("Edges_width_Dialog", "                                   LOW LEVEL"))
        self.label_6.setText(_translate("Edges_width_Dialog", "DIRECTION"))
        self.Edges_width_DERECTION_comboBox.setItemText(0, _translate("Edges_width_Dialog", "OX"))
        self.Edges_width_DERECTION_comboBox.setItemText(1, _translate("Edges_width_Dialog", "OY"))
        self.Edges_width_SAVE_pushButton.setText(_translate("Edges_width_Dialog", "SAVE"))
        self.Edges_width_RESET_pushButton.setText(_translate("Edges_width_Dialog", "RESET"))
        self.label_4.setText(_translate("Edges_width_Dialog", "NUMBER PIXEL DETECTED "))
        self.label_7.setText(_translate("Edges_width_Dialog", "Edge sensitivity(%)"))
        self.label_9.setText(_translate("Edges_width_Dialog", "Edge threshold "))
        self.label_8.setText(_translate("Edges_width_Dialog", "POSITION"))
        self.Edges_width_Position_comboBox.setItemText(0, _translate("Edges_width_Dialog", "MAX"))
        self.Edges_width_Position_comboBox.setItemText(1, _translate("Edges_width_Dialog", "MIN"))
        self.label_10.setText(_translate("Edges_width_Dialog", "Edge1"))
        self.label_11.setText(_translate("Edges_width_Dialog", "Edge2"))

    def Edges_width_open_img(self):
        file_goc=os.getcwd()
        self.ten=self.Edges_with_img_comboBox.currentText()
        file_config=file_goc.replace("/Edges_width","")
        self.file_img=file_config+"/"+self.ten+".jpg"
        self.img=cv2.imread(self.file_img,1)
        self.img_1=cv2.imread(self.file_img,1)
        self.img_0=cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.img_10=cv2.cvtColor(self.img_1, cv2.COLOR_BGR2GRAY)

        height, width,channel = self.img.shape
        step =  width*channel
        qImg = QImage(self.img.data, width, height, step, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.img_Edges_width_label.setPixmap(QPixmap.fromImage(qImg))
        self.img_Edges_width_label.setCursor(QtCore.Qt.CrossCursor)
        self.img_Edges_width_label.setfdk(1)
    def Edges_width_bar(self):
        if  self.img_Edges_width_label.x0 and self.img_Edges_width_label.x1 and self.img_Edges_width_label.y0 and self.img_Edges_width_label.y1 :
            self.x00=self.img_Edges_width_label.x0
            self.x10=self.img_Edges_width_label.x1
            self.y00=self.img_Edges_width_label.y0
            self.y10=self.img_Edges_width_label.y1
            self.img_edges_width=Edges_width_xulyanh(self.img_0,self.img_10,self.x00,self.y00,self.x10,self.y10)
            self.ten_Filter=self.Edges_width_FILTER_comboBox.currentText()
            self.ten_Kernel=self.Edges_width_KERNEL_comboBox.currentText()
          #  print(self.ten_Filter)
           # print(self.ten_Kernel)
            self.img_edges_width.filter_img(self.ten_Filter,self.ten_Kernel)
           # self.ten_category=self.Egdes_with_Category_comboBox.currentText()
            self.lowlevel_value=self.Edges_with_LOW_LEVEL_horizontalSlider.value()
            self.highlevel_value=self.Edges_width_high_level_horizontalSlider.value()
            self.img_edges_width.edges_img(self.lowlevel_value,self.highlevel_value)
            self.img_cuoi=self.img_edges_width.get_img()
                
            height, width  =self.img_cuoi.shape
            step = width
            qImg = QImage(self.img_cuoi.data, width, height, step, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qImg)
            self.img_Edges_width_label.setPixmap(QPixmap.fromImage(qImg))

    def find_counter(self):

         file_goc=os.getcwd()
         self.ten=self.Edges_with_img_comboBox.currentText()
         file_config=file_goc.replace("/Edges_width","")
         self.file_img=file_config+"/"+self.ten+".jpg"
         img_1=cv2.imread(self.file_img,1)
         cv2.rectangle(img_1,(self.x00,self.y00),(self.x10,self.y10),(0,255,0),3) 
         self.img_xuly=self.img_edges_width.edges_count_1(img_1,"OX")
         height, width,channel = self.img_xuly.shape
         step =  width*channel
         qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.img_Edges_width_label.setPixmap(QPixmap.fromImage(qImg))
         self.img_Edges_width_label.setCursor(QtCore.Qt.CrossCursor)
         self.img_Edges_width_label.setfdk(0)
    def Edges_width_controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            # start timer
            self.timer.start(20)
            self.Edges_width_RUN_pushButton.setText("Stop")
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            camera.StopGrabbing()
            # update control_bt text
            self.Edges_width_RUN_pushButton.setText("RUN")
           # self.Threshold_comboBox.setEnabled(1)


    def Edges_width_viewCam(self):
        if  self.x00 and self.x10 and self.y00 and self.y10 : 
            converter = pylon.ImageFormatConverter()
            converter.OutputPixelFormat = pylon.PixelType_BGR8packed
            converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

            # create video capture
            grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grabResult.GrabSucceeded():
        # Access the image data
               image = converter.Convert(grabResult)
               self.img = image.GetArray()
               self.img_0  = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY )
               self.img_10 = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY )
               self.image = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
               self.img_edges_width=Edges_width_xulyanh(self.img_0,self.img_10,self.x00,self.y00,self.x10,self.y10)
               self.ten_Filter=self.Edges_width_FILTER_comboBox.currentText()
               self.ten_Kernel=self.Edges_width_KERNEL_comboBox.currentText()
          #  print(self.ten_Filter)
           # print(self.ten_Kernel)
               self.img_edges_width.filter_img(self.ten_Filter,self.ten_Kernel)
           # self.ten_category=self.Egdes_with_Category_comboBox.currentText()
               self.lowlevel_value=self.Edges_with_LOW_LEVEL_horizontalSlider.value()
               cv2.rectangle( self.image ,(self.x00,self.y00),(self.x10,self.y10),(0,255,0),3) 
               self.highlevel_value=self.Edges_width_high_level_horizontalSlider.value()
               self.img_edges_width.edges_img(self.lowlevel_value,self.highlevel_value)
               self.img_xuly=self.img_edges_width.edges_count(self.image)
               height, width,channel = self.img_xuly.shape
               step =  width*channel
               qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
               pixmap = QPixmap.fromImage(qImg)
               self.img_Edges_width_label.setPixmap(QPixmap.fromImage(qImg))
               self.img_Edges_width_label.setCursor(QtCore.Qt.CrossCursor)
               self.img_Edges_width_label.setfdk(0)
             #cv2.rectangle(self.image_1,(self.x00,self.y00),(self.x10,self.y10),3) 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Edges_width_Dialog = QtWidgets.QDialog()
    ui = Ui_Edges_width_Dialog()
    ui.setupUi(Edges_width_Dialog)
    Edges_width_Dialog.show()
    sys.exit(app.exec_())

