import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui_formdoc import Ui_DOC

class QmyFormDoc(QWidget):
    docFileChanged=pyqtSignal(str)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_DOC()
        self.ui.setupUi(self)

        self.__curFile=""
        self.__buildUI()
        self.setAutoFillBackground(True)
    
    def __del__(self):
        print('qmyformdoc delete')

    def __buildUI(self):
        locToolBar=QToolBar('document',self)
        locToolBar.addAction(self.ui.actionOpen)
        locToolBar.addAction(self.ui.actionFont)
        locToolBar.addSeparator()
        locToolBar.addAction(self.ui.actionCut)
        locToolBar.addAction(self.ui.actionCopy)
        locToolBar.addAction(self.ui.actionPaste)
        locToolBar.addAction(self.ui.actionUndo)
        locToolBar.addAction(self.ui.actionRedo)
        locToolBar.addSeparator()
        locToolBar.addAction(self.ui.actionExit)

        Layout=QVBoxLayout()
        Layout.addWidget(locToolBar)
        Layout.addWidget(self.ui.plainTextEdit)
        Layout.setContentsMargins(2,2,2,2)
        Layout.setSpacing(2)
        self.setLayout(Layout)

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        curpath=os.getcwd()
        filename,flt=QFileDialog.getOpenFileName(self,'open a file',curpath,'text(*.py *.txt);;all(*.*)')
        if filename=="":
            return
        self.__curFile=filename
        print(self.__curFile)
        self.ui.plainTextEdit.clear()
        aFile=open(filename,'r',encoding='utf-8')
        try:
            for i in aFile:
                self.ui.plainTextEdit.appendPlainText(i.strip())
        finally:
            aFile.close()

    @pyqtSlot()
    def on_actionFont_triggered(self):
        iniFont=self.ui.plainTextEdit.font()
        font,ok=QFontDialog.getFont(iniFont)
        if ok:
            self.ui.plainTextEdit.setFont(font)
        



if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=QmyFormDoc()
    form.show()
    sys.exit(app.exec_())
    