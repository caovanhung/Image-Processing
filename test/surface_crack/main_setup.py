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

#camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
import os
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets


global REMOVE_ARE
REMOVE_ARE= 1500

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
        if self.dk==2 or self.dem != 0:
            rect0=QRect(self.x00, self.y00, abs(self.x01-self.x00), abs(self.y01-self.y00))
        painter = QPainter(self)
        if self.dk==1:
            painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
            painter.drawRect(rect)
        if self.dk==2 or self.dem != 0:
            painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
            painter.drawRect(rect0)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1847, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea_Image = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_Image.setGeometry(QtCore.QRect(10, 10, 1000, 800))
        self.scrollArea_Image.setWidgetResizable(True)
        self.scrollArea_Image.setObjectName("scrollArea_Image")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 998, 798))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.img_thresold_label = Threshold_MyLabel()
        self.scrollArea_Image.setBackgroundRole(QPalette.Dark)#THEM DONG
        self.img_thresold_label.setWordWrap(True)
        self.img_thresold_label.setObjectName("label")
        self.scrollArea_Image.setWidget(self.img_thresold_label)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1029, 9, 671, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)


        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(8, 20, 651, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.checkBox_Thresold = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_Thresold.setObjectName("checkBox_Thresold")
        self.verticalLayout_2.addWidget(self.checkBox_Thresold)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)

        self.label_Thresol = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_Thresol.setObjectName("label_Thresol")
        self.horizontalLayout_2.addWidget(self.label_Thresol)

        self.ScrollBar_Thresol = QtWidgets.QScrollBar(self.verticalLayoutWidget_2)
        self.ScrollBar_Thresol.setOrientation(QtCore.Qt.Horizontal)
        self.ScrollBar_Thresol.setObjectName("ScrollBar_Thresol")
        self.ScrollBar_Thresol.setMaximum(255)
        self.ScrollBar_Thresol.setMinimum(0)
        self.horizontalLayout_2.addWidget(self.ScrollBar_Thresol)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem1)

        self.label_typeThresol = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_typeThresol.setObjectName("label_typeThresol")
        self.horizontalLayout_3.addWidget(self.label_typeThresol)

        self.comboBox_typeThresol = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_typeThresol.setObjectName("comboBox_typeThresol")
        self.comboBox_typeThresol.addItem("THRESH_BINARY")
        self.comboBox_typeThresol.addItem("THRESH_BINARY_INV")
        self.comboBox_typeThresol.addItem("THRESH_TRUNC")
        self.comboBox_typeThresol.addItem("THRESH_TOZERO")
        self.comboBox_typeThresol.addItem("THRESH_TOZERO_INV")
        self.horizontalLayout_3.addWidget(self.comboBox_typeThresol)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 230, 651, 101))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.checkBox_removeAREA = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_removeAREA.setObjectName("checkBox_removeAREA")
        self.horizontalLayout_7.addWidget(self.checkBox_removeAREA)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_7.addItem(spacerItem2)

        self.label_removeAREA = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_removeAREA.setObjectName("label_removeAREA")
        self.horizontalLayout_7.addWidget(self.label_removeAREA)

        self.lineEdit_removeAREA = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_removeAREA.setObjectName("lineEdit_removeAREA")
        self.horizontalLayout_7.addWidget(self.lineEdit_removeAREA)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.checkBox_DrawArea = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_DrawArea.setObjectName("checkBox_DrawArea")
        self.verticalLayout_4.addWidget(self.checkBox_DrawArea)

        self.checkBox_WriteArea = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_WriteArea.setObjectName("checkBox_WriteArea")
        self.verticalLayout_4.addWidget(self.checkBox_WriteArea)

        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 150, 651, 71))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.checkBox_CLAHE = QtWidgets.QCheckBox(self.horizontalLayoutWidget_4)
        self.checkBox_CLAHE.setObjectName("checkBox_CLAHE")
        self.verticalLayout_3.addWidget(self.checkBox_CLAHE)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit_clahe = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_clahe.setObjectName("lineEdit_clahe")
        self.horizontalLayout_5.addWidget(self.lineEdit_clahe)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.btn_SaveSetting = QtWidgets.QPushButton(self.groupBox)
        self.btn_SaveSetting.setGeometry(QtCore.QRect(550, 340, 111, 51))
        self.btn_SaveSetting.setObjectName("btn_SaveSetting")

        self.btn_ResetSetting = QtWidgets.QPushButton(self.groupBox)
        self.btn_ResetSetting.setGeometry(QtCore.QRect(10, 340, 111, 51))
        self.btn_ResetSetting.setObjectName("btn_ResetSetting")
        self.verticalLayout.addWidget(self.groupBox)



        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(1030, 430, 671, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setItem(0,0,QTableWidgetItem("Threshold"))
        self.tableWidget.setItem(1,0,QTableWidgetItem("Tong so"))
        self.tableWidget.setItem(2,0,QTableWidgetItem("Tong dien tich"))
        self.tableWidget.setItem(3,0,QTableWidgetItem("Dien tich lon nhat"))
        self.tableWidget.setItem(4,0,QTableWidgetItem("Dien tich nho nhat"))

        self.btn_START = QtWidgets.QPushButton(self.centralwidget)
        self.btn_START.setGeometry(QtCore.QRect(10, 900, 120, 50))
        self.btn_START.setObjectName("btn_START")

        self.comboBox_listImage = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_listImage.setGeometry(QtCore.QRect(550, 900, 120, 50))
        self.comboBox_listImage.setObjectName("comboBox_listImage")
        self.comboBox_listImage.addItem("01")
        self.comboBox_listImage.addItem("02")
        self.comboBox_listImage.addItem("03")
        self.comboBox_listImage.addItem("04")

        self.btn_OpenImage = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OpenImage.setGeometry(QtCore.QRect(700, 900, 120, 50))
        self.btn_OpenImage.setObjectName("btn_OpenImage")

        self.btn_Preview = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Preview.setGeometry(QtCore.QRect(850, 900, 120, 50))
        self.btn_Preview.setObjectName("btn_Preview")

        self.btn_RUN = QtWidgets.QPushButton(self.centralwidget)
        self.btn_RUN.setGeometry(QtCore.QRect(1720, 830, 120, 120))
        self.btn_RUN.setObjectName("btn_RUN")

        self.label_stt_OK_NG = QtWidgets.QLabel(self.centralwidget)
        self.label_stt_OK_NG.setGeometry(QtCore.QRect(1720, 10, 121, 101))
        self.label_stt_OK_NG.setStyleSheet("background: green")
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_stt_OK_NG.setFont(font)
        self.label_stt_OK_NG.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stt_OK_NG.setObjectName("label_stt_OK_NG")


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "SETUP"))
        self.checkBox_Thresold.setText(_translate("MainWindow", "SimpleThresold"))
        self.label_Thresol.setText(_translate("MainWindow", "Thresold"))
        self.label_typeThresol.setText(_translate("MainWindow", "Type"))
        self.checkBox_removeAREA.setText(_translate("MainWindow", "Remove area"))
        self.label_removeAREA.setText(_translate("MainWindow", "Area limit"))
        self.checkBox_DrawArea.setText(_translate("MainWindow", "Draw Area"))
        self.checkBox_WriteArea.setText(_translate("MainWindow", "Write Area"))
        self.checkBox_CLAHE.setText(_translate("MainWindow", "CLAHE (Histogram Equalization)"))
        self.label_3.setText(_translate("MainWindow", "clipLimit"))
        self.btn_SaveSetting.setText(_translate("MainWindow", "SAVE"))
        self.btn_ResetSetting.setText(_translate("MainWindow", "DEFAULT"))
        self.btn_START.setText(_translate("MainWindow", "START"))
        self.btn_OpenImage.setText(_translate("MainWindow", "OPEN"))
        self.btn_Preview.setText(_translate("MainWindow", "Preview"))
        self.btn_RUN.setText(_translate("MainWindow", "RUN"))
        self.label_stt_OK_NG.setText(_translate("MainWindow", "OK"))





        #self.btn_SaveSetting.clicked.connect()
        #self.btn_ResetSetting.clicked.connect()



        self.btn_OpenImage.clicked.connect(self.open_image)
        self.btn_Preview.clicked.connect(self.processing_image)
        self.ScrollBar_Thresol.sliderMoved.connect(self.Threshold_bar)
        self.ScrollBar_Thresol.setEnabled(1)

    def open_image(self):
        self.name_of_image = self.comboBox_listImage.currentText()
        image = self.name_of_image + ".bmp"
        self.img = cv2.imread(image,0)
        self.img_1=cv2.imread(image,0)

        height,width = self.img.shape
        step = width
        qImg = QImage(self.img.data, width, height, step, QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(qImg)
        self.img_thresold_label.setPixmap(QPixmap.fromImage(qImg))
        self.img_thresold_label.setCursor(QtCore.Qt.CrossCursor)
        self.img_thresold_label.setfdk(1)
        self.btn_OpenImage.setEnabled(1)
        self.ScrollBar_Thresol.setEnabled(1)
        self.comboBox_listImage.setEnabled(1)

    def save_image_Thresholded(self):
        self.name_of_image = self.comboBox_listImage.currentText()
        image = self.name_of_image + ".bmp"

        self.img_luu=cv2.imread(image,0)
        self.Threshold_bar()

        self.file_img_bandau = self.name_of_image+"origin"+".bmp"
        self.file_img = self.name_of_image + "process"+".bmp"
        self.file_img_cut = self.name_of_image + "cut"+".bmp"
        imgcat=self.img[self.y00:self.y10,self.x00:self.x10]
        imgcut=self.img_luu[self.y00:self.y10,self.x00:self.x10]
        cv2.imwrite(self.file_img_bandau,self.img)
        cv2.imwrite(self.file_img,imgcat)
        cv2.imwrite(self.file_img_cut,imgcut)

    def Threshold_bar(self):
        if  self.img_thresold_label.x0 and self.img_thresold_label.x1 and self.img_thresold_label.y0 and self.img_thresold_label.y1 :
            self.x00=self.img_thresold_label.x0
            self.x10=self.img_thresold_label.x1
            self.y00=self.img_thresold_label.y0
            self.y10=self.img_thresold_label.y1

            self.thresh_value=self.ScrollBar_Thresol.value()
            self.tableWidget.setItem(0,1,QTableWidgetItem(str(self.thresh_value)))

            self.threshold_img=Class_Threshold(self.img,self.img_1,self.x00,self.y00,self.x10,self.y10)
            self.threshold_img.SimpleThresholding(self.thresh_value,2)

            height, width  =self.img.shape
            step = width
            qImg = QImage(self.img.data, width, height, step, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qImg)
            self.img_thresold_label.setPixmap(QPixmap.fromImage(qImg))
            self.img_thresold_label.setfdk(0)

###############################################Enhance image####################################
    def pre_process_clahe(self,image):
        gray = cv2.cvtColor(image, cv.COLOR_RGB2GRAY)
        clahe = cv2.createCLAHE(5, (8,8))
        dst = clahe.apply(gray)
        cv2.imwrite("03.bmp", dst)
###############################################CONTOURS#########################################
    def remove_are_less_more(self,image,num):
        self.name_of_image = self.comboBox_listImage.currentText()
        name = self.name_of_image +"process"+".bmp"

        #remove are less stand 
        contours,hierarchy = cv2.findContours( image , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contour = contours

        c_max = []
        for i in range(len(contour)):
            cnt = contours[i]
            area = cv2.contourArea(cnt)
            if area < num:
                contour.append(contour[i]) # add them vao chuoi
                c_min = []
                c_min.append(cnt)
                cv2.drawContours(image, c_min, -1, (0, 0, 0), thickness=-1)
                continue
            c_max.append(cnt)
        cv2.drawContours(image, c_max, -1, (255, 255, 255), thickness=-1)
        cv2.imwrite(name,image)

    def  caculate_contourArea(self,image):
        contour,hierarchy = cv2.findContours( image , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        area = 0
        min=111111
        max=0
        for i in range(len(contour)):
            if cv2.contourArea(contour[i])>10:
                if cv2.contourArea(contour[i])>max:
                    max=cv2.contourArea(contour[i])
                if cv2.contourArea(contour[i])<min:
                    min=cv2.contourArea(contour[i])
                area += cv2.contourArea(contour[i])
        self.tableWidget.setItem(1,1,QTableWidgetItem(str(len(contour))))
        self.tableWidget.setItem(2,1,QTableWidgetItem(str(area)))
        self.tableWidget.setItem(3,1,QTableWidgetItem(str(max)))
        self.tableWidget.setItem(4,1,QTableWidgetItem(str(min)))
        return len(contour)

    def draw_contours(self,image):
        self.name_of_image = self.comboBox_listImage.currentText()
        name = self.name_of_image +'process'+'.bmp'

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(image, contours, -1, (0, 0, 255), 1)
        for i in range(len(contours)):
            #cv2.drawContours(image, contours, -1, (0, 0, 255), 1)
            cnt = contours[i]
            M = cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.putText(image,str(cv2.contourArea(contours[i])),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,.5,(0,255,0),1,cv2.LINE_AA)
        cv2.imwrite(name,image)

    def show_img_processed(self,image):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = img.shape
        step = channel * width
        qImg = QImage(img.data, width, height, step, QImage.Format_RGB888)
        self.img_thresold_label.setPixmap(QPixmap.fromImage(qImg))
        self.img_thresold_label.setCursor(QtCore.Qt.CrossCursor)
        self.img_thresold_label.setfdk(1)

    def processing_image(self):
        self.save_image_Thresholded()
        flag_error = 0
        self.name_of_image = self.comboBox_listImage.currentText()
        name = self.name_of_image +'process'+'.bmp'
        self.img_process = cv2.imread(name,0)
     
        self.remove_are_less_more(self.img_process,REMOVE_ARE)
        flag_error = self.caculate_contourArea(self.img_process)

        img = cv2.imread(name)
        self.draw_contours(img)
        self.show_img_processed(img)

        if flag_error > 0:
            self.label_stt_OK_NG.setText("NG")
            self.label_stt_OK_NG.setStyleSheet("background: red")
        else:
            self.label_stt_OK_NG.setText("OK")
            self.label_stt_OK_NG.setStyleSheet("background: green")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
