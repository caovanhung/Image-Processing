import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QScrollArea
from PyQt5.QtGui import QPixmap


class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        main_widget = QWidget(self)

        btn = QPushButton("Bye", self)
        btn.clicked.connect(self.close)

        img = QPixmap("01.jpg")
        label = QLabel(main_widget)
        label.setPixmap(img)

        scrollArea = QScrollArea(main_widget)
        scrollArea.setWidgetResizable(True) 
        scrollArea.setWidget(label)

        l = QVBoxLayout(main_widget)
        l.addWidget(scrollArea)
       # l.addWidget(btn)

        self.setCentralWidget(main_widget)


    def closeEvent(self, ce):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    aw = ApplicationWindow()
    aw.show()
    app.exec_()
