import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from qtpy.QtCore import Qt, QFileSystemWatcher, QSettings, Signal
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect, Qt, QSize
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction,qApp, QFileDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer
import cv2
import os, time, shutil
from pypylon import pylon
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

import tkinter as tk
#Lay kich thuoc man hinh thuc te. CHú ý, nếu sử dụng 2 màn hình thì sẽ là kích thước tổng của 2 màn
root = tk.Tk()
width_px = root.winfo_screenwidth() #1920
height_px = root.winfo_screenheight() #1080
space = 20
displayed_image_size = 100
col = 0
row =0
initial_path =None

class Ui_register_Dialog(QWidget):
    def setupUi(self, register_Dialog):
        register_Dialog.setObjectName("register_Dialog")
        register_Dialog.resize(width_px, height_px)

        self.space = 20
        self.displayed_image_size = 100
        self.col = 0
        self.row =0
        self.initial_path =None

        print(width_px)
        print(height_px)
        self.re_Save_pushButton = QtWidgets.QPushButton(register_Dialog)
        self.re_Save_pushButton.setGeometry(QtCore.QRect(30, 560, 89, 25))
        self.re_Save_pushButton.setObjectName("re_Save_pushButton")

        self.horizontalLayoutWidget = QtWidgets.QWidget(register_Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 351, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.register_Camera_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.register_Camera_comboBox.setObjectName("register_Camera_comboBox")
        self.horizontalLayout.addWidget(self.register_Camera_comboBox)

        self.Register_Zoom_In_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Register_Zoom_In_pushButton.setText("")
        self.Register_Zoom_In_pushButton.setIconSize(QtCore.QSize(25, 25))
        self.Register_Zoom_In_pushButton.setObjectName("Register_Zoom_In_pushButton")
        self.horizontalLayout.addWidget(self.Register_Zoom_In_pushButton)

        self.Register_Zoom_out_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Register_Zoom_out_pushButton.setText("")
        self.Register_Zoom_out_pushButton.setIconSize(QtCore.QSize(25, 25))
        self.Register_Zoom_out_pushButton.setObjectName("Register_Zoom_out_pushButton")
        self.horizontalLayout.addWidget(self.Register_Zoom_out_pushButton)

        self.Register_Zoom_fit_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Register_Zoom_fit_pushButton.setText("")
        self.Register_Zoom_fit_pushButton.setIconSize(QtCore.QSize(25, 25))
        self.Register_Zoom_fit_pushButton.setObjectName("Register_Zoom_fit_pushButton")
        self.horizontalLayout.addWidget(self.Register_Zoom_fit_pushButton)

        self.scrollArea = QtWidgets.QScrollArea(register_Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 701, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 699, 489))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.scrollArea_2 = QtWidgets.QScrollArea(register_Dialog)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setBackgroundRole(QPalette.Dark)#THEM DONG

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()

        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_2.setGeometry(width_px-3*displayed_image_size-space, space,displayed_image_size*2,height_px-displayed_image_size)  # khung show image

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.addWidget(self.scrollArea_2)


        ################################################################################
        register_Dialog.closeEvent = self.CloseEvent
        dir_file_goc=os.getcwd()

        file_config_incon_zoom_in=dir_file_goc+"/resources/icons/zoom-in.png"
        file_config_incon_zoom_out=dir_file_goc+"/resources/icons/zoom-out.png"
        file_config_incon_zoom_fit=dir_file_goc+"/resources/icons/zoom.png"
        self.Register_Zoom_In_pushButton.setIcon(QtGui.QIcon(file_config_incon_zoom_in))
        self.Register_Zoom_out_pushButton.setIcon(QtGui.QIcon(file_config_incon_zoom_out))
        self.Register_Zoom_fit_pushButton.setIcon(QtGui.QIcon(file_config_incon_zoom_fit))

        self.re_img_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)#THEM DONG
        self.scrollArea.setBackgroundRole(QPalette.Dark)#THEM DONG
        self.re_img_label.setWordWrap(True)
        self.re_img_label.setObjectName("label")
        self.scrollArea.setWidget(self.re_img_label)

        self.timer = QTimer()
        #self.Close_pushButton.clicked.connect()
        self.re_Save_pushButton.clicked.connect(self.save_img)
        self.timer.timeout.connect(self.viewCam_1)
        self.controlTimer()
        

        #self.show()
        ################################################################################
        self.retranslateUi(register_Dialog)
        QtCore.QMetaObject.connectSlotsByName(register_Dialog)

    def retranslateUi(self, register_Dialog):
        _translate = QtCore.QCoreApplication.translate
        register_Dialog.setWindowTitle(_translate("register_Dialog", "Dialog"))
        self.re_Save_pushButton.setText(_translate("register_Dialog", "Save"))
        self.label.setText(_translate("register_Dialog", "Camera"))

    def viewCam_1(self):
        converter = pylon.ImageFormatConverter()
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

            # create video capture
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
        # Access the image data
            image = converter.Convert(grabResult)
            self.img = image.GetArray()
            self.image = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            height, width, channel = self.image.shape
            step = channel * width
            qImg = QImage(self.image.data, width, height, step, QImage.Format_RGB888)
            self.re_img_label.setPixmap(QPixmap.fromImage(qImg))

    def controlTimer(self):
        if not self.timer.isActive():
            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            self.timer.start(20)

    def save_img(self):
        dir_image_raw = os.getcwd()+"/image_raw"
        dir_image_raw = dir_image_raw.rstrip()
        count_img_raw_saved = len(os.listdir(dir_image_raw))
        count_img_raw_saved = count_img_raw_saved + 1
 
        if (count_img_raw_saved <10):
            self.name = "image_raw_"+"000"+str(count_img_raw_saved)
        elif (count_img_raw_saved < 100):
            self.name = "image_raw_"+"00"+str(count_img_raw_saved)
        elif (count_img_raw_saved < 1000):
            self.name = "image_raw_"+"0"+str(count_img_raw_saved)
        else:
            self.name = str(count_img_raw_saved)

        name_save = dir_image_raw+"/"+self.name+".jpg"
        cv2.imwrite(name_save,self.image)
        self.remRow()
        self.show_img()

    def CloseEvent(self, event):
        self.timer.stop()
        camera.StopGrabbing()
        print("dong")
      
