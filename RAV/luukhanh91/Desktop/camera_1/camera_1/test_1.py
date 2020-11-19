from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import cv2

from register import *


class register_dialog(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_dialog=Ui_register_Dialog()
        self.ui_dialog.setupUi(self)
        self.timer = QTimer()
        self.ui_dialog.re_Save_pushButton.clicked.connect(self.save_img)
        #self.ui_dialog.Close_pushButton.clicked.connect(self.ui_dialog.rejected)
        # set timer timeout callback function
       # self.ui_dialog.closeEvent = self.CloseEvent
        #self.ui_dialog.register_Dialog.close_event=self.close_event
        self.timer.timeout.connect(self.viewCam_1)
        self.controlTimer()
        
        
    def viewCam_1(self):

        #cap = cv2.VideoCapture(0)
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        self.image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui_dialog.re_img_label.setPixmap(QPixmap.fromImage(qImg))

    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
    def save_img(self):
        ten=self.ui_dialog.comboBox.currentText()
        ret, image = self.cap.read()
        file_img=ten+".jpg"
        
        cv2.imwrite(file_img,image)
 
   # def CloseEvent(self, event):
      #  print("X is clicked")
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui_register = register_dialog()
   
   # self.ui_register.setupUi(self.register_Dialog)
    ui_register.show()
    sys.exit(app.exec_())
