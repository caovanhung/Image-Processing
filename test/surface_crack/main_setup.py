from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QLabel,QCheckBox, QLineEdit
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication, QIcon, QPalette
from Threshold_xulyanh import*
from PyQt5.QtCore import QTimer, QPoint, QRect, Qt
from Threshold_xulyanh import*
from pypylon import pylon

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

import os
import cv2

flag_SimpleThresol = True
THRESOLD = 83
THRESOLD_TYPE = 1
flag_ClaheHistogram = False
CLAHE_LIMIT = 5
flag_RemoveArea = True
REMOVE_ARE= 500
flag_DrawArea = True
flag_WriteArea = False
flag_Camera_Open = False
timeLIMIT_btnRUN = 1000
cnt_OK = 0
cnt_NG = 0

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
     
    def mousePressEvent(self,event):
        if self.dk==1:
            self.flag = True
            self.x0 = event.x()
            self.y0 = event.y()
        if self.dk==2:
            self.flag = True
            self.x00 = event.x()
            self.y00 = event.y()            
    def mouseReleaseEvent(self,event):
        if self.dk:
            self.flag = False
            self.dem=self.dem+1
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
        self.scrollArea_Image.setBackgroundRole(QPalette.Dark)
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


        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 350, 651, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.lineEdit_timeLIMIT_RUN = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_timeLIMIT_RUN.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit_timeLIMIT_RUN)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.groupBox)


        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(1030, 430, 600, 200))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setItem(0,0,QTableWidgetItem("Threshold"))
        self.tableWidget.setItem(1,0,QTableWidgetItem("Tong so"))
        self.tableWidget.setItem(2,0,QTableWidgetItem("Tong dien tich"))
        self.tableWidget.setItem(3,0,QTableWidgetItem("Dien tich lon nhat"))
        self.tableWidget.setItem(4,0,QTableWidgetItem("Dien tich nho nhat"))




        self.label_cnt_OK = QtWidgets.QLabel(self.centralwidget)
        self.label_cnt_OK.setGeometry(QtCore.QRect(1030, 700, 100, 100))
        self.label_cnt_OK.setStyleSheet("background: green")
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_cnt_OK.setFont(font)
        self.label_cnt_OK.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cnt_OK.setObjectName("label_cnt_OK")

        self.cnt_OK = QtWidgets.QLabel(self.centralwidget)
        self.cnt_OK.setGeometry(QtCore.QRect(1150, 700, 100, 100))
        self.cnt_OK.setStyleSheet("background: white")
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.cnt_OK.setFont(font)
        self.cnt_OK.setAlignment(QtCore.Qt.AlignCenter)
        self.cnt_OK.setObjectName("cnt_OK")


        self.label_cnt_NG = QtWidgets.QLabel(self.centralwidget)
        self.label_cnt_NG.setGeometry(QtCore.QRect(1350, 700, 100, 100))
        self.label_cnt_NG.setStyleSheet("background: red")
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_cnt_NG.setFont(font)
        self.label_cnt_NG.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cnt_NG.setObjectName("label_cnt_NG")

        self.cnt_NG = QtWidgets.QLabel(self.centralwidget)
        self.cnt_NG.setGeometry(QtCore.QRect(1500, 700, 100, 100))
        self.cnt_NG.setStyleSheet("background: white")
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.cnt_NG.setFont(font)
        self.cnt_NG.setAlignment(QtCore.Qt.AlignCenter)
        self.cnt_NG.setObjectName("cnt_NG")



        self.btn_START = QtWidgets.QPushButton(self.centralwidget)
        self.btn_START.setGeometry(QtCore.QRect(10, 830, 120, 120))
        self.btn_START.setObjectName("btn_START")

        self.comboBox_listImage = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_listImage.setGeometry(QtCore.QRect(550, 900, 120, 50))
        self.comboBox_listImage.setObjectName("comboBox_listImage")
        self.comboBox_listImage.addItem("0001")
        self.comboBox_listImage.addItem("0002")
        self.comboBox_listImage.addItem("0003")
        self.comboBox_listImage.addItem("0004")

        self.btn_OpenImage = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OpenImage.setGeometry(QtCore.QRect(700, 900, 120, 50))
        self.btn_OpenImage.setObjectName("btn_OpenImage")

        self.btn_Preview = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Preview.setGeometry(QtCore.QRect(850, 900, 120, 50))
        self.btn_Preview.setObjectName("btn_Preview")

        self.btn_GO = QtWidgets.QPushButton(self.centralwidget)
        self.btn_GO.setGeometry(QtCore.QRect(1580, 830, 120, 120))
        self.btn_GO.setObjectName("btn_GO")

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
        self.label_2.setText(_translate("MainWindow", "Times Gap"))
        self.btn_START.setText(_translate("MainWindow", "START"))
        self.btn_OpenImage.setText(_translate("MainWindow", "OPEN"))
        self.btn_Preview.setText(_translate("MainWindow", "Preview"))
        self.btn_GO.setText(_translate("MainWindow", "GO"))
        self.btn_RUN.setText(_translate("MainWindow", "RUN"))
        self.label_stt_OK_NG.setText(_translate("MainWindow", "OK"))

        self.label_cnt_OK.setText(_translate("MainWindow", "OK"))
        self.cnt_OK.setText(_translate("MainWindow", "0"))
        self.label_cnt_NG.setText(_translate("MainWindow", "NG"))
        self.cnt_NG.setText(_translate("MainWindow", "0"))
        
        self.checkBox_Thresold.setChecked(True)
        self.checkBox_CLAHE.setChecked(False)
        self.checkBox_removeAREA.setChecked(True)
        self.checkBox_DrawArea.setChecked(True)
        self.checkBox_WriteArea.setChecked(False)
        self.lineEdit_clahe.setText("5")
        self.lineEdit_timeLIMIT_RUN.setText("1000")
        self.lineEdit_removeAREA.setText("500")

        self.checkBox_Thresold.toggled.connect(self.checkBoxThresold)
        self.checkBox_CLAHE.toggled.connect(self.checkBoxCLAHE)
        self.checkBox_removeAREA.toggled.connect(self.checkBoxRemoveAREA)
        self.checkBox_DrawArea.toggled.connect(self.checkBoxDrawArea)
        self.checkBox_WriteArea.toggled.connect(self.checkBoxWriteArea)

        self.btn_OpenImage.clicked.connect(self.open_image)
        self.btn_Preview.clicked.connect(self.processing_image)
        self.ScrollBar_Thresol.sliderMoved.connect(self.Threshold_bar)
        self.ScrollBar_Thresol.setEnabled(1)

        self.timer = QTimer()
        self.timer1 = QTimer()
        self.timer.timeout.connect(self.Threshold_viewCam)
        self.btn_START.clicked.connect(self.controlTimer)
        self.btn_GO.clicked.connect(self.processing_image_camera)

        self.timer1.timeout.connect(self.processing_image_camera)
        self.btn_RUN.clicked.connect(self.controlTimer1)

