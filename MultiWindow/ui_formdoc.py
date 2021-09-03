# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qwformdoc.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DOC(object):
    def setupUi(self, DOC):
        DOC.setObjectName("DOC")
        DOC.resize(395, 263)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(DOC)
        self.plainTextEdit.setGeometry(QtCore.QRect(6, 6, 256, 192))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.actionOpen = QtWidgets.QAction(DOC)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/open3.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionCut = QtWidgets.QAction(DOC)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/cut.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon1)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(DOC)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/copy.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon2)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(DOC)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/paste.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon3)
        self.actionPaste.setObjectName("actionPaste")
        self.actionFont = QtWidgets.QAction(DOC)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/724.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFont.setIcon(icon4)
        self.actionFont.setObjectName("actionFont")
        self.actionExit = QtWidgets.QAction(DOC)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/exit.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon5)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(DOC)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/undo.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon6)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(DOC)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/redo.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon7)
        self.actionRedo.setObjectName("actionRedo")

        self.retranslateUi(DOC)
        self.actionCopy.triggered.connect(self.plainTextEdit.copy)
        self.actionExit.triggered.connect(DOC.close)
        self.actionUndo.triggered.connect(self.plainTextEdit.undo)
        self.actionRedo.triggered.connect(self.plainTextEdit.redo)
        self.actionPaste.triggered.connect(self.plainTextEdit.paste)
        self.actionCut.triggered.connect(self.plainTextEdit.cut)
        QtCore.QMetaObject.connectSlotsByName(DOC)

    def retranslateUi(self, DOC):
        _translate = QtCore.QCoreApplication.translate
        DOC.setWindowTitle(_translate("DOC", "Form"))
        self.actionOpen.setText(_translate("DOC", "Open"))
        self.actionCut.setText(_translate("DOC", "Cut"))
        self.actionCopy.setText(_translate("DOC", "Copy"))
        self.actionPaste.setText(_translate("DOC", "Paste"))
        self.actionFont.setText(_translate("DOC", "Font"))
        self.actionExit.setText(_translate("DOC", "Exit"))
        self.actionUndo.setText(_translate("DOC", "Undo"))
        self.actionRedo.setText(_translate("DOC", "Redo"))
import res_rc
