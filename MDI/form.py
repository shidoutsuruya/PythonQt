import sys,os,codecs
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_form import Ui_Form

class QmyFormDoc(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('new doc')
        #self.setAttribute(Qt.WA_DeleteOnClose) child window can be deleted
        self.__currentFile=''
        self.__fileOpened=False

    def __del__(self):
        print('my document!!!DELETE')
    
    def loadFromFile(self,aFileName):
        aFile=codecs.open(aFileName,encoding='utf-8')
        try:
            for i in aFile:
                self.ui.plainTextEdit.appendPlainText(i.strip())
        finally:
            aFile.close()
        self.__currentFile=aFileName
        self.__fileOpened=True
        baseFileName=os.path.basename(aFileName)
        self.setWindowTitle(baseFileName)

    def currentFileName(self):
        return self.__currentFile

    def isFileOpened(self):
        return self.__fileOpened
    
    def textCut(self):
        self.ui.plainTextEdit.cut()
    
    def textCopy(self):
        self.ui.plainTextEdit.copy()
        
    def textPaste(self):
        self.ui.plainTextEdit.paste()

    def textSetFont(self):
        iniFont=self.ui.plainTextEdit.font()
        font,ok=QFontDialog.getFont(iniFont)
        if ok:
            self.ui.plainTextEdit.setFont(font)
            

if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=QmyFormDoc()
    form.show()
    sys.exit(app.exec_())
    
