from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtGui import QIcon


from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QRect, Qt

from detection_edges_xulyanh import*
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

class Detection_edges_MyLabel(QLabel):

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

class Ui_Detection_edges_Dialog(object):
    def setupUi(self, Detection_edges_Dialog):
        Detection_edges_Dialog.setObjectName("Detection_edges_Dialog")
        Detection_edges_Dialog.resize(1021, 610)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Detection_edges_Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(620, 10, 381, 581))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setObjectName("groupBox")
        self.Detection_edges_tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.Detection_edges_tableWidget.setGeometry(QtCore.QRect(20, 430, 321, 91))
        self.Detection_edges_tableWidget.setObjectName("Detection_edges_tableWidget")
        self.Detection_edges_tableWidget.setColumnCount(0)
        self.Detection_edges_tableWidget.setRowCount(0)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 390, 321, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.Jubged_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.Jubged_comboBox.setObjectName("Jubged_comboBox")
        self.Jubged_comboBox.addItem("")
        self.Jubged_comboBox.addItem("")
        self.Jubged_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.Jubged_comboBox)
        self.Jubged_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.Jubged_spinBox.setObjectName("Jubged_spinBox")
        self.horizontalLayout_3.addWidget(self.Jubged_spinBox)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 530, 321, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Xuly_detection_edge_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.Xuly_detection_edge_pushButton.setObjectName("Xuly_detection_edge_pushButton")
        self.horizontalLayout_4.addWidget(self.Xuly_detection_edge_pushButton)
        self.Reset_detection_edges_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.Reset_detection_edges_pushButton.setObjectName("Reset_detection_edges_pushButton")
        self.horizontalLayout_4.addWidget(self.Reset_detection_edges_pushButton)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 30, 321, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.Filter_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.Filter_comboBox.setObjectName("Filter_comboBox")
        self.Filter_comboBox.addItem("")
        self.Filter_comboBox.addItem("")
        self.Filter_comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.Filter_comboBox)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(20, 70, 321, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.Kernel_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.Kernel_comboBox.setObjectName("Kernel_comboBox")
        self.Kernel_comboBox.addItem("")
        self.Kernel_comboBox.addItem("")
        self.Kernel_comboBox.addItem("")
        self.Kernel_comboBox.addItem("")
        self.Kernel_comboBox.addItem("")
        self.horizontalLayout_6.addWidget(self.Kernel_comboBox)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(20, 280, 321, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.Shift_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_6)
        self.Shift_spinBox.setObjectName("Shift_spinBox")
        self.horizontalLayout_7.addWidget(self.Shift_spinBox)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(20, 320, 321, 41))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.Scan_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_7)
        self.Scan_comboBox.setObjectName("Scan_comboBox")
        self.Scan_comboBox.addItem("")
        self.Scan_comboBox.addItem("")
      #  self.Scan_comboBox.addItem("")
        self.Scan_comboBox.setItemText(2, "")
        self.horizontalLayout_8.addWidget(self.Scan_comboBox)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 110, 321, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.Low_level_horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.Low_level_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Low_level_horizontalSlider.setObjectName("Low_level_horizontalSlider")
        self.verticalLayout_6.addWidget(self.Low_level_horizontalSlider)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.High_level_horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.High_level_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.High_level_horizontalSlider.setObjectName("High_level_horizontalSlider")
        self.verticalLayout_6.addWidget(self.High_level_horizontalSlider)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(20, 360, 321, 31))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        self.Coordinate_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_9)
        self.Coordinate_comboBox.setObjectName("Coordinate_comboBox")
        self.Coordinate_comboBox.addItem("")
        self.Coordinate_comboBox.addItem("")
        self.Coordinate_comboBox.addItem("")
        self.horizontalLayout_12.addWidget(self.Coordinate_comboBox)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 220, 321, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.Trend_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.Trend_comboBox.setObjectName("Trend_comboBox")
        self.Trend_comboBox.addItem("")
        self.Trend_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.Trend_comboBox)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.Position_Shift_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.Position_Shift_spinBox.setObjectName("Position_Shift_spinBox")
        self.horizontalLayout_2.addWidget(self.Position_Shift_spinBox)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(Detection_edges_Dialog)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 540, 231, 81))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.OK_detection_edges_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.OK_detection_edges_pushButton.setObjectName("OK_detection_edges_pushButton")
        self.horizontalLayout_11.addWidget(self.OK_detection_edges_pushButton)
        self.Image_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_8)
        self.Image_comboBox.setObjectName("Image_comboBox")
        self.Image_comboBox.addItem("")
        self.Image_comboBox.addItem("")
        self.Image_comboBox.addItem("")
        self.Image_comboBox.addItem("")
        self.horizontalLayout_11.addWidget(self.Image_comboBox)
        self.Run_detection_edges_pushButton = QtWidgets.QPushButton(Detection_edges_Dialog)
        self.Run_detection_edges_pushButton.setGeometry(QtCore.QRect(350, 554, 111, 51))
        self.Run_detection_edges_pushButton.setObjectName("Run_detection_edges_pushButton")
        self.scrollArea = QtWidgets.QScrollArea(Detection_edges_Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 601, 511))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 599, 509))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
      #  self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.img_detection_edges_label=Detection_edges_MyLabel(self.scrollAreaWidgetContents)
        self.scrollArea.setBackgroundRole(QPalette.Dark)#THEM DONG
        self.img_detection_edges_label.setWordWrap(True)
        self.img_detection_edges_label.setObjectName("label")
        self.scrollArea.setWidget(self.img_detection_edges_label)# dong quan trong

        self.OK_detection_edges_pushButton.clicked.connect(self.Detection_edges_open_img)
        self.Low_level_horizontalSlider.sliderMoved.connect(self.detection_edges_bar)
        self.High_level_horizontalSlider.sliderMoved.connect(self.detection_edges_bar)
        self.Shift_spinBox.setValue(5)
        self.Shift_spinBox.valueChanged.connect(self.Detection_edges_direction)
        self.Scan_comboBox.currentIndexChanged.connect(self.change_Trend_comboBox)
        self.Shift_spinBox.valueChanged.connect(self.change_Trend_comboBox)
        self.Coordinate_comboBox.currentIndexChanged.connect(self.display_point)
        self.Trend_comboBox.currentIndexChanged.connect(self.Detection_edges_direction)
        self.Position_Shift_spinBox.valueChanged.connect(self.display_line)
        self.Jubged_comboBox.currentIndexChanged.connect(self.change_Jubged_combox)
        self.Jubged_spinBox.valueChanged.connect(self.change_Jubged_spinBox)
        self.Xuly_detection_edge_pushButton.clicked.connect(self.Detection_edges_xyly)
        self.Reset_detection_edges_pushButton.clicked.connect(self.Detection_edges_Reset)
        self.Run_detection_edges_pushButton.clicked.connect(self.find_counter)


        self.Detection_edges_tableWidget.setColumnCount(3)
        self.Detection_edges_tableWidget.setRowCount(2)
        self.Detection_edges_tableWidget.setVerticalHeaderLabels(['X','Y'])
        self.Detection_edges_tableWidget.setHorizontalHeaderLabels(['Min', 'Measure', 'Max'])
        self.Low_level_horizontalSlider.setMaximum(255)
        self.Low_level_horizontalSlider.setMinimum(0)
        self.High_level_horizontalSlider.setMaximum(255)
        self.High_level_horizontalSlider.setMinimum(0)
      #  self.Jubged_spinBox.setValue(1)
    #    self.Jubged_spinBox.setEnabled(0)
        self.Position_Shift_spinBox.setEnabled(0)
        self.Coordinate_comboBox.setEnabled(0)
        self.Scan_comboBox.setEnabled(0)
        self.Shift_spinBox.setEnabled(0)
        self.Jubged_comboBox.setEnabled(0)
        self.Reset_detection_edges_pushButton.setEnabled(0)


        self.retranslateUi(Detection_edges_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Detection_edges_Dialog)

    def retranslateUi(self, Detection_edges_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Detection_edges_Dialog.setWindowTitle(_translate("Detection_edges_Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Detection_edges_Dialog", "SET UP"))
        self.label_8.setText(_translate("Detection_edges_Dialog", "Jubged label"))
        self.Jubged_comboBox.setItemText(0, _translate("Detection_edges_Dialog", "Max"))
        self.Jubged_comboBox.setItemText(1, _translate("Detection_edges_Dialog", "Min"))
        self.Jubged_comboBox.setItemText(2, _translate("Detection_edges_Dialog", "Middle"))
        self.Xuly_detection_edge_pushButton.setText(_translate("Detection_edges_Dialog", "XULY"))
        self.Reset_detection_edges_pushButton.setText(_translate("Detection_edges_Dialog", "RESET"))
        self.label.setText(_translate("Detection_edges_Dialog", "FILTER"))
        self.Filter_comboBox.setItemText(0, _translate("Detection_edges_Dialog", "Averaging"))
        self.Filter_comboBox.setItemText(1, _translate("Detection_edges_Dialog", "Gaussian Filtering"))
        self.Filter_comboBox.setItemText(2, _translate("Detection_edges_Dialog", "Median Filtering"))
        self.label_2.setText(_translate("Detection_edges_Dialog", "KERNEL"))
        self.Kernel_comboBox.setItemText(0, _translate("Detection_edges_Dialog", "3X3"))
        self.Kernel_comboBox.setItemText(1, _translate("Detection_edges_Dialog", "5X5"))
        self.Kernel_comboBox.setItemText(2, _translate("Detection_edges_Dialog", "7x7"))
        self.Kernel_comboBox.setItemText(3, _translate("Detection_edges_Dialog", "9x9"))
        self.Kernel_comboBox.setItemText(4, _translate("Detection_edges_Dialog", "11x11"))
        self.label_5.setText(_translate("Detection_edges_Dialog", "SHIFT"))
        self.label_7.setText(_translate("Detection_edges_Dialog", "Scan Direction"))
        self.Scan_comboBox.setItemText(0, _translate("Detection_edges_Dialog", "high->low"))
        self.Scan_comboBox.setItemText(1, _translate("Detection_edges_Dialog", "low->high"))
        self.label_3.setText(_translate("Detection_edges_Dialog", "                                 LOW LEVEL"))
        self.label_4.setText(_translate("Detection_edges_Dialog", "                                HIGH LEVEL"))
        self.label_10.setText(_translate("Detection_edges_Dialog", "Coordinate                                       "))
        self.Coordinate_comboBox.setItemText(0, _translate("Detection_edges_Dialog", "OX"))
        self.Coordinate_comboBox.setItemText(1, _translate("Detection_edges_Dialog", "OY"))
        self.Coordinate_comboBox.setItemText(2, _translate("Detection_edges_Dialog", "Both"))
        self.label_6.setText(_translate("Detection_edges_Dialog", "Trend Direction"))
        self.Trend_comboBox.setItemText(0, _translate("Detection_edges_Dialog", "->"))
        self.Trend_comboBox.setItemText(1, _translate("Detection_edges_Dialog", "<-"))
        self.label_9.setText(_translate("Detection_edges_Dialog", "Position "))
        self.OK_detection_edges_pushButton.setText(_translate("Detection_edges_Dialog", "OK"))
        self.Image_comboBox.setItemText(0, _translate("Detection_edges_Dialog", "01"))
        self.Image_comboBox.setItemText(1, _translate("Detection_edges_Dialog", "02"))
        self.Image_comboBox.setItemText(2, _translate("Detection_edges_Dialog", "03"))
        self.Image_comboBox.setItemText(3, _translate("Detection_edges_Dialog", "04"))
        self.Run_detection_edges_pushButton.setText(_translate("Detection_edges_Dialog", "RUN"))





    def Detection_edges_open_img(self):
        file_goc=os.getcwd()
        self.ten=self.Image_comboBox.currentText()
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
        self.img_detection_edges_label.setPixmap(QPixmap.fromImage(qImg))
        self.img_detection_edges_label.setCursor(QtCore.Qt.CrossCursor)
        self.img_detection_edges_label.setfdk(1)
        

    def detection_edges_bar(self):
        if  self.img_detection_edges_label.x0 and self.img_detection_edges_label.x1 and self.img_detection_edges_label.y0 and self.img_detection_edges_label.y1 :
            self.x00=self.img_detection_edges_label.x0
            self.x10=self.img_detection_edges_label.x1
            self.y00=self.img_detection_edges_label.y0
            self.y10=self.img_detection_edges_label.y1
            self.threshold_img=detection_edges_xuluanh(self.img_0,self.img_10,self.x00,self.y00,self.x10,self.y10)
            self.ten_Filter=self.Filter_comboBox.currentText()
            self.ten_Kernel=self.Kernel_comboBox.currentText()
            
            self.threshold_img.filter_img(self.ten_Filter,self.ten_Kernel)
            
            self.lowlevel_value=self.Low_level_horizontalSlider.value()
            self.highlevel_value=self.High_level_horizontalSlider.value()
            self.threshold_img.edges_img(self.lowlevel_value,self.highlevel_value)
            self.img_cuoi=self.threshold_img.get_img()
                
            height, width  =self.img_cuoi.shape
            step = width
            qImg = QImage(self.img_cuoi.data, width, height, step, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qImg)
            self.img_detection_edges_label.setPixmap(QPixmap.fromImage(qImg))
            self.img_detection_edges_label.setfdk(0)
            self.Jubged_spinBox.setEnabled(0)
            self.Position_Shift_spinBox.setEnabled(0)
            self.Coordinate_comboBox.setEnabled(0)
            self.Scan_comboBox.setEnabled(0)
            self.Shift_spinBox.setEnabled(0)
            self.Jubged_comboBox.setEnabled(0)
            self.Trend_comboBox.setEnabled(1)
            
    def Detection_edges_direction(self):
     
        self.img_detection_edges_label.setfdk(0)
        img_1=cv2.imread(self.file_img,1)
        img_2=cv2.imread(self.file_img,0)
        Value_shift=self.Shift_spinBox.value()
        self.ten_position=self.Jubged_comboBox.currentText()
        self.threshold_img.edges_count(img_2)
        
     
        self.value_Jubged_comboBox,self.img_color=self.threshold_img.paint_line(img_1)
        self.Position_Shift_spinBox.setRange(1,self.value_Jubged_comboBox)    
  
        height, width,channel = self.img_color.shape
        step =  width*channel
        qImg = QImage(self.img_color.data, width, height, step, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.img_detection_edges_label.setPixmap(QPixmap.fromImage(qImg))
        self.img_detection_edges_label.setCursor(QtCore.Qt.CrossCursor)
        self.img_detection_edges_label.setfdk(0)
        self.Position_Shift_spinBox.setEnabled(1)
        self.Shift_spinBox.setEnabled(1)



        
    def display_line(self):
         self.Value_line=self.Position_Shift_spinBox.value()
         img_1=cv2.imread(self.file_img,1)
         self.img_xuly=self.threshold_img.display_line_xuly(img_1,self.Value_line)
         height, width,channel = self.img_xuly.shape
         step =  width*channel
         qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.img_detection_edges_label.setPixmap(QPixmap.fromImage(qImg))
         self.img_detection_edges_label.setCursor(QtCore.Qt.CrossCursor)
         self.img_detection_edges_label.setfdk(0)
    
    def display_point(self):
         self.Value_shift=self.Shift_spinBox.value()
         self.ten_position=self.Jubged_comboBox.currentText()
         self.Trend_direction=self.Trend_comboBox.currentText()
         self.Scan_direction=self.Scan_comboBox.currentText()
         self.Value_line=self.Position_Shift_spinBox.value()
         self.point=self.Jubged_spinBox.value()-1
         self.coordinate=self.Coordinate_comboBox.currentText()
         img_1=cv2.imread(self.file_img,1)

         self.Jubged_spinBox.setValue(1)
         self.Jubged_spinBox.setEnabled(0)

         self.img_xuly=self.threshold_img.display_point(self.Value_shift,self.Value_line-1,self.coordinate,self.Trend_direction,self.Scan_direction,self.point,img_1)
 
         height, width,channel = self.img_xuly.shape
         step =  width*channel
         qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.img_detection_edges_label.setPixmap(QPixmap.fromImage(qImg))
         self.img_detection_edges_label.setCursor(QtCore.Qt.CrossCursor)
         self.img_detection_edges_label.setfdk(0)
         self.Jubged_comboBox.setEnabled(1)

         
    def change_Trend_comboBox(self):
         self.Value_shift=self.Shift_spinBox.value()
         self.ten_position=self.Jubged_comboBox.currentText()
         self.Trend_direction=self.Trend_comboBox.currentText()
         self.Scan_direction=self.Scan_comboBox.currentText()
         self.Value_line=self.Position_Shift_spinBox.value()
         self.point=self.Jubged_spinBox.value()-1
         self.coordinate=self.Coordinate_comboBox.currentText()
         img_1=cv2.imread(self.file_img,1)
      #   img_1=cv2.resize(img_1,(601, 531))

         self.img_xuly=self.threshold_img.position_direction(self.Value_shift,self.Value_line-1,self.coordinate,self.Trend_direction,self.Scan_direction,self.point,img_1)
 
         height, width,channel = self.img_xuly.shape
         step =  width*channel
         qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.img_detection_edges_label.setPixmap(QPixmap.fromImage(qImg))
         self.img_detection_edges_label.setCursor(QtCore.Qt.CrossCursor)
         self.img_detection_edges_label.setfdk(0)
         self.Scan_comboBox.setEnabled(1)
         self.Coordinate_comboBox.setEnabled(1)
         

    def change_Jubged_combox(self):

         self.Value_shift=self.Shift_spinBox.value()
         self.ten_position=self.Jubged_comboBox.currentText()
         self.Trend_direction=self.Trend_comboBox.currentText()
         self.Scan_direction=self.Scan_comboBox.currentText()
         self.Value_line=self.Position_Shift_spinBox.value()
         self.point=self.Jubged_spinBox.value()-1
         self.coordinate=self.Coordinate_comboBox.currentText()
         img_1=cv2.imread(self.file_img,1)
    #     img_1=cv2.resize(img_1,(601, 531))
         self.value_Jubged_spinBox=self.threshold_img.get_position()
         self.Jubged_spinBox.setRange(1,self.value_Jubged_spinBox)  
         if self.ten_position=="Max":
            self.point=0
            self.Jubged_spinBox.setValue(1)
            self.Jubged_spinBox.setEnabled(0)        
         if self.ten_position=="Min":
            self.point=self.value_Jubged_spinBox-1
            self.Jubged_spinBox.setValue(self.value_Jubged_spinBox)
            self.Jubged_spinBox.setEnabled(0)
            
         if self.ten_position=="Middle":
            self.Jubged_spinBox.setEnabled(1)   
            self.point=self.Jubged_spinBox.value()-1
    

         self.img_xuly=self.threshold_img.display_point(self.Value_shift,self.Value_line-1,self.coordinate,self.Trend_direction,self.Scan_direction,self.point,img_1)
         self.position_X,self.position_Y=self.threshold_img.get_img_position()

         self.Detection_edges_tableWidget.setItem(0,1, QTableWidgetItem(str(self.position_X)))
         self.Detection_edges_tableWidget.setItem(1,1, QTableWidgetItem(str(self.position_Y)))

         height, width,channel = self.img_xuly.shape
         step =  width*channel
         qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.img_detection_edges_label.setPixmap(QPixmap.fromImage(qImg))
         self.img_detection_edges_label.setCursor(QtCore.Qt.CrossCursor)
         self.img_detection_edges_label.setfdk(0)


  
    def find_counter(self):
         img_1=cv2.imread(self.file_img,1)
         self.img_xuly=self.threshold_img.edges_count(img_1)
         height, width,channel = self.img_xuly.shape
         step =  width*channel
         qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.img_detection_edges_label.setPixmap(QPixmap.fromImage(qImg))
         self.img_detection_edges_label.setCursor(QtCore.Qt.CrossCursor)
         self.img_detection_edges_label.setfdk(0)
         
    def change_Jubged_spinBox(self):

         self.Value_shift=self.Shift_spinBox.value()
         file_goc=os.getcwd()
         self.ten=self.Image_comboBox.currentText()
         file_config=file_goc.replace("/detection_edges","")
         self.file_img=file_config+"/"+self.ten+".jpg"        
         self.ten_position=self.Jubged_comboBox.currentText()
         self.Trend_direction=self.Trend_comboBox.currentText()
         self.Scan_direction=self.Scan_comboBox.currentText()
         self.Value_line=self.Position_Shift_spinBox.value()
         self.point=self.Jubged_spinBox.value()-1


         self.coordinate=self.Coordinate_comboBox.currentText()
         img_2=cv2.imread(self.file_img,1)
         self.value_Jubged_spinBox=self.threshold_img.get_position()
         self.Jubged_spinBox.setRange(1,self.value_Jubged_spinBox)        
         self.img_xuly=self.threshold_img.display_point(self.Value_shift,self.Value_line-1,self.coordinate,self.Trend_direction,self.Scan_direction,self.point,img_2)
         self.position_X,self.position_Y=self.threshold_img.get_img_position()

         self.Detection_edges_tableWidget.setItem(0,1, QTableWidgetItem(str(self.position_X)))
         self.Detection_edges_tableWidget.setItem(1,1, QTableWidgetItem(str(self.position_Y)))
 
         height, width,channel = self.img_xuly.shape
         step =  width*channel
         qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.img_detection_edges_label.setPixmap(QPixmap.fromImage(qImg))
         self.img_detection_edges_label.setCursor(QtCore.Qt.CrossCursor)
         self.img_detection_edges_label.setfdk(0)


    def Detection_edges_xyly(self):
        file_goc=os.getcwd()
        self.x00=self.img_detection_edges_label.x0
        self.x10=self.img_detection_edges_label.x1
        self.y00=self.img_detection_edges_label.y0
        self.y10=self.img_detection_edges_label.y1
        if file_goc.find("detection_edges",20)==-1:
             self.file_img_bandau=file_goc+"/image_function"
             self.file_img=os.getcwd()+"/cut_image_function"
        else:
             self.file_img_bandau=file_goc.replace("detection_edges","image_function")
             self.file_img=file_goc.replace("detection_edges","cut_image_function")
        self.file_img_bandau=self.file_img_bandau.rstrip()
        
        self.file_img=self.file_img.rstrip()
        Count_img=len(os.listdir(self.file_img))
        Count_img=Count_img+1
        length=len (str(Count_img))
        if length==1:
           self.ten="000"+str(Count_img)
        if length==2:
           self.ten="00"+str(Count_img)
        if length==3:
           self.ten="0"+str(Count_img)

        self.file_img_bandau=self.file_img_bandau+"/"+self.ten+"dau"+".jpg"
        self.file_img=self.file_img+"/"+self.ten+"cat"+".jpg"

        cv2.imwrite(self.file_img_bandau, self.img_xuly)
        self.img_cat=self.img_xuly[self.y00:self.y10,self.x00:self.x10]
        cv2.imwrite(self.file_img,self.img_cat)
        file_goc=os.getcwd()
        file_config=file_goc.replace("/detection_edges","/")+"/config"
        List_file=os.listdir(file_config)


        filedata=file_config+"/"+self.ten+".txt"
        
        detection_edges_file = open(filedata, 'w')
        detection_edges_file.write( self.file_img+"\n")
        detection_edges_file.write(self.file_img_bandau+"\n")

        detection_edges_file.write("detection_edges\n")
        
        detection_edges_file.write(str(self.x00)+"\n")
        detection_edges_file.write(str(self.x10)+"\n")
        detection_edges_file.write(str(self.y00)+"\n")
        detection_edges_file.write(str(self.y10)+"\n")
        self.Jubged_spinBox.setEnabled(0)
        self.Position_Shift_spinBox.setEnabled(0)
        self.Coordinate_comboBox.setEnabled(0)
        self.Scan_comboBox.setEnabled(0)
        self.Shift_spinBox.setEnabled(0)
        self.Jubged_comboBox.setEnabled(0)
        self.High_level_horizontalSlider.setEnabled(0)
        self.Low_level_horizontalSlider.setEnabled(0)
        self.Filter_comboBox.setEnabled(0)
        self.Kernel_comboBox.setEnabled(0)
        self.Detection_edges_tableWidget.setEnabled(0)
        self.Xuly_detection_edge_pushButton.setEnabled(0)
        self.OK_detection_edges_pushButton.setEnabled(0)
        self.Trend_comboBox.setEnabled(0)
        self.Reset_detection_edges_pushButton.setEnabled(1)
  
    def Detection_edges_Reset(self):
        self.High_level_horizontalSlider.setEnabled(1)
        self.Low_level_horizontalSlider.setEnabled(1)
        self.Filter_comboBox.setEnabled(1)
        self.Kernel_comboBox.setEnabled(1)
        self.Detection_edges_tableWidget.setEnabled(1)
        self.Xuly_detection_edge_pushButton.setEnabled(1)
        self.OK_detection_edges_pushButton.setEnabled(1)
        self.Reset_detection_edges_pushButton.setEnabled(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Detection_edges_Dialog = QtWidgets.QDialog()
    ui = Ui_Detection_edges_Dialog()
    ui.setupUi(Detection_edges_Dialog)
    Detection_edges_Dialog.show()
    sys.exit(app.exec_())

