# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combo.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ComboBox(object):
    def setupUi(self, ComboBox):
        ComboBox.setObjectName("ComboBox")
        ComboBox.resize(390, 189)
        self.gridLayout = QtWidgets.QGridLayout(ComboBox)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox1 = QtWidgets.QGroupBox(ComboBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.groupBox1.setFont(font)
        self.groupBox1.setObjectName("groupBox1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox1)
        self.lineEdit.setInputMask("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox1, 0, 0, 1, 2)
        self.groupBox2 = QtWidgets.QGroupBox(ComboBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.groupBox2.setFont(font)
        self.groupBox2.setObjectName("groupBox2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnClear = QtWidgets.QPushButton(self.groupBox2)
        self.btnClear.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/324.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClear.setIcon(icon)
        self.btnClear.setCheckable(False)
        self.btnClear.setObjectName("btnClear")
        self.gridLayout_2.addWidget(self.btnClear, 0, 1, 1, 1)
        self.btnInitialize = QtWidgets.QPushButton(self.groupBox2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/212.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnInitialize.setIcon(icon1)
        self.btnInitialize.setObjectName("btnInitialize")
        self.gridLayout_2.addWidget(self.btnInitialize, 0, 0, 1, 1)
        self.cbEdit = QtWidgets.QCheckBox(self.groupBox2)
        self.cbEdit.setObjectName("cbEdit")
        self.gridLayout_2.addWidget(self.cbEdit, 0, 2, 1, 1)
        self.CBprovince = QtWidgets.QComboBox(self.groupBox2)
        self.CBprovince.setObjectName("CBprovince")
        self.gridLayout_2.addWidget(self.CBprovince, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.groupBox2, 1, 0, 1, 1)
        self.groupBox3 = QtWidgets.QGroupBox(ComboBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.groupBox3.setFont(font)
        self.groupBox3.setObjectName("groupBox3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnCityarea = QtWidgets.QPushButton(self.groupBox3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/aim.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCityarea.setIcon(icon2)
        self.btnCityarea.setObjectName("btnCityarea")
        self.gridLayout_3.addWidget(self.btnCityarea, 0, 0, 1, 1)
        self.CBcity = QtWidgets.QComboBox(self.groupBox3)
        self.CBcity.setObjectName("CBcity")
        self.gridLayout_3.addWidget(self.CBcity, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox3, 1, 1, 1, 1)

        self.retranslateUi(ComboBox)
        QtCore.QMetaObject.connectSlotsByName(ComboBox)

    def retranslateUi(self, ComboBox):
        _translate = QtCore.QCoreApplication.translate
        ComboBox.setWindowTitle(_translate("ComboBox", "Form"))
        self.groupBox1.setTitle(_translate("ComboBox", "select content"))
        self.groupBox2.setTitle(_translate("ComboBox", "simple combox"))
        self.btnClear.setText(_translate("ComboBox", "clear list"))
        self.btnInitialize.setText(_translate("ComboBox", "Initialize list"))
        self.cbEdit.setText(_translate("ComboBox", "edit"))
        self.groupBox3.setTitle(_translate("ComboBox", "user name combox"))
        self.btnCityarea.setText(_translate("ComboBox", "city+area"))
import res_rc
