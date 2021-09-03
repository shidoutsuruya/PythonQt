import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui_dialogsize import Ui_size

class QmyDialogsize(QDialog):
    def __init__(self,parent=None,rowCount=3,colCount=5):     
        super().__init__(parent)
        self.ui=Ui_size()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)#fixed window size
        self.setIniSize(rowCount,colCount)

    def __del__(self):
        print('delete')

    def setIniSize(self,rowCount,colCount):
        self.ui.spinBoxRow.setValue(rowCount)
        self.ui.spinBoxColumn.setValue(colCount)

    def getTableSize(self):
        rows=self.ui.spinBoxRow.value()
        cols=self.ui.spinBoxColumn.value()
        return rows,cols



if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=QmyDialogsize()
    form.show()
    sys.exit(app.exec_())