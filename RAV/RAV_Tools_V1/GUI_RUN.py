from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QRect
import sys
import cv2
from pypylon import pylon

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())


class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent) #ham cua lop cha
 
        self.timer_camera = QtCore.QTimer() #xac dinh timer de kiem soat toc do khung hinh cua video 
        self.CAM_NUM = 0                    # = 0 co ngia la luong video den tu camera laptop
 
        self.set_ui()                       #Khoi tao giao dien
        self.slot_init()                    #khoi tao vi tri
 
    '''bo cuc giao dien chuong trinh'''
    def set_ui(self):
        self.__layout_main = QtWidgets.QHBoxLayout()           #bo cuc chung
        self.__layout_fun_button = QtWidgets.QVBoxLayout()      #viec bo tri nut
        self.__layout_data_show = QtWidgets.QVBoxLayout()       #bo cuc hien thi du lieu(video)
        self.button_open_camera = QtWidgets.QPushButton('Play') #nut nhan de bat may anh
        self.button_close = QtWidgets.QPushButton('Exit')           #nut nhan thoat khoi chuong trinh
        self.button_open_camera.setMinimumHeight(20)                #Kich thuoc nut nhan
        self.button_close.setMinimumHeight(20)
 
        #self.button_close.move(10,100)                      #nut nhan di chuyen
        '''Tin nhan den'''
        self.label_show_camera = QtWidgets.QLabel()   #xac dinh Label de hien thi video
        self.label_show_camera.setFixedSize(1024,700)    #dat kich thuoc label 640x481 de hien thi video 
        '''them nut vao bo cuc nut'''
        self.__layout_fun_button.addWidget(self.button_open_camera) #Dat nut bat may anh vao bo cuc nut
        self.__layout_fun_button.addWidget(self.button_close)       #dat nut thoat may anh vao bo cuc phim
        '''them mot so dieu khien vao bo cuc tong the'''
        self.__layout_main.addLayout(self.__layout_fun_button)      #them bo cuc nut vao bo cuc tong the
        self.__layout_main.addWidget(self.label_show_camera)        #them Label duoc su dung de hien thi video vao bo cuc tong the
        '''sau khi bo cuc tong the duoc sap xep, co the chuyen bo cuc tong the lam tham so cho ham sau'''
        self.setLayout(self.__layout_main) #khi do tat ca cac dieu khien moi duoc hien thi
 
    '''khoi tao tat ca cac chuc nang cua khe'''
    def slot_init(self):
        self.button_open_camera.clicked.connect(self.button_open_camera_clicked)    #neu nut duoc nhan, goi ham button_open_camera_clicked()
        self.timer_camera.timeout.connect(self.show_camera) #Nếu bộ hẹn giờ kết thúc, hãy gọi show_camera()
        self.button_close.clicked.connect(self.close)#neu nut duoc nhan, goi close(). Lenh nay di kem voi QtWidgets.QWidget cua lop cha va se dong chuong trinh
 
    '''mot trong cac chung nang cua khe'''
    def button_open_camera_clicked(self):
        if self.timer_camera.isActive() == False:   #neu bo hen gio ko duoc khoi dong
            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            self.timer_camera.start(30)
            self.button_open_camera.setText("STOP")
        else:
            self.timer_camera.stop()
            camera.StopGrabbing()
            self.button_open_camera.setText("RUN")
 
    def show_camera(self):
        converter = pylon.ImageFormatConverter()
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        
        if grabResult.GrabSucceeded():
            image = converter.Convert(grabResult)
            self.img = image.GetArray()

            show = cv2.resize(self.img,(1024,700))
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
            showImage = QtGui.QImage(show.data,show.shape[1],show.shape[0],QtGui.QImage.Format_RGB888)
            self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))  
if __name__ =='__main__':
    app = QtWidgets.QApplication(sys.argv)  #Ung dung chuong trinh
    ui = Ui_MainWindow()                    #khoi tao Ui_MainWindow
    ui.show()                               #goi show() cua ui hien thi. Cung mot show() co nguon goc tu lop cha QtWidgets.QWidget
    sys.exit(app.exec_())                   