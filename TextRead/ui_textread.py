# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textread.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TextRead(object):
    def setupUi(self, TextRead):
        TextRead.setObjectName("TextRead")
        TextRead.resize(800, 600)
        TextRead.setMinimumSize(QtCore.QSize(800, 600))
        self.centralWidget = QtWidgets.QWidget(TextRead)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        TextRead.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(TextRead)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menuBar.setObjectName("menuBar")
        TextRead.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(TextRead)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        TextRead.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(TextRead)
        self.statusBar.setObjectName("statusBar")
        TextRead.setStatusBar(self.statusBar)
        self.actionQFileOpen = QtWidgets.QAction(TextRead)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Open.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQFileOpen.setIcon(icon)
        self.actionQFileOpen.setObjectName("actionQFileOpen")
        self.actionQFileSave = QtWidgets.QAction(TextRead)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/Save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQFileSave.setIcon(icon1)
        self.actionQFileSave.setObjectName("actionQFileSave")
        self.actionStreamOpen = QtWidgets.QAction(TextRead)
        self.actionStreamOpen.setIcon(icon)
        self.actionStreamOpen.setObjectName("actionStreamOpen")
        self.actionSteamSave = QtWidgets.QAction(TextRead)
        self.actionSteamSave.setIcon(icon1)
        self.actionSteamSave.setObjectName("actionSteamSave")
        self.actionPythonOpen = QtWidgets.QAction(TextRead)
        self.actionPythonOpen.setIcon(icon)
        self.actionPythonOpen.setObjectName("actionPythonOpen")
        self.actionPythonSave = QtWidgets.QAction(TextRead)
        self.actionPythonSave.setIcon(icon1)
        self.actionPythonSave.setObjectName("actionPythonSave")
        self.actionExit = QtWidgets.QAction(TextRead)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/Close.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName("actionExit")
        self.mainToolBar.addAction(self.actionQFileOpen)
        self.mainToolBar.addAction(self.actionQFileSave)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionStreamOpen)
        self.mainToolBar.addAction(self.actionSteamSave)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionPythonOpen)
        self.mainToolBar.addAction(self.actionPythonSave)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionExit)

        self.retranslateUi(TextRead)
        self.actionExit.triggered.connect(TextRead.close)
        QtCore.QMetaObject.connectSlotsByName(TextRead)

    def retranslateUi(self, TextRead):
        _translate = QtCore.QCoreApplication.translate
        TextRead.setWindowTitle(_translate("TextRead", "TextRead"))
        self.actionQFileOpen.setText(_translate("TextRead", "QFileOpen"))
        self.actionQFileSave.setText(_translate("TextRead", "QFileSave"))
        self.actionStreamOpen.setText(_translate("TextRead", "StreamOpen"))
        self.actionSteamSave.setText(_translate("TextRead", "SteamSave"))
        self.actionPythonOpen.setText(_translate("TextRead", "PythonOpen"))
        self.actionPythonSave.setText(_translate("TextRead", "PythonSave"))
        self.actionExit.setText(_translate("TextRead", "Exit"))
import res_rc
