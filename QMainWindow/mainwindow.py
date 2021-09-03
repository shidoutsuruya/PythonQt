# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 17))
        self.menuBar.setObjectName("menuBar")
        self.menuFile_F = QtWidgets.QMenu(self.menuBar)
        self.menuFile_F.setObjectName("menuFile_F")
        self.menuEdit_E = QtWidgets.QMenu(self.menuBar)
        self.menuEdit_E.setObjectName("menuEdit_E")
        self.menuFormat_M = QtWidgets.QMenu(self.menuBar)
        self.menuFormat_M.setObjectName("menuFormat_M")
        self.menulanguage = QtWidgets.QMenu(self.menuFormat_M)
        self.menulanguage.setObjectName("menulanguage")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setAutoFillBackground(False)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/122.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionopen.setIcon(icon)
        self.actionopen.setObjectName("actionopen")
        self.actioncut = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/200.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncut.setIcon(icon1)
        self.actioncut.setObjectName("actioncut")
        self.actioncopy = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/202.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncopy.setIcon(icon2)
        self.actioncopy.setObjectName("actioncopy")
        self.actionpaste = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/204.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionpaste.setIcon(icon3)
        self.actionpaste.setObjectName("actionpaste")
        self.actionfont_bold = QtWidgets.QAction(MainWindow)
        self.actionfont_bold.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/500.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfont_bold.setIcon(icon4)
        self.actionfont_bold.setObjectName("actionfont_bold")
        self.actionitalic = QtWidgets.QAction(MainWindow)
        self.actionitalic.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/502.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionitalic.setIcon(icon5)
        self.actionitalic.setObjectName("actionitalic")
        self.actionunderline = QtWidgets.QAction(MainWindow)
        self.actionunderline.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/images/504.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionunderline.setIcon(icon6)
        self.actionunderline.setObjectName("actionunderline")
        self.actionclose = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionclose.setIcon(icon7)
        self.actionclose.setObjectName("actionclose")
        self.actiontoggletext = QtWidgets.QAction(MainWindow)
        self.actiontoggletext.setObjectName("actiontoggletext")
        self.actionclear = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/images/212.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionclear.setIcon(icon8)
        self.actionclear.setObjectName("actionclear")
        self.actionundo = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/images/206.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionundo.setIcon(icon9)
        self.actionundo.setObjectName("actionundo")
        self.actionredo = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/images/208.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionredo.setIcon(icon10)
        self.actionredo.setObjectName("actionredo")
        self.actionselect_all = QtWidgets.QAction(MainWindow)
        self.actionselect_all.setObjectName("actionselect_all")
        self.actionnew_file = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/images/100.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionnew_file.setIcon(icon11)
        self.actionnew_file.setObjectName("actionnew_file")
        self.actionfile_save = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/images/104.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfile_save.setIcon(icon12)
        self.actionfile_save.setObjectName("actionfile_save")
        self.actionchinese = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/images/CN.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionchinese.setIcon(icon13)
        self.actionchinese.setObjectName("actionchinese")
        self.actionenglish = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/images/timg2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionenglish.setIcon(icon14)
        self.actionenglish.setObjectName("actionenglish")
        self.menuFile_F.addAction(self.actionopen)
        self.menuFile_F.addAction(self.actionnew_file)
        self.menuFile_F.addAction(self.actionfile_save)
        self.menuFile_F.addSeparator()
        self.menuFile_F.addAction(self.actionclose)
        self.menuEdit_E.addAction(self.actioncut)
        self.menuEdit_E.addAction(self.actioncopy)
        self.menuEdit_E.addAction(self.actionpaste)
        self.menuEdit_E.addSeparator()
        self.menuEdit_E.addAction(self.actionundo)
        self.menuEdit_E.addAction(self.actionredo)
        self.menuEdit_E.addSeparator()
        self.menuEdit_E.addAction(self.actionselect_all)
        self.menuEdit_E.addAction(self.actionclear)
        self.menulanguage.addAction(self.actionenglish)
        self.menulanguage.addAction(self.actionchinese)
        self.menuFormat_M.addAction(self.actionfont_bold)
        self.menuFormat_M.addAction(self.actionitalic)
        self.menuFormat_M.addAction(self.actionunderline)
        self.menuFormat_M.addSeparator()
        self.menuFormat_M.addAction(self.actiontoggletext)
        self.menuFormat_M.addAction(self.menulanguage.menuAction())
        self.menuBar.addAction(self.menuFile_F.menuAction())
        self.menuBar.addAction(self.menuEdit_E.menuAction())
        self.menuBar.addAction(self.menuFormat_M.menuAction())
        self.mainToolBar.addAction(self.actionopen)
        self.mainToolBar.addAction(self.actionnew_file)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actioncut)
        self.mainToolBar.addAction(self.actioncopy)
        self.mainToolBar.addAction(self.actionpaste)
        self.mainToolBar.addAction(self.actionfile_save)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionfont_bold)
        self.mainToolBar.addAction(self.actionitalic)
        self.mainToolBar.addAction(self.actionunderline)
        self.mainToolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.actioncut.triggered.connect(self.textEdit.cut)
        self.actionpaste.triggered.connect(self.textEdit.paste)
        self.actioncopy.triggered.connect(self.textEdit.copy)
        self.actionundo.triggered.connect(self.textEdit.undo)
        self.actionredo.triggered.connect(self.textEdit.redo)
        self.actionclear.triggered.connect(self.textEdit.clear)
        self.actionclose.triggered.connect(MainWindow.close)
        self.actionselect_all.triggered.connect(self.textEdit.selectAll)
        self.textEdit.undoAvailable['bool'].connect(self.actionundo.setEnabled)
        self.textEdit.redoAvailable['bool'].connect(self.actionredo.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile_F.setTitle(_translate("MainWindow", "File(F)"))
        self.menuEdit_E.setTitle(_translate("MainWindow", "Edit(E)"))
        self.menuFormat_M.setTitle(_translate("MainWindow", "Format(M)"))
        self.menulanguage.setTitle(_translate("MainWindow", "language"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionopen.setToolTip(_translate("MainWindow", "open files"))
        self.actioncut.setText(_translate("MainWindow", "cut"))
        self.actioncut.setToolTip(_translate("MainWindow", "cut"))
        self.actioncopy.setText(_translate("MainWindow", "copy"))
        self.actionpaste.setText(_translate("MainWindow", "paste"))
        self.actionfont_bold.setText(_translate("MainWindow", "font_bold"))
        self.actionitalic.setText(_translate("MainWindow", "italic"))
        self.actionunderline.setText(_translate("MainWindow", "underline"))
        self.actionclose.setText(_translate("MainWindow", "close"))
        self.actiontoggletext.setText(_translate("MainWindow", "toggletext"))
        self.actionclear.setText(_translate("MainWindow", "clear"))
        self.actionundo.setText(_translate("MainWindow", "undo"))
        self.actionredo.setText(_translate("MainWindow", "redo"))
        self.actionselect_all.setText(_translate("MainWindow", "select_all"))
        self.actionnew_file.setText(_translate("MainWindow", "new_file"))
        self.actionfile_save.setText(_translate("MainWindow", "file_save"))
        self.actionchinese.setText(_translate("MainWindow", "chinese"))
        self.actionenglish.setText(_translate("MainWindow", "english"))
import res_rc