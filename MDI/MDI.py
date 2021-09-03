import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_mainwindow import Ui_MainWindow
from form import QmyFormDoc

class Qmain(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.mdiArea) #fill out all window
       
    def closeEvent(self,event):
        self.ui.mdiArea.closeAllSubWindows()
        event.accept()

    @pyqtSlot()
    def on_actionNew_triggered(self):
        formDoc=QmyFormDoc(self)
        self.ui.mdiArea.addSubWindow(formDoc)
        formDoc.show()
        self.__enableEditActions(True)

    def __enableEditActions(self,enabled):
        self.ui.actionCopy.setEnabled(enabled)
        self.ui.actionCut.setEnabled(enabled)
        self.ui.actionPaste.setEnabled(enabled)
        self.ui.actionFont.setEnabled(enabled)

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        needNew=False
        if len(self.ui.mdiArea.subWindowList())>0:
            formDoc=self.ui.mdiArea.activeSubWindow().widget()
            needNew=formDoc.isFileOpened()
        else:
            needNew=True

        curpath=os.getcwd()
        filename,flt=QFileDialog.getOpenFileName(self,'open file',
        curpath,'text file(*.cpp *.py *txt);;all(*.*)')
        if filename=="":
            return
        
        if needNew:
            formDoc=QmyFormDoc(self)
            self.ui.mdiArea.addSubWindow(formDoc)
        formDoc.loadFromFile(filename)
        formDoc.show()
        self.__enableEditActions(True)

    @pyqtSlot()
    def on_actionCascade_triggered(self):
        self.ui.mdiArea.cascadeSubWindows()
    @pyqtSlot()
    def on_actionTile_triggered(self):
        self.ui.mdiArea.tileSubWindows()
    @pyqtSlot()
    def on_actionClose_triggered(self):
        self.ui.mdiArea.closeAllSubWindows()
        
    @pyqtSlot(bool)
    def on_actionMDI_triggered(self,checked):
        print('hello')
        if checked:
            self.ui.mdiArea.setViewMode(QMdiArea.TabbedView)
            self.ui.mdiArea.setTabsClosable(True)
            self.ui.actionCascade.setEnabled(False)
            self.ui.actionTile.setEnabled(False)
        else:
            self.ui.mdiArea.setViewMode(QMdiArea.SubWindowView)
            self.ui.actionCascade.setEnabled(True)
            self.ui.actionTile.setEnabled(True)
            
    def on_mdiArea_subWindowActivated(self,args):
        cnt=len(self.ui.mdiArea.subWindowList())
        if cnt==0:
            self.__enableEditActions(False)
            self.ui.statusBar.clearMessage()
        else:
            formDoc=self.ui.mdiArea.activeSubWindow().widget()
            self.ui.statusBar.showMessage(formDoc.currentFileName())
            
    @pyqtSlot()
    def on_actionCut_triggered(self):
        formDoc=self.ui.mdiArea.activeSubWindow().widget()
        formDoc.textCut()
    @pyqtSlot()
    def on_actionPaste_triggered(self):
        formDoc=self.ui.mdiArea.activeSubWindow().widget()
        formDoc.textPaste()
    @pyqtSlot()
    def on_actionCopy_triggered(self):
        formDoc=self.ui.mdiArea.activeSubWindow().widget()
        formDoc.textCopy()
    @pyqtSlot()
    def on_actionFont_triggered(self):
        formDoc=self.ui.mdiArea.activeSubWindow().widget()
        formDoc.textSetFont()




if __name__ == "__main__":
    app=QApplication(sys.argv)
    new=Qmain()
    new.show()
    sys.exit(app.exec_())
    
