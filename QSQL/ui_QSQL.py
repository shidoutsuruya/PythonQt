# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qsql.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QSQL(object):
    def setupUi(self, QSQL):
        QSQL.setObjectName("QSQL")
        QSQL.resize(1200, 600)
        QSQL.setMinimumSize(QtCore.QSize(1200, 600))
        self.centralWidget = QtWidgets.QWidget(QSQL)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.centralWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        QSQL.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(QSQL)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 17))
        self.menuBar.setObjectName("menuBar")
        QSQL.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(QSQL)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        QSQL.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(QSQL)
        self.statusBar.setObjectName("statusBar")
        QSQL.setStatusBar(self.statusBar)
        self.actionOpen = QtWidgets.QAction(QSQL)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/open3.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionInsert = QtWidgets.QAction(QSQL)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/306.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsert.setIcon(icon1)
        self.actionInsert.setObjectName("actionInsert")
        self.actionEdit = QtWidgets.QAction(QSQL)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/812.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit.setIcon(icon2)
        self.actionEdit.setObjectName("actionEdit")
        self.actionDelete = QtWidgets.QAction(QSQL)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/delete1.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon3)
        self.actionDelete.setObjectName("actionDelete")
        self.actionBonus = QtWidgets.QAction(QSQL)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/up.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBonus.setIcon(icon4)
        self.actionBonus.setObjectName("actionBonus")
        self.actionSQLTest = QtWidgets.QAction(QSQL)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/828.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSQLTest.setIcon(icon5)
        self.actionSQLTest.setObjectName("actionSQLTest")
        self.actionExit = QtWidgets.QAction(QSQL)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/exit.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon6)
        self.actionExit.setObjectName("actionExit")
        self.mainToolBar.addAction(self.actionOpen)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionInsert)
        self.mainToolBar.addAction(self.actionEdit)
        self.mainToolBar.addAction(self.actionDelete)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionBonus)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionSQLTest)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionExit)

        self.retranslateUi(QSQL)
        self.actionExit.triggered.connect(QSQL.close)
        QtCore.QMetaObject.connectSlotsByName(QSQL)

    def retranslateUi(self, QSQL):
        _translate = QtCore.QCoreApplication.translate
        QSQL.setWindowTitle(_translate("QSQL", "QSQL"))
        self.actionOpen.setText(_translate("QSQL", "Open"))
        self.actionInsert.setText(_translate("QSQL", "Insert"))
        self.actionEdit.setText(_translate("QSQL", "Edit"))
        self.actionDelete.setText(_translate("QSQL", "Delete"))
        self.actionBonus.setText(_translate("QSQL", "Bonus"))
        self.actionSQLTest.setText(_translate("QSQL", "SQLTest"))
        self.actionExit.setText(_translate("QSQL", "Exit"))
import res_rc