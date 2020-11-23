from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QTimer
from demoCemera import *

import sys
import cv2
from pypylon import pylon

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

class MyForm(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.timer_camera = QtCore.QTimer()
		self.ui.btn_Click_Run.clicked.connect(self.button_open_camera_clicked)
		self.timer_camera.timeout.connect(self.show_camera) #Nếu bộ hẹn giờ kết thúc, hãy gọi show_camera()
		self.show()



	def button_open_camera_clicked(self):
		if self.timer_camera.isActive() == False:   #neu bo hen gio ko duoc khoi dong
			camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
			self.timer_camera.start(30)
			self.ui.btn_Click_Run.setText("STOP")
		else:
			self.timer_camera.stop()
			camera.StopGrabbing()
			self.ui.btn_Click_Run.setText("RUN")

	def show_camera(self):
		converter = pylon.ImageFormatConverter()
		converter.OutputPixelFormat = pylon.PixelType_BGR8packed
		converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
		grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

		if grabResult.GrabSucceeded():
			image = converter.Convert(grabResult)
			img = image.GetArray()

			show = cv2.resize(img,(480,320))
			show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
			showImage = QtGui.QImage(show.data,show.shape[1],show.shape[0],QtGui.QImage.Format_RGB888)
			self.ui.label_Show_Image.setPixmap(QtGui.QPixmap.fromImage(showImage))  

if __name__=="__main__":
	app = QApplication(sys.argv)
	w = MyForm()
	w.show()
	sys.exit(app.exec_())