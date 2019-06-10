# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game_interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 583)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UpButton = QtWidgets.QPushButton(self.centralwidget)
        self.UpButton.setGeometry(QtCore.QRect(640, 120, 75, 23))
        self.UpButton.setObjectName("UpButton")
        self.DownButton = QtWidgets.QPushButton(self.centralwidget)
        self.DownButton.setGeometry(QtCore.QRect(640, 230, 75, 23))
        self.DownButton.setObjectName("DownButton")
        self.rightButton = QtWidgets.QPushButton(self.centralwidget)
        self.rightButton.setGeometry(QtCore.QRect(710, 180, 75, 23))
        self.rightButton.setObjectName("rightButton")
        self.LeftButton = QtWidgets.QPushButton(self.centralwidget)
        self.LeftButton.setGeometry(QtCore.QRect(580, 180, 75, 23))
        self.LeftButton.setObjectName("LeftButton")
        self.rotateButton = QtWidgets.QPushButton(self.centralwidget)
        self.rotateButton.setGeometry(QtCore.QRect(640, 350, 75, 23))
        self.rotateButton.setObjectName("rotateButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 571, 541))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.verticalHeader().setDefaultSectionSize(100)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(640, 20, 75, 23))
        self.startButton.setObjectName("startButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quarda"))
        self.UpButton.setText(_translate("MainWindow", "Up (W)"))
        self.DownButton.setText(_translate("MainWindow", "Down (S)"))
        self.rightButton.setText(_translate("MainWindow", "Right (D)"))
        self.LeftButton.setText(_translate("MainWindow", "Left (A)"))
        self.rotateButton.setText(_translate("MainWindow", "Rotate (F)"))
        self.tableWidget.setSortingEnabled(False)
        self.startButton.setText(_translate("MainWindow", "Start"))

