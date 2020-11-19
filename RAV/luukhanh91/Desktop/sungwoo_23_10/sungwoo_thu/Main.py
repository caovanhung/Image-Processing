from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import pyqtSlot, QIODevice, QByteArray
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort

from PyQt5.QtWidgets import QWidget, QMessageBox

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
#import RPi.GPIO as GPIO
output_dc_10 = 23
output_dc_11=18
output_dc_20=17
output_dc_21=27

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

class Detection_edges_MyLabel(QLabel):

     x0 = 0
     y0 = 0
     x1 = 0
     y1 = 0
     
     flag = False
     dk=0
     x01=0
     y01=0
     x11=0
     y11=0

     x02=0
     y02=0
     x12=0
     y12=0

     x03=0
     y03=0
     x13=0
     y13=0
     dem=0
     #painter = QPainter()
 #Mouse click event
     def mousePressEvent(self,event):
        print("....",self.dem)
        if self.dem!=0:
           self.flag = True
        if self.dem!=0 and self.dk ==1:
             self.x0 = event.x()
             self.y0 = event.y()
            # self.flag = True
        if self.dem!=0 and self.dk ==2:
             self.x01= event.x()
             self.y01 = event.y()
            # self.flag = True
        if self.dem!=0 and self.dk ==3:
              self.x02= event.x()
              self.y02 = event.y()
        if self.dem!=0 and self.dk ==4:
              self.x03= event.x()
              self.y03 = event.y()
            #  self.flag = True
 #Mouse release event
     def set_dem(self,dem):
          self.dem=dem
     def get_dem(self):
          return self.dem
          
     def mouseReleaseEvent(self,event):
          if self.dem!=0:
             self.flag = False
             self.dk=self.dk+1
             self.dem=self.dem+1
             
           #  print("dem",self.dem)
            # if self.dem==3:
             #     self.flag = False
                  
 #Mouse movement events
     def mouseMoveEvent(self,event):
        if self.flag :
            if self.dem!=0 and self.dk==1:
                 self.x1 = event.x()
                 self.y1 = event.y()
                 self.update()
            if self.dem!=0 and self.dk==2:
                 self.x11 = event.x()
                 self.y11 = event.y()
                 self.update()
            if self.dem!=0 and self.dk==3:
                 self.x12 = event.x()
                 self.y12 = event.y()
                 self.update()
            if self.dem!=0 and self.dk==4:
                 self.x13 = event.x()
                 self.y13 = event.y()
                 self.update() 
     def setfdk(self,dk):
          self.dk=dk
     def getdk(self):
          return self.dk;
#Draw events
     def paintEvent(self, event):
          
     
          super().paintEvent(event)
          painter = QPainter(self)
          painter.setPen(QPen(Qt.red,2,Qt.SolidLine))

          if self.dem!=0 and self.dk==1:
              # painter = QPainter(self)
              # painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
               self.rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
               painter.drawRect(self.rect)
               #print(self.rect)
               
          if self.dem!=0 and self.dk==2:
              # painter = QPainter(self)
              # painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
              # painter1 = QPainter(self)
              # painter1.setPen(QPen(Qt.red,2,Qt.SolidLine))
               self.rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
               self.rect1 =QRect(self.x01, self.y01, abs(self.x11-self.x01), abs(self.y11-self.y01))
               painter.drawRect(self.rect)
               painter.drawRect(self.rect1)
          if self.dem!=0 and self.dk==3:

              # painter1 = QPainter(self)
              # painter1.setPen(QPen(Qt.red,2,Qt.SolidLine))
              # painter2 = QPainter(self)
              # painter2.setPen(QPen(Qt.red,2,Qt.SolidLine))
               self.rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
               self.rect1 =QRect(self.x01, self.y01, abs(self.x11-self.x01), abs(self.y11-self.y01))
               self.rect2 =QRect(self.x02, self.y02, abs(self.x12-self.x02), abs(self.y12-self.y02))
               painter.drawRect(self.rect)
               painter.drawRect(self.rect1)
               painter.drawRect(self.rect2)
          if self.dem!=0 and self.dk==4:

              # painter1 = QPainter(self)
              # painter1.setPen(QPen(Qt.red,2,Qt.SolidLine))
              # painter2 = QPainter(self)
              # painter2.setPen(QPen(Qt.red,2,Qt.SolidLine))
               self.rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
               self.rect1 =QRect(self.x01, self.y01, abs(self.x11-self.x01), abs(self.y11-self.y01))
               self.rect2 =QRect(self.x02, self.y02, abs(self.x12-self.x02), abs(self.y12-self.y02))
               self.rect3 =QRect(self.x03, self.y03, abs(self.x13-self.x03), abs(self.y13-self.y03))
               painter.drawRect(self.rect)
               painter.drawRect(self.rect1)
               painter.drawRect(self.rect2)
               painter.drawRect(self.rect3)

