import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from ui_relationtable import Ui_relationTable

class Q(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui=Ui_relationTable()
        self.ui.setupUi(self)
        
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.verticalHeader().setDefaultSectionSize(22)
        self.ui.tableView.horizontalHeader().setDefaultSectionSize(100)
        
        self.ui.actionPlus.setEnabled(False)
        self.ui.actionInsert.setEnabled(False)
        self.ui.actionDelete.setEnabled(False)
        self.ui.actionSave.setEnabled(False)
        self.ui.actionUndo.setEnabled(False)
        self.ui.actionList.setEnabled(False)
        
    @pyqtSlot()
    def on_actionOpen_triggered(self):
        filename,filt=QFileDialog.getOpenFileName(self,'select database','','SQL Lite(*.db *.db3)')
        if filename=="":
            return
        self.db=QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(filename)
        if self.db.open():
            self.__openTable()
        else:
            QMessageBox.warning(self,'error','cannot open database')
            
    def __getFieldNames(self):
        emptyRec=self.tabModel.record()
        self.fldNum={}
        for i in range(emptyRec.count()):
            fieldName=emptyRec.fieldName(i)
            self.fldNum.setdefault(fieldName)
            self.fldNum[fieldName]=i
        print(self.fldNum)
    
    def __openTable(self):
        self.tabModel=QSqlRelationalTableModel(self,self.db)
        self.tabModel.setTable('studInfo')
        self.tabModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.tabModel.setSort(self.tabModel.fieldIndex('studID'),Qt.AscendingOrder)
        if self.tabModel.select()==False:
            QMessageBox.critical(self,'error','cannot open database\n'+self.tabModel.lastError().text())
            return
        self.__getFieldNames()
        #show tab head name    
        self.tabModel.setHeaderData(self.fldNum['studID'],Qt.Horizontal,'student id')
        self.tabModel.setHeaderData(self.fldNum['Name'],Qt.Horizontal,'name')
        self.tabModel.setHeaderData(self.fldNum['Gender'],Qt.Horizontal,'gender')
        self.tabModel.setHeaderData(self.fldNum['departID'],Qt.Horizontal,'college')
        self.tabModel.setHeaderData(self.fldNum['majorID'],Qt.Horizontal,'major')
        #setRelation
        self.tabModel.setRelation(self.fldNum['departID'],QSqlRelation('departInfo','departID','department'))
        self.tabModel.setRelation(self.fldNum['majorID'],QSqlRelation('majorInfo','majorID','major'))
        #select model datatype selectiontype
        self.selModel=QItemSelectionModel(self.tabModel)
        self.selModel.currentChanged.connect(self.do_currentChanged)
        self.ui.tableView.setModel(self.tabModel)
        self.ui.tableView.setSelectionModel(self.selModel)
        
        delegate=QSqlRelationalDelegate(self.ui.tableView)
        self.ui.tableView.setItemDelegate(delegate)
        self.tabModel.select()
        #refresh action
        self.ui.actionPlus.setEnabled(True)
        self.ui.actionInsert.setEnabled(True)
        self.ui.actionDelete.setEnabled(True)
        self.ui.actionSave.setEnabled(True)
        self.ui.actionUndo.setEnabled(True)
        self.ui.actionList.setEnabled(True)
        
    def do_currentChanged(self,current,previous):   
      self.ui.actionSave.setEnabled(self.tabModel.isDirty()) 
      self.ui.actionUndo.setEnabled(self.tabModel.isDirty())
        
            
    
            
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)    
    mainform=Q()        
    mainform.show()                
    sys.exit(app.exec_())  