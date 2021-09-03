# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qstringlistmodel.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QStringListModel(object):
    def setupUi(self, QStringListModel):
        QStringListModel.setObjectName("QStringListModel")
        QStringListModel.resize(803, 607)
        QStringListModel.setMinimumSize(QtCore.QSize(800, 600))
        self.gridLayout_2 = QtWidgets.QGridLayout(QStringListModel)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(QStringListModel)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnSetList = QtWidgets.QPushButton(self.groupBox)
        self.btnSetList.setObjectName("btnSetList")
        self.gridLayout_3.addWidget(self.btnSetList, 0, 0, 1, 1)
        self.btnAdd = QtWidgets.QPushButton(self.groupBox)
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayout_3.addWidget(self.btnAdd, 1, 0, 1, 1)
        self.btnInsert = QtWidgets.QPushButton(self.groupBox)
        self.btnInsert.setObjectName("btnInsert")
        self.gridLayout_3.addWidget(self.btnInsert, 1, 1, 1, 1)
        self.btnDelete = QtWidgets.QPushButton(self.groupBox)
        self.btnDelete.setObjectName("btnDelete")
        self.gridLayout_3.addWidget(self.btnDelete, 2, 0, 1, 1)
        self.btnClear = QtWidgets.QPushButton(self.groupBox)
        self.btnClear.setObjectName("btnClear")
        self.gridLayout_3.addWidget(self.btnClear, 2, 1, 1, 1)
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setObjectName("listView")
        self.gridLayout_3.addWidget(self.listView, 3, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 2, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(QStringListModel)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnClearText = QtWidgets.QPushButton(self.groupBox_2)
        self.btnClearText.setObjectName("btnClearText")
        self.verticalLayout.addWidget(self.btnClearText)
        self.btnShowList = QtWidgets.QPushButton(self.groupBox_2)
        self.btnShowList.setObjectName("btnShowList")
        self.verticalLayout.addWidget(self.btnShowList)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 2, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(QStringListModel)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 3)

        self.retranslateUi(QStringListModel)
        QtCore.QMetaObject.connectSlotsByName(QStringListModel)

    def retranslateUi(self, QStringListModel):
        _translate = QtCore.QCoreApplication.translate
        QStringListModel.setWindowTitle(_translate("QStringListModel", "QStringListModel"))
        self.groupBox.setTitle(_translate("QStringListModel", "QListView"))
        self.btnSetList.setText(_translate("QStringListModel", "set list"))
        self.btnAdd.setText(_translate("QStringListModel", "add"))
        self.btnInsert.setText(_translate("QStringListModel", "insert"))
        self.btnDelete.setText(_translate("QStringListModel", "delete"))
        self.btnClear.setText(_translate("QStringListModel", "clear"))
        self.groupBox_2.setTitle(_translate("QStringListModel", "QPlainTextEdit"))
        self.btnClearText.setText(_translate("QStringListModel", "clear "))
        self.btnShowList.setText(_translate("QStringListModel", "show list"))
        self.label.setText(_translate("QStringListModel", "TextLabel"))
