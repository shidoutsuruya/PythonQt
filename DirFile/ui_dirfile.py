# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dirfile.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DirFile(object):
    def setupUi(self, DirFile):
        DirFile.setObjectName("DirFile")
        DirFile.resize(1000, 800)
        DirFile.setMinimumSize(QtCore.QSize(1000, 800))
        self.centralWidget = QtWidgets.QWidget(DirFile)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolBox = QtWidgets.QToolBox(self.centralWidget)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 328, 665))
        self.page.setObjectName("page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_10 = QtWidgets.QGroupBox(self.page)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_11.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.btnFile_exists = QtWidgets.QPushButton(self.groupBox_10)
        self.btnFile_exists.setMinimumSize(QtCore.QSize(0, 30))
        self.btnFile_exists.setObjectName("btnFile_exists")
        self.verticalLayout_11.addWidget(self.btnFile_exists)
        self.btnFile_copy = QtWidgets.QPushButton(self.groupBox_10)
        self.btnFile_copy.setMinimumSize(QtCore.QSize(0, 30))
        self.btnFile_copy.setObjectName("btnFile_copy")
        self.verticalLayout_11.addWidget(self.btnFile_copy)
        self.btnFile_remove = QtWidgets.QPushButton(self.groupBox_10)
        self.btnFile_remove.setMinimumSize(QtCore.QSize(0, 30))
        self.btnFile_remove.setObjectName("btnFile_remove")
        self.verticalLayout_11.addWidget(self.btnFile_remove)
        self.btnFile_rename = QtWidgets.QPushButton(self.groupBox_10)
        self.btnFile_rename.setMinimumSize(QtCore.QSize(0, 30))
        self.btnFile_rename.setObjectName("btnFile_rename")
        self.verticalLayout_11.addWidget(self.btnFile_rename)
        self.btnFile_copy.raise_()
        self.btnFile_remove.raise_()
        self.btnFile_rename.raise_()
        self.btnFile_exists.raise_()
        self.horizontalLayout_2.addWidget(self.groupBox_10)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 328, 665))
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_4.setContentsMargins(5, 3, 5, 3)
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnInfo_baseName = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_baseName.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_baseName.setObjectName("btnInfo_baseName")
        self.gridLayout_4.addWidget(self.btnInfo_baseName, 3, 0, 1, 1)
        self.btnInfo_absPath = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_absPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_absPath.setObjectName("btnInfo_absPath")
        self.gridLayout_4.addWidget(self.btnInfo_absPath, 0, 1, 1, 1)
        self.btnInfo_absFilePath = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_absFilePath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_absFilePath.setObjectName("btnInfo_absFilePath")
        self.gridLayout_4.addWidget(self.btnInfo_absFilePath, 0, 0, 1, 1)
        self.btnInfo_baseName2 = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_baseName2.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_baseName2.setObjectName("btnInfo_baseName2")
        self.gridLayout_4.addWidget(self.btnInfo_baseName2, 3, 1, 1, 1)
        self.btnInfo_isDir = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_isDir.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_isDir.setObjectName("btnInfo_isDir")
        self.gridLayout_4.addWidget(self.btnInfo_isDir, 6, 0, 1, 1)
        self.btnInfo_isFile = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_isFile.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_isFile.setObjectName("btnInfo_isFile")
        self.gridLayout_4.addWidget(self.btnInfo_isFile, 6, 1, 1, 1)
        self.btnInfo_isExec = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_isExec.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_isExec.setObjectName("btnInfo_isExec")
        self.gridLayout_4.addWidget(self.btnInfo_isExec, 7, 0, 1, 1)
        self.btnInfo_lastModified = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_lastModified.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_lastModified.setObjectName("btnInfo_lastModified")
        self.gridLayout_4.addWidget(self.btnInfo_lastModified, 8, 0, 1, 1)
        self.btnInfo_lastRead = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_lastRead.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_lastRead.setObjectName("btnInfo_lastRead")
        self.gridLayout_4.addWidget(self.btnInfo_lastRead, 8, 1, 1, 1)
        self.btnInfo_fileName = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_fileName.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_fileName.setObjectName("btnInfo_fileName")
        self.gridLayout_4.addWidget(self.btnInfo_fileName, 1, 0, 1, 1)
        self.btnInfo_exists2 = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_exists2.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_exists2.setObjectName("btnInfo_exists2")
        self.gridLayout_4.addWidget(self.btnInfo_exists2, 10, 1, 1, 1)
        self.btnInfo_suffix = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_suffix.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_suffix.setObjectName("btnInfo_suffix")
        self.gridLayout_4.addWidget(self.btnInfo_suffix, 4, 0, 1, 1)
        self.btnInfo_exists = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_exists.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_exists.setObjectName("btnInfo_exists")
        self.gridLayout_4.addWidget(self.btnInfo_exists, 10, 0, 1, 1)
        self.btnInfo_suffix2 = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_suffix2.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_suffix2.setObjectName("btnInfo_suffix2")
        self.gridLayout_4.addWidget(self.btnInfo_suffix2, 4, 1, 1, 1)
        self.btnInfo_filePath = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_filePath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_filePath.setObjectName("btnInfo_filePath")
        self.gridLayout_4.addWidget(self.btnInfo_filePath, 1, 1, 1, 1)
        self.btnInfo_path = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_path.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_path.setObjectName("btnInfo_path")
        self.gridLayout_4.addWidget(self.btnInfo_path, 2, 1, 1, 1)
        self.btnInfo_size = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_size.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_size.setObjectName("btnInfo_size")
        self.gridLayout_4.addWidget(self.btnInfo_size, 2, 0, 1, 1)
        self.btnInfo_birthTime = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_birthTime.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_birthTime.setObjectName("btnInfo_birthTime")
        self.gridLayout_4.addWidget(self.btnInfo_birthTime, 7, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_6)
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 328, 665))
        self.page_3.setObjectName("page_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.page_3)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btnDir_homePath = QtWidgets.QPushButton(self.groupBox)
        self.btnDir_homePath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_homePath.setObjectName("btnDir_homePath")
        self.gridLayout_5.addWidget(self.btnDir_homePath, 1, 0, 1, 1)
        self.btnDir_tempPath = QtWidgets.QPushButton(self.groupBox)
        self.btnDir_tempPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_tempPath.setObjectName("btnDir_tempPath")
        self.gridLayout_5.addWidget(self.btnDir_tempPath, 0, 0, 1, 1)
        self.btnDir_rootPath = QtWidgets.QPushButton(self.groupBox)
        self.btnDir_rootPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_rootPath.setObjectName("btnDir_rootPath")
        self.gridLayout_5.addWidget(self.btnDir_rootPath, 0, 1, 1, 1)
        self.btnDir_drives = QtWidgets.QPushButton(self.groupBox)
        self.btnDir_drives.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_drives.setObjectName("btnDir_drives")
        self.gridLayout_5.addWidget(self.btnDir_drives, 1, 1, 1, 1)
        self.btnDir_curPath = QtWidgets.QPushButton(self.groupBox)
        self.btnDir_curPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_curPath.setObjectName("btnDir_curPath")
        self.gridLayout_5.addWidget(self.btnDir_curPath, 2, 0, 1, 1)
        self.btnDir_setCurPath = QtWidgets.QPushButton(self.groupBox)
        self.btnDir_setCurPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_setCurPath.setObjectName("btnDir_setCurPath")
        self.gridLayout_5.addWidget(self.btnDir_setCurPath, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnDir_mkdir = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDir_mkdir.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_mkdir.setObjectName("btnDir_mkdir")
        self.gridLayout_3.addWidget(self.btnDir_mkdir, 0, 0, 1, 1)
        self.btnDir_remove = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDir_remove.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_remove.setObjectName("btnDir_remove")
        self.gridLayout_3.addWidget(self.btnDir_remove, 2, 0, 1, 1)
        self.btnDir_rename = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDir_rename.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_rename.setObjectName("btnDir_rename")
        self.gridLayout_3.addWidget(self.btnDir_rename, 2, 1, 1, 1)
        self.btnDir_setPath = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDir_setPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_setPath.setObjectName("btnDir_setPath")
        self.gridLayout_3.addWidget(self.btnDir_setPath, 3, 0, 1, 1)
        self.btnDir_rmdir = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDir_rmdir.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_rmdir.setObjectName("btnDir_rmdir")
        self.gridLayout_3.addWidget(self.btnDir_rmdir, 0, 1, 1, 1)
        self.btnDir_removeALL = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDir_removeALL.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_removeALL.setObjectName("btnDir_removeALL")
        self.gridLayout_3.addWidget(self.btnDir_removeALL, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.btnDir_absPath = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_absPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_absPath.setObjectName("btnDir_absPath")
        self.gridLayout_6.addWidget(self.btnDir_absPath, 0, 1, 1, 1)
        self.btnDir_canonPath = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_canonPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_canonPath.setObjectName("btnDir_canonPath")
        self.gridLayout_6.addWidget(self.btnDir_canonPath, 1, 0, 1, 1)
        self.btnDir_filePath = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_filePath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_filePath.setObjectName("btnDir_filePath")
        self.gridLayout_6.addWidget(self.btnDir_filePath, 1, 1, 1, 1)
        self.btnDir_dirName = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_dirName.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_dirName.setObjectName("btnDir_dirName")
        self.gridLayout_6.addWidget(self.btnDir_dirName, 2, 1, 1, 1)
        self.btnDir_exists = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_exists.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_exists.setObjectName("btnDir_exists")
        self.gridLayout_6.addWidget(self.btnDir_exists, 2, 0, 1, 1)
        self.btnDir_absFilePath = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_absFilePath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_absFilePath.setObjectName("btnDir_absFilePath")
        self.gridLayout_6.addWidget(self.btnDir_absFilePath, 0, 0, 1, 1)
        self.btnDir_listFile = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_listFile.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_listFile.setObjectName("btnDir_listFile")
        self.gridLayout_6.addWidget(self.btnDir_listFile, 3, 1, 1, 1)
        self.btnDir_listDir = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_listDir.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_listDir.setObjectName("btnDir_listDir")
        self.gridLayout_6.addWidget(self.btnDir_listDir, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 328, 665))
        self.page_4.setObjectName("page_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_11 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_11)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btnWatch_addDir = QtWidgets.QPushButton(self.groupBox_11)
        self.btnWatch_addDir.setMinimumSize(QtCore.QSize(0, 30))
        self.btnWatch_addDir.setObjectName("btnWatch_addDir")
        self.verticalLayout_6.addWidget(self.btnWatch_addDir)
        self.btnWatch_addFiles = QtWidgets.QPushButton(self.groupBox_11)
        self.btnWatch_addFiles.setMinimumSize(QtCore.QSize(0, 30))
        self.btnWatch_addFiles.setObjectName("btnWatch_addFiles")
        self.verticalLayout_6.addWidget(self.btnWatch_addFiles)
        self.btnWatch_remove = QtWidgets.QPushButton(self.groupBox_11)
        self.btnWatch_remove.setMinimumSize(QtCore.QSize(0, 30))
        self.btnWatch_remove.setObjectName("btnWatch_remove")
        self.verticalLayout_6.addWidget(self.btnWatch_remove)
        self.btnWatch_dirs = QtWidgets.QPushButton(self.groupBox_11)
        self.btnWatch_dirs.setMinimumSize(QtCore.QSize(0, 30))
        self.btnWatch_dirs.setObjectName("btnWatch_dirs")
        self.verticalLayout_6.addWidget(self.btnWatch_dirs)
        self.btnWatch_files = QtWidgets.QPushButton(self.groupBox_11)
        self.btnWatch_files.setMinimumSize(QtCore.QSize(0, 30))
        self.btnWatch_files.setObjectName("btnWatch_files")
        self.verticalLayout_6.addWidget(self.btnWatch_files)
        self.verticalLayout_2.addWidget(self.groupBox_11)
        self.toolBox.addItem(self.page_4, "")
        self.gridLayout_2.addWidget(self.toolBox, 0, 0, 2, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralWidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSelectFile = QtWidgets.QPushButton(self.widget_2)
        self.btnSelectFile.setObjectName("btnSelectFile")
        self.horizontalLayout.addWidget(self.btnSelectFile)
        self.btnSelectDirectory = QtWidgets.QPushButton(self.widget_2)
        self.btnSelectDirectory.setObjectName("btnSelectDirectory")
        self.horizontalLayout.addWidget(self.btnSelectDirectory)
        self.btnClear = QtWidgets.QPushButton(self.widget_2)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout.addWidget(self.btnClear)
        self.btnExit = QtWidgets.QPushButton(self.widget_2)
        self.btnExit.setObjectName("btnExit")
        self.horizontalLayout.addWidget(self.btnExit)
        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditDir = QtWidgets.QLineEdit(self.widget)
        self.lineEditDir.setObjectName("lineEditDir")
        self.gridLayout.addWidget(self.lineEditDir, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditFile = QtWidgets.QLineEdit(self.widget)
        self.lineEditFile.setObjectName("lineEditFile")
        self.gridLayout.addWidget(self.lineEditFile, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 1, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        DirFile.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(DirFile)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 17))
        self.menuBar.setObjectName("menuBar")
        DirFile.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(DirFile)
        self.statusBar.setObjectName("statusBar")
        DirFile.setStatusBar(self.statusBar)

        self.retranslateUi(DirFile)
        self.toolBox.setCurrentIndex(1)
        self.btnExit.clicked.connect(DirFile.close)
        self.btnClear.clicked.connect(self.lineEditDir.clear)
        self.btnClear.clicked.connect(self.lineEditFile.clear)
        self.btnClear.clicked.connect(self.plainTextEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(DirFile)

    def retranslateUi(self, DirFile):
        _translate = QtCore.QCoreApplication.translate
        DirFile.setWindowTitle(_translate("DirFile", "DirFile"))
        self.groupBox_10.setTitle(_translate("DirFile", "static function"))
        self.btnFile_exists.setToolTip(_translate("DirFile", "Returns true if the file specified by fileName exists; otherwise returns false."))
        self.btnFile_exists.setText(_translate("DirFile", "exists()"))
        self.btnFile_copy.setToolTip(_translate("DirFile", "Copies the file fileName to newName."))
        self.btnFile_copy.setText(_translate("DirFile", "copy()"))
        self.btnFile_remove.setToolTip(_translate("DirFile", "Removes the file specified by the fileName given."))
        self.btnFile_remove.setText(_translate("DirFile", "remove()"))
        self.btnFile_rename.setToolTip(_translate("DirFile", "Renames the file oldName to newName. "))
        self.btnFile_rename.setText(_translate("DirFile", "rename()"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("DirFile", "QFile"))
        self.groupBox_6.setTitle(_translate("DirFile", "file info"))
        self.btnInfo_baseName.setToolTip(_translate("DirFile", "The base name consists of all characters in the file up to (but not including) the first \'.\' character"))
        self.btnInfo_baseName.setText(_translate("DirFile", "baseName()"))
        self.btnInfo_absPath.setToolTip(_translate("DirFile", "Returns a file\'s path absolute path. This doesn\'t include the file name"))
        self.btnInfo_absPath.setText(_translate("DirFile", "absolutePath() "))
        self.btnInfo_absFilePath.setToolTip(_translate("DirFile", "Returns an absolute path including the file name"))
        self.btnInfo_absFilePath.setText(_translate("DirFile", "absoluteFilePath()"))
        self.btnInfo_baseName2.setToolTip(_translate("DirFile", "The complete base name consists of all characters in the file up to (but not including) the last \'.\' character"))
        self.btnInfo_baseName2.setText(_translate("DirFile", "completeBaseName()"))
        self.btnInfo_isDir.setToolTip(_translate("DirFile", "Returns true if this object points to a directory or to a symbolic link to a directory; otherwise returns false"))
        self.btnInfo_isDir.setText(_translate("DirFile", "isDir()"))
        self.btnInfo_isFile.setToolTip(_translate("DirFile", "Returns true if this object points to a file or to a symbolic link to a file"))
        self.btnInfo_isFile.setText(_translate("DirFile", "isFile()"))
        self.btnInfo_isExec.setToolTip(_translate("DirFile", "Returns true if the file is executable; otherwise returns false."))
        self.btnInfo_isExec.setText(_translate("DirFile", "isExecutable()"))
        self.btnInfo_lastModified.setToolTip(_translate("DirFile", "Returns the date and time when the file was last modified."))
        self.btnInfo_lastModified.setText(_translate("DirFile", "lastModified()"))
        self.btnInfo_lastRead.setToolTip(_translate("DirFile", "Returns the date and time when the file was last read (accessed)."))
        self.btnInfo_lastRead.setText(_translate("DirFile", "lastRead()"))
        self.btnInfo_fileName.setToolTip(_translate("DirFile", "Returns the name of the file, excluding the path."))
        self.btnInfo_fileName.setText(_translate("DirFile", "fileName()"))
        self.btnInfo_exists2.setToolTip(_translate("DirFile", "Returns true if the file exists; otherwise returns false"))
        self.btnInfo_exists2.setText(_translate("DirFile", "exists()"))
        self.btnInfo_suffix.setToolTip(_translate("DirFile", "The suffix consists of all characters in the file after (but not including) the last \'.\'"))
        self.btnInfo_suffix.setText(_translate("DirFile", "suffix()"))
        self.btnInfo_exists.setToolTip(_translate("DirFile", "Returns true if the file exists; otherwise returns false"))
        self.btnInfo_exists.setText(_translate("DirFile", "static exists()"))
        self.btnInfo_suffix2.setToolTip(_translate("DirFile", "The complete suffix consists of all characters in the file after (but not including) the first \'.\'"))
        self.btnInfo_suffix2.setText(_translate("DirFile", "completeSuffix()"))
        self.btnInfo_filePath.setToolTip(_translate("DirFile", "Returns the file name, including the path (which may be absolute or relative)."))
        self.btnInfo_filePath.setText(_translate("DirFile", "filePath()"))
        self.btnInfo_path.setToolTip(_translate("DirFile", "Returns the file\'s path. This doesn\'t include the file name."))
        self.btnInfo_path.setText(_translate("DirFile", "path()"))
        self.btnInfo_size.setToolTip(_translate("DirFile", "Returns the file size in bytes."))
        self.btnInfo_size.setText(_translate("DirFile", "size()"))
        self.btnInfo_birthTime.setToolTip(_translate("DirFile", "Returns the date and time when the file was created / born"))
        self.btnInfo_birthTime.setText(_translate("DirFile", "birthTime()"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("DirFile", "QFileInfo"))
        self.groupBox.setTitle(_translate("DirFile", "static function"))
        self.btnDir_homePath.setToolTip(_translate("DirFile", "Returns the absolute path of the user\'s home directory"))
        self.btnDir_homePath.setText(_translate("DirFile", "homePath()"))
        self.btnDir_tempPath.setToolTip(_translate("DirFile", "Returns the absolute path of the system\'s temporary directory"))
        self.btnDir_tempPath.setText(_translate("DirFile", "tempPath()"))
        self.btnDir_rootPath.setToolTip(_translate("DirFile", "Returns the absolute path of the root directory"))
        self.btnDir_rootPath.setText(_translate("DirFile", "rootPath()"))
        self.btnDir_drives.setToolTip(_translate("DirFile", "Returns a list of the root directories on this system"))
        self.btnDir_drives.setText(_translate("DirFile", "drives()"))
        self.btnDir_curPath.setToolTip(_translate("DirFile", "Returns the absolute path of the application\'s current directory"))
        self.btnDir_curPath.setText(_translate("DirFile", "currentPath()"))
        self.btnDir_setCurPath.setToolTip(_translate("DirFile", "Sets the application\'s current working directory to path"))
        self.btnDir_setCurPath.setText(_translate("DirFile", "setCurrent()"))
        self.groupBox_4.setTitle(_translate("DirFile", "file operation"))
        self.btnDir_mkdir.setToolTip(_translate("DirFile", "Creates a sub-directory called dirName."))
        self.btnDir_mkdir.setText(_translate("DirFile", "mkdir()"))
        self.btnDir_remove.setToolTip(_translate("DirFile", "Removes the file, fileName."))
        self.btnDir_remove.setText(_translate("DirFile", "remove()"))
        self.btnDir_rename.setToolTip(_translate("DirFile", "Renames a file or directory from oldName to newName"))
        self.btnDir_rename.setText(_translate("DirFile", "rename()"))
        self.btnDir_setPath.setToolTip(_translate("DirFile", "Sets the path of the directory to path"))
        self.btnDir_setPath.setText(_translate("DirFile", "setPath()"))
        self.btnDir_rmdir.setToolTip(_translate("DirFile", "Removes the directory specified by dirName."))
        self.btnDir_rmdir.setText(_translate("DirFile", "rmdir()"))
        self.btnDir_removeALL.setToolTip(_translate("DirFile", "Removes the directory, including all its contents."))
        self.btnDir_removeALL.setText(_translate("DirFile", "removeRecursively()"))
        self.groupBox_3.setTitle(_translate("DirFile", "file information"))
        self.btnDir_absPath.setToolTip(_translate("DirFile", "Returns the absolute path (a path that starts with \"/\" or with a drive specification)"))
        self.btnDir_absPath.setText(_translate("DirFile", "absolutePath()"))
        self.btnDir_canonPath.setToolTip(_translate("DirFile", "Returns the canonical path, i.e. a path without symbolic links or redundant \".\" or \"..\" elements."))
        self.btnDir_canonPath.setText(_translate("DirFile", "canonicalPath()"))
        self.btnDir_filePath.setToolTip(_translate("DirFile", "Returns the path name of a file in the directory"))
        self.btnDir_filePath.setText(_translate("DirFile", "filePath()"))
        self.btnDir_dirName.setToolTip(_translate("DirFile", "Returns the name of the directory"))
        self.btnDir_dirName.setText(_translate("DirFile", "dirName()"))
        self.btnDir_exists.setToolTip(_translate("DirFile", "Returns true if the directory exists"))
        self.btnDir_exists.setText(_translate("DirFile", "exists()directory"))
        self.btnDir_absFilePath.setToolTip(_translate("DirFile", "Returns the absolute path name of a file in the directory"))
        self.btnDir_absFilePath.setText(_translate("DirFile", "absoluteFilePath()"))
        self.btnDir_listFile.setToolTip(_translate("DirFile", "Returns a list of the names of all the files and directories in the directory"))
        self.btnDir_listFile.setText(_translate("DirFile", "entryList(file)"))
        self.btnDir_listDir.setToolTip(_translate("DirFile", "Returns a list of the names of all the files and directories in the directory"))
        self.btnDir_listDir.setText(_translate("DirFile", "entryList(dir)"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("DirFile", "QDir"))
        self.btnWatch_addDir.setToolTip(_translate("DirFile", "Adds path to the file system watcher if path exists. "))
        self.btnWatch_addDir.setText(_translate("DirFile", "addPath()"))
        self.btnWatch_addFiles.setToolTip(_translate("DirFile", "Adds each path in paths to the file system watcher. "))
        self.btnWatch_addFiles.setText(_translate("DirFile", "addPaths()"))
        self.btnWatch_remove.setToolTip(_translate("DirFile", "Removes the specified path from the file system watcher."))
        self.btnWatch_remove.setText(_translate("DirFile", "removePaths()"))
        self.btnWatch_dirs.setToolTip(_translate("DirFile", "Returns a list of paths to directories that are being watched."))
        self.btnWatch_dirs.setText(_translate("DirFile", "directories()"))
        self.btnWatch_files.setToolTip(_translate("DirFile", "Returns a list of paths to files that are being watched."))
        self.btnWatch_files.setText(_translate("DirFile", "files()"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("DirFile", "QFileSystemWatcher"))
        self.btnSelectFile.setText(_translate("DirFile", "select file"))
        self.btnSelectDirectory.setText(_translate("DirFile", "select directory"))
        self.btnClear.setText(_translate("DirFile", "clear"))
        self.btnExit.setText(_translate("DirFile", "exit"))
        self.label_2.setText(_translate("DirFile", "directory"))
        self.label.setText(_translate("DirFile", "file"))
        self.label_3.setText(_translate("DirFile", "info"))
