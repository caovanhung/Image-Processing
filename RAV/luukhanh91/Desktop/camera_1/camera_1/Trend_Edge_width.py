from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtGui import QIcon


from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QRect, Qt

from Trend_Edge_width_xulyanh import*
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

from PyQt5 import QtCore, QtGui, QtWidgets
class Trend_Edge_width_MyLabel(QLabel):

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

class Ui_Trend_Edge_width_Dialog(object):
    def setupUi(self, Trend_Edge_width_Dialog):
        Trend_Edge_width_Dialog.setObjectName("Trend_Edge_width_Dialog")
        Trend_Edge_width_Dialog.resize(1106, 721)
        self.scrollArea = QtWidgets.QScrollArea(Trend_Edge_width_Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 651, 581))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 649, 579))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
      #  self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.Trend_Edge_width_RUN_pushButton = QtWidgets.QPushButton(Trend_Edge_width_Dialog)
        self.Trend_Edge_width_RUN_pushButton.setGeometry(QtCore.QRect(490, 600, 141, 81))
        self.Trend_Edge_width_RUN_pushButton.setObjectName("Trend_Edge_width_RUN_pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(Trend_Edge_width_Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(670, 0, 421, 631))
        self.groupBox_2.setObjectName("groupBox_2")
        self.Trend_Edge_width_tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.Trend_Edge_width_tableWidget.setGeometry(QtCore.QRect(50, 430, 321, 141))
        self.Trend_Edge_width_tableWidget.setObjectName("Trend_Edge_width_tableWidget")
        self.Trend_Edge_width_tableWidget.setColumnCount(0)
        self.Trend_Edge_width_tableWidget.setRowCount(0)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(50, 580, 321, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Trend_Edge_width_SAVE_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Trend_Edge_width_SAVE_pushButton.setObjectName("Trend_Edge_width_SAVE_pushButton")
        self.horizontalLayout_6.addWidget(self.Trend_Edge_width_SAVE_pushButton)
        self.Trend_Edge_width_RESET_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Trend_Edge_width_RESET_pushButton.setObjectName("Trend_Edge_width_RESET_pushButton")
        self.horizontalLayout_6.addWidget(self.Trend_Edge_width_RESET_pushButton)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(20, 30, 381, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.Trend_Edge_width_Filter_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_6)
        self.Trend_Edge_width_Filter_comboBox.setObjectName("Trend_Edge_width_Filter_comboBox")
        self.Trend_Edge_width_Filter_comboBox.addItem("")
        self.Trend_Edge_width_Filter_comboBox.addItem("")
        self.Trend_Edge_width_Filter_comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.Trend_Edge_width_Filter_comboBox)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(20, 70, 381, 41))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.Trend_Edge_width_Kernel_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_7)
        self.Trend_Edge_width_Kernel_comboBox.setObjectName("Trend_Edge_width_Kernel_comboBox")
        self.Trend_Edge_width_Kernel_comboBox.addItem("")
        self.Trend_Edge_width_Kernel_comboBox.addItem("")
        self.Trend_Edge_width_Kernel_comboBox.addItem("")
        self.Trend_Edge_width_Kernel_comboBox.addItem("")
        self.Trend_Edge_width_Kernel_comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.Trend_Edge_width_Kernel_comboBox)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(20, 280, 381, 41))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.Trend_Edge_width_Scan_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_9)
        self.Trend_Edge_width_Scan_comboBox.setObjectName("Trend_Edge_width_Scan_comboBox")
        self.Trend_Edge_width_Scan_comboBox.addItem("")
        self.Trend_Edge_width_Scan_comboBox.addItem("")
        self.Trend_Edge_width_Scan_comboBox.addItem("")
        self.Trend_Edge_width_Scan_comboBox.setItemText(2, "")
        self.horizontalLayout_10.addWidget(self.Trend_Edge_width_Scan_comboBox)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.Trend_Edge_width_Shift_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_9)
        self.Trend_Edge_width_Shift_spinBox.setObjectName("Trend_Edge_width_Shift_spinBox")
        self.horizontalLayout_10.addWidget(self.Trend_Edge_width_Shift_spinBox)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 120, 381, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.Trend_Edge_width_Low_level_horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.Trend_Edge_width_Low_level_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Trend_Edge_width_Low_level_horizontalSlider.setObjectName("Trend_Edge_width_Low_level_horizontalSlider")
        self.verticalLayout_6.addWidget(self.Trend_Edge_width_Low_level_horizontalSlider)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.Trend_Edge_width_High_level_horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.Trend_Edge_width_High_level_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Trend_Edge_width_High_level_horizontalSlider.setObjectName("Trend_Edge_width_High_level_horizontalSlider")
        self.verticalLayout_6.addWidget(self.Trend_Edge_width_High_level_horizontalSlider)
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(20, 220, 381, 51))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.Trend_Edge_width_Trend_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_11)
        self.Trend_Edge_width_Trend_comboBox.setObjectName("Trend_Edge_width_Trend_comboBox")
        self.Trend_Edge_width_Trend_comboBox.addItem("")
        self.Trend_Edge_width_Trend_comboBox.addItem("")
        self.horizontalLayout_11.addWidget(self.Trend_Edge_width_Trend_comboBox)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.Trend_Edge_width_Coordinate_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_11)
        self.Trend_Edge_width_Coordinate_comboBox.setObjectName("Trend_Edge_width_Coordinate_comboBox")
        self.Trend_Edge_width_Coordinate_comboBox.addItem("")
        self.Trend_Edge_width_Coordinate_comboBox.addItem("")
        self.Trend_Edge_width_Coordinate_comboBox.addItem("")
        self.horizontalLayout_11.addWidget(self.Trend_Edge_width_Coordinate_comboBox)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 380, 381, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.Trend_Edge_width_Jubged_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.Trend_Edge_width_Jubged_comboBox.setObjectName("Trend_Edge_width_Jubged_comboBox")
        self.Trend_Edge_width_Jubged_comboBox.addItem("")
        self.Trend_Edge_width_Jubged_comboBox.addItem("")
        self.Trend_Edge_width_Jubged_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.Trend_Edge_width_Jubged_comboBox)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Trend_Edge_width_Point_1_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.Trend_Edge_width_Point_1_spinBox.setObjectName("Trend_Edge_width_Point_1_spinBox")
        self.horizontalLayout_2.addWidget(self.Trend_Edge_width_Point_1_spinBox)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(20, 330, 381, 41))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_9.addWidget(self.label_14)
        self.Trend_Edge_width_Position_Shift_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_8)
        self.Trend_Edge_width_Position_Shift_spinBox.setObjectName("Trend_Edge_width_Position_Shift_spinBox")
        self.horizontalLayout_9.addWidget(self.Trend_Edge_width_Position_Shift_spinBox)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        self.Trend_Edge_width_Position_2_Shift_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_8)
        self.Trend_Edge_width_Position_2_Shift_spinBox.setObjectName("Trend_Edge_width_Position_2_Shift_spinBox")
        self.horizontalLayout_9.addWidget(self.Trend_Edge_width_Position_2_Shift_spinBox)
        self.Trend_Edge_width_img_comboBox = QtWidgets.QComboBox(Trend_Edge_width_Dialog)
        self.Trend_Edge_width_img_comboBox.setGeometry(QtCore.QRect(200, 630, 106, 41))
        self.Trend_Edge_width_img_comboBox.setObjectName("Trend_Edge_width_img_comboBox")
        self.Trend_Edge_width_img_comboBox.addItem("")
        self.Trend_Edge_width_img_comboBox.addItem("")
        self.Trend_Edge_width_img_comboBox.addItem("")
        self.Trend_Edge_width_img_comboBox.addItem("")
        self.Trend_Edge_width_img_comboBox.addItem("")
        self.Trend_Edge_width_img_comboBox.addItem("")
        self.Trend_Edge_width_OK_pushButton = QtWidgets.QPushButton(Trend_Edge_width_Dialog)
        self.Trend_Edge_width_OK_pushButton.setGeometry(QtCore.QRect(20, 630, 131, 41))
        self.Trend_Edge_width_OK_pushButton.setObjectName("Trend_Edge_width_OK_pushButton")


        self.img_Trend_Edge_width_label=Trend_Edge_width_MyLabel(self.scrollAreaWidgetContents)
        self.scrollArea.setBackgroundRole(QPalette.Dark)#THEM DONG
        self.img_Trend_Edge_width_label.setWordWrap(True)
        self.img_Trend_Edge_width_label.setObjectName("label")
        self.scrollArea.setWidget(self.img_Trend_Edge_width_label)
        self.Trend_Edge_width_OK_pushButton.clicked.connect(self.open_img_Trend_Edge_width)
        self.Trend_Edge_width_Low_level_horizontalSlider.sliderMoved.connect(self.Trend_Edge_width_bar)
        self.Trend_Edge_width_High_level_horizontalSlider.sliderMoved.connect(self.Trend_Edge_width_bar)

        self.Trend_Edge_width_Low_level_horizontalSlider.setMaximum(255)
        self.Trend_Edge_width_Low_level_horizontalSlider.setMinimum(0)
        self.Trend_Edge_width_High_level_horizontalSlider.setMaximum(255)
        self.Trend_Edge_width_High_level_horizontalSlider.setMinimum(0)
       # self.Trend_Edge_width_OK_pushButton.clicked.connect(self.open_img_Trend_Edge_width)

        self.Trend_Edge_width_Trend_comboBox.currentIndexChanged.connect(self.find_counter)
        self.Trend_Edge_width_Shift_spinBox.valueChanged.connect(self.change_Trend_comboBox)
        self.Trend_Edge_width_Position_Shift_spinBox.valueChanged.connect(self.Change_Position_Shift)
        self.Trend_Edge_width_Position_2_Shift_spinBox.valueChanged.connect(self.Change_Position_Shift)
        self.Trend_Edge_width_Scan_comboBox.currentIndexChanged.connect(self.find_counter)


        
        self.Trend_Edge_width_Jubged_comboBox.currentIndexChanged.connect(self.Change_point)
        self.Trend_Edge_width_Point_1_spinBox.valueChanged.connect(self.Change_middle_point)



        self.retranslateUi(Trend_Edge_width_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Trend_Edge_width_Dialog)

    def retranslateUi(self, Trend_Edge_width_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Trend_Edge_width_Dialog.setWindowTitle(_translate("Trend_Edge_width_Dialog", "Dialog"))
        self.Trend_Edge_width_RUN_pushButton.setText(_translate("Trend_Edge_width_Dialog", "RUN"))
        self.groupBox_2.setTitle(_translate("Trend_Edge_width_Dialog", "SET UP"))
        self.Trend_Edge_width_SAVE_pushButton.setText(_translate("Trend_Edge_width_Dialog", "SAVE"))
        self.Trend_Edge_width_RESET_pushButton.setText(_translate("Trend_Edge_width_Dialog", "RESET"))
        self.label_5.setText(_translate("Trend_Edge_width_Dialog", "FILTER"))
        self.Trend_Edge_width_Filter_comboBox.setItemText(0, _translate("Trend_Edge_width_Dialog", "Averaging"))
        self.Trend_Edge_width_Filter_comboBox.setItemText(1, _translate("Trend_Edge_width_Dialog", "Gaussian Filtering"))
        self.Trend_Edge_width_Filter_comboBox.setItemText(2, _translate("Trend_Edge_width_Dialog", "Median Filtering"))
        self.label_6.setText(_translate("Trend_Edge_width_Dialog", "KERNEL"))
        self.Trend_Edge_width_Kernel_comboBox.setItemText(0, _translate("Trend_Edge_width_Dialog", "3X3"))
        self.Trend_Edge_width_Kernel_comboBox.setItemText(1, _translate("Trend_Edge_width_Dialog", "5X5"))
        self.Trend_Edge_width_Kernel_comboBox.setItemText(2, _translate("Trend_Edge_width_Dialog", "7X7"))
        self.Trend_Edge_width_Kernel_comboBox.setItemText(3, _translate("Trend_Edge_width_Dialog", "9X9"))
        self.Trend_Edge_width_Kernel_comboBox.setItemText(4, _translate("Trend_Edge_width_Dialog", "11x11"))
        self.label_9.setText(_translate("Trend_Edge_width_Dialog", "Scan Direction"))
        self.Trend_Edge_width_Scan_comboBox.setItemText(0, _translate("Trend_Edge_width_Dialog", "high->low"))
        self.Trend_Edge_width_Scan_comboBox.setItemText(1, _translate("Trend_Edge_width_Dialog", "low->high"))
        self.label_7.setText(_translate("Trend_Edge_width_Dialog", "SHIFT"))
        self.label_10.setText(_translate("Trend_Edge_width_Dialog", "                                 LOW LEVEL"))
        self.label_11.setText(_translate("Trend_Edge_width_Dialog", "                                HIGH LEVEL"))
        self.label_13.setText(_translate("Trend_Edge_width_Dialog", "Trend Direction"))
        self.Trend_Edge_width_Trend_comboBox.setItemText(0, _translate("Trend_Edge_width_Dialog", "->"))
        self.Trend_Edge_width_Trend_comboBox.setItemText(1, _translate("Trend_Edge_width_Dialog", "<-"))
        self.label_12.setText(_translate("Trend_Edge_width_Dialog", "Coordinate     "))
        self.Trend_Edge_width_Coordinate_comboBox.setItemText(0, _translate("Trend_Edge_width_Dialog", "OX"))
        self.Trend_Edge_width_Coordinate_comboBox.setItemText(1, _translate("Trend_Edge_width_Dialog", "OY"))
        self.Trend_Edge_width_Coordinate_comboBox.setItemText(2, _translate("Trend_Edge_width_Dialog", "Both"))
        self.label_8.setText(_translate("Trend_Edge_width_Dialog", "Jubged label"))
        self.Trend_Edge_width_Jubged_comboBox.setItemText(0, _translate("Trend_Edge_width_Dialog", "Max"))
        self.Trend_Edge_width_Jubged_comboBox.setItemText(1, _translate("Trend_Edge_width_Dialog", "Min"))
        self.Trend_Edge_width_Jubged_comboBox.setItemText(2, _translate("Trend_Edge_width_Dialog", "MIddle"))
        self.label_2.setText(_translate("Trend_Edge_width_Dialog", "Point"))
        self.label_14.setText(_translate("Trend_Edge_width_Dialog", "Position1 "))
        self.label.setText(_translate("Trend_Edge_width_Dialog", "Position2"))
        self.Trend_Edge_width_img_comboBox.setItemText(0, _translate("Trend_Edge_width_Dialog", "01"))
        self.Trend_Edge_width_img_comboBox.setItemText(1, _translate("Trend_Edge_width_Dialog", "02"))
        self.Trend_Edge_width_img_comboBox.setItemText(2, _translate("Trend_Edge_width_Dialog", "03"))
        self.Trend_Edge_width_img_comboBox.setItemText(3, _translate("Trend_Edge_width_Dialog", "04"))
        self.Trend_Edge_width_img_comboBox.setItemText(4, _translate("Trend_Edge_width_Dialog", "05"))
        self.Trend_Edge_width_img_comboBox.setItemText(5, _translate("Trend_Edge_width_Dialog", "06"))
        self.Trend_Edge_width_OK_pushButton.setText(_translate("Trend_Edge_width_Dialog", "OK"))

    def open_img_Trend_Edge_width(self):
        file_goc=os.getcwd()
        self.ten=self.Trend_Edge_width_img_comboBox.currentText()
        file_config=file_goc.replace("/Trend_Edge_width","")
       # print(file_config)
        self.file_img=file_config+"/"+self.ten+".jpg"
   #     print(self.file_img)
        self.img=cv2.imread(self.file_img,1)
        self.img_1=cv2.imread(self.file_img,1)
    #    print (self.img)
        self.img_0=cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.img_10=cv2.cvtColor(self.img_1, cv2.COLOR_BGR2GRAY)

        height, width,channel = self.img.shape
        step =  width*channel
        qImg = QImage(self.img.data, width, height, step, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.img_Trend_Edge_width_label.setPixmap(QPixmap.fromImage(qImg))
        self.img_Trend_Edge_width_label.setCursor(QtCore.Qt.CrossCursor)
        self.img_Trend_Edge_width_label.setfdk(1)
    def Trend_Edge_width_bar(self):
        if  self.img_Trend_Edge_width_label.x0 and self.img_Trend_Edge_width_label.x1 and self.img_Trend_Edge_width_label.y0 and self.img_Trend_Edge_width_label.y1 :
            self.x00=self.img_Trend_Edge_width_label.x0
            self.x10=self.img_Trend_Edge_width_label.x1
            self.y00=self.img_Trend_Edge_width_label.y0
            self.y10=self.img_Trend_Edge_width_label.y1
            self.Trend_Edge_width_threshold_img=Trend_Edge_width_xuluanh(self.img_0,self.img_10,self.x00,self.y00,self.x10,self.y10)
            self.ten_Trend_Edge_width_Filter=self.Trend_Edge_width_Filter_comboBox.currentText()
            self.ten_Trend_Edge_width_Kernel=self.Trend_Edge_width_Kernel_comboBox.currentText()
            
            self.Trend_Edge_width_threshold_img.filter_img(self.ten_Trend_Edge_width_Filter,self.ten_Trend_Edge_width_Kernel)
            
            self.lowlevel_value=self.Trend_Edge_width_Low_level_horizontalSlider.value()
            self.highlevel_value=self.Trend_Edge_width_High_level_horizontalSlider.value()
            self.Trend_Edge_width_threshold_img.Trend_Edge_width_edges_img(self.lowlevel_value,self.highlevel_value)
            self.img_cuoi=self.Trend_Edge_width_threshold_img.get_img()
                
            height, width  =self.img_cuoi.shape
            step = width
            qImg = QImage(self.img_cuoi.data, width, height, step, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qImg)
            self.img_Trend_Edge_width_label.setPixmap(QPixmap.fromImage(qImg))
            self.img_Trend_Edge_width_label.setfdk(0)

    def find_counter(self):
         img_1=cv2.imread(self.file_img,1)


         self.Trend_direction=self.Trend_Edge_width_Trend_comboBox.currentText()
         self.Scan_direction=self.Trend_Edge_width_Scan_comboBox.currentText()
         self.coordinate=self.Trend_Edge_width_Coordinate_comboBox.currentText()
     
         self.img_xuly=self.Trend_Edge_width_threshold_img.edges_count(img_1,self.Trend_direction,self.coordinate,self.Scan_direction)
         height, width,channel = self.img_xuly.shape
         step =  width*channel
         qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.img_Trend_Edge_width_label.setPixmap(QPixmap.fromImage(qImg))
         self.img_Trend_Edge_width_label.setCursor(QtCore.Qt.CrossCursor)
         self.img_Trend_Edge_width_label.setfdk(0)
    def change_Trend_comboBox(self):
         self.Value_shift=self.Trend_Edge_width_Shift_spinBox.value()
         
         self.ten_position_1=self.Trend_Edge_width_Jubged_comboBox.currentText()      
         self.Trend_direction=self.Trend_Edge_width_Trend_comboBox.currentText()
         self.Scan_direction=self.Trend_Edge_width_Scan_comboBox.currentText()

         self.Value_line_1=self.Trend_Edge_width_Position_Shift_spinBox.value()
         self.Value_line_2=self.Trend_Edge_width_Position_2_Shift_spinBox.value()
         
         self.point_1=self.Trend_Edge_width_Point_1_spinBox.value()-1
       #  self.point_2=self.Trend_Edge_width_Point_2_spinBox.value()-1
         
         self.coordinate=self.Trend_Edge_width_Coordinate_comboBox.currentText()
         img_1=cv2.imread(self.file_img,1)
       #  print(self.Value_shift)
      #   img_1=cv2.resize(img_1,(601, 531))
      
         #self.img_xuly=self.Trend_Edge_width_threshold_img.divid_line(self.Value_shift,self.Value_line_1-1,self.coordinate,self.Trend_direction,self.Scan_direction,self.point_1,img_1)
         self_value_line,self.img_xuly=self.Trend_Edge_width_threshold_img.divid_line_shift(self.Value_shift,self.coordinate,self.Trend_direction,self.Scan_direction,self.point_1,img_1)     
        # print(self.img_xuly)
         self.Trend_Edge_width_Position_Shift_spinBox.setRange(1,self_value_line)
         self.Trend_Edge_width_Position_2_Shift_spinBox.setRange(1,self_value_line)         
         height, width,channel = self.img_xuly.shape
         step =  width*channel
         qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.img_Trend_Edge_width_label.setPixmap(QPixmap.fromImage(qImg))
         self.img_Trend_Edge_width_label.setCursor(QtCore.Qt.CrossCursor)
         self.img_Trend_Edge_width_label.setfdk(0)
         #self.Scan_comboBox.setEnabled(1)
        # self.Coordinate_comboBox.setEnabled(1)
    def Change_Position_Shift(self):
         self.Value_shift=self.Trend_Edge_width_Shift_spinBox.value()
         
         self.ten_position_1=self.Trend_Edge_width_Jubged_comboBox.currentText()      
         self.Trend_direction=self.Trend_Edge_width_Trend_comboBox.currentText()
         self.Scan_direction=self.Trend_Edge_width_Scan_comboBox.currentText()

         self.Value_line_1=self.Trend_Edge_width_Position_Shift_spinBox.value()-1
         self.Value_line_2=self.Trend_Edge_width_Position_2_Shift_spinBox.value()-1
         
         self.point_1=self.Trend_Edge_width_Point_1_spinBox.value()-1
      #   self.point_2=self.Trend_Edge_width_Point_2_spinBox.value()-1
         
         self.coordinate=self.Trend_Edge_width_Coordinate_comboBox.currentText()
         
         img_1=cv2.imread(self.file_img,1)
         self.img_xuly=self.Trend_Edge_width_threshold_img.divid_line(self.Value_shift,self.Value_line_1,self.Value_line_2,self.coordinate,self.Trend_direction,self.Scan_direction,self.point_1,img_1)     
        # print(self.img_xuly)
         height, width,channel = self.img_xuly.shape
         step =  width*channel
         qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.img_Trend_Edge_width_label.setPixmap(QPixmap.fromImage(qImg))
         self.img_Trend_Edge_width_label.setCursor(QtCore.Qt.CrossCursor)
         self.img_Trend_Edge_width_label.setfdk(0)

    def Change_point(self):
         self.Value_shift=self.Trend_Edge_width_Shift_spinBox.value()
         
         self.ten_position_1=self.Trend_Edge_width_Jubged_comboBox.currentText()      
         self.Trend_direction=self.Trend_Edge_width_Trend_comboBox.currentText()
         self.Scan_direction=self.Trend_Edge_width_Scan_comboBox.currentText()
         #Trend_Edge_width_Jubged_comboBox

         self.Value_line_1=self.Trend_Edge_width_Position_Shift_spinBox.value()-1
         self.Value_line_2=self.Trend_Edge_width_Position_2_Shift_spinBox.value()-1
         
         self.point_1=self.Trend_Edge_width_Point_1_spinBox.value()-1
        # self.point_2=self.Trend_Edge_width_Point_2_spinBox.value()-1
         
         self.coordinate=self.Trend_Edge_width_Coordinate_comboBox.currentText()
         img_1=cv2.imread(self.file_img,1)
         #print(self.ten_position_1)
         length_tt,self.img_xuly=self.Trend_Edge_width_threshold_img.divid_point(self.Value_shift,self.point_1,self.Trend_direction,self.coordinate,self.Scan_direction,self.ten_position_1,img_1)     
        # print(self.img_xuly)
         self.Trend_Edge_width_Point_1_spinBox.setRange(1,length_tt)
         height, width,channel = self.img_xuly.shape
         step =  width*channel
         qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.img_Trend_Edge_width_label.setPixmap(QPixmap.fromImage(qImg))
         self.img_Trend_Edge_width_label.setCursor(QtCore.Qt.CrossCursor)
         self.img_Trend_Edge_width_label.setfdk(0)

    def Change_middle_point(self):
         self.Value_shift=self.Trend_Edge_width_Shift_spinBox.value()
         
         self.ten_position_1=self.Trend_Edge_width_Jubged_comboBox.currentText()      
         self.Trend_direction=self.Trend_Edge_width_Trend_comboBox.currentText()
         self.Scan_direction=self.Trend_Edge_width_Scan_comboBox.currentText()
         #Trend_Edge_width_Jubged_comboBox

         self.Value_line_1=self.Trend_Edge_width_Position_Shift_spinBox.value()-1
         self.Value_line_2=self.Trend_Edge_width_Position_2_Shift_spinBox.value()-1
         
         self.point_1=self.Trend_Edge_width_Point_1_spinBox.value()-1
       #  self.point_2=self.Trend_Edge_width_Point_2_spinBox.value()-1
         
         self.coordinate=self.Trend_Edge_width_Coordinate_comboBox.currentText()
         img_1=cv2.imread(self.file_img,1)
      #   print(self.ten_position_1)
         self.img_xuly=self.Trend_Edge_width_threshold_img.divid_middle_point(self.Value_shift,self.point_1,self.Trend_direction,self.coordinate,self.Scan_direction,self.ten_position_1,img_1)     
        # print(self.img_xuly)
         height, width,channel = self.img_xuly.shape
         step =  width*channel
         qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.img_Trend_Edge_width_label.setPixmap(QPixmap.fromImage(qImg))
         self.img_Trend_Edge_width_label.setCursor(QtCore.Qt.CrossCursor)
         self.img_Trend_Edge_width_label.setfdk(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Trend_Edge_width_Dialog = QtWidgets.QDialog()
    ui = Ui_Trend_Edge_width_Dialog()
    ui.setupUi(Trend_Edge_width_Dialog)
    Trend_Edge_width_Dialog.show()
    sys.exit(app.exec_())

