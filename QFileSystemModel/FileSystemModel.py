# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filesystemmodel.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileSystemModel(object):
    def setupUi(self, FileSystemModel):
        FileSystemModel.setObjectName("FileSystemModel")
        FileSystemModel.resize(800, 600)
        FileSystemModel.setMinimumSize(QtCore.QSize(800, 600))
        self.centralWidget = QtWidgets.QWidget(FileSystemModel)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_1 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_1.setObjectName("groupBox_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_1)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeView = QtWidgets.QTreeView(self.groupBox_1)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.gridLayout_2.addWidget(self.groupBox_1, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listView = QtWidgets.QListView(self.groupBox_2)
        self.listView.setObjectName("listView")
        self.verticalLayout_2.addWidget(self.listView)
        self.tableView = QtWidgets.QTableView(self.groupBox_2)
        self.tableView.setMinimumSize(QtCore.QSize(0, 0))
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_1 = QtWidgets.QLabel(self.groupBox_3)
        self.label_1.setAutoFillBackground(True)
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setAutoFillBackground(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 0, 1, 2)
        FileSystemModel.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(FileSystemModel)
        self.statusBar.setObjectName("statusBar")
        FileSystemModel.setStatusBar(self.statusBar)

        self.retranslateUi(FileSystemModel)
        QtCore.QMetaObject.connectSlotsByName(FileSystemModel)

    def retranslateUi(self, FileSystemModel):
        _translate = QtCore.QCoreApplication.translate
        FileSystemModel.setWindowTitle(_translate("FileSystemModel", "FileSystemModel"))
        self.groupBox_1.setTitle(_translate("FileSystemModel", "TreeView"))
        self.groupBox_2.setTitle(_translate("FileSystemModel", "List and Table View"))
        self.checkBox.setText(_translate("FileSystemModel", "node"))
