import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os

from ui_mainwindow import Ui_MainWindow
from formdoc import QmyFormDoc
from formtable import QmyFormTable

curpath=os.path.dirname(__file__)
picture=os.path.join(curpath,'sakura.jpg')

class QmyMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.setVisible(False)
        self.ui.tabWidget.clear()
        self.ui.tabWidget.setTabsClosable(True)
        self.ui.tabWidget.setDocumentMode(True)

        self.setCentralWidget(self.ui.tabWidget)
        self.setWindowState(Qt.WindowMaximized)
        self.setAutoFillBackground(True)
        self.__pic=QPixmap(picture)

    def paintEvent(self,event):
        painter=QPainter(self)
        painter.drawPixmap(0,self.ui.mainToolBar.height(),self.width(),
        self.height()-self.ui.mainToolBar.height()-self.ui.statusBar.height(),self.__pic)
    
    def on_tabWidget_currentChanged(self,index):
        hasTabs=self.ui.tabWidget.count()>0
        self.ui.tabWidget.setVisible(hasTabs)
    def on_tabWidget_tabCloseRequested(self,index):
        if index<0:
            return
        aForm=self.ui.tabWidget.widget(index)
        aForm.close()
    #embedding
    @pyqtSlot()
    def on_actionembedding_widget_triggered(self):
        formDoc=QmyFormDoc(self)
        formDoc.setAttribute(Qt.WA_DeleteOnClose)
        formDoc.docFileChanged.connect(self.do_docFileChanged)
        title='DOC%d'%self.ui.tabWidget.count()
        curIndex=self.ui.tabWidget.addTab(formDoc,title)
        self.ui.tabWidget.setCurrentIndex(curIndex)
        self.ui.tabWidget.setVisible(True)
    @pyqtSlot(str)
    def do_docFileChanged(self,shotFilename):
        index=self.ui.tabWidget.currentIndex()
        self.ui.tabWidget.setTabText(index,shotFilename)
    #independent
    @pyqtSlot()
    def on_actionindependent_widget_triggered(self):
        formDoc=QmyFormDoc(self)
        formDoc.setAttribute(Qt.WA_DeleteOnClose)
        formDoc.setWindowTitle('hello world')
        formDoc.setWindowFlag(Qt.Window,True)
        #formDoc.setWindowFlag(Qt.CustomizeWindowHint,True)
        #formDoc.setWindowFlag(Qt.WindowMinMaxButtonsHint,False) analyze the - o x setting
        formDoc.setWindowOpacity(0.9)
        formDoc.show()
   #mainwindow embedding
    @pyqtSlot()
    def on_actionembedding_mainwindow_triggered(self):
        formTable=QmyFormTable(self)
        formTable.setAttribute(Qt.WA_DeleteOnClose)
        title='table %d'%self.ui.tabWidget.count()
        curIndex=self.ui.tabWidget.addTab(formTable,title)
        self.ui.tabWidget.setCurrentIndex(curIndex)
        self.ui.tabWidget.setVisible(True)

    @pyqtSlot()
    def on_actionindependent_mainwindow_triggered(self):
        formTable=QmyFormTable(self)
        formTable.setAttribute(Qt.WA_DeleteOnClose)
        formTable.setWindowTitle('HELLO WORLD')
        formTable.show()






if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
