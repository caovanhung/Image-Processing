import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt

class Windo(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(150,250,500,500)
        self.setWindowTitle("Ammyyy")
        self.setWindowIcon(QtGui.QIcon('a.jpeg'))

        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()

        self.show()

    def paintEvent(self,event):
        qp = QPainter(self)
        qp.begin(self)
        qp.setPen(QPen(Qt.black, 2, Qt.SolidLine))

        qp.drawRect(QtCore.QRect(self.begin, self.end))
        qp.drawEllipse(QtCore.QRect(self.begin, self.end))

        qp.end()

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()

app = QApplication(sys.argv)
win = Windo()
sys.exit(app.exec_())
