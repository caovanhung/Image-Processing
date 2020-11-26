import sys
import os
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from pypylon import pylon
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication

import cv2

from main_window_ui import *
from register_image import *


# conecting to the first available camera
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

def open_register_ui(self):
    self.Dialog = QtWidgets.QDialog()
    self.ui_1 = Ui_register_Dialog()
    self.ui_1.setupUi(self.Dialog)
    self.Dialog.show()
def open_function_ui(self):
    self.function_Dialog= QtWidgets.QDialog()
    self.ui_function=Ui_function_Dialog()
    self.ui_function.setupUi(self.function_Dialog)
    self.function_Dialog.show()

def open_detection_color(self,dk,file_txt):
    self.detction_color_Dialog=QtWidgets.QDialog()
    self.ui_detction_color=Ui_detecton_clor_Dialog(dk,file_txt)
   # self.ui_detction_color.set_dk_function_color(dk)
   # self.ui_detction_color.set_linkfile(file)
    self.ui_detction_color.setupUi(self.detction_color_Dialog)
    self.detction_color_Dialog.show()

def open_detection_pixel(self,dk,file_txt):
    self.detction_pixel_Dialog=QtWidgets.QDialog()
    self.ui_detction_pixel=Ui_Threshold_Dialog(dk,file_txt)

    self.ui_detction_pixel.setupUi(self.detction_pixel_Dialog)
    self.detction_pixel_Dialog.show()
def open_detection_OCR(self,dk,file_txt):
    self.detction_OCR_Dialog=QtWidgets.QDialog()
    self.ui_detction_OCR=Ui_Dialog_OCR(dk,file_txt)

    self.ui_detction_OCR.setupUi(self.detction_OCR_Dialog)
    self.detction_OCR_Dialog.show()
def open_detection_edges(self):
    self.detction_edges_Dialog=QtWidgets.QDialog()
    self.ui_detction_edges=Ui_Threshold_Dialog()

    self.ui_detction_edges.setupUi(self.detction_edges_Dialog)
    self.detction_edges_Dialog.show()

