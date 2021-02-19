from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import configparser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from I_DlogDC_1Dcode import Ui_Class_DlogDC_1Dcode

config = configparser.ConfigParser()
config.add_section("1D")
config.read("config/setting.ini")

class Class_DlogDC_1Dcode(QDialog):
    var_signal_DC = pyqtSignal(str,str)

    def __init__(self, parent, *args):
        super(Class_DlogDC_1Dcode, self).__init__(*args)
        self.var_Ui_DC_1Dcode=Ui_Class_DlogDC_1Dcode()
        self.var_Ui_DC_1Dcode.setupUi(self)

        self.var_Ui_DC_1Dcode.btn_Ok_DC_TableSetting.clicked.connect(self.func_createSignal_DC_1Dcode)
        

    def func_createSignal_DC_1Dcode(self):
        #self.var_CodeType = config.get("1D", "CodeType")
        self.var_CodeType_ = self.var_Ui_DC_1Dcode.combox_CodeType_DC_TableSetting.currentText()
        self.var_ReferecContrast = self.var_Ui_DC_1Dcode.combox_ReferenceConstrast_DC_TableSetting.currentText()
        self.var_CodeColor = self.var_Ui_DC_1Dcode.combox_CodeColor_DC_TableSetting.currentText()
        self.var_ScaleVariation = self.var_Ui_DC_1Dcode.combox_ScaleVariation_DC_TableSetting.currentText()

        self.var_checkCodeResulation = self.var_Ui_DC_1Dcode.cbox_CodeResulation_DC_TableSetting.checkState()
        self.var_checkReferenContrast = self.var_Ui_DC_1Dcode.cbox_ReferenceConstrast_DC_TableSetting.checkState()
        self.var_checkNumberReadDigit = self.var_Ui_DC_1Dcode.cbox_NumberOfReadDigit_DC_TableSetting.checkState()      
        self.var_checkCodeColor = self.var_Ui_DC_1Dcode.cbox_CodeColor_DC_TableSetting.checkState()
        self.var_checkBaseAngle = self.var_Ui_DC_1Dcode.cbox_BaseAngle_DC_TableSetting.checkState()
        self.var_checkEnableCheckDigit = self.var_Ui_DC_1Dcode.cbox_EnableCheckDigit_DC_TableSetting.checkState()

        self.var_ValueCodeResulation = self.var_Ui_DC_1Dcode.ledit_CodeResulation_DC_TableSetting.text()
        self.var_ValueMinNumberReadDigit = self.var_Ui_DC_1Dcode.ledit_MinNumberReadDigit_DC_TableSetting.text()
        self.var_ValueMaxNumberReadDigit = self.var_Ui_DC_1Dcode.ledit_MaxNumberReadDigit_DC_TableSetting.text()
        self.var_ValueBaseAngle = self.var_Ui_DC_1Dcode.ledit_BaseAngle_DC_TableSetting.text()
        self.var_ValueTimeOut = self.var_Ui_DC_1Dcode.ledit_TimeOut_DC_TableSetting.text()
        self.var_signal_DC.emit(self.var_CodeType_, self.var_ValueCodeResulation)


