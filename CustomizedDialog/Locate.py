from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from dialoglocation import Ui_Locate

class QmyDialogLocate(QDialog):
    changeActionEnable=pyqtSignal(bool)
    changeCellText=pyqtSignal(int,int,str)

    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.ui=Ui_Locate()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

    def __del__(self):
        print('delete!!!')

    def setSpinRange(self,rowCount,colCount):
        self.ui.spinBoxRow.setMaximum(rowCount-1)
        self.ui.spinBoxColumn.setMaximum(colCount-1)

    def showEvent(self,event):
        self.changeActionEnable.emit(False)
        super().showEvent(event)

    def closeEvent(self, event):
       self.changeActionEnable.emit(True)
       super().closeEvent(event)

    @pyqtSlot()
    def on_btnOk_clicked(self):
        row=self.ui.spinBoxRow.value()
        col=self.ui.spinBoxRow.value()
        text=self.ui.lineEdit.text()
        self.changeCellText.emit(row,col,text)
        if (self.ui.checkBoxRow.isChecked()):
            self.ui.spinBoxRow.setValue(1+self.ui.spinBoxRow.value())
        if (self.ui.checkBoxColumn.isChecked()):
            self.ui.spinBoxColumn.setValue(1+self.ui.spinBoxColumn.value())

    @pyqtSlot(int,int)
    def do_setSpinValue(self,rowNo,colNo):
        self.ui.spinBoxRow.setValue(rowNo)
        self.ui.spinBoxColumn.setValue(colNo)
        

    
