# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'event.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Event(object):
    def setupUi(self, Event):
        Event.setObjectName("Event")
        Event.resize(453, 285)
        self.centralWidget = QtWidgets.QWidget(Event)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(6, 6, 600, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(80, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_1.setGeometry(QtCore.QRect(40, 125, 80, 30))
        self.pushButton_1.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(6, 215, 80, 30))
        self.pushButton_2.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        Event.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Event)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 453, 17))
        self.menuBar.setObjectName("menuBar")
        Event.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Event)
        self.mainToolBar.setObjectName("mainToolBar")
        Event.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Event)
        self.statusBar.setObjectName("statusBar")
        Event.setStatusBar(self.statusBar)

        self.retranslateUi(Event)
        QtCore.QMetaObject.connectSlotsByName(Event)

    def retranslateUi(self, Event):
        _translate = QtCore.QCoreApplication.translate
        Event.setWindowTitle(_translate("Event", "Event"))
        self.label.setText(_translate("Event", "clicke this"))
        self.pushButton_1.setText(_translate("Event", "hello1"))
        self.pushButton_2.setText(_translate("Event", "hello2"))