class MainWindow(QWidget):
    # class constructor
    #dodai_button_hientai=0
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        print("goi chuong trinh")
        self.ui =  Ui_Form_camera()
        self.ui.setupUi(self)
        self.dodai_button_hientai=0
        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.OpenCamera_pushButton.clicked.connect(self.controlTimer)
        self.ui.Register_pushButton.clicked.connect(self.open_register)
        self.ui.fuction_pushButton.clicked.connect(self.open_function)
        self.ui.Update_function_pushButton.clicked.connect(self.open_function_file)
        #self.ui.button.clicked.conncet(self.showText1)
        self.dodai_button_hientai=0
        self.dodai_button=0
        self.open_function_file()
        print(self.get_buton())
        

       # view camera
    def viewCam(self):
        converter = pylon.ImageFormatConverter()
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

            # create video capture
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
        # Access the image data
            image = converter.Convert(grabResult)
            self.img = image.GetArray()
            image = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            
           # image=cv2.resize(image,(1117, 710))
        # get image infos
            height, width, channel = image.shape
            step = channel * width
        # create QImage from image
            qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
           # pixmapQPixmap.fromImage(qImg)
        # show image in img_label
           # pixmap_resized = pixmap.scaled(720, 405, QtCore.Qt.KeepAspectRatio)
            self.ui.img_label.setPixmap(QPixmap.fromImage(qImg))
            #self.ui.img_label.setScaledContents(True)

        # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():

            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.OpenCamera_pushButton.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            camera.StopGrabbing()
            # update control_bt text
            self.ui.OpenCamera_pushButton.setText("Start")
    def open_register(self):
        self.timer.stop()
        camera.StopGrabbing()
        self.ui.OpenCamera_pushButton.setText("Start")
        open_register_ui(self)
    def open_function(self):
        open_function_ui(self)
    def open_function_detection_color_1(self):
        #print(len(self.ui.button))
        sending_button = self.sender() #lay  id cua button
       # print(sending_button)
        ten=sending_button.objectName()# lay ten cua button
        #  print(ten)
        file_goc =os.getcwd() #lay file goc
        file_txt_can=file_goc+'/config/'+ten+'.txt'# ten file txt du lieu
        open_detection_color(self,1,file_txt_can)  
    def get_buton(self):
        return self.ui
        
    def open_function_file(self):
        file_goc =os.getcwd() 
        file_config=file_goc+'/config'
        self.list_file=os.listdir(file_config)
        self.kiemtra=0
        #self.dodai_button_hientai=10
        #xoa cac button dang co hien tai
        #print("Do dai hien tai")
        #print (self.dodai_button_hientai)
        for  x in range (self.dodai_button_hientai):
        
            self.ui.button[x].setParent(None)
            self.ui.horizontalLayout.removeWidget(self.ui.button[x])
        
        
        self.ui.button=[]
        #self.ui.button.remove(0)
        self.sofile_=len(self.list_file)
        self.dodai_button=len(self.list_file)
 

        self.list_file=sorted(self.list_file)
        for i in range(len(self.list_file)):
            self.file_txt=file_config+'/'+self.list_file[i]
           # print(self.file_txt)
            f=open (self.file_txt)
            f_anh=f.readline()
            f_anh=f_anh.rstrip()
            self.kiemtra=i
            self.ui.button.append(i)
            self.dk_button=1
            self.ui.button[i]=mouse_envent(self.ui.scrollAreaWidgetContents_2)
            #self.ui.button[i].mousePressEvent(self)
            self.list_file[i]=self.list_file[i].replace(".txt","")
            self.ui.button[i].setObjectName(self.list_file[i])
            self.ui.button[i].setIcon(QtGui.QIcon(f_anh))       
            self.ui.button[i].setText(self.list_file[i])
            self.ui.button[i].clicked.connect(self.open_function_detection_color_1)
            self.ui.button[i].setIconSize(QtCore.QSize(100,100))
            self.ui.horizontalLayout.addWidget(self.ui.button[i])
            #print(button[i].x())
        self.dodai_button_hientai=self.dodai_button#lay so nut cu



                  

    def open_function_detection_color(self):
        #print(len(self.ui.button))
         sending_button = self.sender() #lay  id cua button
         ten=sending_button.objectName()# lay ten cua button
        # print(ten)
         file_goc =os.getcwd() #lay file goc
         file_txt_can=file_goc+'/config/'+ten+'.txt'# ten file txt du lieu
         open_detection_color(self,1,file_txt_can)     