########################################Open Image##########################################
    def open_image(self):
        self.dir_image_raw = os.getcwd()+"/image_raw"
        self.dir_image_raw = self.dir_image_raw.rstrip()
        self.dir_image_processed = os.getcwd()+"/image_processed"
        self.dir_image_processed = self.dir_image_processed.rstrip()

        global flag_ClaheHistogram
        global flag_Camera_Open

        flag_Camera_Open = False
        self.name = self.comboBox_listImage.currentText()
        name_image = self.dir_image_raw+"/"+self.name + ".bmp"

        if flag_ClaheHistogram == True:
            name_image = self.dir_image_raw+"/"+self.name + ".bmp"
            img_constrast = cv2.imread(name_image)
            self.pre_process_clahe(img_constrast)
            self.checkBox_CLAHE.setChecked(False)


        self.img = cv2.imread(name_image,0)
        self.img_1=cv2.imread(name_image,0)
        self.img_2=cv2.imread(name_image,0)

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
        global flag_Camera_Open
        if flag_Camera_Open == True:
            image = self.dir_image_raw+"/"+self.name + ".bmp"
        else:
            self.name = self.comboBox_listImage.currentText()
            image = self.dir_image_raw+"/"+self.name + ".bmp"
        self.img_luu=cv2.imread(image,0)
        self.Threshold_bar()

        self.file_img_bandau = self.dir_image_processed +"/"+ self.name+"origin_cut"+".bmp"
        self.file_img = self.dir_image_processed +"/"+ self.name + "process"+".bmp"
        self.file_img_cut = self.dir_image_processed +"/"+ self.name + "cut"+".bmp"

        self.img_2 = cv2.rectangle(self.img_2, (self.x00,self.y00),(self.x10,self.y10),(0,0,255),2)
        imgcat=    self.img[self.y00:self.y10,self.x00:self.x10]
        imgcut=self.img_luu[self.y00:self.y10,self.x00:self.x10]

        cv2.imwrite(self.file_img_bandau,self.img_2)
        cv2.imwrite(self.file_img,imgcat)
        cv2.imwrite(self.file_img_cut,imgcut)

