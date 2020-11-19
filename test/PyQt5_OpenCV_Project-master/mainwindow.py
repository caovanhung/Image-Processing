# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(823, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.agregarTab = QtWidgets.QWidget()
        self.agregarTab.setObjectName("agregarTab")
        self.gridLayout = QtWidgets.QGridLayout(self.agregarTab)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.agregarTab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.agregar_nombre_lineedit = QtWidgets.QLineEdit(self.agregarTab)
        self.agregar_nombre_lineedit.setObjectName("agregar_nombre_lineedit")
        self.gridLayout.addWidget(self.agregar_nombre_lineedit, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 539, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.agregar_listo_button = QtWidgets.QPushButton(self.agregarTab)
        self.agregar_listo_button.setObjectName("agregar_listo_button")
        self.gridLayout.addWidget(self.agregar_listo_button, 1, 0, 1, 1)
        self.tabWidget.addTab(self.agregarTab, "")
        self.buscarTab = QtWidgets.QWidget()
        self.buscarTab.setObjectName("buscarTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.buscarTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.buscarTab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.buscar_nombre_lineedit = QtWidgets.QLineEdit(self.buscarTab)
        self.buscar_nombre_lineedit.setObjectName("buscar_nombre_lineedit")
        self.gridLayout_2.addWidget(self.buscar_nombre_lineedit, 0, 1, 1, 1)
        self.buscar_tableview = QtWidgets.QTableView(self.buscarTab)
        self.buscar_tableview.setObjectName("buscar_tableview")
        self.gridLayout_2.addWidget(self.buscar_tableview, 1, 0, 1, 2)
        self.tabWidget.addTab(self.buscarTab, "")
        self.eliminarTab = QtWidgets.QWidget()
        self.eliminarTab.setObjectName("eliminarTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.eliminarTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.eliminar_tableview = QtWidgets.QTableView(self.eliminarTab)
        self.eliminar_tableview.setObjectName("eliminar_tableview")
        self.gridLayout_3.addWidget(self.eliminar_tableview, 0, 0, 1, 1)
        self.tabWidget.addTab(self.eliminarTab, "")
        self.modificarTab = QtWidgets.QWidget()
        self.modificarTab.setObjectName("modificarTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.modificarTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.modificar_tableview = QtWidgets.QTableView(self.modificarTab)
        self.modificar_tableview.setObjectName("modificar_tableview")
        self.gridLayout_4.addWidget(self.modificar_tableview, 0, 0, 1, 1)
        self.tabWidget.addTab(self.modificarTab, "")
        self.opencvTab = QtWidgets.QWidget()
        self.opencvTab.setObjectName("opencvTab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.opencvTab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox = QtWidgets.QGroupBox(self.opencvTab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.nombre_combobox = QtWidgets.QComboBox(self.groupBox)
        self.nombre_combobox.setObjectName("nombre_combobox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nombre_combobox)
        self.gridLayout_6.addLayout(self.formLayout, 0, 0, 1, 1)
        self.iniciar_capturas_button = QtWidgets.QPushButton(self.groupBox)
        self.iniciar_capturas_button.setObjectName("iniciar_capturas_button")
        self.gridLayout_6.addWidget(self.iniciar_capturas_button, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.opencvTab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.iniciar_entrenamiento_button = QtWidgets.QPushButton(self.groupBox_2)
        self.iniciar_entrenamiento_button.setObjectName("iniciar_entrenamiento_button")
        self.gridLayout_7.addWidget(self.iniciar_entrenamiento_button, 0, 0, 1, 1)
        self.entrenamiento_progressbar = QtWidgets.QProgressBar(self.groupBox_2)
        self.entrenamiento_progressbar.setProperty("value", 24)
        self.entrenamiento_progressbar.setObjectName("entrenamiento_progressbar")
        self.gridLayout_7.addWidget(self.entrenamiento_progressbar, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.iniciar_reconocimiento_button = QtWidgets.QPushButton(self.groupBox_2)
        self.iniciar_reconocimiento_button.setObjectName("iniciar_reconocimiento_button")
        self.gridLayout_8.addWidget(self.iniciar_reconocimiento_button, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_2, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 411, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem1, 2, 1, 1, 1)
        self.tabWidget.addTab(self.opencvTab, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 20))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nombre"))
        self.agregar_listo_button.setText(_translate("MainWindow", "Listo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.agregarTab), _translate("MainWindow", "Agregar"))
        self.label_2.setText(_translate("MainWindow", "Nombre"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.buscarTab), _translate("MainWindow", "Buscar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.eliminarTab), _translate("MainWindow", "Eliminar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.modificarTab), _translate("MainWindow", "Modificar"))
        self.groupBox.setTitle(_translate("MainWindow", "Captura de cara"))
        self.label_3.setText(_translate("MainWindow", "Nombre"))
        self.iniciar_capturas_button.setText(_translate("MainWindow", "Iniciar capturas"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Entrenamiento y reconocimiento"))
        self.iniciar_entrenamiento_button.setText(_translate("MainWindow", "Iniciar entrenamiento"))
        self.iniciar_reconocimiento_button.setText(_translate("MainWindow", "Iniciar reconocimiento"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.opencvTab), _translate("MainWindow", "OpenCV"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
