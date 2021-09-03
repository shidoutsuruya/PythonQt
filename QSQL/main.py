import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from ui_QSQL import Ui_QSQL
from dialog import Dialog

class QMain(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_QSQL()
        self.ui.setupUi(self)
    #tableview show
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.verticalHeader().setDefaultSectionSize(50)
        self.ui.tableView.horizontalHeader().setDefaultSectionSize(150)
    #initial condition
        self.ui.actionInsert.setEnabled(False)
        self.ui.actionEdit.setEnabled(False)
        self.ui.actionDelete.setEnabled(False)
        self.ui.actionBonus.setEnabled(False)
        self.ui.actionSQLTest.setEnabled(False)
    
    @pyqtSlot()
    def on_actionOpen_triggered(self):
        fileName,filt=QFileDialog.getOpenFileName(self,'select sql document','','sql lite(*.db *db3)')
        if (fileName==''):
            return
        self.db=QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(fileName)
        if self.db.open():
            self.__openTable()
        else:
            QMessageBox.warning(self,'wrong','cannot open database')
            
    def __openTable(self):
        self.qryModel=QSqlQueryModel(self)
        self.qryModel.setQuery('SELECT ID,Name,Sex,Birth,Country,Age,Salary,Image FROM qttest ORDER BY ID')
       
        if self.qryModel.lastError().isValid():
            QMessageBox.critical(self,'wrong','cannot find,please check your sql sentence\n'+self.qryModel.lastError().text())
            return
        headerList=['ID','Name','Sex','Birth','Country','Age','Salary','Image']
        for index,header in enumerate(headerList):
            self.qryModel.setHeaderData(index,Qt.Horizontal,header)
            
        self.selModel=QItemSelectionModel(self.qryModel)
        self.selModel.currentRowChanged.connect(self.do_currentRowChanged)#connect table and model
        self.ui.tableView.setModel(self.qryModel)
        self.ui.tableView.setSelectionModel(self.selModel)
        self.ui.tableView.setColumnHidden(headerList.index('Image'),True)
        
        self.ui.actionInsert.setEnabled(True)
        self.ui.actionEdit.setEnabled(True)
        self.ui.actionDelete.setEnabled(True)
        self.ui.actionBonus.setEnabled(True)
        self.ui.actionSQLTest.setEnabled(True)
        
    def do_currentRowChanged(self,current,previous):
        if current.isValid()==False:
            return
        curRec=self.qryModel.record(current.row())
        Id=curRec.value('ID')
        self.ui.statusBar.showMessage('record id:%d'%(Id))
        
    @pyqtSlot()
    def on_actionEdit_triggered(self):
        curRecNo=self.selModel.currentIndex().row()
        self.__updateRecord(curRecNo)
        
    def __updateRecord(self,recNo):
        curRec=self.qryModel.record(recNo)
        Id=curRec.value('ID')
        query=QSqlQuery(self.db)
        query.prepare('SELECT * FROM qttest WHERE ID = ?')
        query.bindValue(0,Id)
        query.exec()
        query.first()
        if not query.isValid():
            return
        curRec=query.record()
        dlgData=Dialog(self)
        dlgData.setUpdateRecord(curRec)
        ret=dlgData.exec()
        if ret!=Dialog.Accepted:
            return
        recData=dlgData.getRecordData()
        query.prepare('UPDATE qttest SET Name=:name,Sex=:sex,Birth=:birth,Country=:country,Age=:age,Salary=:salary,Image=:image WHERE ID=:Id')
        sqlList=[':Id',':name',':sex',':birth',':country',':age',':salary',':image']
        headerList=['ID','Name','Sex','Birth','Country','Age','Salary','Image']
        for s,h in zip(sqlList,headerList):
            query.bindValue(s,recData.value(h))
            
        if (not query.exec()):
            QMessageBox.critical(self,'error','cannot update to database')
        else:         
            self.qryModel.query().exec()
            QMessageBox.information(self,'info','database has changed')
    
    @pyqtSlot()
    def on_actionInsert_triggered(self):
        query=QSqlQuery(self.db)
        query.exec('SELECT * FROM qttest where ID=-1')
        curRec=query.record()
        curRec.setValue('ID',self.qryModel.rowCount())
        
        dlgData=Dialog(self)
        dlgData.setInsertRecord(curRec)
        ret=dlgData.exec()
        
        if ret!=QDialog.Accepted:
            return
        recData=dlgData.getRecordData()
        query.prepare('INSERT INTO qttest (ID,Name,Sex,Birth,Country,Age,Salary,Image) \
            VALUES(:Id,:name,:sex,:birth,:country,:age,:salary,:image)')
        
        sqlList=[':Id',':name',':sex',':birth',':country',':age',':salary',':image']
        headerList=['ID','Name','Sex','Birth','Country','Age','Salary','Image']
        for s,h in zip(sqlList,headerList):
            query.bindValue(s,recData.value(h))
        res=query.exec()
        if (res==False):
            QMessageBox.critical(self,'error','insert content error')
        else:
            sqlStr=self.qryModel.query().executedQuery()
            self.qryModel.setQuery(sqlStr)
            QMessageBox.information(self,'info','database has changed')
    @pyqtSlot()
    def on_actionDelete_triggered(self):
        curRecNo=self.selModel.currentIndex().row()
        curRec=self.qryModel.record(curRecNo)
        if curRec.isEmpty():
            return
        Id=curRec.value('ID')
        query=QSqlQuery(self.db)
        query.prepare('DELETE FROM qttest WHERE ID=?')
        query.bindValue(0,Id)
        if query.exec()==False:
            QMessageBox.critical(self,'error','cannot delete\n'+query.lastError().text())
        else:
            sqlStr=self.qryModel.query().executedQuery()
            self.qryModel.setQuery(sqlStr)
            QMessageBox.information(self,'info','database has changed')
    @pyqtSlot()
    def on_actionBonus_triggered(self):
        qryList=QSqlQuery(self.db)
        qryList.exec('SELECT ID,Salary FROM qttest ORDER BY ID')
        qryUpdate=QSqlQuery(self.db)
        qryUpdate.prepare('UPDATE qttest SET Salary=:s WHERE ID=:i')
        qryList.first()
        while (qryList.isValid()):
            ids=qryList.value('ID')
            salary=qryList.value('Salary')
            salary+=500
            qryUpdate.bindValue(':i',ids)
            qryUpdate.bindValue(':s',salary)
            qryUpdate.exec()
            if not qryList.next():
                break
        self.qryModel.query().exec()
        QMessageBox.information(self,'bonus','bonus up!!!')
    @pyqtSlot()
    def on_actionSQLTest_triggered(self):
        query=QSqlQuery(self.db)
        query.exec('UPDATE qttest SET Salary=500+Salary')
        sqlStr=self.qryModel.query().executedQuery()
        self.qryModel.setQuery(sqlStr)
        
        
            
        
        
        
       
        
    
                  
if __name__=='__main__':
    app=QApplication(sys.argv)
    form=QMain()
    form.show()
    sys.exit(app.exec_())