import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from ui_formtable import Ui_formTable
from dialogsize import QmyDialogsize
from dialogheaders import QmyDialogHeaders

class QmyFormTable(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_formTable()
        self.ui.setupUi(self)
        self.__dlgSetHeaders=None
        self.setAutoFillBackground(True)
        self.setCentralWidget(self.ui.tableView)
        self.ui.tableView.setAlternatingRowColors(True)
    #create model view
        self.itemModel=QStandardItemModel(10,5,self)
        self.selectionModel=QItemSelectionModel(self.itemModel)
        self.ui.tableView.setModel(self.itemModel)
        self.ui.tableView.setSelectionModel(self.selectionModel)
    def __del__(self):
        print('delete')
    @pyqtSlot()
    def on_actionSize_triggered(self):
        dlgTableSize=QmyDialogsize()
        dlgTableSize.setIniSize(self.itemModel.rowCount(),self.itemModel.columnCount())
        ret=dlgTableSize.exec()
        if ret==QDialog.Accepted:
            rows,cols=dlgTableSize.getTableSize()
            self.itemModel.setRowCount(rows)
            self.itemModel.setColumnCount(cols)
        
    @pyqtSlot()
    def on_actionTitle_triggered(self):
        if self.__dlgSetHeaders==None:
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
        




if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=QmyFormTable()
    form.show()
    sys.exit(app.exec_())

    