############################################################################
    def show_img(self):
        dir_image_raw = os.getcwd()+"/image_raw"
        file_path = dir_image_raw.rstrip()#bo khoang trang
        img_type = 'jpg'
        png_list = list(i for i in os.listdir(file_path) if str(i).endswith('.{}'.format(img_type)))
        png_list = sorted(png_list) #mang 1 chieu
        num = len(png_list)
        print(num)
        if num !=0:
            for i in range(num):
                print(png_list[i])
                image_id = str(file_path + '/'+png_list[i])
                pixmap = QPixmap(image_id)
                image_id = str(png_list[i])
                self.addImage(pixmap, image_id)
                QApplication.processEvents()

    def addImage(self, pixmap, image_id):
        self.row +=1
        clickable_image = QClickableImage(self.displayed_image_size, self.displayed_image_size, pixmap, image_id)
        self.gridLayout.addWidget(clickable_image, self.row, 0)

    def remRow(self):
        while self.gridLayout.count():
            item = self.gridLayout.takeAt(0)
            widget = item.widget()
            widget.deleteLater()

class QClickableImage(QWidget):
    image_id =''
    def __init__(self,width =0,height =0,pixmap =None,image_id = ''):
        QWidget.__init__(self)
        self.layout =QVBoxLayout(self) #sua o day
        #self.label1 = QLabel()
        #self.label1.setObjectName('label1') # cot 1
        self.lable2 =QLabel()
        self.lable2.setObjectName('label2') #cot 2
        self.width =width
        self.height = height
        self.pixmap =pixmap

        if self.width and self.height:
            self.resize(self.width,self.height)
        if self.pixmap and image_id:
            pixmap = self.pixmap.scaled(QSize(self.width,self.height),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
            #self.label1.setPixmap(pixmap)
            #self.label1.setAlignment(Qt.AlignTop)
            self.label1 = MyLabel(pixmap,image_id)
            self.layout.addWidget(self.label1)
        if image_id:
            self.image_id =image_id
            self.lable2.setText(image_id.split('\\')[-1])
            self.lable2.setAlignment(Qt.AlignTop)
            #Lam cho label thich ung voi kich thuoc
            self.lable2.adjustSize()
            self.layout.addWidget(self.lable2)
        self.setLayout(self.layout)


class MyLabel(QLabel,QWidget):
    def __init__(self, pixmap =None, image_id = None):
        QLabel.__init__(self)
        self.pixmap = pixmap
        self.image_id = image_id
        self.setPixmap(pixmap)
 
        self.setAlignment(Qt.AlignCenter)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)  
 
    def rightMenuShow(self, point):
        #Menu chuot phai
        self.popMenu = QMenu()
        ch = QAction(u'Back', self)
        sc = QAction(u'Delete', self)
        xs = QAction(u'Show', self)
        self.popMenu.addAction(ch)
        self.popMenu.addAction(sc)
        self.popMenu.addAction(xs)
        # Event
        ch.triggered.connect(self.reback)
        sc.triggered.connect(self.delete)
        xs.triggered.connect(self.rshow)
        self.showContextMenu(QCursor.pos())
 
 
    def rshow(self):
        print("show")
        print(self.image_id)
    def delete(self):
        dir_image_raw = os.getcwd()+"/image_raw"
        file_path = dir_image_raw.rstrip()#bo khoang trang
        print("delete")
        os.remove(file_path + '/' + self.image_id)
        print(self.image_id)
    def reback(self):
        print("back")
        print(self.image_id)

 
    def showContextMenu(self, pos):
        self.popMenu.move(pos)
        self.popMenu.show()
 
    def menuSlot(self, act):
        print(act.text())

#####################################################################################
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_Dialog = QtWidgets.QDialog()
    ui = Ui_register_Dialog()
    ui.setupUi(register_Dialog)
    register_Dialog.show()
    sys.exit(app.exec_())
'''