import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from dialogsize import Ui_DialogSize

class QmyDialogSize(QDialog):
    def __init__(self,rowCount=3,colCount=5,parent=None):
        super().__init__(parent)
        self.ui=Ui_DialogSize()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)

    def __del__(self):
        print('QmyDialogSize is deleted')

    def setIniSize(self,rowCount,colCount):
        self.ui.spinBoxRow.setValue(rowCount)
        self.ui.spinBoxColumn.setValue(colCount)

    def getTableSize(self):
        rows=self.ui.spinBoxRow.value()
        cols=self.ui.spinBoxColumn.value()
        return rows,cols