####################################################Func for DC####################################################
	#Show GUI of table setting DC_1D
    def func_show_DC_1Dcode(self):
        self.show()

    #Close GUI of table setting DC_1D
    def func_close_DC_1Dcode(self):
        self.close()    

    #Save data for Setting of DC
    def func_saveDataSetting_DC(self):
        config.set("1D", "CodeType", self.var_CodeType)
        config.set("1D", "ReferecContrast", self.var_ReferecContrast)
        config.set("1D", "CodeColor", self.var_CodeColor)
        config.set("1D", "ScaleVariation", self.var_ScaleVariation)

        config.set("1D", "checkCodeResulation", str(self.var_checkCodeResulation))
        config.set("1D", "checkReferenContrast", str(self.var_checkReferenContrast))
        config.set("1D", "checkNumberReadDigit", str(self.var_checkNumberReadDigit))
        config.set("1D", "checkCodeColor", str(self.var_checkCodeColor))
        config.set("1D", "checkBaseAngle", str(self.var_checkBaseAngle))
        config.set("1D", "checkEnableCheckDigit", str(self.var_checkEnableCheckDigit))

        config.set("1D", "ValueCodeResulation", self.var_ValueCodeResulation)
        config.set("1D", "ValueMinNumberReadDigit", self.var_ValueMinNumberReadDigit)
        config.set("1D", "ValueMaxNumberReadDigit", self.var_ValueMaxNumberReadDigit)
        config.set("1D", "ValueBaseAngle", self.var_ValueBaseAngle)
        config.set("1D", "ValueTimeOut", self.var_ValueTimeOut)

        config.write(open("config/setting.ini", "w"))

    #Load data for Setup from file config of DC    
    def func_loadDataSetup_DC(self):

        self.var_CodeType = config.get("1D", "CodeType")
        self.var_ReferecContrast = config.get("1D", "ReferecContrast")
        self.var_CodeColor = config.get("1D", "CodeColor")
        self.var_ScaleVariation = config.get("1D", "ScaleVariation")

        self.var_checkCodeResulation = config.get("1D", "checkCodeResulation")
        self.var_checkReferenContrast = config.get("1D", "checkReferenContrast")
        self.var_checkNumberReadDigit = config.get("1D", "checkNumberReadDigit")
        self.var_checkCodeColor = config.get("1D", "checkCodeColor")
        self.var_checkBaseAngle = config.get("1D", "checkBaseAngle")
        self.var_checkEnableCheckDigit = config.get("1D", "checkEnableCheckDigit")

        self.var_ValueCodeResulation = config.get("1D", "ValueCodeResulation")
        self.var_ValueMinNumberReadDigit = config.get("1D", "ValueMinNumberReadDigit")
        self.var_ValueMaxNumberReadDigit = config.get("1D", "ValueMaxNumberReadDigit")
        self.var_ValueBaseAngle = config.get("1D", "ValueBaseAngle")
        self.var_ValueTimeOut = config.get("1D", "ValueTimeOut")


    #Setting for DC of Data load from file config
    def func_showSetupLoading_DC(self):
        self.var_Ui_DC_1Dcode.combox_CodeType_DC_TableSetting.setCurrentText(self.var_CodeType)
        self.var_Ui_DC_1Dcode.combox_ReferenceConstrast_DC_TableSetting.setCurrentText(self.var_ReferecContrast)
        self.var_Ui_DC_1Dcode.combox_CodeColor_DC_TableSetting.setCurrentText(self.var_CodeColor)
        self.var_Ui_DC_1Dcode.combox_ScaleVariation_DC_TableSetting.setCurrentText(self.var_ScaleVariation)

        self.var_Ui_DC_1Dcode.ledit_CodeResulation_DC_TableSetting.setText(self.var_ValueCodeResulation)
        self.var_Ui_DC_1Dcode.ledit_MinNumberReadDigit_DC_TableSetting.setText(self.var_ValueMinNumberReadDigit)
        self.var_Ui_DC_1Dcode.ledit_MaxNumberReadDigit_DC_TableSetting.setText(self.var_ValueMaxNumberReadDigit)
        self.var_Ui_DC_1Dcode.ledit_BaseAngle_DC_TableSetting.setText(self.var_ValueBaseAngle)
        self.var_Ui_DC_1Dcode.ledit_TimeOut_DC_TableSetting.setText(self.var_ValueTimeOut)


        if self.var_checkCodeResulation == "2":
            self.var_Ui_DC_1Dcode.cbox_CodeResulation_DC_TableSetting.setChecked(True)
        else:
            self.var_Ui_DC_1Dcode.cbox_CodeResulation_DC_TableSetting.setChecked(False)

        if self.var_checkReferenContrast == "2":
            self.var_Ui_DC_1Dcode.cbox_ReferenceConstrast_DC_TableSetting.setChecked(True)
        else:
            self.var_Ui_DC_1Dcode.cbox_ReferenceConstrast_DC_TableSetting.setChecked(False)

        if self.var_checkNumberReadDigit == "2":
            self.var_Ui_DC_1Dcode.cbox_NumberOfReadDigit_DC_TableSetting.setChecked(True)
        else:
            self.var_Ui_DC_1Dcode.cbox_NumberOfReadDigit_DC_TableSetting.setChecked(False)        

        if self.var_checkCodeColor == "2":
            self.var_Ui_DC_1Dcode.cbox_CodeColor_DC_TableSetting.setChecked(True)
        else:
            self.var_Ui_DC_1Dcode.cbox_CodeColor_DC_TableSetting.setChecked(False)

        if self.var_checkBaseAngle == "2":
            self.var_Ui_DC_1Dcode.cbox_BaseAngle_DC_TableSetting.setChecked(True)
        else:
            self.var_Ui_DC_1Dcode.cbox_BaseAngle_DC_TableSetting.setChecked(False)

        if self.var_checkEnableCheckDigit == "2":
            self.var_Ui_DC_1Dcode.cbox_EnableCheckDigit_DC_TableSetting.setChecked(True)
        else:
            self.var_Ui_DC_1Dcode.cbox_EnableCheckDigit_DC_TableSetting.setChecked(False)