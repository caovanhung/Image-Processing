# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detection_OCR.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QRect, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtGui import QIcon
from detect_OCR_xulyanh import*
from pypylon import pylon
import cv2
import os 
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
class Detection_OCR_MyLabel(QLabel):

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






class Ui_Dialog_OCR(object):
    dk_detection_OCR=0
    detection_OCR_file='/home/tranthang/Desktop/camera_1/config/1.txt'
    def __init__(self,dk_OCR,detection_OCR_file):
         self.dk_detection=dk_OCR
         self.detection_OCR_file=detection_OCR_file
    def setupUi(self, Dialog_OCR):
        Dialog_OCR.setObjectName("Dialog_OCR")
        Dialog_OCR.resize(978, 637)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog_OCR)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 671, 521))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_OCR_label = Detection_OCR_MyLabel(self.horizontalLayoutWidget)
        self.img_OCR_label.setText("")
        self.img_OCR_label.setObjectName("img_OCR_label")
        self.horizontalLayout.addWidget(self.img_OCR_label)
        self.OK_OCR_pushButton = QtWidgets.QPushButton(Dialog_OCR)
        self.OK_OCR_pushButton.setGeometry(QtCore.QRect(10, 580, 89, 25))
        self.OK_OCR_pushButton.setObjectName("OK_OCR_pushButton")
        self.OCR_comboBox = QtWidgets.QComboBox(Dialog_OCR)
        self.OCR_comboBox.setGeometry(QtCore.QRect(180, 580, 86, 25))
        self.OCR_comboBox.setObjectName("OCR_comboBox")
        self.OCR_comboBox.addItem("")
        self.OCR_comboBox.addItem("")
        self.OCR_comboBox.addItem("")
        self.OCR_comboBox.addItem("")
        self.OCR_horizontalScrollBar = QtWidgets.QScrollBar(Dialog_OCR)
        self.OCR_horizontalScrollBar.setGeometry(QtCore.QRect(0, 540, 671, 16))
        self.OCR_horizontalScrollBar.setMaximum(255)
        self.OCR_horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.OCR_horizontalScrollBar.setObjectName("OCR_horizontalScrollBar")
        self.XuLy_OCR_pushButton = QtWidgets.QPushButton(Dialog_OCR)
        self.XuLy_OCR_pushButton.setGeometry(QtCore.QRect(340, 580, 89, 25))
        self.XuLy_OCR_pushButton.setObjectName("XuLy_OCR_pushButton")
        self.OCR_Run_pushButton = QtWidgets.QPushButton(Dialog_OCR)
        self.OCR_Run_pushButton.setGeometry(QtCore.QRect(580, 580, 89, 25))
        self.OCR_Run_pushButton.setObjectName("OCR_Run_pushButton")
        self.OCR_tableWidget = QtWidgets.QTableWidget(Dialog_OCR)
        self.OCR_tableWidget.setGeometry(QtCore.QRect(680, 220, 271, 192))
        self.OCR_tableWidget.setObjectName("OCR_tableWidget")
        self.OCR_tableWidget.setColumnCount(3)
        self.OCR_tableWidget.setRowCount(1)

        if self.dk_detection==0 :
        
             self.OK_OCR_pushButton.clicked.connect(self.OCR_openc_image)
             self.XuLy_OCR_pushButton.clicked.connect(self.OCR_xuly)
             self.OCR_horizontalScrollBar.sliderMoved.connect(self.Threshold_OCR_bar)
             self.OCR_comboBox.currentIndexChanged.connect(self.Detection_OCR_selectionchange)        
             self.timer = QTimer()
             self.timer.timeout.connect(self.OCR_viewCam)
             self.OCR_Run_pushButton.clicked.connect(self.OCR_controlTimer)
             self.XuLy_OCR_pushButton.setEnabled(0)
             self.OCR_horizontalScrollBar.setEnabled(0)
            # self.OCR_comboBox.setEnabled(0)
             self.OCR_Run_pushButton.setEnabled(0)
        if self.dk_detection !=0:
             self.read_data_OCR()
             self.OK_OCR_pushButton.clicked.connect(self.OCR_openc_image)
             self.XuLy_OCR_pushButton.clicked.connect(self.OCR_xuly)
             self.OCR_horizontalScrollBar.sliderMoved.connect(self.Threshold_OCR_bar)
             self.OCR_comboBox.currentIndexChanged.connect(self.Detection_OCR_selectionchange)        
             self.timer = QTimer()
             self.timer.timeout.connect(self.OCR_viewCam)
             self.OCR_Run_pushButton.clicked.connect(self.OCR_controlTimer)

             self.XuLy_OCR_pushButton.setEnabled(0)
             self.OCR_horizontalScrollBar.setEnabled(0)
             self.OCR_comboBox.setEnabled(0)
             self.OK_OCR_pushButton.setEnabled(0)
       
        self.retranslateUi(Dialog_OCR)
        QtCore.QMetaObject.connectSlotsByName(Dialog_OCR)

    def retranslateUi(self, Dialog_OCR):
        _translate = QtCore.QCoreApplication.translate
        Dialog_OCR.setWindowTitle(_translate("Dialog_OCR", "Dialog"))
        self.OK_OCR_pushButton.setText(_translate("Dialog_OCR", "OK"))
        self.OCR_comboBox.setItemText(0, _translate("Dialog_OCR", "01"))
        self.OCR_comboBox.setItemText(1, _translate("Dialog_OCR", "02"))
        self.OCR_comboBox.setItemText(2, _translate("Dialog_OCR", "03"))
        self.OCR_comboBox.setItemText(3, _translate("Dialog_OCR", "04"))
        self.XuLy_OCR_pushButton.setText(_translate("Dialog_OCR", "XULY"))
        self.OCR_Run_pushButton.setText(_translate("Dialog_OCR", "RUN"))
    def OCR_openc_image(self):
        self.ten=self.OCR_comboBox.currentText()
        file_goc=os.getcwd()
        file_img=file_goc.replace("detection_OCR","")
        file_img=file_img+"/"+self.ten+".jpg"
        self.img_2=cv2.imread(file_img,1)

        self.img_2=cv2.resize(self.img_2,(671, 521))
        self.img=cv2.cvtColor(self.img_2, cv2.COLOR_BGR2GRAY)
        self.img_1=cv2.imread(file_img,0)
        
        
        self.img_1=cv2.resize(self.img_1,(671, 521))
        height, width ,channel= self.img_2.shape
        #channel=1
        step = channel * width
        #qImg = QImage(self.img.data, width, height, step, QImage.Format_Grayscale8)
        qImg = QImage(self.img_2.data, width, height, step, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.img_OCR_label.setPixmap(QPixmap.fromImage(qImg))
        self.img_OCR_label.setCursor(QtCore.Qt.CrossCursor)
        self.img_OCR_label.setfdk(1)
        self.OK_OCR_pushButton.setEnabled(0)
        self.XuLy_OCR_pushButton.setEnabled(1)
        self.OCR_horizontalScrollBar.setEnabled(1) 


    def Threshold_OCR_bar(self):
        if  self.img_OCR_label.x0 and self.img_OCR_label.x1 and self.img_OCR_label.y0 and self.img_OCR_label.y1 :
            self.x00=self.img_OCR_label.x0
            self.x10=self.img_OCR_label.x1
            self.y00=self.img_OCR_label.y0
            self.y10=self.img_OCR_label.y1

            #self.dk=1;
            self.threshold_img=Detect_OCR_xulyanh(self.img,self.img_1,self.img_2,self.x00,self.y00,self.x10,self.y10)
            self.thresh_value=self.OCR_horizontalScrollBar.value()
            self.threshold_img.Threshold_xuly(self.thresh_value)
            height, width =self.img.shape
            step = width
            qImg = QImage(self.img.data, width, height, step, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qImg)
            self.img_OCR_label.setPixmap(QPixmap.fromImage(qImg))
            self.img_OCR_label.setfdk(0)
    def OCR_xuly(self):
        self.Threshold_OCR_bar()
        print (self.threshold_img.Detect_OCR())
        img_box=self.threshold_img.Threshold_getdata()
        height, width ,channel= img_box.shape
        step = width*channel
        qImg = QImage(img_box.data, width, height, step, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.img_OCR_label.setPixmap(QPixmap.fromImage(qImg))       
        self.OCR_tableWidget.setItem(0,1, QTableWidgetItem(self.threshold_img.Detect_OCR()))
        self.XuLy_OCR_pushButton.setEnabled(0)
        self.OCR_horizontalScrollBar.setEnabled(0)
        self.OCR_Run_pushButton.setEnabled(1)
  
        file_goc=os.getcwd()
        if file_goc.find("detection_OCR",20)==-1:
             self.file_img_bandau=file_goc+"/image_function"
             self.file_img=os.getcwd()+"/cut_image_function"
        else:
             self.file_img_bandau=file_goc.replace("detection_OCR","image_function")
             self.file_img=file_goc.replace("detection_OCR","cut_image_function")
        self.file_img_bandau=self.file_img_bandau.rstrip()
        
        self.file_img=self.file_img.rstrip()
        #print(self.file_img_bandau)
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


        cv2.imwrite(self.file_img_bandau,img_box)
        self.img_cat=img_box[self.y00:self.y10,self.x00:self.x10]

        cv2.imwrite(self.file_img,self.img_cat)
        file_goc=os.getcwd()
        file_config=file_goc.replace("/detection_OCR","/")+"/config"
        List_file=os.listdir(file_config)
        #print(len(List_file))
        filedata=file_config+"/"+self.ten+".txt"
        
        detection_OCR_file = open(filedata, 'w')
        detection_OCR_file.write( self.file_img+"\n")
        detection_OCR_file.write(self.file_img_bandau+"\n")

        detection_OCR_file.write("detection_OCR\n")
        
        detection_OCR_file.write(str(self.x00)+"\n")
        detection_OCR_file.write(str(self.x10)+"\n")
        detection_OCR_file.write(str(self.y00)+"\n")
        detection_OCR_file.write(str(self.y10)+"\n")
        self.thresh_value=self.OCR_horizontalScrollBar.value()
        detection_OCR_file.write(str(self.thresh_value)+"\n")
        detection_OCR_file.close()
     #   detection_color_file.write(str(self.checkBox.isChecked())+"\n")









        
    def Detection_OCR_selectionchange(self):
        #self.XuLy_OCR_pushButton.setEnabled(1)         
        self.OK_OCR_pushButton.setEnabled(1)
        #self.OCR_horizontalScrollBar.setEnabled(1)




    def OCR_controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            # start timer
            self.timer.start(20)
            self.OCR_Run_pushButton.setText("Stop")
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            camera.StopGrabbing()
            # update control_bt text
            self.OCR_Run_pushButton.setText("RUN")
            self.OCR_comboBox.setEnabled(1)


    def OCR_viewCam(self):
        if  self.img_OCR_label.x0 and self.img_OCR_label.x1 and self.img_OCR_label.y0 and self.img_OCR_label.y1 : 
            converter = pylon.ImageFormatConverter()
            converter.OutputPixelFormat = pylon.PixelType_BGR8packed
            converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

            # create video capture
            grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grabResult.GrabSucceeded():
        # Access the image data
               image = converter.Convert(grabResult)
               self.img = image.GetArray()
            #print(self.img.shape)
               self.img_0=cv2.resize(self.img,(671, 521))
               image_1  = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY )
               self.image_1=cv2.resize(image_1,(671, 521))
            
               image_2 = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY )
               self.image_2=cv2.resize(image_2,(671, 521))
               
               cv2.rectangle(self.img_0,(self.x00,self.y00),(self.x10,self.y10),(0,0,255),3)                
               self.OCR_img_0=Detect_OCR_xulyanh(self.image_1,self.image_2,self.img_0,self.x00,self.y00,self.x10,self.y10)
               thresh_value_1=self.OCR_horizontalScrollBar.value()
               #self.dk=0;
               
              # if self.White_checkBox.isChecked() == True:
               self.OCR_img_0.Threshold_xuly(thresh_value_1)      
               self.img_c=self.OCR_img_0.Threshold_getdata()
               self.OCR_tableWidget.setItem(0,1, QTableWidgetItem(self.OCR_img_0.Detect_OCR()))
               #if self.Black_checkBox.isChecked() == True:
                 #   self.threshold_img_1.Threshold_xuly(thresh_value_1,2)      
                #    img_c=self.threshold_img_1.Threshold_getdata()
                 #   self.Threshold_tableWidget.setItem(0,1, QTableWidgetItem(str(self.threshold_img_1.Threshold_count_den())))  
               height, width,channel = self.img_c.shape
               step =  width*channel
               qImg = QImage(self.img_c.data, width, height, step, QImage.Format_RGB888)
               self.img_OCR_label.setPixmap(QPixmap.fromImage(qImg))

    def read_data_OCR(self):
         f=open(self.detection_OCR_file)
         #print(self.link_file)
         f_anh=f.readline()
         f_anh=f_anh.rstrip()
         f_anh_sasds=f.readline()
         f_anh_sasds=f_anh_sasds.rstrip()
         f_ten_function=f.readline()
         self.x00=int(f.readline())
         self.x10=int(f.readline())
         self.y00=int(f.readline())
         self.y10=int(f.readline())
         self.value_bar=int(f.readline())
         self.OCR_horizontalScrollBar.setValue(self.value_bar)
         print(f_anh_sasds)
         img_hienthi=cv2.imread(f_anh_sasds,1)
         img_hienthi=cv2.resize(img_hienthi,(671, 521))
         height, width,channel = img_hienthi.shape
         step =width*channel
         qImg = QImage(img_hienthi.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.img_OCR_label.setPixmap(QPixmap.fromImage(qImg))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_OCR = QtWidgets.QDialog()
    ui = Ui_Dialog_OCR(0,'a')
    ui.setupUi(Dialog_OCR)
    Dialog_OCR.show()
    sys.exit(app.exec_())

