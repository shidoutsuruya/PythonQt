import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from PyQt5.QtGui import *
from ui_sqlquery import Ui_SqlQuery

class QMain(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_SqlQuery()
        self.ui.setupUi(self)
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.verticalHeader().setDefaultSectionSize(22)
        self.ui.tableView.horizontalHeader().setDefaultSectionSize(60)
    @pyqtSlot()
    def on_actionOpen_triggered(self):
        fileName,flt=QFileDialog.getOpenFileName(self,'select database','','SQL lite(*.db *.db3)')
        if fileName=="":
            return
        self.db=QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(fileName)
        if self.db.open():
            self.__openTable()
        else:
            QMessageBox.warning(self,'error','cannot load')
    def __openTable(self):
        self.qryModel=QSqlQueryModel(self)
        self.qryModel.setQuery('SELECT ID,Name,Sex,Birth,Country,Age,Salary,Image FROM qttest ORDER BY ID')
        if self.qryModel.lastError().isValid():
            QMessageBox.critical(self,'error','please check your input')
            return
        self.ui.statusBar.showMessage('record:%d'%self.qryModel.rowCount())
        HeaderList=['ID','Name','Sex','Birth','Country','Age','Salary','Image']
        for i,j in enumerate(HeaderList):
            self.qryModel.setHeaderData(i,Qt.Horizontal,j)
        self.mapper=QDataWidgetMapper()
        self.mapper.setModel(self.qryModel)
        #connection of head and button
        self.mapper.addMapping(self.ui.spinBoxID,HeaderList.index('ID'))
        self.mapper.addMapping(self.ui.lineEditName,HeaderList.index('Name'))
        self.mapper.addMapping(self.ui.comboBoxSex,HeaderList.index('Sex'))
        self.mapper.addMapping(self.ui.dateEdit,HeaderList.index('Birth'))
        self.mapper.addMapping(self.ui.lineEditCountry,HeaderList.index('Country'))
        self.mapper.addMapping(self.ui.spinBoxAge,HeaderList.index('Age'))
        self.mapper.addMapping(self.ui.doubleSpinBoxSalary,HeaderList.index('Salary'))
        self.mapper.addMapping(self.ui.LabImage,HeaderList.index('Image'))
        self.mapper.toFirst()
        
        self.selModel=QItemSelectionModel(self.qryModel)
        self.selModel.currentRowChanged.connect(self.do_currentRowChanged)
        self.ui.tableView.setModel(self.qryModel)
        self.ui.tableView.setSelectionModel(self.selModel)
        self.ui.tableView.setColumnHidden(HeaderList.index('Image'),True)
        self.ui.actionOpen.setEnabled(False)
        
    def do_currentRowChanged(self,current,previous):
        if current.isValid()==False:
            self.ui.LabImage.clear()
            return
        self.mapper.setCurrentIndex(current.row())
        first=(current.row()==0)
        last=(current.row()==self.qryModel.rowCount()-1)
        self.ui.actionFirst.setEnabled(not first)
        self.ui.actionBack.setEnabled(not first)
        self.ui.actionNext.setEnabled(not last)
        self.ui.actionLast.setEnabled(not last)
        
        curRec=self.qryModel.record(current.row())
        Id=curRec.value('ID')
        query=QSqlQuery(self.db)
        query.prepare('SELECT ID,Image FROM qttest WHERE ID=:ID')
        query.bindValue(':ID',Id)
        if not query.exec():
            QMessageBox.critical(self,'ERROR','sql sentence error\n'+query.lastError().text())
            return
        else:
            query.first()
        picData=query.value('Image')           
        try:    
            pic=QPixmap()
            pic.loadFromData(picData)
            h=self.ui.LabImage.size().height()
            self.ui.LabImage.setPixmap(pic.scaledToWidth(h))
        except:
            self.ui.LabImage.setText('null')  
            
    @pyqtSlot()
    def on_actionFirst_triggered(self):
        self.mapper.toFirst()
        self.__refreshTableView()
    @pyqtSlot()
    def on_actionBack_triggered(self):
        self.mapper.toPrevious()
        self.__refreshTableView()
    @pyqtSlot()
    def on_actionNext_triggered(self):
        self.mapper.toNext()
        self.__refreshTableView()
    @pyqtSlot()
    def on_actionLast_triggered(self):
        self.mapper.toLast()
        self.__refreshTableView()
        
    def __refreshTableView(self):
        index=self.mapper.currentIndex()
        curIndex=self.qryModel.index(index,1)
        self.selModel.clearSelection()
        self.selModel.setCurrentIndex(curIndex,QItemSelectionModel.Select)
        
        
        
        
        
        
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    form=QMain()
    form.show()
    sys.exit(app.exec_())