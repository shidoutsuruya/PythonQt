# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qwdialogheaders.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogHeader(object):
    def setupUi(self, DialogHeader):
        DialogHeader.setObjectName("DialogHeader")
        DialogHeader.resize(399, 157)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogHeader)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(DialogHeader)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btnOk = QtWidgets.QPushButton(self.widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/322.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOk.setIcon(icon)
        self.btnOk.setObjectName("btnOk")
        self.gridLayout.addWidget(self.btnOk, 0, 1, 1, 1)
        self.btnCancel = QtWidgets.QPushButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/324.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon1)
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout.addWidget(self.btnCancel, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.widget)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(DialogHeader)
        self.btnOk.clicked.connect(DialogHeader.accept)
        self.btnCancel.clicked.connect(DialogHeader.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogHeader)

    def retranslateUi(self, DialogHeader):
        _translate = QtCore.QCoreApplication.translate
        DialogHeader.setWindowTitle(_translate("DialogHeader", "Dialog"))
        self.groupBox.setTitle(_translate("DialogHeader", "Title"))
        self.btnOk.setText(_translate("DialogHeader", "ok"))
        self.btnCancel.setText(_translate("DialogHeader", "cancel"))
