import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from customdialog import Ui_CustomDialog
from Size import QmyDialogSize
from Header import QmyDialogHeaders
from Locate import QmyDialogLocate

class QmyMainWindow(QMainWindow):
    cellIndexChanged=pyqtSignal(int,int)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_CustomDialog()
        self.ui.setupUi(self)

        self.__dlgSetHeaders=None
        self.setCentralWidget(self.ui.tableView)
    #create status bar
        self.LabCellPos=QLabel('now cell:',self)
        self.LabCellPos.setMinimumWidth(180)
        self.ui.statusBar.addWidget(self.LabCellPos)
        self.LabCellText=QLabel('content:',self)
        self.LabCellText.setMinimumWidth(200)
        self.ui.statusBar.addWidget(self.LabCellText)
    # create item/view
        self.itemModel=QStandardItemModel(10,5,self)
        self.selectionModel=QItemSelectionModel(self.itemModel)
        self.selectionModel.currentChanged.connect(self.do_currentChanged)
        self.ui.tableView.setModel(self.itemModel)
        self.ui.tableView.setSelectionModel(self.selectionModel)

    def do_currentChanged(self,current,previous):
        if current!=None:
            self.LabCellPos.setText('now row: %d column:%d'%(current.row(),current.column()))
            item=self.itemModel.itemFromIndex(current)
            self.LabCellText.setText('content:'+item.text())
            self.cellIndexChanged.emit(current.row(),current.column())
    #link dialogsize
    @pyqtSlot()
    def on_actionSet_line_triggered(self):
        dlgTableSize=QmyDialogSize()
        dlgTableSize.setIniSize(self.itemModel.rowCount(),self.itemModel.columnCount())
        ret=dlgTableSize.exec()
        if ret==QDialog.Accepted:
            rows,cols=dlgTableSize.getTableSize()
            self.itemModel.setRowCount(rows)
            self.itemModel.setColumnCount(cols)

    #link dialogheader
    @pyqtSlot()
    def on_actionSet_title_triggered(self):
        if (self.__dlgSetHeaders==None):
            self.__dlgSetHeaders=QmyDialogHeaders(self)
        count=len(self.__dlgSetHeaders.headerList())

        if count!=self.itemModel.columnCount():
            strList=[]
            for i in range(self.itemModel.columnCount()):
                text=str(self.itemModel.headerData(i,Qt.Horizontal,Qt.DisplayRole))
                strList.append(text)
            self.__dlgSetHeaders.setHeaderList(strList)

        ret=self.__dlgSetHeaders.exec()
        if ret==QDialog.Accepted:
            strList2=self.__dlgSetHeaders.headerList()
            self.itemModel.setHorizontalHeaderLabels(strList2)
        
    cellIndexChanged=pyqtSignal(int,int)
    @pyqtSlot()
    def on_actionSet_cell_triggered(self):
        dlgLocate=QmyDialogLocate(self)
        dlgLocate.setSpinRange(self.itemModel.rowCount(),self.itemModel.columnCount())
        dlgLocate.changeActionEnable.connect(self.do_setActLocateEnable)
        dlgLocate.changeCellText.connect(self.do_setACellText)
        self.cellIndexChanged.connect(dlgLocate.do_setSpinValue)
        dlgLocate.setAttribute(Qt.WA_DeleteOnClose)
        dlgLocate.show()

    def do_currentChanged(self,current,previous):
        if current!=None:
            self.LabCellPos.setText('now row:%d col:%d'%(current.row(),current.column()))
            item=self.itemModel.itemFromIndex(current)
            self.LabCellText.setText('cell:'+item.text())
            self.cellIndexChanged.emit(current.row(),current.column())

    def do_setActLocateEnable(self,enable):
        self.ui.actionSet_cell.setEnabled(enable)
    def do_setACellText(self,row,column,text):
        index=self.itemModel.index(row,column)
        self.selectionModel.clearSelection()
        self.selectionModel.setCurrentIndex(index,QItemSelectionModel.Select)
        self.itemModel.setData(index,text,Qt.DisplayRole)







if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainform=QmyMainWindow()
    mainform.show()
    sys.exit(app.exec_())
