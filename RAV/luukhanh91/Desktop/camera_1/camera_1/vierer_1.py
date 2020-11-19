from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
    qApp, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import  os
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 421, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imageLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.imageLabel .setObjectName("label")
      #  self.verticalLayout.addWidget(self.label)
       # MainWindow.setCentralWidget(self.centralwidget)
     #   self.imageLabel.setBackgroundRole(QtGui.QPalette.Base)
     #   self.imageLabel.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
      #  self.imageLabel.setScaledContents(True)

      #  self.scrollArea = QScrollArea()
      #  self.scrollArea.setBackgroundRole(QPalette.Dark)
      #  self.scrollArea.setWidget(self.imageLabel)
       # self.scrollArea.setVisible(False)
      #  self.scrollArea.setWidgetResizable(True)
       # MainWindow.setCentralWidget(self.scrollArea)
        self.Detection_edges_open_img()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
       # self.label.setText(_translate("MainWindow", "TextLabel"))

    def Detection_edges_open_img(self):
        file_goc=os.getcwd()
       # self.ten=self.Image_comboBox.currentText()
        file_config=file_goc.replace("/detection_edges","")
        self.file_img=file_config+"/"+"01.jpg"
      #  print(file_img)
        self.img=cv2.imread(self.file_img,1)
       # self.img_1=cv2.imread(self.file_img,1)
       # self.img=cv2.resize(self.img,(601, 531))
       # self.img_1=cv2.resize(self.img_1,(601, 531))
       # self.img_0=cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
       # self.img_10=cv2.cvtColor(self.img_1, cv2.COLOR_BGR2GRAY)
        print (self.img)
        height, width,channel = self.img.shape
        step =  width*channel
        qImg = QImage(self.img.data, width, height, step, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.imageLabel.setPixmap(QPixmap.fromImage(qImg))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

