# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'standarditemmodel.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StandardItemModel(object):
    def setupUi(self, StandardItemModel):
        StandardItemModel.setObjectName("StandardItemModel")
        StandardItemModel.resize(800, 600)
        StandardItemModel.setMinimumSize(QtCore.QSize(800, 600))
        self.centralWidget = QtWidgets.QWidget(StandardItemModel)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.horizontalLayout.addWidget(self.groupBox_2)
        StandardItemModel.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(StandardItemModel)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menuBar.setObjectName("menuBar")
        StandardItemModel.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(StandardItemModel)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        StandardItemModel.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(StandardItemModel)
        self.statusBar.setObjectName("statusBar")
        StandardItemModel.setStatusBar(self.statusBar)
        self.actionfile = QtWidgets.QAction(StandardItemModel)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/open3.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfile.setIcon(icon)
        self.actionfile.setObjectName("actionfile")
        self.actionsave = QtWidgets.QAction(StandardItemModel)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/save1.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionsave.setIcon(icon1)
        self.actionsave.setObjectName("actionsave")
        self.actionmodel_data = QtWidgets.QAction(StandardItemModel)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/copy.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionmodel_data.setIcon(icon2)
        self.actionmodel_data.setObjectName("actionmodel_data")
        self.actionAdd_row = QtWidgets.QAction(StandardItemModel)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/316.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_row.setIcon(icon3)
        self.actionAdd_row.setObjectName("actionAdd_row")
        self.actionInsert_row = QtWidgets.QAction(StandardItemModel)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/306.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsert_row.setIcon(icon4)
        self.actionInsert_row.setObjectName("actionInsert_row")
        self.actionDelete_row = QtWidgets.QAction(StandardItemModel)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/delete1.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_row.setIcon(icon5)
        self.actionDelete_row.setObjectName("actionDelete_row")
        self.actionLeft = QtWidgets.QAction(StandardItemModel)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/508.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLeft.setIcon(icon6)
        self.actionLeft.setObjectName("actionLeft")
        self.actionCenter = QtWidgets.QAction(StandardItemModel)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/510.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCenter.setIcon(icon7)
        self.actionCenter.setObjectName("actionCenter")
        self.actionRight = QtWidgets.QAction(StandardItemModel)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/512.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRight.setIcon(icon8)
        self.actionRight.setObjectName("actionRight")
        self.actionBold = QtWidgets.QAction(StandardItemModel)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/500.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBold.setIcon(icon9)
        self.actionBold.setObjectName("actionBold")
        self.actionExit = QtWidgets.QAction(StandardItemModel)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/exit.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon10)
        self.actionExit.setObjectName("actionExit")
        self.mainToolBar.addAction(self.actionfile)
        self.mainToolBar.addAction(self.actionsave)
        self.mainToolBar.addAction(self.actionmodel_data)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionAdd_row)
        self.mainToolBar.addAction(self.actionInsert_row)
        self.mainToolBar.addAction(self.actionDelete_row)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionLeft)
        self.mainToolBar.addAction(self.actionCenter)
        self.mainToolBar.addAction(self.actionRight)
        self.mainToolBar.addAction(self.actionBold)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionExit)

        self.retranslateUi(StandardItemModel)
        self.actionExit.triggered.connect(StandardItemModel.close)
        QtCore.QMetaObject.connectSlotsByName(StandardItemModel)

    def retranslateUi(self, StandardItemModel):
        _translate = QtCore.QCoreApplication.translate
        StandardItemModel.setWindowTitle(_translate("StandardItemModel", "StandardItemModel"))
        self.groupBox.setTitle(_translate("StandardItemModel", "tableView"))
        self.groupBox_2.setTitle(_translate("StandardItemModel", "plainTextEdit"))
        self.actionfile.setText(_translate("StandardItemModel", "File"))
        self.actionsave.setText(_translate("StandardItemModel", "Save"))
        self.actionmodel_data.setText(_translate("StandardItemModel", "Model data"))
        self.actionAdd_row.setText(_translate("StandardItemModel", "Add row"))
        self.actionInsert_row.setText(_translate("StandardItemModel", "Insert row"))
        self.actionDelete_row.setText(_translate("StandardItemModel", "Delete row"))
        self.actionLeft.setText(_translate("StandardItemModel", "Left"))
        self.actionCenter.setText(_translate("StandardItemModel", "Center"))
        self.actionRight.setText(_translate("StandardItemModel", "Right"))
        self.actionBold.setText(_translate("StandardItemModel", "Bold"))
        self.actionExit.setText(_translate("StandardItemModel", "Exit"))
import res_rc
