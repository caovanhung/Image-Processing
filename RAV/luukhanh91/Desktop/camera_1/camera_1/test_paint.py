# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_paint.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtCore import QPoint




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
          if self.dk==1 or self.dk==2:
               rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
         # print(self.x1)
          if self.dk==2  :
               rect0=QRect(self.x00, self.y00, abs(self.x01-self.x00), abs(self.y01-self.y00))
        #  print(self.y1)
          painter = QPainter(self)
          self.p=QPoint(self.x00,self.y00)
          if self.dk==1 or self.dk==2:
             painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
             painter.drawRect(rect)
          if self.dk==2:
             painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
             #painter.drawRect(rect0)
             painter.drawEllipse(self.p, abs(self.y01-self.y00), abs(self.y01-self.y00))
          

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(571, 611)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 451, 501))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = Threshold_MyLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 540, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 540, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton.clicked.connect(self.show_img)
        self.pushButton_2.clicked.connect(self.show_img_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
    def show_img(self):
        self.label.setfdk(1)
    def show_img_2(self):
        self.label.setfdk(2)
        
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

