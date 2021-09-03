import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_dirfile import Ui_DirFile

class QMain(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_DirFile()
        self.ui.setupUi(self)
        
        self.ui.toolBox.setCurrentIndex(0)
        self.fileWatcher=QFileSystemWatcher()
        #self.fileWatcher.directoryChanged.connect(self.do_directoryChanged)
        #self.fileWatcher.fileChanged.connect(self.do_fileChanged)
        
    @pyqtSlot()
    def on_btnSelectFile_clicked(self):
        curdir=QDir.currentPath()
        aFile,filt=QFileDialog.getOpenFileName(self,'open file',curdir,'all(*.*)')
        self.ui.lineEditFile.setText(aFile)
    @pyqtSlot()
    def on_btnSelectDirectory_clicked(self):
        curdir=QDir.currentPath()
        aDir=QFileDialog.getExistingDirectory(self,'select direcory',curdir,QFileDialog.ShowDirsOnly)
        self.ui.lineEditDir.setText(aDir)
        
    @pyqtSlot()
    def on_btnInfo_baseName_clicked(self):
        self.__showBtnInfo(self.sender())
        fileInfo=QFileInfo(self.ui.lineEditFile.text())
        text=fileInfo.baseName()
        self.ui.plainTextEdit.appendPlainText(text+'\n')
        
    def __showBtnInfo(self,btn):
        self.ui.plainTextEdit.appendPlainText('===='+btn.text())
        self.ui.plainTextEdit.appendPlainText(btn.toolTip()+'\n')
        
    @pyqtSlot()
    def on_btnInfo_exists2_clicked(self):
        self.__showBtnInfo(self.sender())
        sous=self.ui.lineEditFile.text().strip()
        if QFile.exists(sous):
            self.ui.plainTextEdit.appendPlainText('True\n')
        else:
            self.ui.plainTextEdit.appendPlainText('False\n')
            
    @pyqtSlot()
    def on_btnDir_drives_clicked(self):
        self.__showBtnInfo(self.sender())
        strList=QDir.drives()
        for line in strList:
            self.ui.plainTextEdit.appendPlainText(line.path())
        self.ui.plainTextEdit.appendPlainText("")
    @pyqtSlot()
    def on_btnDir_rename_clicked(self):
        self.__showBtnInfo(self.sender())
        sous=self.ui.lineEditFile.text().strip()
        if sous=="":
            self.ui.plainTextEdit.appendPlainText('please select a file')
            return
        fileInfo=QFileInfo(sous)
        newFile=fileInfo.path()+'/'+fileInfo.baseName()+'.xxx'
        if QFile.rename(sous,newFile):
            self.ui.plainTextEdit.appendPlainText('origin:'+sous)
            self.ui.plainTextEdit.appendPlainText('rename:'+newFile+'\n')
        else:
            self.ui.plainTextEdit.appendPlainText('error!!!')
            
    @pyqtSlot()
    def on_btnDir_listDir_clicked(self):
        self.__showBtnInfo(self.sender())
        sous=self.ui.lineEditDir.text()
        dirObj=QDir(sous)
        strList=dirObj.entryList(QDir.Dirs|QDir.NoDotAndDotDot)
        self.ui.plainTextEdit.appendPlainText('all category')
        for i in strList:
            self.ui.plainTextEdit.appendPlainText(i)
        self.ui.plainTextEdit.appendPlainText('\n')
        
    @pyqtSlot()
    def on_btnDir_listFile_clicked(self):
        self.__showBtnInfo(self.sender())
        sous=self.ui.lineEditDir.text()
        dirObj=QDir(sous)
        strList=dirObj.entryList(QDir.Files)
        self.ui.plainTextEdit.appendPlainText('xxx')
        for i in strList:
            self.ui.plainTextEdit.appendPlainText(i)
        self.ui.plainTextEdit.appendPlainText('\n')
        
    def do_directoryChanged(self,path):
        self.ui.plainTextEdit.appendPlainText(path)
        self.ui.plainTextEdit.appendPlainText('directory changed\n')
    def do_fileChanged(self,path):
        self.ui.plainTextEdit.appendPlainText(path)
        self.ui.plainTextEdit.appendPlainText('file changed\n')
        
    @pyqtSlot()
    def on_btnWatch_addDir_clicked(self):
        self.__showBtnInfo(self.sender())
        curDir=QDir.currentPath()
        aDir=QFileDialog.getExistingDirectory(self,'select a directory',curDir,QFileDialog.ShowDirsOnly)
        self.fileWatcher.addPath(aDir)
        self.ui.plainTextEdit.appendPlainText('add listening directory')
        self.ui.plainTextEdit.appendPlainText(aDir+'\n')
    @pyqtSlot()
    def on_btnWatch_addFiles_clicked(self):
        self.__showBtnInfo(self.sender())
        curDir=QDir.currentPath()
        fileList,filt=QFileDialog.getOpenFileNames(self,'select listening files',curDir,'all (*.*)')
        self.fileWatcher.addPaths(fileList)
        self.ui.plainTextEdit.appendPlainText('add listening directory')
        for i in fileList:
            self.ui.plainTextEdit.appendPlainText(i)
        self.ui.plainTextEdit.appendPlainText("")
        
    @pyqtSlot()
    def on_btnWatch_remove_clicked(self):
        self.__showBtnInfo(self.sender())
        self.ui.plainTextEdit.appendPlainText('remove all listening directory and files')
        dirList=self.fileWatcher.directories()
        self.fileWatcher.removePaths(dirList)
        fileList=self.fileWatcher.files()
        self.fileWatcher.removePaths(fileList)
        
    @pyqtSlot()
    def on_btnWatch_dirs_clicked(self):
        self.__showBtnInfo(self.sender())
        strList=self.fileWatcher.directories()
        self.ui.plainTextEdit.appendPlainText('listening directory:')
        for i in strList:
            self.ui.plainTextEdit.appendPlainText(i)
        self.ui.plainTextEdit.appendPlainText('\n')
        
    @pyqtSlot()
    def on_btnWatch_files_clicked(self):
        self.__showBtnInfo(self.sender())
        strList=self.fileWatcher.files()
        self.ui.plainTextEdit.appendPlainText('listening files:')
        for i in strList:
            self.ui.plainTextEdit.appendPlainText(i)
        self.ui.plainTextEdit.appendPlainText('\n')
        
        

        
        

if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=QMain()
    form.show()
    sys.exit(app.exec_())