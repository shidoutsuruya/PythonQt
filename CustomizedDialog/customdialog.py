# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customdialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CustomDialog(object):
    def setupUi(self, CustomDialog):
        CustomDialog.setObjectName("CustomDialog")
        CustomDialog.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(CustomDialog)
        self.centralWidget.setObjectName("centralWidget")
        self.tableView = QtWidgets.QTableView(self.centralWidget)
        self.tableView.setGeometry(QtCore.QRect(0, 5, 396, 211))
        self.tableView.setObjectName("tableView")
        CustomDialog.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(CustomDialog)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 17))
        self.menuBar.setObjectName("menuBar")
        CustomDialog.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(CustomDialog)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        CustomDialog.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(CustomDialog)
        self.statusBar.setObjectName("statusBar")
        CustomDialog.setStatusBar(self.statusBar)
        self.actionSet_line = QtWidgets.QAction(CustomDialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/130.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_line.setIcon(icon)
        self.actionSet_line.setObjectName("actionSet_line")
        self.actionSet_title = QtWidgets.QAction(CustomDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/516.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_title.setIcon(icon1)
        self.actionSet_title.setObjectName("actionSet_title")
        self.actionSet_cell = QtWidgets.QAction(CustomDialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/128.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_cell.setIcon(icon2)
        self.actionSet_cell.setObjectName("actionSet_cell")
        self.actionExit = QtWidgets.QAction(CustomDialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/exit.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon3)
        self.actionExit.setObjectName("actionExit")
        self.mainToolBar.addAction(self.actionSet_line)
        self.mainToolBar.addAction(self.actionSet_title)
        self.mainToolBar.addAction(self.actionSet_cell)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionExit)

        self.retranslateUi(CustomDialog)
        QtCore.QMetaObject.connectSlotsByName(CustomDialog)

    def retranslateUi(self, CustomDialog):
        _translate = QtCore.QCoreApplication.translate
        CustomDialog.setWindowTitle(_translate("CustomDialog", "CustomDialog"))
        self.actionSet_line.setText(_translate("CustomDialog", "Set line"))
        self.actionSet_title.setText(_translate("CustomDialog", "Set title"))
        self.actionSet_cell.setText(_translate("CustomDialog", "Set cell"))
        self.actionExit.setText(_translate("CustomDialog", "Exit"))
import res_rc
