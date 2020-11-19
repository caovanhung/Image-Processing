from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtGui import QIcon
from Threshold_xulyanh import*
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QRect, Qt
from pypylon import pylon
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
import os

class Threshold_MyLabel(QLabel):

     x0 = 0
     y0 = 0
     x1 = 0
     y1 = 0
     flag = False



     x00=0
     y00=0
     x01=0
     y01=0
     dem=0
     dk=0
     
 #Mouse click event
     def mousePressEvent(self,event):
        if self.dk==1:

          self.flag = True
          self.x0 = event.x()
          self.y0 = event.y()
        if self.dk==2:
           self.flag = True
           self.x00 = event.x()
           self.y00 = event.y()            
 #Mouse release event
     def mouseReleaseEvent(self,event):
          if self.dk:
             self.flag = False
             self.dem=self.dem+1
 #Mouse movement events
     def mouseMoveEvent(self,event):
        if self.flag and self.dk==1:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()
        if self.flag and self.dk==2:
            self.x01 = event.x()
            self.y01 = event.y()
            self.update()             
     def setfdk(self,flag):
          self.dk=flag
     def getdk(self):
          return self.dk;
      #Draw events
     def get_flag(self):
         return self.dem
     def paintEvent(self, event):
          
     
          super().paintEvent(event)
          if self.dk==1:
               rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
         # print(self.x1)
          if self.dk==2 or self.dem != 0:
               rect0=QRect(self.x00, self.y00, abs(self.x01-self.x00), abs(self.y01-self.y00))
        #  print(self.y1)
          painter = QPainter(self)
          
          if self.dk==1:
             painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
             painter.drawRect(rect)
          if self.dk==2 or self.dem != 0:
             painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
             painter.drawRect(rect0)




             
