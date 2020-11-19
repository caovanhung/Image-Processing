from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtGui import QIcon

from detect_color_xulyanh import*
from template_matching import*
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
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())




class Detection_color_MyLabel(QLabel):

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

class Ui_detecton_clor_Dialog(object):


    dk_function_color=0
    link_file='/home/tranthang/Desktop/camera_1/config/1.txt'
    def set_dk_function_color(self,dk,link_file):
         self.dk_function_color=dk
         self.link_file=link_file
    def set_linkfile(self,file):
         self.link_file=file
    def __init__(self,dk,link_file):
        self.dk_function_color=dk
        self.link_file=link_file
    
    def setupUi(self, detecton_clor_Dialog):
        detecton_clor_Dialog.setObjectName("detecton_clor_Dialog")
        detecton_clor_Dialog.resize(886, 581)
        detecton_clor_Dialog.setBaseSize(QtCore.QSize(3, 3))
        self.pushButton = QtWidgets.QPushButton(detecton_clor_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 510, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(detecton_clor_Dialog)
        self.comboBox.setGeometry(QtCore.QRect(170, 510, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox = QtWidgets.QCheckBox(detecton_clor_Dialog)
        self.checkBox.setGeometry(QtCore.QRect(630, 170, 92, 23))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(detecton_clor_Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(750, 170, 92, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.tableWidget = QtWidgets.QTableWidget(detecton_clor_Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(610, 230, 256, 192))
        self.tableWidget.setBaseSize(QtCore.QSize(3, 3))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)
        self.xulyanh_pushButton = QtWidgets.QPushButton(detecton_clor_Dialog)
        self.xulyanh_pushButton.setGeometry(QtCore.QRect(320, 510, 89, 25))
        self.xulyanh_pushButton.setObjectName("xulyanh_pushButton")
        self.detect_color_run_pushButton = QtWidgets.QPushButton(detecton_clor_Dialog)
        self.detect_color_run_pushButton.setGeometry(QtCore.QRect(510, 510, 89, 25))
        self.detect_color_run_pushButton.setObjectName("detect_color_run_pushButton")
        self.scrollArea = QtWidgets.QScrollArea(detecton_clor_Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 591, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 589, 489))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")


       # self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.img_label=Detection_color_MyLabel(self.scrollAreaWidgetContents)
        self.scrollArea.setBackgroundRole(QPalette.Dark)#THEM DONG
        self.img_label.setWordWrap(True)
        self.img_label.setObjectName("label")
        self.scrollArea.setWidget(self.img_label)# 


        self.xulyanh_pushButton = QtWidgets.QPushButton(detecton_clor_Dialog)
        self.xulyanh_pushButton.setGeometry(QtCore.QRect(320, 510, 89, 25))
        self.xulyanh_pushButton.setObjectName("xulyanh_pushButton")

        self.detect_color_run_pushButton = QtWidgets.QPushButton(detecton_clor_Dialog)
        self.detect_color_run_pushButton.setGeometry(QtCore.QRect(510, 510, 89, 25))
        self.detect_color_run_pushButton.setObjectName("detect_color_run_pushButton")
        self.checkBox.setChecked(1)
        self.checkBox.setEnabled(0)


        
        if self.dk_function_color == 0 :
       

             self.timer = QTimer()
             self.timer.timeout.connect(self.Detection_color_viewCam)   
             self.comboBox.currentIndexChanged.connect(self.Detection_color_selectionchange)

             self.tableWidget.setVerticalHeaderLabels(['Min', 'Measure', 'Max'])
             self.pushButton.clicked.connect(self.Detection_color_open_img)
             self.checkBox.toggled.connect(self.GRB_show)
             self.checkBox_2.toggled.connect(self.HSV_show)

       
             self.xulyanh_pushButton.clicked.connect(self.Detection_color_xyly_GRB)
             self.retranslateUi(detecton_clor_Dialog)
             QtCore.QMetaObject.connectSlotsByName(detecton_clor_Dialog)
             self.detect_color_run_pushButton.clicked.connect(self.Detection_color_controlTimer)
             self.detect_color_run_pushButton.setEnabled(0)
             self.xulyanh_pushButton.setEnabled(0)
        if self.dk_function_color != 0 :
             self.read_data()    
             self.timer = QTimer()
             self.timer.timeout.connect(self.Detection_color_viewCam)   
             self.comboBox.currentIndexChanged.connect(self.Detection_color_selectionchange)

             self.tableWidget.setVerticalHeaderLabels(['Min', 'Measure', 'Max'])
             self.pushButton.clicked.connect(self.Detection_color_open_img)
             self.checkBox.toggled.connect(self.GRB_show)
             self.checkBox_2.toggled.connect(self.HSV_show)

       
             self.xulyanh_pushButton.clicked.connect(self.Detection_color_xyly_GRB)
             self.retranslateUi(detecton_clor_Dialog)
             QtCore.QMetaObject.connectSlotsByName(detecton_clor_Dialog)
             self.detect_color_run_pushButton.clicked.connect(self.Detection_color_controlTimer)
             self.detect_color_run_pushButton.setEnabled(1)
             self.xulyanh_pushButton.setEnabled(0)
             self.pushButton.setEnabled(0)
             self.comboBox.setEnabled(0)

        self.retranslateUi(detecton_clor_Dialog)
        QtCore.QMetaObject.connectSlotsByName(detecton_clor_Dialog)







    def retranslateUi(self, detecton_clor_Dialog):
        _translate = QtCore.QCoreApplication.translate
        detecton_clor_Dialog.setWindowTitle(_translate("detecton_clor_Dialog", "Dialog"))
        self.pushButton.setText(_translate("detecton_clor_Dialog", "OK"))
        self.comboBox.setItemText(0, _translate("detecton_clor_Dialog", "01"))
        self.comboBox.setItemText(1, _translate("detecton_clor_Dialog", "02"))
        self.comboBox.setItemText(2, _translate("detecton_clor_Dialog", "03"))
        self.comboBox.setItemText(3, _translate("detecton_clor_Dialog", "04"))
        self.comboBox.setItemText(4, _translate("detecton_clor_Dialog", "05"))
        self.comboBox.setItemText(5, _translate("detecton_clor_Dialog", "06"))
        self.comboBox.setItemText(6, _translate("detecton_clor_Dialog", "07"))
        self.comboBox.setItemText(7, _translate("detecton_clor_Dialog", "08"))     
        self.checkBox.setText(_translate("detecton_clor_Dialog", "GRB"))
        self.checkBox_2.setText(_translate("detecton_clor_Dialog", "HSV"))
        self.xulyanh_pushButton.setText(_translate("detecton_clor_Dialog", "Xuly"))
        self.detect_color_run_pushButton.setText(_translate("detecton_clor_Dialog", "RUN"))


    def Detection_color_open_img(self):
        
        self.ten=self.comboBox.currentText()
        file_goc=os.getcwd()
        file_config=file_goc.replace("/detection_color_1"," ")
        file_config=file_config.rstrip()
        print (file_config)
        file_img=file_config+"/"+self.ten+".jpg"
        print(file_img)
        self.img=cv2.imread(file_img,1)
       # self.img=cv2.resize(self.img,(581, 491))
        height, width, channel = self.img.shape
        step = channel * width
        qImg = QImage(self.img.data, width, height, step, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.img_label.setPixmap(QPixmap.fromImage(qImg))
        self.img_label.setCursor(QtCore.Qt.CrossCursor)
        self.img_label.setfdk(1)
        self.pushButton.setEnabled(0)
        
        self.detect_color_run_pushButton.setEnabled(0)
        self.xulyanh_pushButton.setEnabled(1)

    def Detection_color_selectionchange(self):
        self.pushButton.setEnabled(1)         
        self.xulyanh_pushButton.setEnabled(1)
        self.detect_color_run_pushButton.setEnabled(0)
        self.xulyanh_pushButton.setEnabled(0)        


        
    def Detection_color_xyly_GRB(self):
      
        self.x00=self.img_label.x0
        self.x10=self.img_label.x1
        self.y00=self.img_label.y0
        self.y10=self.img_label.y1
        
        
        image=self.img
       
        #list_file=os.listdir(os.getcwd()+'/'+"detection_color_image/")





        file_goc=os.getcwd()
        if file_goc.find("detection_color_1",20)==-1:
             self.file_img_bandau=file_goc+"/image_function"
             self.file_img=os.getcwd()+"/cut_image_function"
             self.file_img_cut=os.getcwd()+"/cut_image"
             
        else:
             self.file_img_bandau=file_goc.replace("detection_color_1","image_function")
             self.file_img=file_goc.replace("detection_color_1","cut_image_function")
             self.file_img_cut=file_goc.replace("detection_color_1","cut_image")
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
        self.file_img_cut=self.file_img_cut+"/"+self.ten+"cut"+".jpg"


    #    print(self.file_img_bandau)
    #    print(self.file_img)

        self.img_1=self.img[self.img_label.y0:self.img_label.y1,self.img_label.x0:self.img_label.x1]
        cv2.imwrite(self.file_img_cut,self.img_1)
        cv2.rectangle(image,(self.x00,self.y00),(self.x10,self.y10),(0,255,0),3)
        cv2.imwrite(self.file_img_bandau,image)
        self.xuly_img=xulyanh(self.img)
        
       # print(self.file_img)
       # print(self.file_img_bandau)
        cv2.imwrite(self.file_img,self.xuly_img.getdata()[self.img_label.y0:self.img_label.y1,self.img_label.x0:self.img_label.x1])
        self.GRB_trungbinh=self.xuly_img.GRB()
        self.HSV_trungbinh=self.xuly_img.HSV()
        file_goc=os.getcwd()
        file_config=file_goc.replace("/detection_color_1","/")+"/config"
        List_file=os.listdir(file_config)
        #print(len(List_file))
        filedata=file_config+"/"+self.ten+".txt"
        
        detection_color_file = open(filedata, 'w')
        detection_color_file.write( self.file_img+"\n")
        detection_color_file.write(self.file_img_bandau+"\n")

        detection_color_file.write("detection_color\n")
        
        detection_color_file.write(str(self.x00)+"\n")
        detection_color_file.write(str(self.x10)+"\n")
        detection_color_file.write(str(self.y00)+"\n")
        detection_color_file.write(str(self.y10)+"\n")
        detection_color_file.write(str(self.checkBox.isChecked())+"\n")
        self.xulyanh_pushButton.setEnabled(0)
        self.img_label.setfdk(0)
        self.pushButton.setEnabled(0)
        self.detect_color_run_pushButton.setEnabled(1)
        self.comboBox.setEnabled(0)
        

        
 
    def GRB_show(self):
        self.x00=self.img_label.x0
        self.x10=self.img_label.x1
        self.y00=self.img_label.y0
        self.y10=self.img_label.y1
        
      #  image=self.img
        cv2.rectangle(self.img,(self.x00,self.y00),(self.x10,self.y10),(0,255,0),3)
        self.img_1=self.img[self.img_label.y0:self.img_label.y1,self.img_label.x0:self.img_label.x1]
        self.xuly_img=xulyanh(self.img_1)
        
        self.GRB_trungbinh=self.xuly_img.GRB()
        self.HSV_trungbinh=self.xuly_img.HSV()

        if self.checkBox.isChecked() == True:      
            self.tableWidget.setHorizontalHeaderLabels(['R', 'G', 'B'])
            for i in range(0,3):
                self.tableWidget.setItem(1,i, QTableWidgetItem(str(self.GRB_trungbinh[i])))
            self.checkBox_2.setChecked(0)
            self.checkBox.setEnabled(0)
            self.checkBox_2.setEnabled(1)
        

    def HSV_show(self):
        self.x00=self.img_label.x0
        self.x10=self.img_label.x1
        self.y00=self.img_label.y0
        self.y10=self.img_label.y1
        
      #  image=self.img
        cv2.rectangle(self.img,(self.x00,self.y00),(self.x10,self.y10),(0,255,0),3)
        self.img_1=self.img[self.img_label.y0:self.img_label.y1,self.img_label.x0:self.img_label.x1]
        self.xuly_img=xulyanh(self.img_1)
        
        self.GRB_trungbinh=self.xuly_img.GRB()
        self.HSV_trungbinh=self.xuly_img.HSV()

        if self.checkBox_2.isChecked() == True:         
            self.tableWidget.setHorizontalHeaderLabels(['H', 'S', 'V'])
            for i in range(0,3):
                self.tableWidget.setItem(1,i, QTableWidgetItem(str(self.HSV_trungbinh[i])))
            self.checkBox.setChecked(0)
            self.checkBox.setEnabled(1)
            self.checkBox_2.setEnabled(0)
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
         print(f_anh_sasds)
         img_hienthi=cv2.imread(f_anh_sasds,1)
         #img_hienthi=cv2.resize(img_hienthi,(581, 491))
         height, width, channel = img_hienthi.shape
         step = channel * width
         qImg = QImage(img_hienthi.data, width, height, step, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(qImg)
         self.img_label.setPixmap(QPixmap.fromImage(qImg))
         #self.img_label.setPixmap(QPixmap.fromImage(qImg))


    # start/stop timer
    def Detection_color_controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.detect_color_run_pushButton.setText("Stop")
            self.comboBox.setEnabled(0)
            #self.img_label.setfdk(0)
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            camera.StopGrabbing()
            # update control_bt text
            self.detect_color_run_pushButton.setText("RUN")
            self.comboBox.setEnabled(1)
        
    def Detection_color_viewCam(self):
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
               image = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
               image_1 = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
               image_3 = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            #   image=cv2.resize(image,(581, 491))
               height, width, channel = image.shape
               step = channel * width
            #   cv2.rectangle(image,(self.x00,self.y00),(self.x10,self.y10),(0,255,0),3)
               print(self.file_img_cut)
               img_cut=cv2.imread(self.file_img_cut,1)
        
               #img_1=image[self.x00:self.x10,self.y00:self.y10]
              # self.img_2=xulyanh(img_1,image);
               top,button,image_2=template_matching(img_cut,image)

               self.img_1=image_3[top[0]:button[0],top[0]:button[1]]
               self.xuly_img=xulyanh(self.img_1)
        
               self.GRB_trungbinh=self.xuly_img.GRB()
               self.HSV_trungbinh=self.xuly_img.HSV()



               
               cv2.rectangle(image_1,top, button, (0,255,0), 2)
             #  print(img_00)
               #print(pt)
              # img2 = cv.polylines(image_1,[pt],True,(255,0,0),3, cv.LINE_AA)
               if self.checkBox_2.isChecked() == True:         
                 self.tableWidget.setHorizontalHeaderLabels(['H', 'S', 'V'])
                 for i in range(0,3):
                     self.tableWidget.setItem(1,i, QTableWidgetItem(str(self.HSV_trungbinh[i])))
                 self.checkBox.setChecked(0)
                 self.checkBox.setEnabled(1)
                 self.checkBox_2.setEnabled(0)

               if self.checkBox.isChecked() == True:      
                 self.tableWidget.setHorizontalHeaderLabels(['R', 'G', 'B'])
                 for i in range(0,3):
                     self.tableWidget.setItem(1,i, QTableWidgetItem(str(self.GRB_trungbinh[i])))
                 self.checkBox_2.setChecked(0)
                 self.checkBox.setEnabled(0)
                 self.checkBox_2.setEnabled(1)

               height, width,channel =image_1.shape
               step =  width*channel
              # self.HSV_trungbinh=self.img_2.HSV()
               #self.GRB_trungbinh=self.img_2.GRB()
               #if self.checkBox.isChecked() == True:   
               #   self.GRB_show()
               #if self.checkBox_2.isChecked() == True:
               #   self.HSV_show()
        
               qImg = QImage(image_1.data, width, height, step, QImage.Format_RGB888)
               self.img_label.setPixmap(QPixmap.fromImage(qImg))
               #print(self.img_label.getdk())
               
              # height, width  =img_00.shape
              # step = width
              # qImg = QImage(img_00.data, width, height, step, QImage.Format_Grayscale8)
              # pixmap = QPixmap.fromImage(qImg)
              # self.img_label.setPixmap(QPixmap.fromImage(qImg))

            







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    detecton_clor_Dialog = QtWidgets.QDialog()
    ui = Ui_detecton_clor_Dialog(0,'/home/tranthang/Desktop/camera_1/config/1.txt')
    ui.setupUi(detecton_clor_Dialog)
    detecton_clor_Dialog.show()
    sys.exit(app.exec_())

