# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rsrc/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 741)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBox_zz = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_zz.setProperty("value", 6)
        self.spinBox_zz.setObjectName("spinBox_zz")
        self.gridLayout.addWidget(self.spinBox_zz, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 2, 0, 1, 1)
        self.spinBox_nn = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_nn.setProperty("value", 6)
        self.spinBox_nn.setObjectName("spinBox_nn")
        self.gridLayout.addWidget(self.spinBox_nn, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.spinBox_qq = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_qq.setMinimum(1)
        self.spinBox_qq.setMaximum(150)
        self.spinBox_qq.setProperty("value", 6)
        self.spinBox_qq.setObjectName("spinBox_qq")
        self.gridLayout.addWidget(self.spinBox_qq, 3, 1, 1, 1)
        self.comboBox_name = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_name.setObjectName("comboBox_name")
        self.gridLayout.addWidget(self.comboBox_name, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label_name = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setLineWidth(1)
        self.label_name.setText("")
        self.label_name.setTextFormat(QtCore.Qt.AutoText)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_2.addWidget(self.label_name)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_nav_nw = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_nw.setObjectName("pushButton_nav_nw")
        self.gridLayout_2.addWidget(self.pushButton_nav_nw, 0, 0, 1, 1)
        self.pushButton_nav_n = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_n.setObjectName("pushButton_nav_n")
        self.gridLayout_2.addWidget(self.pushButton_nav_n, 0, 1, 1, 1)
        self.pushButton_nav_ne = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_ne.setObjectName("pushButton_nav_ne")
        self.gridLayout_2.addWidget(self.pushButton_nav_ne, 0, 2, 1, 1)
        self.pushButton_nav_w = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_w.setObjectName("pushButton_nav_w")
        self.gridLayout_2.addWidget(self.pushButton_nav_w, 1, 0, 1, 1)
        self.pushButton_nav_e = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_e.setObjectName("pushButton_nav_e")
        self.gridLayout_2.addWidget(self.pushButton_nav_e, 1, 2, 1, 1)
        self.pushButton_nav_sw = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_sw.setObjectName("pushButton_nav_sw")
        self.gridLayout_2.addWidget(self.pushButton_nav_sw, 2, 0, 1, 1)
        self.pushButton_nav_s = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_s.setObjectName("pushButton_nav_s")
        self.gridLayout_2.addWidget(self.pushButton_nav_s, 2, 1, 1, 1)
        self.pushButton_nav_se = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_se.setObjectName("pushButton_nav_se")
        self.gridLayout_2.addWidget(self.pushButton_nav_se, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.comboBox_ring = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_ring.setObjectName("comboBox_ring")
        self.gridLayout_3.addWidget(self.comboBox_ring, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.doubleSpinBox_energy = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_energy.setDecimals(4)
        self.doubleSpinBox_energy.setMaximum(10000.0)
        self.doubleSpinBox_energy.setSingleStep(0.0001)
        self.doubleSpinBox_energy.setProperty("value", 400.0)
        self.doubleSpinBox_energy.setObjectName("doubleSpinBox_energy")
        self.gridLayout_3.addWidget(self.doubleSpinBox_energy, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)
        self.doubleSpinBox_path_length = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_path_length.setEnabled(False)
        self.doubleSpinBox_path_length.setDecimals(3)
        self.doubleSpinBox_path_length.setMaximum(100000.0)
        self.doubleSpinBox_path_length.setSingleStep(0.001)
        self.doubleSpinBox_path_length.setProperty("value", 100.0)
        self.doubleSpinBox_path_length.setObjectName("doubleSpinBox_path_length")
        self.gridLayout_3.addWidget(self.doubleSpinBox_path_length, 3, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setEnabled(False)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 3, 0, 1, 1)
        self.doubleSpinBox_f_analysis = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_f_analysis.setDecimals(4)
        self.doubleSpinBox_f_analysis.setMaximum(10000.0)
        self.doubleSpinBox_f_analysis.setSingleStep(0.0001)
        self.doubleSpinBox_f_analysis.setProperty("value", 245.0)
        self.doubleSpinBox_f_analysis.setObjectName("doubleSpinBox_f_analysis")
        self.gridLayout_3.addWidget(self.doubleSpinBox_f_analysis, 1, 1, 1, 1)
        self.doubleSpinBox_beam_current = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_beam_current.setDecimals(4)
        self.doubleSpinBox_beam_current.setMaximum(10000.0)
        self.doubleSpinBox_beam_current.setSingleStep(0.0001)
        self.doubleSpinBox_beam_current.setProperty("value", 1.0)
        self.doubleSpinBox_beam_current.setObjectName("doubleSpinBox_beam_current")
        self.gridLayout_3.addWidget(self.doubleSpinBox_beam_current, 2, 1, 1, 1)
        self.checkBox_circum = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_circum.setChecked(True)
        self.checkBox_circum.setObjectName("checkBox_circum")
        self.gridLayout_3.addWidget(self.checkBox_circum, 5, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_23 = QtWidgets.QLabel(self.groupBox_6)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 3, 0, 1, 1)
        self.spinBox_range_zz = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBox_range_zz.setMinimum(1)
        self.spinBox_range_zz.setMaximum(150)
        self.spinBox_range_zz.setProperty("value", 4)
        self.spinBox_range_zz.setObjectName("spinBox_range_zz")
        self.gridLayout_5.addWidget(self.spinBox_range_zz, 3, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_6)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 4, 0, 1, 1)
        self.spinBox_range_nn = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBox_range_nn.setMinimum(1)
        self.spinBox_range_nn.setMaximum(150)
        self.spinBox_range_nn.setProperty("value", 4)
        self.spinBox_range_nn.setObjectName("spinBox_range_nn")
        self.gridLayout_5.addWidget(self.spinBox_range_nn, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_6)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 5, 0, 1, 1)
        self.lineEdit_f_actual = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_f_actual.setObjectName("lineEdit_f_actual")
        self.gridLayout_5.addWidget(self.lineEdit_f_actual, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 1, 0, 1, 1)
        self.lineEdit_f_unknown = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_f_unknown.setObjectName("lineEdit_f_unknown")
        self.gridLayout_5.addWidget(self.lineEdit_f_unknown, 1, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_6)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 2, 0, 1, 1)
        self.spinBox_max_ee = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBox_max_ee.setMaximum(150)
        self.spinBox_max_ee.setProperty("value", 3)
        self.spinBox_max_ee.setObjectName("spinBox_max_ee")
        self.gridLayout_5.addWidget(self.spinBox_max_ee, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_6)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)
        self.doubleSpinBox_accuracy = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_accuracy.setDecimals(5)
        self.doubleSpinBox_accuracy.setMinimum(1e-05)
        self.doubleSpinBox_accuracy.setMaximum(9.0)
        self.doubleSpinBox_accuracy.setSingleStep(1e-05)
        self.doubleSpinBox_accuracy.setProperty("value", 0.001)
        self.doubleSpinBox_accuracy.setObjectName("doubleSpinBox_accuracy")
        self.gridLayout_5.addWidget(self.doubleSpinBox_accuracy, 5, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_6, 1, 1, 2, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_calculate = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        self.gridLayout_6.addWidget(self.pushButton_calculate, 0, 0, 1, 1)
        self.pushButton_isotopes = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_isotopes.setObjectName("pushButton_isotopes")
        self.gridLayout_6.addWidget(self.pushButton_isotopes, 0, 1, 1, 1)
        self.pushButton_table_data = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_table_data.setObjectName("pushButton_table_data")
        self.gridLayout_6.addWidget(self.pushButton_table_data, 1, 0, 1, 1)
        self.pushButton_isobars = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_isobars.setObjectName("pushButton_isobars")
        self.gridLayout_6.addWidget(self.pushButton_isobars, 1, 1, 1, 1)
        self.pushButton_isotones = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_isotones.setObjectName("pushButton_isotones")
        self.gridLayout_6.addWidget(self.pushButton_isotones, 2, 1, 1, 1)
        self.pushButton_identify = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_identify.setObjectName("pushButton_identify")
        self.gridLayout_6.addWidget(self.pushButton_identify, 2, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_5, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_copy_table = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_copy_table.setObjectName("pushButton_copy_table")
        self.horizontalLayout.addWidget(self.pushButton_copy_table)
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableView = QtWidgets.QTableView(self.groupBox_3)
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setShowGrid(True)
        self.tableView.setGridStyle(QtCore.Qt.DotLine)
        self.tableView.setSortingEnabled(True)
        self.tableView.setWordWrap(False)
        self.tableView.setCornerButtonEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.tableView, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuParticle = QtWidgets.QMenu(self.menubar)
        self.menuParticle.setObjectName("menuParticle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClear_results = QtWidgets.QAction(MainWindow)
        self.actionClear_results.setObjectName("actionClear_results")
        self.actionSave_results = QtWidgets.QAction(MainWindow)
        self.actionSave_results.setObjectName("actionSave_results")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCalculate = QtWidgets.QAction(MainWindow)
        self.actionCalculate.setObjectName("actionCalculate")
        self.actionShow_table_data = QtWidgets.QAction(MainWindow)
        self.actionShow_table_data.setObjectName("actionShow_table_data")
        self.actionIdentify = QtWidgets.QAction(MainWindow)
        self.actionIdentify.setObjectName("actionIdentify")
        self.actionIsotopes = QtWidgets.QAction(MainWindow)
        self.actionIsotopes.setObjectName("actionIsotopes")
        self.actionIsobars = QtWidgets.QAction(MainWindow)
        self.actionIsobars.setObjectName("actionIsobars")
        self.actionIsotones = QtWidgets.QAction(MainWindow)
        self.actionIsotones.setObjectName("actionIsotones")
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_results)
        self.menuFile.addAction(self.actionClear_results)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuParticle.addAction(self.actionCalculate)
        self.menuParticle.addAction(self.actionShow_table_data)
        self.menuParticle.addAction(self.actionIdentify)
        self.menuParticle.addSeparator()
        self.menuParticle.addAction(self.actionIsotopes)
        self.menuParticle.addAction(self.actionIsobars)
        self.menuParticle.addAction(self.actionIsotones)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuParticle.menuAction())

        self.retranslateUi(MainWindow)
        self.checkBox_circum.toggled['bool'].connect(self.doubleSpinBox_path_length.setDisabled)
        self.checkBox_circum.toggled['bool'].connect(self.label_19.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "barion"))
        self.groupBox.setTitle(_translate("MainWindow", "Navigation"))
        self.label_2.setText(_translate("MainWindow", "Z:"))
        self.label_20.setText(_translate("MainWindow", "N:"))
        self.label_3.setText(_translate("MainWindow", "Q:"))
        self.label_21.setText(_translate("MainWindow", "Name:"))
        self.pushButton_nav_nw.setText(_translate("MainWindow", "↖︎"))
        self.pushButton_nav_n.setText(_translate("MainWindow", "↑"))
        self.pushButton_nav_ne.setText(_translate("MainWindow", "↗︎"))
        self.pushButton_nav_w.setText(_translate("MainWindow", "←"))
        self.pushButton_nav_e.setText(_translate("MainWindow", "→"))
        self.pushButton_nav_sw.setText(_translate("MainWindow", "↙︎"))
        self.pushButton_nav_s.setText(_translate("MainWindow", "↓"))
        self.pushButton_nav_se.setText(_translate("MainWindow", "↘︎"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Parameters"))
        self.label_10.setText(_translate("MainWindow", "Analysis Freq. [MHz]:"))
        self.label_4.setText(_translate("MainWindow", "Energy [MeV/u]:"))
        self.label_17.setText(_translate("MainWindow", "Ring:"))
        self.label_8.setText(_translate("MainWindow", "Beam Current [µA]:"))
        self.label_19.setText(_translate("MainWindow", "Path length [m]:"))
        self.checkBox_circum.setText(_translate("MainWindow", "Use circum."))
        self.groupBox_6.setTitle(_translate("MainWindow", "Freuquency Identification"))
        self.label_23.setText(_translate("MainWindow", "P range ±:"))
        self.label_24.setText(_translate("MainWindow", "N range ±:"))
        self.label.setText(_translate("MainWindow", "Sensitivity radius:"))
        self.label_14.setText(_translate("MainWindow", "Unknown particle [MHz]"))
        self.label_22.setText(_translate("MainWindow", "Max No. Electrons:"))
        self.label_12.setText(_translate("MainWindow", "Known particle [MHz]"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Actions"))
        self.pushButton_calculate.setText(_translate("MainWindow", "Calculate"))
        self.pushButton_isotopes.setText(_translate("MainWindow", "Isotopes"))
        self.pushButton_table_data.setText(_translate("MainWindow", "Table Data"))
        self.pushButton_isobars.setText(_translate("MainWindow", "Isobars"))
        self.pushButton_isotones.setText(_translate("MainWindow", "Isotones"))
        self.pushButton_identify.setText(_translate("MainWindow", "Identify"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Results Pane"))
        self.pushButton_copy_table.setText(_translate("MainWindow", "Copy table"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Results Table"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuParticle.setTitle(_translate("MainWindow", "Particle"))
        self.actionClear_results.setText(_translate("MainWindow", "Clear results"))
        self.actionClear_results.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionSave_results.setText(_translate("MainWindow", "Save results"))
        self.actionSave_results.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionCalculate.setText(_translate("MainWindow", "Calculate"))
        self.actionCalculate.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionShow_table_data.setText(_translate("MainWindow", "Show table data"))
        self.actionShow_table_data.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionIdentify.setText(_translate("MainWindow", "Identify"))
        self.actionIdentify.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionIsotopes.setText(_translate("MainWindow", "Isotopes"))
        self.actionIsobars.setText(_translate("MainWindow", "Isobars"))
        self.actionIsotones.setText(_translate("MainWindow", "Isotones"))
