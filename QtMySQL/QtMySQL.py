import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from PyQt5.QtGui import *
import PyQt5.QtSql as sql
from ui_QtMySQL import Ui_QtMySQL

class QmyComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
      super().__init__(parent)
      self.__itemList=[]
      self.__isEditable=False
        

    def setItems(self,itemList, isEditable=False):
      self.__itemList=itemList
      self.__isEditable=isEditable

    def createEditor(self, parent, option, index):
      editor = QComboBox(parent)
      editor.setFrame(False)
      editor.setEditable(self.__isEditable)
      editor.addItems(self.__itemList)
      return editor

    def setEditorData(self,editor,index):
      model=index.model()
      text = model.data(index, Qt.EditRole)
##      text = str(index.model().data(index, Qt.EditRole))
      editor.setCurrentText(text)
        
    def setModelData(self,editor,model,index):
      text = editor.currentText()
      model.setData(index, text, Qt.EditRole)
    
    def updateEditorGeometry(self,editor,option,index):
      editor.setGeometry(option.rect)

class QMain(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_QtMySQL()
        self.ui.setupUi(self)
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.actionOpen.setEnabled(True)
        self.ui.actionAdd.setEnabled(False)
        self.ui.actionInsert.setEnabled(False)
        self.ui.actionDelete.setEnabled(False)
        self.ui.actionBonus.setEnabled(False)
        self.ui.actionSave.setEnabled(False)
        self.ui.actionUndo.setEnabled(False)
        self.ui.actionSet_Picture.setEnabled(False)
        self.ui.actionClear_picture.setEnabled(False)
        
    @pyqtSlot()
    def on_actionOpen_triggered(self):
        dbFilename,flt=QFileDialog.getOpenFileName(self,'select file','','sql(*.db *.db3 *.sql)')
        self.db=sql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(dbFilename)
        if self.db.open():
            self.__openTable()
        else:
            QMessageBox.warning(self,'wrong','cannot open sql document')
            
    def __getFieldNames(self):
        emptyRec=self.tabModel.record()
        self.fldNum={}
        for i in range(emptyRec.count()):
            fieldName=emptyRec.fieldName(i)
            self.ui.comboBoxArrange.addItem(fieldName)
            self.fldNum.setdefault(fieldName)
            self.fldNum[fieldName]=i
        print(self.fldNum)
    def __openTable(self):
        self.tabModel=QSqlTableModel(self,self.db)
        self.tabModel.setTable('qttest')
        self.tabModel.setSort(self.tabModel.fieldIndex('ID'),Qt.AscendingOrder)
        self.tabModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        if(self.tabModel.select()==False):
            QMessageBox.critical(self,'wrong','open file is wrong'+self.tabModel.lastError().text())
            return
        self.__getFieldNames()
#set headerdata        
        self.tabModel.setHeaderData(self.fldNum['ID'],Qt.Horizontal,'id')
        self.tabModel.setHeaderData(self.fldNum['Name'],Qt.Horizontal,'name')
        self.tabModel.setHeaderData(self.fldNum['Sex'],Qt.Horizontal,'sex')
        self.tabModel.setHeaderData(self.fldNum['Birth'],Qt.Horizontal,'birth')
        self.tabModel.setHeaderData(self.fldNum['Country'],Qt.Horizontal,'country')
        self.tabModel.setHeaderData(self.fldNum['Age'],Qt.Horizontal,'age')
        self.tabModel.setHeaderData(self.fldNum['Salary'],Qt.Horizontal,'salary')
#create mapper
        self.mapper=QDataWidgetMapper()
        self.mapper.setModel(self.tabModel)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit)