class mouse_envent(QtWidgets.QPushButton):
    def mousePressEvent(self,QMouseEvent):
        if QMouseEvent.buttons() == Qt.LeftButton:
           ten=self.objectName()
           #print(ten)
           file_goc =os.getcwd() 
           file_config=file_goc+'/config'
           self.list_file=os.listdir(file_config)
           
           file_goc =os.getcwd() #lay file goc
           self.file_txt_can=file_goc+'/config/'+ten+'.txt'# ten file txt du lieu
           f=open(self.file_txt_can,'r')
           file_anh=f.readline()
           file_anh_cat=f.readline()
           file_function=f.readline()
           file_function=file_function.rstrip()
           print(file_function)

           if file_function=="detection_color":
               open_detection_color(self,1,self.file_txt_can)
           if file_function=="detection_pixel":
               open_detection_pixel(self,1,self.file_txt_can)
           if file_function=="detection_OCR":
               open_detection_OCR(self,1,self.file_txt_can)
               
            
        if QMouseEvent.buttons() == Qt.RightButton:

           ten=self.objectName()
          # print(ten)
           print(self.sender())
           file_goc =os.getcwd() 
           file_config=file_goc+'/config'
           self.list_file=os.listdir(file_config)

           file_goc =os.getcwd() #lay file goc
           file_txt_can=file_goc+'/config/'+ten+'.txt'# ten file txt du lieu
           open_detection_color(self,1,file_txt_can)
           msg = QtWidgets.QMessageBox()
           self.buttonReply = msg.question(self, 'Function Message', "Do you like delete function", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
           
           if self.buttonReply == QMessageBox.Yes:
                      ten=self.objectName()
                      file_goc =os.getcwd() #lay file goc
              #lay cac file trong config ,image_function,cut_image_funcion
                      file_txt_can=file_goc+'/config/'+ten+'.txt'# ten file txt du lieu
                      file_image=file_goc+'/image_function/'+ten+'dau.jpg'
                      flie_image_cut=file_goc+'/cut_image_function/'+ten+'cat.jpg'       
                      ten=int(ten)
            ## lay list file
                      file_cofig=os.listdir(file_goc+'/config')#list file /config
                      file_image_list=os.listdir(file_goc+'/image_function')
                      file_image_cut_list=os.listdir(file_goc+'/cut_image_function')
            #sap xep list file
                      file_cofig=sorted(file_cofig,reverse=True)
                      file_image_list=sorted(file_image_list,reverse=True)
                      file_image_cut_list=sorted(file_image_cut_list,reverse=True)
        
                      leng_file=len(os.listdir(file_goc+'/config'))
                      self.dodai= leng_file
            
                      file_cofig = file_cofig[::-1]
                      file_image_list = file_image_list[::-1]
                      file_image_cut_list = file_image_cut_list[::-1]
            #xoa cac fle
                      os.remove(file_txt_can)
                      os.remove(file_image)
                      os.remove(flie_image_cut)



                      for i in range(ten,leng_file):
                    #xep ca file trong config
                        file_1=file_goc+'/config'+'/'+file_cofig[i]
                        file_2=file_goc+'/config'+'/'+file_cofig[i-1]
                        os.rename( file_1,file_2 )
                    #xep cac file trong file_img_list
                        file_img_1=file_goc+'/image_function'+'/'+file_image_list[i]
                        file_img_2=file_goc+'/image_function'+'/'+file_image_list[i-1]
                        os.rename( file_img_1,file_img_2 )
                    #xep cac file trong file_img_cat
                        file_img_cut_1=file_goc+'/cut_image_function'+'/'+file_image_cut_list[i]
                        file_img_cut_2=file_goc+'/cut_image_function'+'/'+file_image_cut_list[i-1]
                        os.rename( file_img_cut_1,file_img_cut_2 )

                      list_ten=os.listdir(file_goc+'/config')
                      list_ten=sorted(list_ten,reverse=True)
                      list_ten = list_ten[::-1] 
                      leng_file=len(os.listdir(file_goc+'/config'))
              
                       #  print(leng_file)
                      for i in range(0,leng_file):
                         ten=int(i)
                         file_config=file_goc+'/config/'+list_ten[ten]
                         print(file_config)
                         studentList = []
                         File = open (file_config, "r")
                         #print(File)
                         studentList = File.readlines()

                         ten_1=studentList[0]
                         ten_2=studentList[1]
                         str_1=".jpg"
                         vitri=ten_1.find(str_1)
                         vitri_2=ten_2.find(str_1)

                         str_ten_thay=ten_1[vitri-7:vitri-3]
                         str_ten_thay_2=ten_2[vitri_2-7:vitri_2-3]

                         str_2="config"
                         vitri_3=file_config.find(str_2)
                         str_canthay=file_config[vitri_3+7:vitri_3+11]

                         studentList[0]=ten_1.replace(str_ten_thay,str_canthay)
                         studentList[1]=ten_2.replace(str_ten_thay_2,str_canthay)
                         File_1 = open (file_config, "w")
                         File_1.writelines(studentList)

                         File_1.close()        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    a=mainWindow.get_buton()
    mainWindow.showMaximized()
   # a.show()
    sys.exit(app.exec_())