#######################################check_box##############################################
    def checkBoxThresold(self):
        global flag_SimpleThresol
        if self.checkBox_Thresold.isChecked() == True:
            flag_SimpleThresol = True
        else:
            flag_SimpleThresol = False

    def checkBoxCLAHE(self):
        global flag_ClaheHistogram
        if self.checkBox_CLAHE.isChecked() == True:
            flag_ClaheHistogram = True
        else:
            flag_ClaheHistogram = False

    def checkBoxRemoveAREA(self):
        global flag_RemoveArea
        if self.checkBox_removeAREA.isChecked() == True:
            flag_RemoveArea = True
        else:
            flag_RemoveArea = False

    def checkBoxDrawArea(self):
        global flag_DrawArea
        if self.checkBox_DrawArea.isChecked() == True:
            flag_DrawArea = True
        else:
            flag_DrawArea = False

    def checkBoxWriteArea(self):
        global flag_WriteArea
        if self.checkBox_WriteArea.isChecked() == True:
            flag_WriteArea = True
        else:
            flag_WriteArea = False


################################################Threshold#######################################
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

###############################################Camera Viewer####################################

    def controlTimer(self):
        if not self.timer.isActive():
            if  self.img_thresold_label.x0 and self.img_thresold_label.x1 and self.img_thresold_label.y0 and self.img_thresold_label.y1 :
                self.x00=self.img_thresold_label.x0
                self.x10=self.img_thresold_label.x1
                self.y00=self.img_thresold_label.y0
                self.y10=self.img_thresold_label.y1
            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            self.timer.start(200)#ms
            self.btn_START.setText("STOP")
            print("STOP")
        else:
            self.timer.stop()
            camera.StopGrabbing()
            self.btn_START.setText("START")
            print("START")

        self.img_thresold_label.setfdk(1)
        self.btn_OpenImage.setEnabled(1)
        self.ScrollBar_Thresol.setEnabled(1)
        self.comboBox_listImage.setEnabled(1)

    def controlTimer1(self):
        timeLIMIT_btnRUN = int(self.lineEdit_timeLIMIT_RUN.text())
        if not self.timer1.isActive():
            self.timer1.start(timeLIMIT_btnRUN) #ms
        else:
            self.timer1.stop()
  
    def Threshold_viewCam(self):
        global flag_Camera_Open
        flag_Camera_Open = True
        if  self.img_thresold_label.x0 and self.img_thresold_label.x1 and self.img_thresold_label.y0 and self.img_thresold_label.y1 :
            self.x00=self.img_thresold_label.x0
            self.x10=self.img_thresold_label.x1
            self.y00=self.img_thresold_label.y0
            self.y10=self.img_thresold_label.y1
            converter = pylon.ImageFormatConverter()
            converter.OutputPixelFormat = pylon.PixelType_BGR8packed
            converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
            grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grabResult.GrabSucceeded():
               image = converter.Convert(grabResult)
               self.img = image.GetArray()
               self.image_1  = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY )            
               self.image_2 = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY )
               
               height, width = self.image_1.shape
               step =  width
               qImg = QImage(self.image_1.data, width, height, step,  QImage.Format_Grayscale8)
               self.img_thresold_label.setPixmap(QPixmap.fromImage(qImg))
        else:
            converter = pylon.ImageFormatConverter()
            converter.OutputPixelFormat = pylon.PixelType_BGR8packed
            converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
            grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grabResult.GrabSucceeded():
               image = converter.Convert(grabResult)
               self.img = image.GetArray()
               self.image_1  = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY )            
               self.image_2 = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY )

               height, width = self.image_1.shape
               step =  width
               qImg = QImage(self.image_1.data, width, height, step,  QImage.Format_Grayscale8)
               self.img_thresold_label.setPixmap(QPixmap.fromImage(qImg))

    def processing_image_camera(self):
        print("processing_image_camera")
        self.dir_image_raw = os.getcwd()+"/image_raw"
        self.dir_image_raw = self.dir_image_raw.rstrip()
        self.dir_image_processed = os.getcwd()+"/image_processed"
        self.dir_image_processed = self.dir_image_processed.rstrip()
        count_img_raw_saved = len(os.listdir(self.dir_image_raw))
        count_img_raw_saved = count_img_raw_saved + 1
 
        #save image
        if (count_img_raw_saved <10):
            self.name = "000"+str(count_img_raw_saved)
        elif (count_img_raw_saved < 100):
            self.name = "00"+str(count_img_raw_saved)
        elif (count_img_raw_saved < 1000):
            self.name = "0"+str(count_img_raw_saved)
        else:
            self.name = str(count_img_raw_saved)
        name_save = self.dir_image_raw+"/"+self.name+".bmp"
        cv2.imwrite(name_save,self.image_1)

        if flag_ClaheHistogram == True:
            img_constrast = cv2.imread(name_save)
            self.pre_process_clahe(img_constrast)
            self.checkBox_CLAHE.setChecked(False)
  
        #show image
        self.img = cv2.imread(name_save,0)
        self.img_1=cv2.imread(name_save,0)
        self.img_2=cv2.imread(name_save,0)

        #process image
        self.processing_image()


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
        
        #process image
        #self.processing_image()
