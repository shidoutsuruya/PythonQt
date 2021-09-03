# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qwformtable.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_formTable(object):
    def setupUi(self, formTable):
        formTable.setObjectName("formTable")
        formTable.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(formTable)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(75, 25, 256, 192))
        self.tableView.setObjectName("tableView")
        formTable.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(formTable)
        self.statusbar.setObjectName("statusbar")
        formTable.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(formTable)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menubar.setObjectName("menubar")
        formTable.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(formTable)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        formTable.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSize = QtWidgets.QAction(formTable)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSize.setIcon(icon)
        self.actionSize.setObjectName("actionSize")
        self.actionTitle = QtWidgets.QAction(formTable)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/312.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTitle.setIcon(icon1)
        self.actionTitle.setObjectName("actionTitle")
        self.actionExit = QtWidgets.QAction(formTable)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/exit.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName("actionExit")
        self.toolBar.addAction(self.actionSize)
        self.toolBar.addAction(self.actionTitle)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(formTable)
        self.actionExit.triggered.connect(formTable.close)
        QtCore.QMetaObject.connectSlotsByName(formTable)

    def retranslateUi(self, formTable):
        _translate = QtCore.QCoreApplication.translate
        formTable.setWindowTitle(_translate("formTable", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("formTable", "toolBar"))
        self.actionSize.setText(_translate("formTable", "Size"))
        self.actionTitle.setText(_translate("formTable", "Title"))
        self.actionExit.setText(_translate("formTable", "Exit"))
import res_rc
