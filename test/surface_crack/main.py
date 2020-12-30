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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)

        self.scrollArea_ShowImage = QtWidgets.QScrollArea(Form)
        self.scrollArea_ShowImage.setGeometry(QtCore.QRect(10, 10, 1000, 800))
        self.scrollArea_ShowImage.setWidgetResizable(True)
        self.scrollArea_ShowImage.setObjectName("scrollArea_ShowImage")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 998, 798))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        #self.scrollArea_ShowImage.setWidget(self.scrollAreaWidgetContents)
        self.img_thresold_label = Threshold_MyLabel()
        self.scrollArea_ShowImage.setBackgroundRole(QPalette.Dark)#THEM DONG
        self.img_thresold_label.setWordWrap(True)
        self.img_thresold_label.setObjectName("label")
        self.scrollArea_ShowImage.setWidget(self.img_thresold_label)


        self.label_stt_OK_NG = QtWidgets.QLabel(Form)
        self.label_stt_OK_NG.setGeometry(QtCore.QRect( 1700, 10 , 100, 100))
        self.label_stt_OK_NG.setStyleSheet("background: green")
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_stt_OK_NG.setFont(font)
        self.label_stt_OK_NG.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stt_OK_NG.setObjectName("label_stt_OK_NG")


        self.btn_Open = QtWidgets.QPushButton(Form)
        self.btn_Open.setGeometry(QtCore.QRect(10, 950, 100, 50))
        self.btn_Open.setObjectName("btn_Open")

        self.box_SelecImage = QtWidgets.QComboBox(Form)
        self.box_SelecImage.setGeometry(QtCore.QRect(160, 950, 100, 50))
        self.box_SelecImage.setObjectName("box_SelecImage")
        self.box_SelecImage.addItem("")
        self.box_SelecImage.addItem("")
        self.box_SelecImage.addItem("")
        self.box_SelecImage.addItem("")

        self.btn_SaveImage = QtWidgets.QPushButton(Form)
        self.btn_SaveImage.setGeometry(QtCore.QRect(310, 950, 100, 50))
        self.btn_SaveImage.setObjectName("btn_SaveImage")

        self.btn_Process = QtWidgets.QPushButton(Form)
        self.btn_Process.setGeometry(QtCore.QRect(460, 950, 100, 50))
        self.btn_Process.setObjectName("btn_Process")

        self.btn_Run = QtWidgets.QPushButton(Form)
        self.btn_Run.setGeometry(QtCore.QRect(610, 950, 100, 50))
        self.btn_Run.setObjectName("btn_Run")

        self.horizontalScrollBar_Thresold = QtWidgets.QScrollBar(Form)
        self.horizontalScrollBar_Thresold.setGeometry(QtCore.QRect(10, 850, 1000, 25))
        self.horizontalScrollBar_Thresold.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_Thresold.setObjectName("horizontalScrollBar_Thresold")
        self.horizontalScrollBar_Thresold.setMaximum(255)
        self.horizontalScrollBar_Thresold.setMinimum(0)

        self.tableWidget_Infor = QtWidgets.QTableWidget(Form)
        self.tableWidget_Infor.setGeometry(QtCore.QRect(1100, 10, 300, 200))
        self.tableWidget_Infor.setObjectName("tableWidget_Infor")
        self.tableWidget_Infor.setColumnCount(2)
        self.tableWidget_Infor.setRowCount(5)
        self.tableWidget_Infor.setItem(0,0,QTableWidgetItem("Threshold"))
        self.tableWidget_Infor.setItem(1,0,QTableWidgetItem("Tong so"))
        self.tableWidget_Infor.setItem(2,0,QTableWidgetItem("Tong dien tich"))
        self.tableWidget_Infor.setItem(3,0,QTableWidgetItem("Dien tich lon nhat"))
        self.tableWidget_Infor.setItem(4,0,QTableWidgetItem("Dien tich nho nhat"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_Open.setText(_translate("Form", "Open"))
        self.btn_SaveImage.setText(_translate("Form", "Save Image"))
        self.btn_Process.setText(_translate("Form", "Xu Ly"))
        self.btn_Run.setText(_translate("Form", "Run"))
        self.box_SelecImage.setItemText(0, _translate("Form", "01"))
        self.box_SelecImage.setItemText(1, _translate("Form", "02"))
        self.box_SelecImage.setItemText(2, _translate("Form", "03"))
        self.box_SelecImage.setItemText(3, _translate("Form", "04"))
        self.box_SelecImage.setItemText(4, _translate("Form", "05"))


        self.btn_Open.clicked.connect(self.open_image)
        self.btn_SaveImage.clicked.connect(self.save_image_Thresholded)
        self.btn_Process.clicked.connect(self.processing_image)

        self.horizontalScrollBar_Thresold.sliderMoved.connect(self.Threshold_bar)
        self.horizontalScrollBar_Thresold.setEnabled(1)

        self.label_stt_OK_NG.setText(_translate("Form", "OK"))


    def open_image(self):
        self.name_of_image = self.box_SelecImage.currentText()
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
        self.btn_Open.setEnabled(1)
        self.horizontalScrollBar_Thresold.setEnabled(1)
        self.box_SelecImage.setEnabled(1)

    def save_image_Thresholded(self):
        self.name_of_image = self.box_SelecImage.currentText()
        image = self.name_of_image + ".bmp"

        self.img_luu=cv2.imread(image,0)
        self.Threshold_bar()

        self.file_img_bandau = self.name_of_image+"dau"+".bmp"
        self.file_img = self.name_of_image + "cat"+".bmp"
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

            self.thresh_value=self.horizontalScrollBar_Thresold.value()
            self.tableWidget_Infor.setItem(0,1,QTableWidgetItem(str(self.thresh_value)))

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
        self.name_of_image = self.box_SelecImage.currentText()
        name = self.name_of_image +"cat"+".bmp"
        name1 = self.name_of_image +'removed'+'.bmp'

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
        cv2.imwrite(name1,image)

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
        self.tableWidget_Infor.setItem(1,1,QTableWidgetItem(str(len(contour))))
        self.tableWidget_Infor.setItem(2,1,QTableWidgetItem(str(area)))
        self.tableWidget_Infor.setItem(3,1,QTableWidgetItem(str(max)))
        self.tableWidget_Infor.setItem(4,1,QTableWidgetItem(str(min)))
        return len(contour)

    def draw_contours(self,image):
        self.name_of_image = self.box_SelecImage.currentText()
        name = self.name_of_image +'cat'+'.bmp'
        name1 = self.name_of_image +'drawed'+'.bmp'

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
        cv2.imwrite(name1,image)


    def show_img_processed(self,image):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = img.shape
        step = channel * width
        qImg = QImage(img.data, width, height, step, QImage.Format_RGB888)
        self.img_thresold_label.setPixmap(QPixmap.fromImage(qImg))
        self.img_thresold_label.setCursor(QtCore.Qt.CrossCursor)
        self.img_thresold_label.setfdk(1)

    def processing_image(self):
        flag_error = 0
        self.name_of_image = self.box_SelecImage.currentText()
        name = self.name_of_image +'cat'+'.bmp'
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
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
