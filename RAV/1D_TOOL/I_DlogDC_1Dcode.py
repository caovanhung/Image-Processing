from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Class_DlogDC_1Dcode(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #Dialog.move(1920-1252+60, 310)
        Dialog.move(1920 - 1236 + 60, 310)
        Dialog.resize(1160, 700)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_DC_TableSetting = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_DC_TableSetting.sizePolicy().hasHeightForWidth())
        self.frame_DC_TableSetting.setSizePolicy(sizePolicy)
        self.frame_DC_TableSetting.setMinimumSize(QtCore.QSize(400, 700))
        self.frame_DC_TableSetting.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_DC_TableSetting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_DC_TableSetting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_DC_TableSetting.setObjectName("frame_DC_TableSetting")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_DC_TableSetting)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lab_NoImport_1 = QtWidgets.QLabel(self.frame_DC_TableSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_NoImport_1.sizePolicy().hasHeightForWidth())
        self.lab_NoImport_1.setSizePolicy(sizePolicy)
        self.lab_NoImport_1.setMinimumSize(QtCore.QSize(0, 50))
        self.lab_NoImport_1.setStyleSheet("background-color: rgb(0, 58, 88);\n"
"color: rgb(255, 255, 255);")
        self.lab_NoImport_1.setObjectName("lab_NoImport_1")
        self.verticalLayout.addWidget(self.lab_NoImport_1)
        self.scroll_AreaSettong_DC_TableSetting = QtWidgets.QScrollArea(self.frame_DC_TableSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_AreaSettong_DC_TableSetting.sizePolicy().hasHeightForWidth())
        self.scroll_AreaSettong_DC_TableSetting.setSizePolicy(sizePolicy)
        self.scroll_AreaSettong_DC_TableSetting.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.scroll_AreaSettong_DC_TableSetting.setWidgetResizable(True)
        self.scroll_AreaSettong_DC_TableSetting.setObjectName("scroll_AreaSettong_DC_TableSetting")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 616, 594))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lab_NoImport_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_NoImport_8.sizePolicy().hasHeightForWidth())
        self.lab_NoImport_8.setSizePolicy(sizePolicy)
        self.lab_NoImport_8.setMinimumSize(QtCore.QSize(0, 30))
        self.lab_NoImport_8.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.lab_NoImport_8.setObjectName("lab_NoImport_8")
        self.verticalLayout_3.addWidget(self.lab_NoImport_8)
        self.frame_CopyType_DC_TableSetting = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_CopyType_DC_TableSetting.sizePolicy().hasHeightForWidth())
        self.frame_CopyType_DC_TableSetting.setSizePolicy(sizePolicy)
        self.frame_CopyType_DC_TableSetting.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_CopyType_DC_TableSetting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_CopyType_DC_TableSetting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_CopyType_DC_TableSetting.setObjectName("frame_CopyType_DC_TableSetting")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_CopyType_DC_TableSetting)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lab_NoImport_2 = QtWidgets.QLabel(self.frame_CopyType_DC_TableSetting)
        self.lab_NoImport_2.setObjectName("lab_NoImport_2")
        self.horizontalLayout_10.addWidget(self.lab_NoImport_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.combox_CodeType_DC_TableSetting = QtWidgets.QComboBox(self.frame_CopyType_DC_TableSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combox_CodeType_DC_TableSetting.sizePolicy().hasHeightForWidth())
        self.combox_CodeType_DC_TableSetting.setSizePolicy(sizePolicy)
        self.combox_CodeType_DC_TableSetting.setMinimumSize(QtCore.QSize(100, 0))
        self.combox_CodeType_DC_TableSetting.setObjectName("combox_CodeType_DC_TableSetting")
        self.horizontalLayout_10.addWidget(self.combox_CodeType_DC_TableSetting)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.verticalLayout_3.addWidget(self.frame_CopyType_DC_TableSetting)
        self.lab_NoImport_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_NoImport_6.sizePolicy().hasHeightForWidth())
        self.lab_NoImport_6.setSizePolicy(sizePolicy)
        self.lab_NoImport_6.setMinimumSize(QtCore.QSize(0, 30))
        self.lab_NoImport_6.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.lab_NoImport_6.setObjectName("lab_NoImport_6")
        self.verticalLayout_3.addWidget(self.lab_NoImport_6)
        self.frame_TurningParameter_DC_TableSetting = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_TurningParameter_DC_TableSetting.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_TurningParameter_DC_TableSetting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_TurningParameter_DC_TableSetting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_TurningParameter_DC_TableSetting.setObjectName("frame_TurningParameter_DC_TableSetting")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_TurningParameter_DC_TableSetting)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 5, 10, 5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.btn_AutoTurning_DC_TableSetting = QtWidgets.QPushButton(self.frame_TurningParameter_DC_TableSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_AutoTurning_DC_TableSetting.sizePolicy().hasHeightForWidth())
        self.btn_AutoTurning_DC_TableSetting.setSizePolicy(sizePolicy)
        self.btn_AutoTurning_DC_TableSetting.setMinimumSize(QtCore.QSize(100, 0))
        self.btn_AutoTurning_DC_TableSetting.setObjectName("btn_AutoTurning_DC_TableSetting")
        self.horizontalLayout_6.addWidget(self.btn_AutoTurning_DC_TableSetting)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(10, 5, -1, 5)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lab_NoImport_5 = QtWidgets.QLabel(self.frame_TurningParameter_DC_TableSetting)
        self.lab_NoImport_5.setObjectName("lab_NoImport_5")
        self.horizontalLayout_11.addWidget(self.lab_NoImport_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(20, 5, -1, 5)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.cbox_CodeResulation_DC_TableSetting = QtWidgets.QCheckBox(self.frame_TurningParameter_DC_TableSetting)
        self.cbox_CodeResulation_DC_TableSetting.setObjectName("cbox_CodeResulation_DC_TableSetting")
        self.horizontalLayout_12.addWidget(self.cbox_CodeResulation_DC_TableSetting)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 5, 10, 5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.ledit_CodeResulation_DC_TableSetting = QtWidgets.QLineEdit(self.frame_TurningParameter_DC_TableSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_CodeResulation_DC_TableSetting.sizePolicy().hasHeightForWidth())
        self.ledit_CodeResulation_DC_TableSetting.setSizePolicy(sizePolicy)
        self.ledit_CodeResulation_DC_TableSetting.setMinimumSize(QtCore.QSize(100, 0))
        self.ledit_CodeResulation_DC_TableSetting.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ledit_CodeResulation_DC_TableSetting.setText("")
        self.ledit_CodeResulation_DC_TableSetting.setAlignment(QtCore.Qt.AlignCenter)
        self.ledit_CodeResulation_DC_TableSetting.setDragEnabled(False)
        self.ledit_CodeResulation_DC_TableSetting.setObjectName("ledit_CodeResulation_DC_TableSetting")
        self.horizontalLayout_3.addWidget(self.ledit_CodeResulation_DC_TableSetting)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(20, 5, 10, 5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.cbox_ReferenceConstrast_DC_TableSetting = QtWidgets.QCheckBox(self.frame_TurningParameter_DC_TableSetting)
        self.cbox_ReferenceConstrast_DC_TableSetting.setObjectName("cbox_ReferenceConstrast_DC_TableSetting")
        self.horizontalLayout_8.addWidget(self.cbox_ReferenceConstrast_DC_TableSetting)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.combox_ReferenceConstrast_DC_TableSetting = QtWidgets.QComboBox(self.frame_TurningParameter_DC_TableSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combox_ReferenceConstrast_DC_TableSetting.sizePolicy().hasHeightForWidth())
        self.combox_ReferenceConstrast_DC_TableSetting.setSizePolicy(sizePolicy)
        self.combox_ReferenceConstrast_DC_TableSetting.setMinimumSize(QtCore.QSize(100, 0))
        self.combox_ReferenceConstrast_DC_TableSetting.setObjectName("combox_ReferenceConstrast_DC_TableSetting")
        self.horizontalLayout_8.addWidget(self.combox_ReferenceConstrast_DC_TableSetting)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(20, 5, 10, 5)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.cbox_NumberOfReadDigit_DC_TableSetting = QtWidgets.QCheckBox(self.frame_TurningParameter_DC_TableSetting)
        self.cbox_NumberOfReadDigit_DC_TableSetting.setObjectName("cbox_NumberOfReadDigit_DC_TableSetting")
        self.horizontalLayout_19.addWidget(self.cbox_NumberOfReadDigit_DC_TableSetting)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(self.frame_TurningParameter_DC_TableSetting)
        self.label.setObjectName("label")
        self.horizontalLayout_19.addWidget(self.label)
        self.ledit_MinNumberReadDigit_DC_TableSetting = QtWidgets.QLineEdit(self.frame_TurningParameter_DC_TableSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_MinNumberReadDigit_DC_TableSetting.sizePolicy().hasHeightForWidth())
        self.ledit_MinNumberReadDigit_DC_TableSetting.setSizePolicy(sizePolicy)
        self.ledit_MinNumberReadDigit_DC_TableSetting.setMinimumSize(QtCore.QSize(50, 0))
        self.ledit_MinNumberReadDigit_DC_TableSetting.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ledit_MinNumberReadDigit_DC_TableSetting.setAlignment(QtCore.Qt.AlignCenter)
        self.ledit_MinNumberReadDigit_DC_TableSetting.setObjectName("ledit_MinNumberReadDigit_DC_TableSetting")
        self.horizontalLayout_19.addWidget(self.ledit_MinNumberReadDigit_DC_TableSetting)
        spacerItem5 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(self.frame_TurningParameter_DC_TableSetting)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_19.addWidget(self.label_2)
        self.ledit_MaxNumberReadDigit_DC_TableSetting = QtWidgets.QLineEdit(self.frame_TurningParameter_DC_TableSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_MaxNumberReadDigit_DC_TableSetting.sizePolicy().hasHeightForWidth())
        self.ledit_MaxNumberReadDigit_DC_TableSetting.setSizePolicy(sizePolicy)
        self.ledit_MaxNumberReadDigit_DC_TableSetting.setMinimumSize(QtCore.QSize(50, 0))
        self.ledit_MaxNumberReadDigit_DC_TableSetting.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ledit_MaxNumberReadDigit_DC_TableSetting.setSizeIncrement(QtCore.QSize(0, 0))
        self.ledit_MaxNumberReadDigit_DC_TableSetting.setText("")
        self.ledit_MaxNumberReadDigit_DC_TableSetting.setAlignment(QtCore.Qt.AlignCenter)
        self.ledit_MaxNumberReadDigit_DC_TableSetting.setObjectName("ledit_MaxNumberReadDigit_DC_TableSetting")
        self.horizontalLayout_19.addWidget(self.ledit_MaxNumberReadDigit_DC_TableSetting)
        self.verticalLayout_5.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(20, 5, 10, 5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.cbox_CodeColor_DC_TableSetting = QtWidgets.QCheckBox(self.frame_TurningParameter_DC_TableSetting)
        self.cbox_CodeColor_DC_TableSetting.setObjectName("cbox_CodeColor_DC_TableSetting")
        self.horizontalLayout_9.addWidget(self.cbox_CodeColor_DC_TableSetting)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.combox_CodeColor_DC_TableSetting = QtWidgets.QComboBox(self.frame_TurningParameter_DC_TableSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combox_CodeColor_DC_TableSetting.sizePolicy().hasHeightForWidth())
        self.combox_CodeColor_DC_TableSetting.setSizePolicy(sizePolicy)
        self.combox_CodeColor_DC_TableSetting.setMinimumSize(QtCore.QSize(100, 0))
        self.combox_CodeColor_DC_TableSetting.setObjectName("combox_CodeColor_DC_TableSetting")
        self.horizontalLayout_9.addWidget(self.combox_CodeColor_DC_TableSetting)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(20, 5, 10, 5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cbox_BaseAngle_DC_TableSetting = QtWidgets.QCheckBox(self.frame_TurningParameter_DC_TableSetting)
        self.cbox_BaseAngle_DC_TableSetting.setObjectName("cbox_BaseAngle_DC_TableSetting")
        self.horizontalLayout_4.addWidget(self.cbox_BaseAngle_DC_TableSetting)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.ledit_BaseAngle_DC_TableSetting = QtWidgets.QLineEdit(self.frame_TurningParameter_DC_TableSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_BaseAngle_DC_TableSetting.sizePolicy().hasHeightForWidth())
        self.ledit_BaseAngle_DC_TableSetting.setSizePolicy(sizePolicy)
        self.ledit_BaseAngle_DC_TableSetting.setMinimumSize(QtCore.QSize(100, 0))
        self.ledit_BaseAngle_DC_TableSetting.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ledit_BaseAngle_DC_TableSetting.setText("")
        self.ledit_BaseAngle_DC_TableSetting.setAlignment(QtCore.Qt.AlignCenter)
        self.ledit_BaseAngle_DC_TableSetting.setObjectName("ledit_BaseAngle_DC_TableSetting")
        self.horizontalLayout_4.addWidget(self.ledit_BaseAngle_DC_TableSetting)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addWidget(self.frame_TurningParameter_DC_TableSetting)
        self.lab_NoImport_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_NoImport_7.sizePolicy().hasHeightForWidth())
        self.lab_NoImport_7.setSizePolicy(sizePolicy)
        self.lab_NoImport_7.setMinimumSize(QtCore.QSize(0, 30))
        self.lab_NoImport_7.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.lab_NoImport_7.setObjectName("lab_NoImport_7")
        self.verticalLayout_3.addWidget(self.lab_NoImport_7)
        self.frame_Options_DC_TableSetting = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_Options_DC_TableSetting.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_Options_DC_TableSetting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Options_DC_TableSetting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Options_DC_TableSetting.setObjectName("frame_Options_DC_TableSetting")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_Options_DC_TableSetting)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(20, 5, 10, 5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lab_NoImport_3 = QtWidgets.QLabel(self.frame_Options_DC_TableSetting)
        self.lab_NoImport_3.setObjectName("lab_NoImport_3")
        self.horizontalLayout_7.addWidget(self.lab_NoImport_3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.combox_ScaleVariation_DC_TableSetting = QtWidgets.QComboBox(self.frame_Options_DC_TableSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combox_ScaleVariation_DC_TableSetting.sizePolicy().hasHeightForWidth())
        self.combox_ScaleVariation_DC_TableSetting.setSizePolicy(sizePolicy)
        self.combox_ScaleVariation_DC_TableSetting.setMinimumSize(QtCore.QSize(100, 0))
        self.combox_ScaleVariation_DC_TableSetting.setObjectName("combox_ScaleVariation_DC_TableSetting")
        self.horizontalLayout_7.addWidget(self.combox_ScaleVariation_DC_TableSetting)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(20, -1, 5, 5)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.cbox_EnableCheckDigit_DC_TableSetting = QtWidgets.QCheckBox(self.frame_Options_DC_TableSetting)
        self.cbox_EnableCheckDigit_DC_TableSetting.setObjectName("cbox_EnableCheckDigit_DC_TableSetting")
        self.horizontalLayout_18.addWidget(self.cbox_EnableCheckDigit_DC_TableSetting)
        self.verticalLayout_7.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(20, 5, 10, 5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lab_NoImport_4 = QtWidgets.QLabel(self.frame_Options_DC_TableSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_NoImport_4.sizePolicy().hasHeightForWidth())
        self.lab_NoImport_4.setSizePolicy(sizePolicy)
        self.lab_NoImport_4.setMinimumSize(QtCore.QSize(0, 0))
        self.lab_NoImport_4.setObjectName("lab_NoImport_4")
        self.horizontalLayout_5.addWidget(self.lab_NoImport_4)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.ledit_TimeOut_DC_TableSetting = QtWidgets.QLineEdit(self.frame_Options_DC_TableSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledit_TimeOut_DC_TableSetting.sizePolicy().hasHeightForWidth())
        self.ledit_TimeOut_DC_TableSetting.setSizePolicy(sizePolicy)
        self.ledit_TimeOut_DC_TableSetting.setMinimumSize(QtCore.QSize(100, 0))
        self.ledit_TimeOut_DC_TableSetting.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ledit_TimeOut_DC_TableSetting.setText("")
        self.ledit_TimeOut_DC_TableSetting.setAlignment(QtCore.Qt.AlignCenter)
        self.ledit_TimeOut_DC_TableSetting.setObjectName("ledit_TimeOut_DC_TableSetting")
        self.horizontalLayout_5.addWidget(self.ledit_TimeOut_DC_TableSetting)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_3.addWidget(self.frame_Options_DC_TableSetting)
        spacerItem10 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.scroll_AreaSettong_DC_TableSetting.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scroll_AreaSettong_DC_TableSetting)
        self.frame_OkCancel_DC_TableSetting = QtWidgets.QFrame(self.frame_DC_TableSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_OkCancel_DC_TableSetting.sizePolicy().hasHeightForWidth())
        self.frame_OkCancel_DC_TableSetting.setSizePolicy(sizePolicy)
        self.frame_OkCancel_DC_TableSetting.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_OkCancel_DC_TableSetting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_OkCancel_DC_TableSetting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_OkCancel_DC_TableSetting.setLineWidth(0)
        self.frame_OkCancel_DC_TableSetting.setObjectName("frame_OkCancel_DC_TableSetting")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_OkCancel_DC_TableSetting)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.btn_Ok_DC_TableSetting = QtWidgets.QPushButton(self.frame_OkCancel_DC_TableSetting)
        self.btn_Ok_DC_TableSetting.setObjectName("btn_Ok_DC_TableSetting")
        self.horizontalLayout.addWidget(self.btn_Ok_DC_TableSetting)
        spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.btn_Cancel_DC_TableSetting = QtWidgets.QPushButton(self.frame_OkCancel_DC_TableSetting)
        self.btn_Cancel_DC_TableSetting.setObjectName("btn_Cancel_DC_TableSetting")
        self.horizontalLayout.addWidget(self.btn_Cancel_DC_TableSetting)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame_OkCancel_DC_TableSetting)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_11.addWidget(self.frame_DC_TableSetting)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lab_NoImport_1.setText(_translate("Dialog", "1D Code Reader > Detection Conditions "))
        self.lab_NoImport_8.setText(_translate("Dialog", "Code Type"))
        self.lab_NoImport_2.setText(_translate("Dialog", "Code Type"))
        self.lab_NoImport_6.setText(_translate("Dialog", "Turning Parameters"))
        self.btn_AutoTurning_DC_TableSetting.setText(_translate("Dialog", "Auto-turning"))
        self.lab_NoImport_5.setText(_translate("Dialog", "Menual Setting"))
        self.cbox_CodeResulation_DC_TableSetting.setText(_translate("Dialog", "Code Resulation (pixel)"))
        self.cbox_ReferenceConstrast_DC_TableSetting.setText(_translate("Dialog", "Reference Contrast"))
        self.cbox_NumberOfReadDigit_DC_TableSetting.setText(_translate("Dialog", "Number of Read Digits"))
        self.label.setText(_translate("Dialog", "MIN "))
        self.label_2.setText(_translate("Dialog", "MAX "))
        self.cbox_CodeColor_DC_TableSetting.setText(_translate("Dialog", "Code Color"))
        self.cbox_BaseAngle_DC_TableSetting.setText(_translate("Dialog", "Base Angle"))
        self.lab_NoImport_7.setText(_translate("Dialog", "Options"))
        self.lab_NoImport_3.setText(_translate("Dialog", "Scale Variations"))
        self.cbox_EnableCheckDigit_DC_TableSetting.setText(_translate("Dialog", "Enable Check Digit"))
        self.lab_NoImport_4.setText(_translate("Dialog", "Timeout(s)"))
        self.btn_Ok_DC_TableSetting.setText(_translate("Dialog", "OK"))
        self.btn_Cancel_DC_TableSetting.setText(_translate("Dialog", "Cancel"))

        #Define item for comboxCodeType
        self.combox_CodeType_DC_TableSetting.addItem("")
        self.combox_CodeType_DC_TableSetting.addItem("")
        self.combox_CodeType_DC_TableSetting.addItem("")
        self.combox_CodeType_DC_TableSetting.addItem("")
        self.combox_CodeType_DC_TableSetting.addItem("")
        self.combox_CodeType_DC_TableSetting.addItem("")
        self.combox_CodeType_DC_TableSetting.addItem("")
        self.combox_CodeType_DC_TableSetting.addItem("")
        self.combox_CodeType_DC_TableSetting.addItem("")
        self.combox_CodeType_DC_TableSetting.setItemText(0, _translate("Dialog", "Not Specified"))
        self.combox_CodeType_DC_TableSetting.setItemText(1, _translate("Dialog", "CODE39"))
        self.combox_CodeType_DC_TableSetting.setItemText(2, _translate("Dialog", "CODE128"))
        self.combox_CodeType_DC_TableSetting.setItemText(3, _translate("Dialog", "EAN/JAN/UPC"))
        self.combox_CodeType_DC_TableSetting.setItemText(4, _translate("Dialog", "GS1 Databar"))
        self.combox_CodeType_DC_TableSetting.setItemText(5, _translate("Dialog", "ITF"))
        self.combox_CodeType_DC_TableSetting.setItemText(6, _translate("Dialog", "Codabar/NW- 7"))
        self.combox_CodeType_DC_TableSetting.setItemText(7, _translate("Dialog", "pHARMACODE"))
        self.combox_CodeType_DC_TableSetting.setItemText(8, _translate("Dialog", "CODE93"))

        #Define item for comboxReferenceContrast
        self.combox_ReferenceConstrast_DC_TableSetting.addItem("")
        self.combox_ReferenceConstrast_DC_TableSetting.addItem("")
        self.combox_ReferenceConstrast_DC_TableSetting.addItem("")
        self.combox_ReferenceConstrast_DC_TableSetting.addItem("")
        self.combox_ReferenceConstrast_DC_TableSetting.addItem("")
        self.combox_ReferenceConstrast_DC_TableSetting.setItemText(0, _translate("Dialog", "Highest"))
        self.combox_ReferenceConstrast_DC_TableSetting.setItemText(1, _translate("Dialog", "High"))
        self.combox_ReferenceConstrast_DC_TableSetting.setItemText(2, _translate("Dialog", "Normal"))
        self.combox_ReferenceConstrast_DC_TableSetting.setItemText(3, _translate("Dialog", "Low"))
        self.combox_ReferenceConstrast_DC_TableSetting.setItemText(4, _translate("Dialog", "Lowest"))

        #Define item for comboxCodeColor
        self.combox_CodeColor_DC_TableSetting.addItem("")
        self.combox_CodeColor_DC_TableSetting.addItem("")
        self.combox_CodeColor_DC_TableSetting.addItem("")
        self.combox_CodeColor_DC_TableSetting.setItemText(0, _translate("Dialog", "Both"))
        self.combox_CodeColor_DC_TableSetting.setItemText(1, _translate("Dialog", "Black"))
        self.combox_CodeColor_DC_TableSetting.setItemText(2, _translate("Dialog", "White"))



        #Define item for Scale Variations
        self.combox_ScaleVariation_DC_TableSetting.addItem("")
        self.combox_ScaleVariation_DC_TableSetting.addItem("")
        self.combox_ScaleVariation_DC_TableSetting.addItem("")
        self.combox_ScaleVariation_DC_TableSetting.addItem("")
        self.combox_ScaleVariation_DC_TableSetting.setItemText(0, _translate("Dialog", "Small"))
        self.combox_ScaleVariation_DC_TableSetting.setItemText(1, _translate("Dialog", "Medium"))
        self.combox_ScaleVariation_DC_TableSetting.setItemText(2, _translate("Dialog", "Large"))
        self.combox_ScaleVariation_DC_TableSetting.setItemText(3, _translate("Dialog", "Unlimited"))
      