class Ui_Threshold_Dialog(object):
    dk=0
    dk_function_pixel=0
    link_file='/home/tranthang/Desktop/camera_1/config/1.txt'
    
    def __init__(self,dk_pixel,link_file):
        self.dk_function_pixel=dk_pixel
        self.link_file=link_file
        
    def setupUi(self, Threshold_Dialog):
        Threshold_Dialog.setObjectName("Threshold_Dialog")
        Threshold_Dialog.resize(795, 588)
        self.Threshold_Bar = QtWidgets.QScrollBar(Threshold_Dialog)
        self.Threshold_Bar.setGeometry(QtCore.QRect(0, 500, 511, 20))
        self.Threshold_Bar.setOrientation(QtCore.Qt.Horizontal)
        self.Threshold_Bar.setObjectName("Threshold_Bar")
        self.Threshold_OK_pushButton = QtWidgets.QPushButton(Threshold_Dialog)
        self.Threshold_OK_pushButton.setGeometry(QtCore.QRect(30, 540, 89, 25))
        self.Threshold_OK_pushButton.setObjectName("Threshold_OK_pushButton")
        self.Threashold_xuly_pushButton = QtWidgets.QPushButton(Threshold_Dialog)
        self.Threashold_xuly_pushButton.setGeometry(QtCore.QRect(360, 540, 89, 25))
        self.Threashold_xuly_pushButton.setObjectName("Threashold_xuly_pushButton")
        self.Threshold_run_pushButton = QtWidgets.QPushButton(Threshold_Dialog)
        self.Threshold_run_pushButton.setGeometry(QtCore.QRect(560, 540, 89, 25))
        self.Threshold_run_pushButton.setObjectName("Threshold_run_pushButton")
        self.Threshold_comboBox = QtWidgets.QComboBox(Threshold_Dialog)
        self.Threshold_comboBox.setGeometry(QtCore.QRect(220, 540, 86, 25))
        self.Threshold_comboBox.setObjectName("Threshold_comboBox")
        self.Threshold_comboBox.addItem("")
        self.Threshold_comboBox.addItem("")
        self.Threshold_comboBox.addItem("")
        self.Threshold_comboBox.addItem("")
        self.Threshold_tableWidget = QtWidgets.QTableWidget(Threshold_Dialog)
        self.Threshold_tableWidget.setGeometry(QtCore.QRect(530, 230, 256, 51))
        self.Threshold_tableWidget.setObjectName("Threshold_tableWidget")
        self.Threshold_tableWidget.setColumnCount(3)
        self.Threshold_tableWidget.setRowCount(1)
        self.White_checkBox = QtWidgets.QCheckBox(Threshold_Dialog)
        self.White_checkBox.setGeometry(QtCore.QRect(560, 200, 92, 23))
        self.White_checkBox.setObjectName("White_checkBox")
        self.Black_checkBox = QtWidgets.QCheckBox(Threshold_Dialog)
        self.Black_checkBox.setGeometry(QtCore.QRect(680, 200, 92, 23))
        self.Black_checkBox.setObjectName("Black_checkBox")
        self.scrollArea = QtWidgets.QScrollArea(Threshold_Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 10, 521, 481))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 519, 479))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
       # self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.img_thresold_label = Threshold_MyLabel()

        self.scrollArea.setBackgroundRole(QPalette.Dark)#THEM DONG
        self.img_thresold_label.setWordWrap(True)
        self.img_thresold_label.setObjectName("label")
        self.scrollArea.setWidget(self.img_thresold_label)
        self.Threshold_Bar.setMaximum(255)
        self.Threshold_Bar.setMinimum(0)


        if self.dk_function_pixel == 0 :
             self.Black_checkBox.toggled.connect(self.Black_show)
             self.White_checkBox.toggled.connect(self.White_show)
             self.timer = QTimer()
             self.timer.timeout.connect(self.Threshold_viewCam)
             self.Threshold_run_pushButton.clicked.connect(self.Threshold_controlTimer)
             self.Threshold_OK_pushButton.clicked.connect(self.Threshold_open_img)
             self.Threashold_xuly_pushButton.clicked.connect(self.Threshold_xuly)
             self.Threshold_comboBox.currentIndexChanged.connect(self.Detection_color_selectionchange)
             self.Threshold_Bar.sliderMoved.connect(self.Threshold_bar)
             self.White_checkBox.setChecked(1)
             self.Threshold_Bar.setEnabled(0)
        if self.dk_function_pixel != 0 :
             self.read_data()
             self.Black_checkBox.toggled.connect(self.Black_show)
             self.White_checkBox.toggled.connect(self.White_show)
             self.timer = QTimer()
         #    self.timer.timeout.connect(self.Threshold_viewCam)
          #   self.Threshold_run_pushButton.clicked.connect(self.Threshold_controlTimer)
             self.Threshold_OK_pushButton.clicked.connect(self.Threshold_open_img)
             self.Threashold_xuly_pushButton.clicked.connect(self.Threshold_xuly)
             self.Threshold_comboBox.currentIndexChanged.connect(self.Detection_color_selectionchange)
             self.Threshold_Bar.sliderMoved.connect(self.Threshold_bar)
             self.White_checkBox.setChecked(1)
             self.Threshold_OK_pushButton.setEnabled(0)
             self.Threashold_xuly_pushButton.setEnabled(0)
             self.Threshold_Bar.setEnabled(0)
             self.Threshold_comboBox.setEnabled(0)


        self.retranslateUi(Threshold_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Threshold_Dialog)

    def retranslateUi(self, Threshold_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Threshold_Dialog.setWindowTitle(_translate("Threshold_Dialog", "Dialog"))
        self.Threshold_OK_pushButton.setText(_translate("Threshold_Dialog", "OK"))
        self.Threashold_xuly_pushButton.setText(_translate("Threshold_Dialog", "Xuly"))
        self.Threshold_run_pushButton.setText(_translate("Threshold_Dialog", "RUN"))
        self.Threshold_comboBox.setItemText(0, _translate("Threshold_Dialog", "01"))
        self.Threshold_comboBox.setItemText(1, _translate("Threshold_Dialog", "02"))
        self.Threshold_comboBox.setItemText(2, _translate("Threshold_Dialog", "03"))
        self.Threshold_comboBox.setItemText(3, _translate("Threshold_Dialog", "04"))
        self.White_checkBox.setText(_translate("Threshold_Dialog", "White"))
        self.Black_checkBox.setText(_translate("Threshold_Dialog", "Black"))


    def Threshold_open_img(self):
        file_goc=os.getcwd()
        self.ten=self.Threshold_comboBox.currentText()
        file_config=file_goc.replace("/dection_pixel","")
        file_img=file_config+"/"+self.ten+".jpg"
     #   print(file_img)
        self.img=cv2.imread(file_img,0)
        self.img_1=cv2.imread(file_img,0)
       # self.img=cv2.resize(self.img,(521, 481))
        #self.img_1=cv2.resize(self.img_1,(521, 481))
        height, width  = self.img.shape
        step =  width
        qImg = QImage(self.img.data, width, height, step, QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(qImg)
        self.img_thresold_label.setPixmap(QPixmap.fromImage(qImg))
        self.img_thresold_label.setCursor(QtCore.Qt.CrossCursor)
        self.img_thresold_label.setfdk(1)
        self.Threshold_OK_pushButton.setEnabled(0)
        self.Threshold_Bar.setEnabled(1)
        self.Threshold_comboBox.setEnabled(0)
        if self.img_thresold_label.get_flag()!=0:
             self.img_thresold_label.setfdk(2)
        #print(self.img_thresold_label.get_flag())
             


    def Threshold_xuly(self):
        file_goc=os.getcwd()
        self.ten=self.Threshold_comboBox.currentText()
        file_config=file_goc.replace("/dection_pixel","")
        file_img=file_config+"/"+self.ten+".jpg"
       # print(file_img)
        self.img_luu=cv2.imread(file_img,0)
        self.Threshold_bar()
        file_goc=os.getcwd()
        if file_goc.find("dection_pixel",20)==-1:
             self.file_img_bandau=file_goc+"/image_function"
             self.file_img=os.getcwd()+"/cut_image_function"
             self.file_img_cut=os.getcwd()+"/cut_image"
        else:
             self.file_img_bandau=file_goc.replace("dection_pixel","image_function")
             self.file_img=file_goc.replace("dection_pixel","cut_image_function")
             self.file_img_cut=file_goc.replace("dection_pixel","cut_image")
        self.file_img_bandau=self.file_img_bandau.rstrip()
        self.file_img=self.file_img.rstrip()
        self.file_img_cut=self.file_img_cut.rstrip()


        
        #print(self.file_img_bandau)
        Count_img=len(os.listdir(self.file_img))
        print(self.file_img)
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
        self.file_img_cut=self.file_img_cut+"/"+self.ten+"cut"+".jpg"
        print ( self.file_img_cut)

        cv2.imwrite(self.file_img_bandau,self.img)
        imgcat=self.img[self.y00:self.y10,self.x00:self.x10]
        imgcut=self.img_luu[self.y00:self.y10,self.x00:self.x10]
        cv2.imwrite(self.file_img,imgcat)
        cv2.imwrite(self.file_img_cut,imgcut)
        print(self.file_img_bandau)
        print(self.file_img)
        file_goc=os.getcwd()
        file_config=file_goc.replace("/dection_pixel","")+"/config"
        List_file=os.listdir(file_config)
        #print(len(List_file))
        filedata=file_config+"/"+self.ten+".txt"
        
        detection_pixel_file = open(filedata, 'w')
        detection_pixel_file.write( self.file_img+"\n")
        detection_pixel_file.write(self.file_img_bandau+"\n")
        detection_pixel_file.write("detection_pixel\n")
        detection_pixel_file.write(str(self.x00)+"\n")
        detection_pixel_file.write(str(self.x10)+"\n")
        detection_pixel_file.write(str(self.y00)+"\n")
        detection_pixel_file.write(str(self.y10)+"\n")
        detection_pixel_file.write(str(self.thresh_value)+"\n")
        detection_pixel_file.write(str(self.White_checkBox.isChecked())+"\n")



        
        self.Threashold_xuly_pushButton.setEnabled(0)
        self.Threshold_Bar.setEnabled(0)

    def Detection_color_selectionchange(self):
        self.Threashold_xuly_pushButton.setEnabled(1)         
        self.Threshold_OK_pushButton.setEnabled(1)
        self.Threshold_Bar.setEnabled(1)

    def Threshold_bar(self):
        if  self.img_thresold_label.x0 and self.img_thresold_label.x1 and self.img_thresold_label.y0 and self.img_thresold_label.y1 :
            self.x00=self.img_thresold_label.x0
            self.x10=self.img_thresold_label.x1
            self.y00=self.img_thresold_label.y0
            self.y10=self.img_thresold_label.y1

            self.dk=1;
            self.threshold_img=Threshold_xulyanh(self.img,self.img_1,self.x00,self.y00,self.x10,self.y10)
            self.thresh_value=self.Threshold_Bar.value()
            if self.White_checkBox.isChecked() == True:
                 self.threshold_img.Threshold_xuly(self.thresh_value,1)
                 img_2=self.threshold_img.Threshold_getdata()
            if self.Black_checkBox.isChecked() == True:
                 self.threshold_img.Threshold_xuly(self.thresh_value,2)
                 img_2=self.threshold_img.Threshold_getdata()                 
            height, width  =self.img.shape
            step = width
            qImg = QImage(self.img.data, width, height, step, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qImg)
            self.img_thresold_label.setPixmap(QPixmap.fromImage(qImg))
            self.img_thresold_label.setfdk(0)

            self.Threshold_tableWidget.setItem(0,1, QTableWidgetItem(str(self.threshold_img.Threshold_count_den())))

   
    def Threshold_controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            # start timer
            self.timer.start(20)
            self.Threshold_run_pushButton.setText("Stop")
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            camera.StopGrabbing()
            # update control_bt text
            self.Threshold_run_pushButton.setText("RUN")
            self.Threshold_comboBox.setEnabled(1)

    def Threshold_viewCam(self):
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
            #print(self.img.shape)

               self.image_1  = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY )
             #  self.image_1=cv2.resize(image_1,(521, 481))
            
               self.image_2 = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY )
              # self.image_2=cv2.resize(image_2,(521, 481))
               self.threshold_img_1=Threshold_xulyanh(self.image_1,self.image_2,self.x00,self.y00,self.x10,self.y10)
               #Threshold_xulyanh.template_matching(self,img_cut,img)
               
               cv2.rectangle(self.image_1,(self.x00,self.y00),(self.x10,self.y10),3)                
               
               thresh_value_1=self.Threshold_Bar.value()
               self.dk=0;
               
               if self.White_checkBox.isChecked() == True:
                    self.threshold_img_1.Threshold_xuly(thresh_value_1,1)      
                    img_c=self.threshold_img_1.Threshold_getdata()
                    self.Threshold_tableWidget.setItem(0,1, QTableWidgetItem(str(self.threshold_img_1.Threshold_count_den())))
               if self.Black_checkBox.isChecked() == True:
                    self.threshold_img_1.Threshold_xuly(thresh_value_1,2)      
                    img_c=self.threshold_img_1.Threshold_getdata()
                    self.Threshold_tableWidget.setItem(0,1, QTableWidgetItem(str(self.threshold_img_1.Threshold_count_den())))  
               height, width = self.image_1.shape
               step =  width
               qImg = QImage(self.image_1.data, width, height, step,  QImage.Format_Grayscale8)
               self.img_thresold_label.setPixmap(QPixmap.fromImage(qImg))
    def White_show(self):
         if self.White_checkBox.isChecked() == True:
            if self.dk:
                 self.threshold_img.Threshold_xuly(self.thresh_value,1)
                 img_2=self.threshold_img.Threshold_getdata()
                 
                 height, width  =self.img.shape
                 step = width
                 qImg = QImage(self.img.data, width, height, step, QImage.Format_Grayscale8)
                 pixmap = QPixmap.fromImage(qImg)
                 self.img_thresold_label.setPixmap(QPixmap.fromImage(qImg))
                 self.Threshold_tableWidget.setItem(0,1, QTableWidgetItem(str(self.threshold_img.Threshold_count_den())))
            self.Black_checkBox.setChecked(0)
            self.White_checkBox.setEnabled(0)
            self.Black_checkBox.setEnabled(1)
        

    def Black_show(self):

        if self.Black_checkBox.isChecked() == True:
           if self.dk:
              self.threshold_img.Threshold_xuly(self.thresh_value,2)
              img_2=self.threshold_img.Threshold_getdata()
             
              height, width  =self.img.shape
              step = width
              qImg = QImage(self.img.data, width, height, step, QImage.Format_Grayscale8)
              pixmap = QPixmap.fromImage(qImg)
              self.img_thresold_label.setPixmap(QPixmap.fromImage(qImg))
              self.Threshold_tableWidget.setItem(0,1, QTableWidgetItem(str(self.threshold_img.Threshold_count_den())))                
           self.White_checkBox.setChecked(0)
           self.White_checkBox.setEnabled(1)
           self.Black_checkBox.setEnabled(0)

    def read_data(self):
         f=open(self.link_file)
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
         self.Threshold_Bar.setValue(self.value_bar)
         print(f_anh_sasds)
         img_hienthi=cv2.imread(f_anh_sasds,1)
         img_hienthi=cv2.resize(img_hienthi,(521, 481))
         height, width = img_hienthi.shape
         step =width
         qImg = QImage(img_hienthi.data, width, height, step, QImage.Format_Grayscale8)
         pixmap = QPixmap.fromImage(qImg)
         self.img_thresold_label.setPixmap(QPixmap.fromImage(qImg))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Threshold_Dialog = QtWidgets.QDialog()
    ui = Ui_Threshold_Dialog(0,'/home/tranthang/Desktop/camera_1/config/1.txt')
    ui.setupUi(Threshold_Dialog)
    Threshold_Dialog.show()
    sys.exit(app.exec_())

