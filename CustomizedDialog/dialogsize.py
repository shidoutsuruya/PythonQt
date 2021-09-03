# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qwdialogsize.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogSize(object):
    def setupUi(self, DialogSize):
        DialogSize.setObjectName("DialogSize")
        DialogSize.resize(393, 121)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogSize)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gbSetRowAndColumn = QtWidgets.QGroupBox(DialogSize)
        self.gbSetRowAndColumn.setObjectName("gbSetRowAndColumn")
        self.gridLayout = QtWidgets.QGridLayout(self.gbSetRowAndColumn)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBoxRow = QtWidgets.QSpinBox(self.gbSetRowAndColumn)
        self.spinBoxRow.setObjectName("spinBoxRow")
        self.gridLayout.addWidget(self.spinBoxRow, 0, 1, 1, 1)
        self.btnOk = QtWidgets.QPushButton(self.gbSetRowAndColumn)
        self.btnOk.setObjectName("btnOk")
        self.gridLayout.addWidget(self.btnOk, 0, 3, 1, 1)
        self.btnCancel = QtWidgets.QPushButton(self.gbSetRowAndColumn)
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout.addWidget(self.btnCancel, 1, 3, 1, 1)
        self.labColumn = QtWidgets.QLabel(self.gbSetRowAndColumn)
        self.labColumn.setAlignment(QtCore.Qt.AlignCenter)
        self.labColumn.setObjectName("labColumn")
        self.gridLayout.addWidget(self.labColumn, 1, 0, 1, 1)
        self.labRow = QtWidgets.QLabel(self.gbSetRowAndColumn)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labRow.setFont(font)
        self.labRow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.labRow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labRow.setAlignment(QtCore.Qt.AlignCenter)
        self.labRow.setObjectName("labRow")
        self.gridLayout.addWidget(self.labRow, 0, 0, 1, 1)
        self.spinBoxColumn = QtWidgets.QSpinBox(self.gbSetRowAndColumn)
        self.spinBoxColumn.setObjectName("spinBoxColumn")
        self.gridLayout.addWidget(self.spinBoxColumn, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.verticalLayout.addWidget(self.gbSetRowAndColumn)

        self.retranslateUi(DialogSize)
        self.btnOk.clicked.connect(DialogSize.accept)
        self.btnCancel.clicked.connect(DialogSize.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogSize)

    def retranslateUi(self, DialogSize):
        _translate = QtCore.QCoreApplication.translate
        DialogSize.setWindowTitle(_translate("DialogSize", "Dialog"))
        self.gbSetRowAndColumn.setTitle(_translate("DialogSize", "set row and column"))
        self.btnOk.setText(_translate("DialogSize", "ok"))
        self.btnCancel.setText(_translate("DialogSize", "cancel"))
        self.labColumn.setText(_translate("DialogSize", "column"))
        self.labRow.setText(_translate("DialogSize", "row"))
