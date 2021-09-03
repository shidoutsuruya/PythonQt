# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qwdialogheaders.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_headers(object):
    def setupUi(self, headers):
        headers.setObjectName("headers")
        headers.resize(600, 800)
        headers.setMinimumSize(QtCore.QSize(400, 400))
        self.horizontalLayout = QtWidgets.QHBoxLayout(headers)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(headers)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listView = QtWidgets.QListView(self.widget)
        self.listView.setObjectName("listView")
        self.verticalLayout_2.addWidget(self.listView)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(headers)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnOk = QtWidgets.QPushButton(self.widget_2)
        self.btnOk.setObjectName("btnOk")
        self.verticalLayout.addWidget(self.btnOk)
        self.btnCancel = QtWidgets.QPushButton(self.widget_2)
        self.btnCancel.setObjectName("btnCancel")
        self.verticalLayout.addWidget(self.btnCancel)
        self.horizontalLayout.addWidget(self.widget_2)

        self.retranslateUi(headers)
        self.btnOk.clicked.connect(headers.accept)
        self.btnCancel.clicked.connect(headers.reject)
        QtCore.QMetaObject.connectSlotsByName(headers)

    def retranslateUi(self, headers):
        _translate = QtCore.QCoreApplication.translate
        headers.setWindowTitle(_translate("headers", "Dialog"))
        self.btnOk.setText(_translate("headers", "ok"))
        self.btnCancel.setText(_translate("headers", "cancel"))
