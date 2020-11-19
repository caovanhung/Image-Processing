# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detection_color.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtGui import QIcon
from detect_color_xulyanh import*
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui, QtCore, QtWidgets
class MyLabel(QLabel):

     x0 = 0
     y0 = 0
     x1 = 0
     y1 = 0
     flag = False
     
 #Mouse click event
     def mousePressEvent(self,event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()
 #Mouse release event
     def mouseReleaseEvent(self,event):
        self.flag = False
 #Mouse movement events
     def mouseMoveEvent(self,event):
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()
 #Draw events
     def paintEvent(self, event):
        super().paintEvent(event)
        rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
        print(self.x1)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
        painter.drawRect(rect)

class Ui_detecton_clor_Dialog(object):
    def setupUi(self, detecton_clor_Dialog):
        detecton_clor_Dialog.setObjectName("detecton_clor_Dialog")
        detecton_clor_Dialog.resize(886, 581)
        detecton_clor_Dialog.setBaseSize(QtCore.QSize(3, 3))
        self.verticalLayoutWidget = QtWidgets.QWidget(detecton_clor_Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 581, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
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

        self.img_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.img_label.setText("")
        self.img_label.setObjectName("img_label")
        self.verticalLayout.addWidget(self.img_label)
        
        self.checkBox = QtWidgets.QCheckBox(detecton_clor_Dialog)
        self.checkBox.setGeometry(QtCore.QRect(630, 170, 92, 23))
        self.checkBox.setObjectName("checkBox")
        
        self.checkBox_2 = QtWidgets.QCheckBox(detecton_clor_Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(750, 170, 92, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.tableWidget = QtWidgets.QTableWidget(detecton_clor_Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(610, 230, 256, 192))
        self.tableWidget.setBaseSize(QtCore.QSize(1, 1))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)
      # self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        #self.tableWidget.horizontalHeader("G")
        #self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)")
        
        self.tableWidget.setVerticalHeaderLabels(['Min', 'Measure', 'Max'])
        self.pushButton.clicked.connect(self.open_img)
       # self.tableWidget.setHorizontalHeader (QTableWidgetItem("G"),QTableWidgetItem("G"),QTableWidgetItem("G"))
        self.checkBox.toggled.connect(self.GRB_show)
        self.checkBox_2.toggled.connect(self.HSV_show)

        self.retranslateUi(detecton_clor_Dialog)
        QtCore.QMetaObject.connectSlotsByName(detecton_clor_Dialog)
        self.img_label.setPixmap(QPixmap.fromImage(qImg))
        self.lb = MyLabel()
        pixmap = QPixmap.fromImage(self.qImg)
        self.lb.setPixmap(pixmap)
        self.lb.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        img=xulyanh(self.img)

        
        

        

    def retranslateUi(self, detecton_clor_Dialog):
        _translate = QtCore.QCoreApplication.translate
        detecton_clor_Dialog.setWindowTitle(_translate("detecton_clor_Dialog", "Dialog"))
        self.pushButton.setText(_translate("detecton_clor_Dialog", "OK"))
        self.comboBox.setItemText(0, _translate("detecton_clor_Dialog", "01"))
        self.comboBox.setItemText(1, _translate("detecton_clor_Dialog", "02"))
        self.comboBox.setItemText(2, _translate("detecton_clor_Dialog", "03"))
        self.comboBox.setItemText(3, _translate("detecton_clor_Dialog", "04"))
        self.checkBox.setText(_translate("detecton_clor_Dialog", "GRB"))
        self.checkBox_2.setText(_translate("detecton_clor_Dialog", "HSV"))
    def open_img(self):
        
        ten=self.comboBox.currentText()
        file_img=ten+".jpg"
        self.img=cv2.imread(file_img,1)
        height, width, channel = self.img.shape
        step = channel * width
        # create QImage from image
        self.qImg = QImage(self.img.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label

        
        self.GRB_trungbinh=img.GRB()
        self.HSV_trungbinh=img.HSV();
        
 
    def GRB_show(self):
        
        if self.checkBox.isChecked() == True:
            self.tableWidget.setHorizontalHeaderLabels(['R', 'G', 'B'])
        #print(GRB_trungbinh)
        #self.tableWidget.setItem(0,0,QTableWidgetItem(str(GRB_trungbinh[0])))
            for i in range(0,3):
                self.tableWidget.setItem(1,i, QTableWidgetItem(str(self.GRB_trungbinh[i])))
        #self.checkBox.setChecked(1)
            self.checkBox_2.setChecked(0)
        
        #cv2.imwrite(file_img,img_2)
    def HSV_show(self):
        if self.checkBox.isChecked() == True:
            self.tableWidget.setHorizontalHeaderLabels(['H', 'S', 'V'])
            for i in range(0,3):
                self.tableWidget.setItem(1,i, QTableWidgetItem(str(self.HSV_trungbinh[i])))
            self.checkBox.setChecked(0)
      #  self.checkBox_2.setChecked(1)
        
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    detecton_clor_Dialog = QtWidgets.QDialog()
    ui = Ui_detecton_clor_Dialog()
    ui.setupUi(detecton_clor_Dialog)
    detecton_clor_Dialog.show()
    sys.exit(app.exec_())