class Ui_Detection_edges_Dialog(object):
    def setupUi(self, Detection_edges_Dialog):
        Detection_edges_Dialog.setObjectName("Detection_edges_Dialog")
        Detection_edges_Dialog.resize(1021, 647)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Detection_edges_Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(630, 20, 361, 291))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setObjectName("groupBox")
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
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(90, 220, 168, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
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
        self.Image_comboBox.addItem("")
        self.Image_comboBox.addItem("")
        self.Image_comboBox.addItem("")
        self.Image_comboBox.addItem("")
        self.Image_comboBox.addItem("")
        self.Image_comboBox.addItem("")
        self.Image_comboBox.addItem("")
        self.Image_comboBox.addItem("")
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
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(Detection_edges_Dialog)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(640, 320, 351, 72))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.Postion_1_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_7)
        self.Postion_1_textEdit.setObjectName("Postion_1_textEdit")
        self.horizontalLayout_7.addWidget(self.Postion_1_textEdit)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.Position_2_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_7)
        self.Position_2_textEdit.setObjectName("Position_2_textEdit")
        self.horizontalLayout_7.addWidget(self.Position_2_textEdit)

        self.img_detection_edges_label=Detection_edges_MyLabel(self.scrollAreaWidgetContents)
        self.scrollArea.setBackgroundRole(QPalette.Dark)#THEM DONG
        self.img_detection_edges_label.setWordWrap(True)
        self.img_detection_edges_label.setObjectName("label")
        self.scrollArea.setWidget(self.img_detection_edges_label)
        self.Low_level_horizontalSlider.setMaximum(255)
        self.Low_level_horizontalSlider.setMinimum(0)
        self.High_level_horizontalSlider.setMaximum(255)
        self.High_level_horizontalSlider.setMinimum(0)


        #data =self.read_data()
        
 #       GPIO.setmode(GPIO.BCM)
    # set pin as an output pin with optional initial state of HIGH
 #       GPIO.setup(output_dc_10, GPIO.OUT, initial=GPIO.HIGH)
  #      GPIO.setup(output_dc_20, GPIO.OUT, initial=GPIO.HIGH)
  #      GPIO.setup(output_dc_21, GPIO.OUT, initial=GPIO.HIGH)

    #    self.Connect_pushButton.clicked.connect(self.on_buttonConnect_clicked)
  #      self.Disconnect_pushButton.clicked.connect(self.off_buttonDisconnect_clicked)
   #     if (data==1):

        self.OK_detection_edges_pushButton.clicked.connect(self.Detection_edges_open_img)
        self.Low_level_horizontalSlider.sliderMoved.connect(self.detection_edges_bar)
        self.High_level_horizontalSlider.sliderMoved.connect(self.detection_edges_bar)
        #self.Run_detection_edges_pushButton.clicked.connect(self.find_counter)

        self.pushButton.clicked.connect(self.find_direction)
        self.pushButton_2.clicked.connect(self.Reset_function)
        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        self.Run_detection_edges_pushButton.clicked.connect(self.controlTimer)





        self.retranslateUi(Detection_edges_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Detection_edges_Dialog)

    def retranslateUi(self, Detection_edges_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Detection_edges_Dialog.setWindowTitle(_translate("Detection_edges_Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Detection_edges_Dialog", "SET UP"))
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
        self.label_3.setText(_translate("Detection_edges_Dialog", "                                 LOW LEVEL"))
        self.label_4.setText(_translate("Detection_edges_Dialog", "                                HIGH LEVEL"))
        self.pushButton.setText(_translate("Detection_edges_Dialog", "SAVE"))
        self.pushButton_2.setText(_translate("Detection_edges_Dialog", "RESET"))
        self.OK_detection_edges_pushButton.setText(_translate("Detection_edges_Dialog", "OK"))
        self.Image_comboBox.setItemText(0, _translate("Detection_edges_Dialog", "01"))
        self.Image_comboBox.setItemText(1, _translate("Detection_edges_Dialog", "02"))
        self.Image_comboBox.setItemText(2, _translate("Detection_edges_Dialog", "03"))
        self.Image_comboBox.setItemText(3, _translate("Detection_edges_Dialog", "04"))
        self.Image_comboBox.setItemText(4, _translate("Detection_edges_Dialog", "05"))
        self.Image_comboBox.setItemText(5, _translate("Detection_edges_Dialog", "06"))
        self.Image_comboBox.setItemText(6, _translate("Detection_edges_Dialog", "07"))
        self.Image_comboBox.setItemText(7, _translate("Detection_edges_Dialog", "08"))
        self.Image_comboBox.setItemText(8, _translate("Detection_edges_Dialog", "09"))
        self.Image_comboBox.setItemText(9, _translate("Detection_edges_Dialog", "10"))
        self.Image_comboBox.setItemText(10, _translate("Detection_edges_Dialog", "11"))
        self.Image_comboBox.setItemText(11, _translate("Detection_edges_Dialog", "12"))
        self.Image_comboBox.setItemText(12, _translate("Detection_edges_Dialog", "13"))
        self.Image_comboBox.setItemText(13, _translate("Detection_edges_Dialog", "14"))
        self.Image_comboBox.setItemText(14, _translate("Detection_edges_Dialog", "15"))
        self.Image_comboBox.setItemText(15, _translate("Detection_edges_Dialog", "16"))
        self.Run_detection_edges_pushButton.setText(_translate("Detection_edges_Dialog", "RUN"))
        self.label_7.setText(_translate("Detection_edges_Dialog", "Position_1"))
        self.label_8.setText(_translate("Detection_edges_Dialog", "Position_2"))


    def Detection_edges_open_img(self):
        file_goc=os.getcwd()
        self.ten=self.Image_comboBox.currentText()
        file_config=file_goc.replace("/detection_edges","")
        self.file_img=file_config+"/img/"+self.ten+".bmp"
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
        self.img_detection_edges_label.set_dem(1)
        self.img_detection_edges_label.setfdk(1)

    def detection_edges_bar(self):
        if  self.img_detection_edges_label.x0 and self.img_detection_edges_label.x1 and self.img_detection_edges_label.y0 and self.img_detection_edges_label.y1 :
            self.x00=self.img_detection_edges_label.x0
            self.x10=self.img_detection_edges_label.x1
            self.y00=self.img_detection_edges_label.y0
            self.y10=self.img_detection_edges_label.y1

            self.x01=self.img_detection_edges_label.x01
            self.x11=self.img_detection_edges_label.x11
            self.y01=self.img_detection_edges_label.y01
            self.y11=self.img_detection_edges_label.y11

            self.x02=self.img_detection_edges_label.x02
            self.x12=self.img_detection_edges_label.x12
            self.y02=self.img_detection_edges_label.y02
            self.y12=self.img_detection_edges_label.y12

            self.x03=self.img_detection_edges_label.x03
            self.x13=self.img_detection_edges_label.x13
            self.y03=self.img_detection_edges_label.y03
            self.y13=self.img_detection_edges_label.y13

          


            
  #          print(self.img_detection_edges_label.x12)
   #         print(self.img_detection_edges_label.x02)
            self.threshold_img=detection_edges_xuluanh(self.img_0,self.img_10,self.x00,self.y00,self.x10,self.y10,self.x01,self.y01,self.x11,self.y11,
                                                       self.x02,self.y02,self.x12,self.y12,self.x03,self.y03,self.x13,self.y13)
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
    #def find_counter(self):
       #  img_1=cv2.imread(self.file_img,1)
      #   self.img_xuly=self.threshold_img.edges_count(img_1)
      #   height, width,channel = self.img_xuly.shape
        # step =  width*channel
      #   qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
      ##   pixmap = QPixmap.fromImage(qImg)
       #  self.img_detection_edges_label.setPixmap(QPixmap.fromImage(qImg))
       #  self.img_detection_edges_label.setCursor(QtCore.Qt.CrossCursor)
       #  self.img_detection_edges_label.setfdk(0)
    def find_direction(self):
        img_1=cv2.imread(self.file_img,1)
        self.img_xuly=self.threshold_img.edges_count(img_1)
        #self.direction,self.img_xuly=self.threshold_img.find_direction_xuly_2(img_1)
        self.direction=self.threshold_img.find_direction_xuly_2(img_1)
      #  print(self.direction)
        file_goc=os.getcwd()
        self.x00=self.img_detection_edges_label.x0
        self.x10=self.img_detection_edges_label.x1
        self.y00=self.img_detection_edges_label.y0
        self.y10=self.img_detection_edges_label.y1


        self.x01=self.img_detection_edges_label.x01
        self.x11=self.img_detection_edges_label.x11
        self.y01=self.img_detection_edges_label.y01
        self.y11=self.img_detection_edges_label.y11


        self.x02=self.img_detection_edges_label.x02
        self.x12=self.img_detection_edges_label.x12
        self.y02=self.img_detection_edges_label.y02
        self.y12=self.img_detection_edges_label.y12


        self.x03=self.img_detection_edges_label.x03
        self.x13=self.img_detection_edges_label.x13
        self.y03=self.img_detection_edges_label.y03
        self.y13=self.img_detection_edges_label.y13


        
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

        detection_edges_file.write(str(self.x01)+"\n")
        detection_edges_file.write(str(self.x11)+"\n")
        detection_edges_file.write(str(self.y01)+"\n")
        detection_edges_file.write(str(self.y11)+"\n")

        detection_edges_file.write(str(self.x02)+"\n")
        detection_edges_file.write(str(self.x12)+"\n")
        detection_edges_file.write(str(self.y02)+"\n")
        detection_edges_file.write(str(self.y12)+"\n")


        detection_edges_file.write(str(self.x03)+"\n")
        detection_edges_file.write(str(self.x13)+"\n")
        detection_edges_file.write(str(self.y03)+"\n")
        detection_edges_file.write(str(self.y13)+"\n")




        
        self.lowlevel_value=self.Low_level_horizontalSlider.value()
        self.highlevel_value=self.High_level_horizontalSlider.value()
        detection_edges_file.write(str(self.lowlevel_value)+"\n")
       # print(self.lowlevel_value)
        detection_edges_file.write(str(self.highlevel_value)+"\n")
       # print(self.highlevel_value)
        self.ten_Filter=self.Filter_comboBox.currentText()
        self.ten_Kernel=self.Kernel_comboBox.currentText()

        if self.ten_Kernel=="3X3":
            self.kernel=0
        if self.ten_Kernel=="5X5":
            self.kernel=1
        if self.ten_Kernel=="7X7":
            self.kernel=2
        if self.ten_Kernel=="9X9":
            self.kernel=3
        if self.ten_Kernel=="11X11":
            self.kernel=4
       # print(self.kernel)
        if self.ten_Filter=="Averaging":
            self.filter=0
        if self.ten_Filter=="Gaussian Filtering":
            self.filter=1
        if self.ten_Filter=="Median Filtering":
            self.filter=2
        detection_edges_file.write(str(self.kernel)+"\n")
        detection_edges_file.write(str(self.filter)+"\n")
        #print(self.direction[1])
        if len(self.direction)!=0:
             self.Postion_1_textEdit.setText(str(self.direction[0]))
             self.Position_2_textEdit.setText(str(self.direction[1]))


        
        height, width,channel = self.img_xuly.shape
        step =  width*channel
        qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.pushButton.setEnabled(0)
        self.pushButton_2.setEnabled(1)
        
        self.img_detection_edges_label.setPixmap(QPixmap.fromImage(qImg))
        self.img_detection_edges_label.setCursor(QtCore.Qt.CrossCursor)
        self.img_detection_edges_label.setfdk(0)


    def read_data(self):
         file_goc=os.getcwd()
         file_config=file_goc.replace("/detection_edges","/")+"/config"
         list_file=os.listdir(file_config)
         if len(list_file)==0:
              return 0


         filedata=file_config+"/"+"0001.txt"
         
         f=open(filedata)

         #print(self.link_file)
         f_anh=f.readline()
         f_anh=f_anh.rstrip()
         self.file_img=f.readline()
         self.file_img=self.file_img.rstrip()
     #    print(self.file_img)
         f_ten_function=f.readline()


         self.x00=int(f.readline())
         self.x10=int(f.readline())
         self.y00=int(f.readline())
         self.y10=int(f.readline())


         self.x01=int(f.readline())
         self.x11=int(f.readline())
         self.y01=int(f.readline())
         self.y11=int(f.readline())


         self.x02=int(f.readline())
         self.x12=int(f.readline())
         self.y02=int(f.readline())
         self.y12=int(f.readline())


         self.x03=int(f.readline())
         self.x13=int(f.readline())
         self.y03=int(f.readline())
         self.y13=int(f.readline())






         
         self.lowlevel_value=int(f.readline())
         self.highlevel_value=int(f.readline())

         self.kernel=int(f.readline())
         self.filter=int(f.readline())



         
#         self.img_xuly=cv2.imread(f_anh_sasds,1)
         self.img=cv2.imread(self.file_img,1)
         self.img_1=cv2.imread(self.file_img,1)
         self.Low_level_horizontalSlider.setValue(self.lowlevel_value)
         self.High_level_horizontalSlider.setValue(self.highlevel_value)

         self.Filter_comboBox.setCurrentIndex(self.filter)
         self.Kernel_comboBox.setCurrentIndex(self.kernel)

         self.High_level_horizontalSlider.setEnabled(0)
         self.Low_level_horizontalSlider.setEnabled(0)
         self.Filter_comboBox.setEnabled(0)
         self.Kernel_comboBox.setEnabled(0)
         self.Image_comboBox.setEnabled(0)
         self.OK_detection_edges_pushButton.setEnabled(0)
         self.pushButton.setEnabled(0)
        # self.img_0=cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        # self.img_10=cv2.cvtColor(self.img_1, cv2.COLOR_BGR2GRAY)
        # self.threshold_img=detection_edges_xuluanh(self.img_0,self.img_10,self.x00,self.y00,self.x10,self.y10)
        # self.ten_Filter=self.Filter_comboBox.currentText()
       #  self.ten_Kernel=self.Kernel_comboBox.currentText()
            
       #  self.threshold_img.filter_img(self.ten_Filter,self.ten_Kernel)
            
        # self.lowlevel_value=self.Low_level_horizontalSlider.value()
        # self.highlevel_value=self.High_level_horizontalSlider.value()
        # self.threshold_img.edges_img(self.lowlevel_value,self.highlevel_value)
        # img_1=cv2.imread(self.file_img,1)
        # self.img_xuly=self.threshold_img.edges_count(img_1)
        # self.direction,self.img_xuly=self.threshold_img.find_direction_xuly(img_1)
         
         height, width,channel = self.img.shape
         step =  width*channel
         qImg = QImage(self.img.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.img_detection_edges_label.setPixmap(QPixmap.fromImage(qImg))
         self.img_detection_edges_label.setCursor(QtCore.Qt.CrossCursor)
         self.img_detection_edges_label.setfdk(0)
         return 1
    def Reset_function(self):
         self.High_level_horizontalSlider.setEnabled(1)
         self.Low_level_horizontalSlider.setEnabled(1)
         self.Filter_comboBox.setEnabled(1)
         self.Kernel_comboBox.setEnabled(1)
         self.Image_comboBox.setEnabled(1)
         self.OK_detection_edges_pushButton.setEnabled(1)
         self.pushButton.setEnabled(1)
         self.pushButton_2.setEnabled(0)



    def controlTimer(self):
        # if timer is stopped
      #  camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        if not self.timer.isActive():
            # create video capture
            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            # start timer
            self.timer.start(20)
            self.Run_detection_edges_pushButton.setText("Stop")
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            camera.StopGrabbing()
            # update control_bt text
            self.Run_detection_edges_pushButton.setText("RUN")
           # self.Threshold_comboBox.setEnabled(1)


    def viewCam(self):
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

               
               self.threshold_img=detection_edges_xuluanh(self.img_0,self.img_10,self.x00,self.y00,self.x10,self.y10,self.x01,self.y01,self.x11,self.y11,
                                                       self.x02,self.y02,self.x12,self.y12,self.x03,self.y03,self.x13,self.y13)
               self.ten_Filter=self.Filter_comboBox.currentText()
               self.ten_Kernel=self.Kernel_comboBox.currentText()
            
               self.threshold_img.filter_img(self.ten_Filter,self.ten_Kernel)
            
               

               self.lowlevel_value=self.Low_level_horizontalSlider.value()
               self.highlevel_value=self.High_level_horizontalSlider.value()
               self.threshold_img.edges_img(self.lowlevel_value,self.highlevel_value)


               self.img_xuly=self.threshold_img.edges_count(self.image)
               self.direction=self.threshold_img.find_direction_xuly_2(self.image)
               height, width,channel = self.img_xuly.shape
               step =  width*channel
               qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
               pixmap = QPixmap.fromImage(qImg)
               if len(self.direction)!=0:
                  self.Postion_1_textEdit.setText(str(self.direction[0]))
                  self.Position_2_textEdit.setText(str(self.direction[1]))
                  text =str(self.direction[0])+str(self.direction[1])
                  
                  #camera.StopGrabbing()

                  
                ##  print(text)


                #  self.text= QByteArray(text.encode('gb2312'))
              #    print("text",text)
              #    self._serial.write(1)
                #  self.onReadyRead()

           
               self.img_detection_edges_label.setPixmap(QPixmap.fromImage(qImg))
               self.img_detection_edges_label.setCursor(QtCore.Qt.CrossCursor)
               self.img_detection_edges_label.setfdk(0)
         #      curr_value = GPIO.HIGH
           #    GPIO.output(output_dc_10, curr_value)
               self.timer.setInterval(500)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Detection_edges_Dialog = QtWidgets.QDialog()
    ui = Ui_Detection_edges_Dialog()
    ui.setupUi(Detection_edges_Dialog)
    Detection_edges_Dialog.show()
    sys.exit(app.exec_())