#connection of button and model
        self.mapper.addMapping(self.ui.spinBoxID,self.fldNum['ID'])
        self.mapper.addMapping(self.ui.lineEditName,self.fldNum['Name'])
        self.mapper.addMapping(self.ui.comboBoxSex,self.fldNum['Sex'])
        self.mapper.addMapping(self.ui.dateEdit,self.fldNum['Birth'])
        self.mapper.addMapping(self.ui.lineEditCountry,self.fldNum['Country'])
        self.mapper.addMapping(self.ui.spinBoxAge,self.fldNum['Age'])
        self.mapper.addMapping(self.ui.doubleSpinBoxSalary,self.fldNum['Salary'])
        self.mapper.toFirst()
        
        self.selModel=QItemSelectionModel(self.tabModel) #select model
        self.selModel.currentChanged.connect(self.do_currentChanged)
        self.selModel.currentRowChanged.connect(self.do_currentRowChanged)
        #table view
        self.ui.tableView.setModel(self.tabModel)
        self.ui.tableView.setSelectionModel(self.selModel)
        self.ui.tableView.setColumnHidden(self.fldNum['Image'],True)
        #male and female
        strList=('MALE','FEMALE')
        self.__delegateSex=QmyComboBoxDelegate()
        self.__delegateSex.setItems(strList,False)#uneditable
        self.ui.tableView.setItemDelegateForColumn(self.fldNum['Sex'],self.__delegateSex)
        #refresh the action
        self.ui.actionAdd.setEnabled(True)
        self.ui.actionInsert.setEnabled(True)
        self.ui.actionDelete.setEnabled(True)
        self.ui.actionBonus.setEnabled(True)
        self.ui.actionSave.setEnabled(True)
        self.ui.actionUndo.setEnabled(True)
        self.ui.actionSave.setEnabled(True)
        self.ui.actionSet_Picture.setEnabled(True)
        self.ui.actionClear_picture.setEnabled(True)
        
        
    def do_currentChanged(self,previous):
        self.ui.actionSave.setEnabled(self.tabModel.isDirty())
        self.ui.actionUndo.setEnabled(self.tabModel.isDirty())
        
    def do_currentRowChanged(self,current,previous):
        self.ui.actionDelete.setEnabled(current.isValid())
        self.ui.actionSet_Picture.setEnabled(current.isValid())
        self.ui.actionClear_picture.setEnabled(current.isValid())
        if current.isValid()==False:
            self.ui.LabImage.clear()
            return
        self.mapper.setCurrentIndex(current.row())
        curRec=self.tabModel.record(current.row())
        if curRec.isNull('Image'):
            self.ui.LabImage.setText('Null')
        else:
            data=curRec.value('Image')
            pic=QPixmap()
            pic.loadFromData(data)
            w=self.ui.LabImage.size().height()
            self.ui.LabImage.setPixmap(pic.scaledToWidth(w))
            
    @pyqtSlot() #insert
    def on_actionAdd_triggered(self):
        self.tabModel.insertRow(self.tabModel.rowCount(),QModelIndex())
        curIndex=self.tabModel.index(self.tabModel.rowCount()-1,1)
        self.selModel.clearSelection()#clear selection
        self.selModel.setCurrentIndex(curIndex,QItemSelectionModel.Select)
        currow=curIndex.row()
        self.tabModel.setData(self.tabModel.index(currow,self.fldNum['ID']),2000+self.tabModel.rowCount())
    @pyqtSlot()
    def on_actionInsert_triggered(self):
        curIndex=self.ui.tableView.currentIndex()
        self.tabModel.insertRow(curIndex.row(),QModelIndex())
        self.selModel.clearSelection()
        self.selModel.setCurrentIndex(curIndex,QItemSelectionModel.Select)
    @pyqtSlot()
    def on_actionDelete_triggered(self):
        curIndex=self.selModel.currentIndex()
        self.tabModel.removeRow(curIndex.row())
    @pyqtSlot()
    def on_actionSave_triggered(self):
        res=self.tabModel.submitAll()
        if res==False:
            QMessageBox.information(self,'info','save error!!!'+self.tabModel.lastError().text())
        else:
            self.ui.actionSave.setEnabled(False)
            self.ui.actionUndo.setEnabled(False)
    @pyqtSlot()
    def on_actionUndo_triggered(self):
        self.tabModel.revertAll()
        self.ui.actionSave.setEnabled(False)
        self.ui.actionUndo.setEnabled(False)
    @pyqtSlot()
    def on_actionSet_Picture_triggered(self):
        fileName,filt=QFileDialog.getOpenFileName(self,'select image','','image(*.jpg *.png *.bmp)')
        if fileName=='':
            return
        file=QFile(fileName)
        file.open(QIODevice.ReadOnly)
        try:
            data=file.readAll()
        finally:
            file.close()
        curRecNo=self.selModel.currentIndex().row()
        curRec=self.tabModel.record(curRecNo)
        curRec.setValue('Image',data)
        self.tabModel.setRecord(curRecNo,curRec)
        pic=QPixmap()
        pic.loadFromData(data)
        w=self.ui.LabImage.height()
        self.ui.LabImage.setPixmap(pic.scaledToWidth(w))
        
    @pyqtSlot()
    def on_actionClear_picture_triggered(self):
        curRecNo=self.selModel.currentIndex().row()
        curRec=self.tabModel.record(curRecNo)
        curRec.setNull('Image')
        self.tabModel.setRecord(curRecNo,curRec)
        self.ui.LabImage.clear()   
    @pyqtSlot()
    def on_actionBonus_triggered(self):
        if (self.tabModel.rowCount()==0):
            return
        for i in range(self.tabModel.rowCount()):
            record=self.tabModel.record(i)
            salary=record.value('Salary')
            salary=salary*1.1
            record.setValue('Salary',salary)
            self.tabModel.setRecord(i,record)
        if self.tabModel.submitAll():
            QMessageBox.information(self,'info','BONUS!!!!')
#arrangement
    @pyqtSlot(int)
    def on_comboBoxArrange_currentIndexChanged(self,index):
        if self.ui.radioAscend.isChecked():
            self.tabModel.setSort(index,Qt.AscendingOrder)
        else:
            self.tabModel.setSort(index,Qt.DescendingOrder)
        self.tabModel.select()
    @pyqtSlot()
    def on_radioAscend_clicked(self):
        self.tabModel.setSort(self.ui.comboBoxArrange.currentIndex(),Qt.AscendingOrder)
        self.tabModel.select()
    @pyqtSlot()
    def on_radioDescend_clicked(self):
        self.tabModel.setSort(self.ui.comboBoxArrange.currentIndex(),Qt.DescendingOrder)
        self.tabModel.select()
#filter
    @pyqtSlot()
    def on_radioMale_clicked(self):
        self.tabModel.setFilter("Sex='MALE'")
    @pyqtSlot()
    def on_radioFemale_clicked(self):
        self.tabModel.setFilter("Sex='FEMALE'")
    @pyqtSlot()
    def on_radioAll_clicked(self):
        self.tabModel.setFilter('')
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMain()
    window.show()
    sys.exit(app.exec_())
    