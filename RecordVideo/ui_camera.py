# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_video(object):
    def setupUi(self, video):
        video.setObjectName("video")
        video.resize(800, 600)
        video.setMinimumSize(QtCore.QSize(800, 600))
        video.setStyleSheet("color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 170, 0);\n"
"color: rgb(85, 255, 127);")
        self.centralWidget = QtWidgets.QWidget(video)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"border-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 255), stop:0.479904 rgba(255, 0, 0, 255), stop:0.522685 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.cbPicture = QtWidgets.QCheckBox(self.widget)
        self.cbPicture.setObjectName("cbPicture")
        self.gridLayout.addWidget(self.cbPicture, 0, 2, 1, 1)
        self.cbRecord = QtWidgets.QCheckBox(self.widget)
        self.cbRecord.setObjectName("cbRecord")
        self.gridLayout.addWidget(self.cbRecord, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cbDevice = QtWidgets.QComboBox(self.widget)
        self.cbDevice.setObjectName("cbDevice")
        self.gridLayout.addWidget(self.cbDevice, 0, 1, 1, 1)
        self.cbFocus = QtWidgets.QCheckBox(self.widget)
        self.cbFocus.setObjectName("cbFocus")
        self.gridLayout.addWidget(self.cbFocus, 1, 2, 1, 1)
        self.cbExposure = QtWidgets.QCheckBox(self.widget)
        self.cbExposure.setObjectName("cbExposure")
        self.gridLayout.addWidget(self.cbExposure, 1, 3, 1, 1)
        self.cbSavePicture = QtWidgets.QCheckBox(self.widget)
        self.cbSavePicture.setObjectName("cbSavePicture")
        self.gridLayout.addWidget(self.cbSavePicture, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralWidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gbCamera = QtWidgets.QGroupBox(self.widget_2)
        self.gbCamera.setObjectName("gbCamera")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gbCamera)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widgetCamera = QCameraViewfinder(self.gbCamera)
        self.widgetCamera.setStyleSheet("color: rgb(85, 255, 0);\n"
"color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));\n"
"color: rgb(255, 170, 127);")
        self.widgetCamera.setObjectName("widgetCamera")
        self.verticalLayout_3.addWidget(self.widgetCamera)
        self.horizontalLayout.addWidget(self.gbCamera)
        self.gbCatch = QtWidgets.QGroupBox(self.widget_2)
        self.gbCatch.setObjectName("gbCatch")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gbCatch)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labCatch = QtWidgets.QLabel(self.gbCatch)
        self.labCatch.setText("")
        self.labCatch.setObjectName("labCatch")
        self.verticalLayout_2.addWidget(self.labCatch)
        self.horizontalLayout.addWidget(self.gbCatch)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        video.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(video)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menuBar.setObjectName("menuBar")
        video.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(video)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        video.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(video)
        self.statusBar.setObjectName("statusBar")
        video.setStatusBar(self.statusBar)
        self.actionOpenCamera = QtWidgets.QAction(video)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/5.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenCamera.setIcon(icon)
        self.actionOpenCamera.setObjectName("actionOpenCamera")
        self.actionCloseCamera = QtWidgets.QAction(video)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/Shut Down.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCloseCamera.setIcon(icon1)
        self.actionCloseCamera.setObjectName("actionCloseCamera")
        self.actionTakePhoto = QtWidgets.QAction(video)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/picture.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTakePhoto.setIcon(icon2)
        self.actionTakePhoto.setObjectName("actionTakePhoto")
        self.actionExit = QtWidgets.QAction(video)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon3)
        self.actionExit.setObjectName("actionExit")
        self.mainToolBar.addAction(self.actionOpenCamera)
        self.mainToolBar.addAction(self.actionCloseCamera)
        self.mainToolBar.addAction(self.actionTakePhoto)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionExit)

        self.retranslateUi(video)
        QtCore.QMetaObject.connectSlotsByName(video)

    def retranslateUi(self, video):
        _translate = QtCore.QCoreApplication.translate
        video.setWindowTitle(_translate("video", "video"))
        self.cbPicture.setText(_translate("video", "picture"))
        self.cbRecord.setText(_translate("video", "record"))
        self.label.setText(_translate("video", "device"))
        self.cbFocus.setText(_translate("video", "focus"))
        self.cbExposure.setText(_translate("video", "exposure"))
        self.cbSavePicture.setText(_translate("video", "save picture"))
        self.gbCamera.setTitle(_translate("video", "camera"))
        self.gbCatch.setTitle(_translate("video", "catch"))
        self.actionOpenCamera.setText(_translate("video", "OpenCamera"))
        self.actionCloseCamera.setText(_translate("video", "CloseCamera"))
        self.actionTakePhoto.setText(_translate("video", "TakePhoto"))
        self.actionExit.setText(_translate("video", "Exit"))
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
import res_rc