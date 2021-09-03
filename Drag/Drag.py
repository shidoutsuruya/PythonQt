# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drag.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Drag(object):
    def setupUi(self, Drag):
        Drag.setObjectName("Drag")
        Drag.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Drag)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Drag)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.label = QtWidgets.QLabel(Drag)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Drag)
        QtCore.QMetaObject.connectSlotsByName(Drag)

    def retranslateUi(self, Drag):
        _translate = QtCore.QCoreApplication.translate
        Drag.setWindowTitle(_translate("Drag", "Drag"))
        self.label.setText(_translate("Drag", "TextLabel"))
