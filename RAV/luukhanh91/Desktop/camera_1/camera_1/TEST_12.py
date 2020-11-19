# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TEST_2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
    qApp, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import os
class MyLabel(QLabel):

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
          print(self.x1)
          print(self.y1)
          painter = QPainter(self)
          if self.dk:
             painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
             painter.drawRect(rect)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.scaleFactor = 0.0
        Dialog.setObjectName("Dialog")
        Dialog.resize(574, 537)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(20, 60, 531, 431))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 529, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
    #    self.scrollArea.setWidget(self.scrollAreaWidgetContents)# BO DONG NAY THI MOI HIEN THI DUOJ 



        self.label = MyLabel(self.scrollAreaWidgetContents)#THEM DONG
        self.scrollArea.setBackgroundRole(QPalette.Dark)#THEM DONG
        self.Zoom_in_pushButton = QtWidgets.QPushButton(Dialog)
        self.Zoom_in_pushButton.setGeometry(QtCore.QRect(30, 10, 25, 25))
        self.Zoom_in_pushButton.setObjectName("Zoom_in_pushButton")
        self.Zoom_out_pushButton = QtWidgets.QPushButton(Dialog)
        self.Zoom_out_pushButton.setGeometry(QtCore.QRect(150, 10, 25, 25))
        self.Zoom_out_pushButton.setObjectName("Zoom_out_pushButton")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 10, 25, 25))
        self.pushButton.setObjectName("pushButton")
        file_goc=os.getcwd()
       # self.ten=self.Image_comboBox.currentText()
        file_config=file_goc.replace("/detection_edges","")
        file_config_incon_zoom_in=file_config+"/resources/icons/zoom-in.png"
        file_config_incon_zoom_out=file_config+"/resources/icons/zoom-out.png"
        file_config_incon_zoom_fit=file_config+"/resources/icons/zoom.png"



        
        self.scale_textEdit = QtWidgets.QTextEdit(Dialog)
        self.scale_textEdit.setGeometry(QtCore.QRect(360, 9, 104, 31))
        self.scale_textEdit.setObjectName("scale_textEdit")
        self.Zoom_in_pushButton.clicked.connect(self.zoom_In)
        self.Zoom_out_pushButton.clicked.connect(self.zoom_Out)
        self.pushButton.clicked.connect(self.zoom_fit)
        self.Zoom_in_pushButton.setIcon(QtGui.QIcon(file_config_incon_zoom_in))
        self.Zoom_out_pushButton.setIcon(QtGui.QIcon(file_config_incon_zoom_out))
        self.pushButton.setIcon(QtGui.QIcon(file_config_incon_zoom_fit))

        self.label.setfdk(1)
       # print(self.label.x0)
       # print(self.label.y0)
       # print(self.label.x1)
       # print(self.label.y1)

    #    self.label.setGeometry(QtCore.QRect(15, 10, 151, 101))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.scrollArea.setWidget(self.label)
        self.Detection_edges_open_img()

     

        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def zoom_In(self):
        self.scaleImage(1.2)
    def zoom_Out(self):
        self.scaleImage(0.75)
    def zoom_fit(self):
            height, width,channel = self.img.shape
            step =  width*channel
            self.scaleFactor=1
            qImg = QImage(self.img.data, width, height, step, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            self.label.setPixmap(QPixmap.fromImage(qImg))
        
    def scaleImage(self, factor):
        self.scaleFactor *= factor
        height, width,channel = self.img.shape
        if self.scaleFactor<3 or self.scaleFactor>0.4 :

            self.img_1=cv2.resize(self.img,(int(self.scaleFactor*height),int(self.scaleFactor*width)))
            height, width,channel = self.img_1.shape
            step =  width*channel
            qImg = QImage(self.img_1.data, width, height, step, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            self.label.setPixmap(QPixmap.fromImage(qImg))
     #   self.label.resize(self.scaleFactor * self.label.pixmap().size())

     #   self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
    #    self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

       # self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
       # self.zoomOutAct.setEnabled(self.scaleFactor > 0.333)


    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                               + ((factor - 1) * scrollBar.pageStep() / 2)))

    

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
  #      self.Zoom_in_pushButton.setText(_translate("Dialog", "Zoom In"))
  #      self.Zoom_out_pushButton.setText(_translate("Dialog", "Zoom out"))
  #      self.pushButton.setText(_translate("Dialog", "Fit"))
    def Detection_edges_open_img(self):
        file_goc=os.getcwd()
       # self.ten=self.Image_comboBox.currentText()
        file_config=file_goc.replace("/detection_edges","")
        self.file_img=file_config+"/"+"03.jpg"
      #  print(file_img)
        self.img=cv2.imread(self.file_img,1)
       
      #  print (self.img)
        self.scaleFactor = 1.0
        
        height, width,channel = self.img.shape
        print(height,width)
      #  self.label.setGeometry(QtCore.QRect(15, 10, height, width))
        step =  width*channel
        qImg = QImage(self.img.data, width, height, step, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.label.setPixmap(QPixmap.fromImage(qImg))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

