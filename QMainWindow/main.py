# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtGui import QTextCharFormat,QFont
from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.__buildUI()
        self.__spinFontSize.valueChanged[int].connect(self.do_fontSize_Changed)
        self.__comboFontName.currentIndexChanged[str].connect(self.do_fontName_Changed)
     #self.setCentralWidget(self.ui.textEdit)
    def __buildUI(self):
        self.__LabFile=QLabel(self)
        self.__LabFile.setMinimumWidth(150)
        self.__LabFile.setText('file name:')
        self.ui.statusBar.addWidget(self.__LabFile)

        self.__progressBar1=QProgressBar(self)
        self.__progressBar1.setMaximumWidth(200)
        self.__progressBar1.setMinimum(2)
        self.__progressBar1.setMaximum(72)
        sz=self.ui.textEdit.font().pointSize()
        self.__progressBar1.setValue(sz)
        self.ui.statusBar.addWidget(self.__progressBar1)

        self.__LabInfo=QLabel(self)
        self.__LabInfo.setText('select font:')
        self.ui.statusBar.addPermanentWidget(self.__LabInfo)

        actionGroup=QActionGroup(self)
        actionGroup.addAction(self.ui.actionchinese)
        actionGroup.addAction(self.ui.actionenglish)
        actionGroup.setExclusive(True)
        self.ui.actionenglish.setChecked(True)
        #set spinbox for fontsize
        self.__spinFontSize=QSpinBox(self)
        self.__spinFontSize.setMinimum(2)
        self.__spinFontSize.setMaximum(72)
        sz=self.ui.textEdit.font().pointSize()
        self.__spinFontSize.setValue(sz)
        self.__spinFontSize.setMinimumWidth(50)
        self.ui.mainToolBar.addWidget(self.__spinFontSize)
        #set combobox for font format
        self.__comboFontName=QFontComboBox(self)
        self.__comboFontName.setMinimumWidth(100)
        self.ui.mainToolBar.addWidget(self.__comboFontName)

        self.ui.mainToolBar.addSeparator()
        self.ui.mainToolBar.addAction(self.ui.actionclose)
        #set fontsize
    @pyqtSlot(int)
    def do_fontSize_Changed(self,fontSize):
        fmt=self.ui.textEdit.currentCharFormat()
        fmt.setFontPointSize(fontSize)
        self.ui.textEdit.mergeCurrentCharFormat(fmt)
        self.__progressBar1.setValue(fontSize)
        #set font format
    @pyqtSlot(str)
    def do_fontName_Changed(self,fontName):
        fmt=self.ui.textEdit.currentCharFormat()
        fmt.setFontFamily(fontName)
        self.ui.textEdit.mergeCurrentCharFormat(fmt)
        self.__LabInfo.setText('font format:%s'%fontName)
    #set bold
    @pyqtSlot(bool)
    def on_actionfont_bold_triggered(self,checked):     
        fmt=self.ui.textEdit.currentCharFormat()   
        if checked==True:
            fmt.setFontWeight(QFont.Bold)             
        else:
            fmt.setFontWeight(QFont.Normal)
        self.ui.textEdit.mergeCurrentCharFormat(fmt)
    #set italic
    @pyqtSlot(bool)
    def on_actionitalic_triggered(self,checked):
        fmt=self.ui.textEdit.currentCharFormat()
        fmt.setFontItalic(checked)
        self.ui.textEdit.mergeCurrentCharFormat(fmt)
    @pyqtSlot(bool)
    def on_actionunderline_triggered(self,checked):
        fmt=self.ui.textEdit.currentCharFormat()
        fmt.setFontUnderline(checked)
        self.ui.textEdit.mergeCurrentCharFormat(fmt)
    
    def on_textEdit_copyAvailable(self,avi):
        self.ui.actioncut.setEnabled(avi)
        self.ui.actioncopy.setEnabled(avi)
        self.ui.actionpaste.setEnabled(self.ui.textEdit.canPaste())
    
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
