# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 307)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(60, 40, 261, 141))
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 474, 17))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionembedding_widget = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/101.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionembedding_widget.setIcon(icon)
        self.actionembedding_widget.setObjectName("actionembedding_widget")
        self.actionindependent_widget = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/408.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionindependent_widget.setIcon(icon1)
        self.actionindependent_widget.setObjectName("actionindependent_widget")
        self.actionembedding_mainwindow = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionembedding_mainwindow.setIcon(icon2)
        self.actionembedding_mainwindow.setObjectName("actionembedding_mainwindow")
        self.actionindependent_mainwindow = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/31.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionindependent_mainwindow.setIcon(icon3)
        self.actionindependent_mainwindow.setObjectName("actionindependent_mainwindow")
        self.actionexit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/exit.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionexit.setIcon(icon4)
        self.actionexit.setObjectName("actionexit")
        self.mainToolBar.addAction(self.actionembedding_widget)
        self.mainToolBar.addAction(self.actionindependent_widget)
        self.mainToolBar.addAction(self.actionembedding_mainwindow)
        self.mainToolBar.addAction(self.actionindependent_mainwindow)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionexit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.actionexit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "page"))
        self.actionembedding_widget.setText(_translate("MainWindow", "embedding_widget"))
        self.actionindependent_widget.setText(_translate("MainWindow", "independent_widget"))
        self.actionembedding_mainwindow.setText(_translate("MainWindow", "embedding_mainwindow"))
        self.actionindependent_mainwindow.setText(_translate("MainWindow", "independent_mainwindow"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
import res_rc
