import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_textread import Ui_TextRead

class QMain(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent=None)
        self.ui=Ui_TextRead()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.plainTextEdit)
    @pyqtSlot()
    def on_actionQFileOpen_triggered(self):
        curpath=QDir.currentPath()
        title='open a file'
        filt='execute file(*.h *.py *.cpp);;text(*.txt);;all(*.*)'
        fileName,filt=QFileDialog.getOpenFileName(self,title,curpath,filt)
        if fileName=='':
            return
        if self.__openByIODevice(fileName):
            self.ui.statusBar.showMessage(fileName)
        else:
            QMessageBox.critical(self,'error','error to open')
    
    def __openByIODevice(self,fileName):   
        fileDevice=QFile(fileName)
        if not fileDevice.exists():
            return False
        if not fileDevice.open(QIODevice.ReadOnly|QIODevice.Text):
            return False
        
        try:
            self.ui.plainTextEdit.clear()
            
            while not fileDevice.atEnd():          
                qtBytes=fileDevice.readLine()
                pyBytes=bytes(qtBytes.data())
                lineStr=pyBytes.decode('utf-8')
                lineStr=lineStr.strip()
                self.ui.plainTextEdit.appendPlainText(lineStr)
        finally:
            fileDevice.close()
        return True
    
    @pyqtSlot()
    def on_actionQFileSave_triggered(self):
        curpath=QDir.currentPath()
        title='save file'
        filt='python(*.py);;c++(*.h *.cpp);;text(*.txt)'
        fileName,filt=QFileDialog.getSaveFileName(self,title,curpath,filt)
        if fileName=="":
            return
        if self.__saveByIODevice(fileName):
            self.ui.statusBar.showMessage(fileName)
        else:
            QMessageBox.critical(self,'error','cannot save')
    def __saveByIODevice(self,fileName):
        fileDevice=QFile(fileName)
        if not fileDevice.open(QIODevice.WriteOnly|QIODevice.Text):
            return False
        try:
            text=self.ui.plainTextEdit.toPlainText()
            strBytes=text.encode('utf-8')
            fileDevice.write(strBytes)
        finally:
            fileDevice.close()
        return True
    
    @pyqtSlot()
    def on_actionStreamOpen_triggered(self):
        curpath=QDir.currentPath()
        title='open a file'
        filt='exe(*.py *.cpp *.h);;text(*.txt);;all(*.*)'
        fileName,filt=QFileDialog.getOpenFileName(self,title,curpath,filt)
        if fileName=="":
            return
        if self.__openByStream(fileName):
            self.ui.statusBar.showMessage(fileName)
        else:
            QMessageBox.critical(self,'error','eroor')
    def __openByStream(self,fileName):
        fileDevice=QFile(fileName)
        if not fileDevice.exists():
            return False
        if not fileDevice.open(QIODevice.ReadOnly|QIODevice.Text):
            return False
        try:
            filestream=QTextStream(fileDevice)
            filestream.setAutoDetectUnicode(True)
            filestream.setCodec('utf-8')
            self.ui.plainTextEdit.clear()
            while not filestream.atEnd():
                lineStr=filestream.readLine()
                self.ui.plainTextEdit.appendPlainText(lineStr)
        finally:
            fileDevice.close()
        return True
    
    @pyqtSlot()
    def on_actionSteamSave_triggered(self):
        curpath=QDir.currentPath()
        title='save file'
        filt='python(*.py);;c++(*.h *.cpp);;all(*.*)'
        fileName,filt=QFileDialog.getSaveFileName(self,title,curpath,filt)
        if fileName=="":
            return
        if self.__saveByStream(fileName):
            self.ui.statusBar.showMessage(fileName)
        else:
            QMessageBox.critical(self,'error','error')
    def __saveByStream(self,fileName):
        fileDevice=QFile(fileName)
        if not fileDevice.open(QIODevice.WriteOnly|QIODevice.Text):
            return False
        try:
            filestream=QTextStream(fileDevice)
            filestream.setAutoDetectUnicode(True)
            filestream.setCodec('utf-8')
            text=self.ui.plainTextEdit.toPlainText()
            filestream<<text
            QMessageBox.information(self,'save','successfully save')
        finally:
            fileDevice.close()
        return True
    
    @pyqtSlot()
    def on_actionPythonOpen_triggered(self):
        curpath=QDir.currentPath()
        title='open file'
        filt='exe(*.h *.cpp *.py);;all(*.*)'
        fileName,filt=QFileDialog.getOpenFileName(self,title,curpath,filt)
        if fileName=="":
            return
        self.ui.plainTextEdit.clear()
        fileDevice=open(fileName,mode='r',encoding='utf-8')
        try:
            for i in fileDevice:
                lineStr=i.strip()
                self.ui.plainTextEdit.appendPlainText(lineStr)
            self.ui.statusBar.showMessage(fileName)
        finally:
            fileDevice.close()
            
    @pyqtSlot()
    def on_actionPythonSave_triggered(self):
        curpath=QDir.currentPath()
        title='save file'
        filt='python(*.py);;c++(*.h *.cpp);;All(*.*)'
        fileName,filt=QFileDialog.getSaveFileName(self,title,curpath,filt)
        if fileName=="":
            return
        text=self.ui.plainTextEdit.toPlainText()
        fileDevice=open(fileName,mode='w',encoding='utf-8')
        try:
            fileDevice.write(text)
            self.ui.statusBar.showMessage(fileName)       
        finally:
            QMessageBox.information(self,'save','successfully save')
            fileDevice.close()
        
    
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    form=QMain()
    form.show()
    sys.exit(app.exec_())
    