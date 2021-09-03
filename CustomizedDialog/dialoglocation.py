# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qwdialoglocation.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Locate(object):
    def setupUi(self, Locate):
        Locate.setObjectName("Locate")
        Locate.resize(303, 174)
        self.gridLayout = QtWidgets.QGridLayout(Locate)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Locate)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinBoxRow = QtWidgets.QSpinBox(Locate)
        self.spinBoxRow.setObjectName("spinBoxRow")
        self.gridLayout.addWidget(self.spinBoxRow, 0, 1, 1, 1)
        self.checkBoxRow = QtWidgets.QCheckBox(Locate)
        self.checkBoxRow.setObjectName("checkBoxRow")
        self.gridLayout.addWidget(self.checkBoxRow, 0, 2, 1, 1)
        self.btnOk = QtWidgets.QPushButton(Locate)
        self.btnOk.setObjectName("btnOk")
        self.gridLayout.addWidget(self.btnOk, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(Locate)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBoxColumn = QtWidgets.QSpinBox(Locate)
        self.spinBoxColumn.setObjectName("spinBoxColumn")
        self.gridLayout.addWidget(self.spinBoxColumn, 1, 1, 1, 1)
        self.checkBoxColumn = QtWidgets.QCheckBox(Locate)
        self.checkBoxColumn.setObjectName("checkBoxColumn")
        self.gridLayout.addWidget(self.checkBoxColumn, 1, 2, 1, 1)
        self.btnCancel = QtWidgets.QPushButton(Locate)
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout.addWidget(self.btnCancel, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(Locate)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Locate)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 2)

        self.retranslateUi(Locate)
        self.btnOk.clicked.connect(Locate.accept)
        self.btnCancel.clicked.connect(Locate.reject)
        QtCore.QMetaObject.connectSlotsByName(Locate)

    def retranslateUi(self, Locate):
        _translate = QtCore.QCoreApplication.translate
        Locate.setWindowTitle(_translate("Locate", "Locate"))
        self.label.setText(_translate("Locate", "row"))
        self.checkBoxRow.setText(_translate("Locate", "row increase"))
        self.btnOk.setText(_translate("Locate", "ok"))
        self.label_2.setText(_translate("Locate", "column"))
        self.checkBoxColumn.setText(_translate("Locate", "column increase"))
        self.btnCancel.setText(_translate("Locate", "cancel"))
        self.label_3.setText(_translate("Locate", "set text"))
