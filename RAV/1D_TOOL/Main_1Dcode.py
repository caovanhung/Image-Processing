import sys
import os
import configparser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal

from I_1Dcode import Ui_Class_1Dcode
from Main_DlogDC_1Dcode import Class_DlogDC_1Dcode
from Main_DlogJC_1Dcode import Class_DlogJC_1Dcode

config = configparser.ConfigParser()
config.add_section("1D")
config.read("config/setting.ini")

class Class_1Dcode(QDialog):

    def __init__(self, parent, *args):
        super(Class_1Dcode, self).__init__(*args)

        #Declare variable for Main
        self.FormMain = QtWidgets.QWidget()
        self.var_Ui_1Dcode = Ui_Class_1Dcode()
        self.var_Ui_1Dcode.setupUi(self.FormMain)


        #Declare variable for DlogDC
        self.var_UiDlog_DC_1D = Class_DlogDC_1Dcode(self)

        #Declare variable for DlogJC
        self.var_UiDlog_JC_1D = Class_DlogJC_1Dcode(self)


        #Action in Main
        self.var_Ui_1Dcode.btn_selectEditTool_ModGuiMain.clicked.connect(self.hiden_settup)
        self.var_Ui_1Dcode.btn_Ok_setupTool_ModGuiMain.clicked.connect(self.showAndsave_setup)
        self.var_Ui_1Dcode.btn_Cancel_setupTool_ModGuiMain.clicked.connect(self.show_setup)

        self.var_Ui_1Dcode.btn_DetecCondi_setupTool_ModGuiMain.clicked.connect(self.func_open_DlogDC_1D)


        #Action in Main_DlogDC
        self.var_UiDlog_DC_1D.var_signal_DC.connect(self.func_updateSetting_DC)

        self.var_UiDlog_DC_1D.var_Ui_DC_1Dcode.btn_Cancel_DC_TableSetting.clicked.connect(self.var_UiDlog_DC_1D.func_close_DC_1Dcode)
        self.var_UiDlog_DC_1D.var_Ui_DC_1Dcode.btn_Ok_DC_TableSetting.clicked.connect(self.var_UiDlog_DC_1D.func_close_DC_1Dcode)


####################################################Func for Main####################################################
    def hiden_settup(self):
        self.var_Ui_1Dcode.frame_setupToolDetail_ModGuiMain.setHidden(True)
        self.var_Ui_1Dcode.frame_SettingGeneral_ModGuiMain.setHidden(False)

        self.var_Ui_1Dcode.combox_CodeType_setupTool_ModGuiMain.setCurrentText(config.get("1D", "CodeType"))
        self.var_Ui_1Dcode.lab_showPixel_DetecCond_setupTool.setText(config.get("1D", "ValueCodeResulation"))
        #self.var_UiDlog_DC_1D.func_loadDataSetup_DC()
        #self.var_UiDlog_DC_1D.func_showSetupLoading_DC()

    def show_setup(self):
        self.var_Ui_1Dcode.frame_setupToolDetail_ModGuiMain.setHidden(False)
        self.var_Ui_1Dcode.frame_SettingGeneral_ModGuiMain.setHidden(True)

    #Function loading_show data setting form setting.conf and save data setting of Codetype_DC_1D
    def showAndsave_setup(self):
        self.var_Ui_1Dcode.frame_setupToolDetail_ModGuiMain.setHidden(False)
        self.var_Ui_1Dcode.frame_SettingGeneral_ModGuiMain.setHidden(True)
        self.var_UiDlog_DC_1D.func_saveDataSetting_DC()
        self.func_saveDataSetting_DC_1D()

    #function update setting CodeType and ValueCodeResulation of DC(extend) for DC_1D
    def func_updateSetting_DC(self, var_CodeType_DC, var_ValueCodeResulation):
        self.var_CodeType_DC_1D = var_CodeType_DC  	
        self.var_ValueCodeResulation_DC_1D = var_ValueCodeResulation
        self.var_Ui_1Dcode.lab_showPixel_DetecCond_setupTool.setText(self.var_ValueCodeResulation_DC_1D)
        self.var_Ui_1Dcode.combox_CodeType_setupTool_ModGuiMain.setCurrentText(self.var_CodeType_DC_1D)

    #Function save setting Codetype_DC_1D into the setting.ini
    def func_saveDataSetting_DC_1D(self):
        self.var_CodeType_DC_1D = self.var_Ui_1Dcode.combox_CodeType_setupTool_ModGuiMain.currentText()
        config.set("1D", "CodeType", self.var_CodeType_DC_1D)
        config.write(open("config/setting.ini", "w"))

    def func_open_DlogDC_1D(self):
        self.func_saveDataSetting_DC_1D()
        self.var_UiDlog_DC_1D.func_loadDataSetup_DC()
        self.var_UiDlog_DC_1D.func_showSetupLoading_DC()
        self.var_UiDlog_DC_1D.func_show_DC_1Dcode()



###################################################################################################################
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = Class_1Dcode(None)
    application.FormMain.show()
    sys.exit(app.exec())

