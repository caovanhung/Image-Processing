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
import os
import cv2
from pypylon import pylon
#from pypylon import pylon
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

class Detection_circle_MyLabel(QLabel):

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

class Ui_Detection_circle_Dialog(object):
    def setupUi(self, Detection_circle_Dialog):
        Detection_circle_Dialog.setObjectName("Detection_circle_Dialog")
        Detection_circle_Dialog.resize(1026, 657)
        self.RUN_detection_circle_pushButton = QtWidgets.QPushButton(Detection_circle_Dialog)
        self.RUN_detection_circle_pushButton.setGeometry(QtCore.QRect(360, 600, 101, 51))
        self.RUN_detection_circle_pushButton.setObjectName("RUN_detection_circle_pushButton")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Detection_circle_Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(630, 10, 351, 581))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.Setup_detection_circle_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.Setup_detection_circle_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Setup_detection_circle_verticalLayout.setObjectName("Setup_detection_circle_verticalLayout")
        self.Setup_detection_circle_groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.Setup_detection_circle_groupBox.setObjectName("Setup_detection_circle_groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Setup_detection_circle_groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 321, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.Filter_detection_circle_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.Filter_detection_circle_comboBox.setObjectName("Filter_detection_circle_comboBox")
        self.Filter_detection_circle_comboBox.addItem("")
        self.Filter_detection_circle_comboBox.addItem("")
        self.Filter_detection_circle_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.Filter_detection_circle_comboBox)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Setup_detection_circle_groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 210, 321, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.Low_level_detection_circle_horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.Low_level_detection_circle_horizontalSlider.setMaximum(255)
        self.Low_level_detection_circle_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Low_level_detection_circle_horizontalSlider.setObjectName("Low_level_detection_circle_horizontalSlider")
        self.verticalLayout.addWidget(self.Low_level_detection_circle_horizontalSlider)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.Setup_detection_circle_groupBox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 140, 321, 51))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.High_level_detection_circle_horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget_4)
        self.High_level_detection_circle_horizontalSlider.setMinimum(1)
        self.High_level_detection_circle_horizontalSlider.setMaximum(255)
        self.High_level_detection_circle_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.High_level_detection_circle_horizontalSlider.setObjectName("High_level_detection_circle_horizontalSlider")
        self.verticalLayout_2.addWidget(self.High_level_detection_circle_horizontalSlider)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Setup_detection_circle_groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 321, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.Kernel_detection_circle_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.Kernel_detection_circle_comboBox.setObjectName("Kernel_detection_circle_comboBox")
        self.Kernel_detection_circle_comboBox.addItem("")
        self.Kernel_detection_circle_comboBox.addItem("")
        self.Kernel_detection_circle_comboBox.addItem("")
        self.Kernel_detection_circle_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.Kernel_detection_circle_comboBox)
        self.Detection_circle_tableWidget = QtWidgets.QTableWidget(self.Setup_detection_circle_groupBox)
        self.Detection_circle_tableWidget.setGeometry(QtCore.QRect(20, 410, 311, 111))
        self.Detection_circle_tableWidget.setObjectName("Detection_circle_tableWidget")
        self.Detection_circle_tableWidget.setColumnCount(3)
        self.Detection_circle_tableWidget.setRowCount(4)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.Setup_detection_circle_groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 280, 331, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.detection_color_R_Max_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        self.detection_color_R_Max_textEdit.setObjectName("detection_color_R_Max_textEdit")
        self.horizontalLayout_3.addWidget(self.detection_color_R_Max_textEdit)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.R_min_detection_circle_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        self.R_min_detection_circle_textEdit.setObjectName("R_min_detection_circle_textEdit")
        self.horizontalLayout_3.addWidget(self.R_min_detection_circle_textEdit)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.Setup_detection_circle_groupBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(20, 370, 321, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.Number_Detection_circle_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_5)
        self.Number_Detection_circle_spinBox.setObjectName("Number_Detection_circle_spinBox")
        self.horizontalLayout_5.addWidget(self.Number_Detection_circle_spinBox)
        self.OK_pushButton = QtWidgets.QPushButton(self.Setup_detection_circle_groupBox)
        self.OK_pushButton.setGeometry(QtCore.QRect(140, 330, 89, 25))
        self.OK_pushButton.setObjectName("OK_pushButton")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.Setup_detection_circle_groupBox)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(80, 530, 231, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.detection_circle_Save_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.detection_circle_Save_pushButton.setObjectName("detection_circle_Save_pushButton")
        self.horizontalLayout_6.addWidget(self.detection_circle_Save_pushButton)
        self.Detection_circle_Reset_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.Detection_circle_Reset_pushButton.setObjectName("Detection_circle_Reset_pushButton")
        self.horizontalLayout_6.addWidget(self.Detection_circle_Reset_pushButton)
        self.Setup_detection_circle_verticalLayout.addWidget(self.Setup_detection_circle_groupBox)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Detection_circle_Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 600, 231, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.OK_detection_circle_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.OK_detection_circle_pushButton.setObjectName("OK_detection_circle_pushButton")
        self.horizontalLayout_4.addWidget(self.OK_detection_circle_pushButton)
        self.Detection_circle_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.Detection_circle_comboBox.setObjectName("Detection_circle_comboBox")
        self.Detection_circle_comboBox.addItem("")
        self.Detection_circle_comboBox.addItem("")
        self.Detection_circle_comboBox.addItem("")
        self.Detection_circle_comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.Detection_circle_comboBox)
        self.scrollArea = QtWidgets.QScrollArea(Detection_circle_Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 611, 561))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 609, 559))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
      #  self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.Detection_circle_img_label=Detection_circle_MyLabel(self.scrollAreaWidgetContents)
        self.scrollArea.setBackgroundRole(QPalette.Dark)#THEM DONG
        self.Detection_circle_img_label.setWordWrap(True)
        self.Detection_circle_img_label.setObjectName("label")
        self.scrollArea.setWidget(self.Detection_circle_img_label)# dong quan trong
        
        self.OK_detection_circle_pushButton.clicked.connect(self.Detection_circle_open_img)
        self.Low_level_detection_circle_horizontalSlider.sliderMoved.connect(self.detection_circle_bar)
        self.High_level_detection_circle_horizontalSlider.sliderMoved.connect(self.detection_circle_bar)
        self.OK_pushButton.clicked.connect(self.counter)
        self.Number_Detection_circle_spinBox.valueChanged.connect(self.display_circle)
        self.detection_circle_Save_pushButton.clicked.connect(self.Detection_circle_xyly_0)
        self.Detection_circle_Reset_pushButton.clicked.connect(self.Detection_circle_Reset)
        self.timer = QTimer()
        self.timer.timeout.connect(self.Detection_circle_viewCam)
        self.RUN_detection_circle_pushButton.clicked.connect(self.Detection_circle_controlTimer)


        self.Detection_circle_tableWidget.setVerticalHeaderLabels(['X','Y','Number circle','R'])
        self.Detection_circle_tableWidget.setHorizontalHeaderLabels(['Min', 'Measure', 'Max'])
        self.Detection_circle_Reset_pushButton.setEnabled(0)


        self.retranslateUi(Detection_circle_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Detection_circle_Dialog)

    def retranslateUi(self, Detection_circle_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Detection_circle_Dialog.setWindowTitle(_translate("Detection_circle_Dialog", "Dialog"))
        self.RUN_detection_circle_pushButton.setText(_translate("Detection_circle_Dialog", "RUN"))
        self.Setup_detection_circle_groupBox.setTitle(_translate("Detection_circle_Dialog", "SETUP"))
        self.label_2.setText(_translate("Detection_circle_Dialog", "KERNEL"))
        self.Filter_detection_circle_comboBox.setItemText(0, _translate("Detection_circle_Dialog", "Averaging"))
        self.Filter_detection_circle_comboBox.setItemText(1, _translate("Detection_circle_Dialog", "Gaussian Filtering"))
        self.Filter_detection_circle_comboBox.setItemText(2, _translate("Detection_circle_Dialog", "Median Filtering"))
        self.label_3.setText(_translate("Detection_circle_Dialog", "                                    Lowlevel"))
        self.label_4.setText(_translate("Detection_circle_Dialog", "                                    Highlevel"))
        self.label.setText(_translate("Detection_circle_Dialog", "FILTER"))
        self.Kernel_detection_circle_comboBox.setItemText(0, _translate("Detection_circle_Dialog", "3X3"))
        self.Kernel_detection_circle_comboBox.setItemText(1, _translate("Detection_circle_Dialog", "5X5"))
        self.Kernel_detection_circle_comboBox.setItemText(2, _translate("Detection_circle_Dialog", "7X7"))
        self.Kernel_detection_circle_comboBox.setItemText(3, _translate("Detection_circle_Dialog", "9X9"))
        self.label_6.setText(_translate("Detection_circle_Dialog", "R_Max"))
        self.label_7.setText(_translate("Detection_circle_Dialog", "R_Min"))
        self.label_5.setText(_translate("Detection_circle_Dialog", "Number circle"))
        self.OK_pushButton.setText(_translate("Detection_circle_Dialog", "OK"))
        self.detection_circle_Save_pushButton.setText(_translate("Detection_circle_Dialog", "SAVE"))
        self.Detection_circle_Reset_pushButton.setText(_translate("Detection_circle_Dialog", "RESET"))
        self.OK_detection_circle_pushButton.setText(_translate("Detection_circle_Dialog", "OK"))
        self.Detection_circle_comboBox.setItemText(0, _translate("Detection_circle_Dialog", "01"))
        self.Detection_circle_comboBox.setItemText(1, _translate("Detection_circle_Dialog", "02"))
        self.Detection_circle_comboBox.setItemText(2, _translate("Detection_circle_Dialog", "03"))
        self.Detection_circle_comboBox.setItemText(3, _translate("Detection_circle_Dialog", "04"))


    def Detection_circle_open_img(self):
        file_goc=os.getcwd()
        self.ten=self.Detection_circle_comboBox.currentText()
        file_config=file_goc.replace("/detection_circle","")
        self.file_img=file_config+"/"+self.ten+".jpg"
      #  print(file_img)
        self.img=cv2.imread(self.file_img,1)
        self.img_1=cv2.imread(self.file_img,1)
       # self.img=cv2.resize(self.img,(601, 581))
      #  self.img_1=cv2.resize(self.img_1,(601, 581))
        self.img_0=cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.img_10=cv2.cvtColor(self.img_1, cv2.COLOR_BGR2GRAY)

        height, width,channel = self.img.shape
        step =  width*channel
        qImg = QImage(self.img.data, width, height, step, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.Detection_circle_img_label.setPixmap(QPixmap.fromImage(qImg))
        self.Detection_circle_img_label.setCursor(QtCore.Qt.CrossCursor)
        self.Detection_circle_img_label.setfdk(1)



    def detection_circle_bar(self):
        if  self.Detection_circle_img_label.x0 and self.Detection_circle_img_label.x1 and self.Detection_circle_img_label.y0 and self.Detection_circle_img_label.y1 :
            self.x00=self.Detection_circle_img_label.x0
            self.x10=self.Detection_circle_img_label.x1
            self.y00=self.Detection_circle_img_label.y0
            self.y10=self.Detection_circle_img_label.y1
            self.Detection_circle_threshold_img=detection_circle_xuluanh(self.img_0,self.img_10,self.x00,self.y00,self.x10,self.y10)
            self.ten_Filter=self.Filter_detection_circle_comboBox.currentText()
            self.ten_Kernel=self.Kernel_detection_circle_comboBox.currentText()
            
            self.Detection_circle_threshold_img.filter_img(self.ten_Filter,self.ten_Kernel)
            
            self.lowlevel_value=self.Low_level_detection_circle_horizontalSlider.value()
            self.highlevel_value=self.High_level_detection_circle_horizontalSlider.value()

      #      print ("Low",self.lowlevel_value)
      #      print ("High",self.highlevel_value)
            self.Detection_circle_threshold_img.edges_img(self.lowlevel_value,self.highlevel_value)
            self.img_cuoi=self.Detection_circle_threshold_img.get_img()
                
            height, width  =self.img_cuoi.shape
            step = width
            qImg = QImage(self.img_cuoi.data, width, height, step, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qImg)
            self.Detection_circle_img_label.setPixmap(QPixmap.fromImage(qImg))
            self.Detection_circle_img_label.setfdk(0)
  #  def detection_circle_bar(self):
    def Number_Detection_circle(self):
           file_goc=os.getcwd()
           self.ten=self.Detection_circle_comboBox.currentText()
           file_config=file_goc.replace("/detection_circle","")
           self.file_img=file_config+"/"+self.ten+".jpg"
           self.img=cv2.imread(self.file_img,1)     
           self.img_xuly=self.Detection_circle_threshold_img.detect_circle_img(self.img)
           height, width,channel = self.img_xuly.shape
           step =  width*channel
           qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
           pixmap = QPixmap.fromImage(qImg)
           self.Detection_circle_img_label.setPixmap(QPixmap.fromImage(qImg))
           self.Detection_circle_img_label.setCursor(QtCore.Qt.CrossCursor)
           self.Detection_circle_img_label.setfdk(0)
    def counter(self):
           file_goc=os.getcwd()
           self.ten=self.Detection_circle_comboBox.currentText()

           R_min = int (self.R_min_detection_circle_textEdit .toPlainText())
           R_max = int (self.detection_color_R_Max_textEdit .toPlainText())
           file_config=file_goc.replace("/detection_circle","")
           self.file_img=file_config+"/"+self.ten+".jpg"
           self.img=cv2.imread(self.file_img,1)        
           list_circle,sotam,self.img_xuly=self.Detection_circle_threshold_img.detect_counter(self.img,R_max,R_min)
           height, width,channel = self.img_xuly.shape
           step =  width*channel
           qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
           pixmap = QPixmap.fromImage(qImg)

           self.Number_Detection_circle_spinBox.setRange(1,sotam)
          # self.Number_Detection_circle_spinBox.setValue(1)           
           self.Detection_circle_img_label.setPixmap(QPixmap.fromImage(qImg))
           self.Detection_circle_img_label.setCursor(QtCore.Qt.CrossCursor)
           self.Detection_circle_img_label.setfdk(0)
          

    def display_circle(self):
         self.img=cv2.imread(self.file_img,1)
         self.Value_circle=self.Number_Detection_circle_spinBox.value()
         
         tam_x,tam_y,sotam,r,self.img_xuly=self.Detection_circle_threshold_img.position_circle(self.img,self.Value_circle-1)
         height, width,channel = self.img_xuly.shape
         step =  width*channel
         qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.Detection_circle_tableWidget.setItem(0,1, QTableWidgetItem(str(tam_x)))
         self.Detection_circle_tableWidget.setItem(1,1, QTableWidgetItem(str(tam_y)))
         self.Detection_circle_tableWidget.setItem(2,1, QTableWidgetItem(str(sotam)))
         self.Detection_circle_tableWidget.setItem(3,1, QTableWidgetItem(str(r)))
           
         self.Detection_circle_img_label.setPixmap(QPixmap.fromImage(qImg))
         self.Detection_circle_img_label.setCursor(QtCore.Qt.CrossCursor)
         self.Detection_circle_img_label.setfdk(0)          




    def Detection_circle_xyly_0(self):
        file_goc=os.getcwd()
        self.x00=self.Detection_circle_img_label.x0
        self.x10=self.Detection_circle_img_label.x1
        self.y00=self.Detection_circle_img_label.y0
        self.y10=self.Detection_circle_img_label.y1
        if file_goc.find("detection_circle",20)==-1:
             self.file_img_bandau=file_goc+"/image_function"
             self.file_img=os.getcwd()+"/cut_image_function"
        else:
             self.file_img_bandau=file_goc.replace("detection_circle","image_function")
             self.file_img=file_goc.replace("detection_circle","cut_image_function")
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
        file_config=file_goc.replace("/detection_circle","/")+"/config"
        List_file=os.listdir(file_config)


        filedata=file_config+"/"+self.ten+".txt"
        
        detection_circle_file = open(filedata, 'w')
        detection_circle_file.write( self.file_img+"\n")
        detection_circle_file.write(self.file_img_bandau+"\n")

        detection_circle_file.write("detection_circle\n")
        
        detection_circle_file.write(str(self.x00)+"\n")
        detection_circle_file.write(str(self.x10)+"\n")
        detection_circle_file.write(str(self.y00)+"\n")
        detection_circle_file.write(str(self.y10)+"\n")
        self.High_level_detection_circle_horizontalSlider.setEnabled(0)
        self.Low_level_detection_circle_horizontalSlider.setEnabled(0)
        self.Filter_detection_circle_comboBox.setEnabled(0)
        self.Kernel_detection_circle_comboBox.setEnabled(0)
        self.Detection_circle_tableWidget.setEnabled(0)
       # self.Xuly_detection_edge_pushButton.setEnabled(0)
        self.R_min_detection_circle_textEdit .setEnabled(0)
        self.detection_circle_Save_pushButton.setEnabled(0)
        self.detection_color_R_Max_textEdit .setEnabled(0)
        self.OK_pushButton.setEnabled(0)
        self.OK_detection_circle_pushButton.setEnabled(0)
        
        self.Number_Detection_circle_spinBox.setEnabled(0)
        self.Detection_circle_Reset_pushButton.setEnabled(1)

    def Detection_circle_Reset(self):
        self.High_level_detection_circle_horizontalSlider.setEnabled(1)
        self.Low_level_detection_circle_horizontalSlider.setEnabled(1)
        self.Filter_detection_circle_comboBox.setEnabled(1)
        self.Kernel_detection_circle_comboBox.setEnabled(1)
        self.Detection_circle_tableWidget.setEnabled(1)
       # self.Xuly_detection_edge_pushButton.setEnabled(0)
        self.R_min_detection_circle_textEdit .setEnabled(1)
        self.detection_circle_Save_pushButton.setEnabled(1)
        self.detection_color_R_Max_textEdit .setEnabled(1)
        self.OK_pushButton.setEnabled(1)
        
        self.Number_Detection_circle_spinBox.setEnabled(1)
        self.Detection_circle_Reset_pushButton.setEnabled(0)
        self.OK_detection_circle_pushButton.setEnabled(1)        
    def Detection_circle_controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            # start timer
            self.timer.start(20)
            self.RUN_detection_circle_pushButton.setText("Stop")
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            camera.StopGrabbing()
            # update control_bt text
            self.RUN_detection_circle_pushButton.setText("RUN")
           # self.Threshold_comboBox.setEnabled(1)


    def Detection_circle_viewCam(self):
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
               self.Detection_circle_threshold_img=detection_circle_xuluanh(self.img_0,self.img_10,self.x00,self.y00,self.x10,self.y10)
               self.ten_Filter=self.Filter_detection_circle_comboBox.currentText()
               self.ten_Kernel=self.Kernel_detection_circle_comboBox.currentText()
            
               self.Detection_circle_threshold_img.filter_img(self.ten_Filter,self.ten_Kernel)
            
               self.lowlevel_value=self.Low_level_detection_circle_horizontalSlider.value()
               self.highlevel_value=self.High_level_detection_circle_horizontalSlider.value()

      #      print ("Low",self.lowlevel_value)
      #      print ("High",self.highlevel_value)
               self.Detection_circle_threshold_img.edges_img(self.lowlevel_value,self.highlevel_value)
               self.img_cuoi=self.Detection_circle_threshold_img.get_img()
               cv2.rectangle( self.image ,(self.x00,self.y00),(self.x10,self.y10),(0,255,0),3)
               R_min = int (self.R_min_detection_circle_textEdit .toPlainText())
               R_max = int (self.detection_color_R_Max_textEdit .toPlainText())
               list_circle,sotam,self.img_xuly=self.Detection_circle_threshold_img.detect_counter(self.img,R_max,R_min)
               self.Value_circle=self.Number_Detection_circle_spinBox.value()
               cv2.rectangle( self.image ,(self.x00,self.y00),(self.x10,self.y10),(0,255,0),3)
         
               tam_x,tam_y,sotam,r,self.img_xuly=self.Detection_circle_threshold_img.position_circle(self.image,self.Value_circle-1)
               height, width,channel = self.img_xuly.shape
               step =  width*channel
               qImg = QImage(self.img_xuly.data, width, height, step, QImage.Format_RGB888)
               pixmap = QPixmap.fromImage(qImg)
               self.Detection_circle_tableWidget.setItem(0,1, QTableWidgetItem(str(tam_x)))
               self.Detection_circle_tableWidget.setItem(1,1, QTableWidgetItem(str(tam_y)))
               self.Detection_circle_tableWidget.setItem(2,1, QTableWidgetItem(str(sotam)))
               self.Detection_circle_tableWidget.setItem(3,1, QTableWidgetItem(str(r)))
           
               self.Detection_circle_img_label.setPixmap(QPixmap.fromImage(qImg))
               self.Detection_circle_img_label.setCursor(QtCore.Qt.CrossCursor)
               self.Detection_circle_img_label.setfdk(0)          

   
             #cv2.rectangle(self.image_1,(self.x00,self.y00),(self.x10,self.y10),3) 



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Detection_circle_Dialog = QtWidgets.QDialog()
    ui = Ui_Detection_circle_Dialog()
    ui.setupUi(Detection_circle_Dialog)
    Detection_circle_Dialog.show()
    sys.exit(app.exec_())

