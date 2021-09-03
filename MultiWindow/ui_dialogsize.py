# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qwdialogsize.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_size(object):
    def setupUi(self, size):
        size.setObjectName("size")
        size.resize(398, 200)
        size.setMinimumSize(QtCore.QSize(300, 200))
        self.horizontalLayout = QtWidgets.QHBoxLayout(size)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(size)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.labelColumn = QtWidgets.QLabel(self.widget)
        self.labelColumn.setAlignment(QtCore.Qt.AlignCenter)
        self.labelColumn.setObjectName("labelColumn")
        self.gridLayout.addWidget(self.labelColumn, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.spinBoxRow = QtWidgets.QSpinBox(self.widget)
        self.spinBoxRow.setObjectName("spinBoxRow")
        self.gridLayout.addWidget(self.spinBoxRow, 0, 2, 1, 1)
        self.spinBoxColumn = QtWidgets.QSpinBox(self.widget)
        self.spinBoxColumn.setObjectName("spinBoxColumn")
        self.gridLayout.addWidget(self.spinBoxColumn, 2, 2, 1, 1)
        self.labelRow = QtWidgets.QLabel(self.widget)
        self.labelRow.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRow.setObjectName("labelRow")
        self.gridLayout.addWidget(self.labelRow, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(3, 1)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(size)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(20, 8, 26, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnOk = QtWidgets.QPushButton(self.widget_2)
        self.btnOk.setObjectName("btnOk")
        self.verticalLayout.addWidget(self.btnOk)
        self.btnCancel = QtWidgets.QPushButton(self.widget_2)
        self.btnCancel.setObjectName("btnCancel")
        self.verticalLayout.addWidget(self.btnCancel)
        self.horizontalLayout.addWidget(self.widget_2)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(size)
        self.btnOk.clicked.connect(size.accept)
        self.btnCancel.clicked.connect(size.reject)
        QtCore.QMetaObject.connectSlotsByName(size)

    def retranslateUi(self, size):
        _translate = QtCore.QCoreApplication.translate
        size.setWindowTitle(_translate("size", "Dialog"))
        self.labelColumn.setText(_translate("size", "column"))
        self.labelRow.setText(_translate("size", "row"))
        self.btnOk.setText(_translate("size", "ok"))
        self.btnCancel.setText(_translate("size", "cancel"))