###############################################Enhance image####################################
    def pre_process_clahe(self,image):
        global flag_Camera_Open
        global CLAHE_LIMIT

        if flag_Camera_Open == True:
            name_image = self.dir_image_raw+"/"+self.name + ".bmp"
        else:
            self.name = self.comboBox_listImage.currentText()
            name_image = self.dir_image_raw+"/"+self.name + ".bmp"

        CLAHE_LIMIT = int(self.lineEdit_clahe.text())
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        clahe = cv2.createCLAHE(CLAHE_LIMIT, (8,8))
        dst = clahe.apply(gray)
        cv2.imwrite(name_image, dst)

###############################################CONTOURS#########################################
    def remove_are_less_more(self,image,num):
        global flag_Camera_Open
        if flag_Camera_Open == True:
            name_image = self.dir_image_processed+"/"+self.name +"process"+ ".bmp"
        else:
            self.name = self.comboBox_listImage.currentText()
            name_image = self.dir_image_processed+"/"+self.name + "process"+ ".bmp"

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
        cv2.imwrite(name_image,image)

    def caculate_contourArea(self,image):
        contour,hierarchy = cv2.findContours( image , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        area = 0
        min=999999
        max=0
        for i in range(len(contour)):
            if cv2.contourArea(contour[i])>10:
                if cv2.contourArea(contour[i])>max:
                    max=cv2.contourArea(contour[i])
                if cv2.contourArea(contour[i])<min:
                    min=cv2.contourArea(contour[i])
                area += cv2.contourArea(contour[i])
        if min == 999999:
            min = 0
        self.tableWidget.setItem(1,1,QTableWidgetItem(str(len(contour))))
        self.tableWidget.setItem(2,1,QTableWidgetItem(str(area)))
        self.tableWidget.setItem(3,1,QTableWidgetItem(str(max)))
        self.tableWidget.setItem(4,1,QTableWidgetItem(str(min)))
        return len(contour)

    def draw_contours(self,image):
        global flag_Camera_Open
        if flag_Camera_Open == True:
            name_image = self.dir_image_processed+"/"+self.name +"process"+ ".bmp"
        else:
            self.name = self.comboBox_listImage.currentText()
            name_image = self.dir_image_processed+"/"+self.name + "process"+ ".bmp"

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(image, contours, -1, (0, 0, 255), 1)
        #print('write_area')
        for i in range(len(contours)):
            #print(cv2.contourArea(contours[i]))
            cnt = contours[i]
            M = cv2.moments(cnt)
            if M['m00'] == 0:
                break
            else:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.putText(image,str(cv2.contourArea(contours[i])),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,.5,(0,255,0),1,cv2.LINE_AA)
        cv2.imwrite(name_image,image)

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

        global flag_Camera_Open
        global cnt_NG
        global cnt_OK

        if flag_Camera_Open == True:
            name_image = self.dir_image_processed+"/"+self.name +"process"+ ".bmp"
            name_image_origin_cut = self.dir_image_processed +"/"+ self.name+"origin_cut"+".bmp"
        else:
            self.name = self.comboBox_listImage.currentText()
            name_image = self.dir_image_processed+"/"+self.name + "process"+ ".bmp"
            name_image_origin_cut = self.dir_image_processed +"/"+ self.name+"origin_cut"+".bmp"

        self.img_process = cv2.imread(name_image,0)        
        if flag_RemoveArea == True:
            global REMOVE_ARE
            REMOVE_ARE = int(self.lineEdit_removeAREA.text())
            self.remove_are_less_more(self.img_process,REMOVE_ARE)

        flag_error = self.caculate_contourArea(self.img_process)
        self.img_process = cv2.imread(name_image)
        if flag_DrawArea == True:  
            self.draw_contours(self.img_process)

        self.img_process = cv2.imread(name_image)
        self.show_img_processed(self.img_process)

        self.img_settext = cv2.imread(name_image_origin_cut)
        if flag_error > 0:
            self.label_stt_OK_NG.setText("NG")
            self.label_stt_OK_NG.setStyleSheet("background: red")
            cnt_NG = cnt_NG + 1
            self.cnt_NG.setText(str(cnt_NG))
            cv2.putText(self.img_settext, 'NG', (40,120), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 3, cv2.LINE_AA)
            cv2.imwrite(name_image_origin_cut,self.img_settext)
        else:
            self.label_stt_OK_NG.setText("OK")
            self.label_stt_OK_NG.setStyleSheet("background: green")
            cnt_OK = cnt_OK + 1
            self.cnt_OK.setText(str(cnt_OK))

            cv2.putText(self.img_settext, 'OK', (40,120), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 3, cv2.LINE_AA)
            cv2.imwrite(name_image_origin_cut,self.img_settext)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
