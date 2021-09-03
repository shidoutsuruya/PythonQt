# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(400, 300)
        self.menuBar = QtWidgets.QMenuBar(Widget)
        self.menuBar.setObjectName("menuBar")
        Widget.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Widget)
        self.mainToolBar.setObjectName("mainToolBar")
        Widget.addToolBar(self.mainToolBar)
        self.centralWidget = QtWidgets.QWidget(Widget)
        self.centralWidget.setObjectName("centralWidget")
        Widget.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(Widget)
        self.statusBar.setObjectName("statusBar")
        Widget.setStatusBar(self.statusBar)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
