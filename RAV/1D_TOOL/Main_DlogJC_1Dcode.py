from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from I_DlogJC_1Dcode import Ui_Class_DlogJC_1Dcode


class Class_DlogJC_1Dcode(QDialog):
    def __init__(self, parent, *args):
        super(Class_DlogJC_1Dcode, self).__init__(*args)
        self.var_Ui_JC_1Dcode=Ui_Class_DlogJC_1Dcode()
        self.var_Ui_JC_1Dcode.setupUi(self)
