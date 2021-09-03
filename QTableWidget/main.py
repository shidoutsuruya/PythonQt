import sys
from PyQt5.QtWidgets import *
from enum import Enum
from PyQt5.QtCore import pyqtSlot,Qt,QDate
from PyQt5.QtGui import QFont,QBrush,QIcon
from TableWidget import Ui_table_widget

class CellType(Enum):
    ctName=1000
    ctSex=1001
    ctBirth=1002
    ctEthnicity=1003
    ctScore=1004
    ctPartyM=1005
class FieldColNum(Enum):
    colName=0
    colSex=1
    colBirth=2
    colEthnicity=3
    colScore=4
    colPartyM=5
class Q(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_table_widget()
        self.ui.setupUi(self)

        self.labStudID=QLabel('student ID:',self)
        self.labStudID.setMinimumWidth(200)
        self.ui.tableWidget.setAlternatingRowColors(False)
        self.__tableInitialized=False
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
    @pyqtSlot()
    def on_btnSetTitle_clicked(self):
        headerText=['name','sex','birth','ethnicity','score','partisan']
        self.ui.tableWidget.setColumnCount(len(headerText))
        self.ui.tableWidget.setHorizontalHeaderLabels(headerText)
    @pyqtSlot()
    def on_btnSetRow_clicked(self):
        self.ui.tableWidget.setRowCount(self.ui.spinBox.value())
        self.ui.tableWidget.setAlternatingRowColors(self.ui.cbStripe.isChecked())
        self.ui.tableWidget.setAlternatingRowColors(True)
    @pyqtSlot()
    def on_btnInitialize_clicked(self):
        self.ui.tableWidget.clearContents()
        birth=QDate(2000,1,1)
        isParty=True
        ethnicity='han'
        score=250
        rowCount=self.ui.tableWidget.rowCount()
        for i in range(0,rowCount):
            strName='student%d'%(i+1)
            if((i%2)==0):
                strSex='male'
            else:
                strSex='female'
            self.__createItemsArow(i,strName,strSex,birth,ethnicity,isParty,score)
            birth=birth.addDays(20)
            isParty=not isParty
        self.__tableInitialized=True
    #create information
    def __createItemsArow(self,rowNo,name,sex,birth,ethnicity,isParty,score):
        studID=202005000+rowNo
        #name
        item=QTableWidgetItem(name,CellType.ctName.value)
        item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter) 
        font=item.font()  
        font.setBold(True)
        item.setFont(font)
        item.setData(Qt.UserRole,studID)
        self.ui.tableWidget.setItem(rowNo,FieldColNum.colName.value,item)
        #sex
        if (sex=='male'):
            icon=QIcon(':/icons/1.png')
        else:
            icon=QIcon(':/icons/2.png')
        item=QTableWidgetItem(sex,CellType.ctSex.value)
        item.setIcon(icon)
        item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        self.ui.tableWidget.setItem(rowNo,FieldColNum.colSex.value,item)
        #birthday
        strBirth=birth.toString('yyyy-MM-dd')
        item=QTableWidgetItem(strBirth,CellType.ctBirth.value)
        item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        self.ui.tableWidget.setItem(rowNo,FieldColNum.colBirth.value,item)
        #ethnicity
        item=QTableWidgetItem(ethnicity,CellType.ctEthnicity.value)
        item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        if (ethnicity!='han'):
            item.setForeground(QBrush(Qt.blue))
        self.ui.tableWidget.setItem(rowNo,FieldColNum.colEthnicity.value,item)
        #score
        strScore=str(score)
        item=QTableWidgetItem(strScore,CellType.ctScore.value)
        item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        self.ui.tableWidget.setItem(rowNo,FieldColNum.colScore.value,item)
        #partisan
        item=QTableWidgetItem('partisan',CellType.ctPartyM.value)
        item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        if (isParty==True):
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)
        item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsUserCheckable)
        item.setBackground(QBrush(Qt.red))
        self.ui.tableWidget.setItem(rowNo,FieldColNum.colPartyM.value,item)
    @pyqtSlot(int,int,int,int)
    def on_tableWidget_currentCellChanged(self,currentRow,currentColumn,previousRow,previousColumn):
        if (self.__tableInitialized==False):
            return
        item=self.ui.tableWidget.item(currentRow,FieldColNum.colName.value)
        if (item==None):
            return
        item2=self.ui.tableWidget.item(currentRow,FieldColNum.colName.value)
        studID=item2.data(Qt.UserRole)
        self.labStudID.setText('student ID:%d'%studID)
    #insert row    
    @pyqtSlot()
    def on_btnInsertRow_clicked(self):
        curRow=self.ui.tableWidget.currentRow()
        self.ui.tableWidget.insertRow(curRow)
        birth=QDate.fromString('2000-01-01',"yyyy-MM-dd")
        self.__createItemsArow(curRow,'insertnew','female',birth,'xxxd',False,86)
    #add row
    @pyqtSlot()
    def on_btnAddRow_clicked(self):
        curRow=self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(curRow)
        birth=QDate.fromString('2000-01-02','yyyy-MM-dd')
        self.__createItemsArow(curRow,'addnew','female',birth,'xxx',False,86)
    #delete row
    @pyqtSlot()
    def on_btnDelete_clicked(self):
        curRow=self.ui.tableWidget.currentRow()
        self.ui.tableWidget.removeRow(curRow)
    #clear 
    @pyqtSlot()
    def on_btnClear_clicked(self):
        self.ui.tableWidget.clearContents()
    #auto height
    @pyqtSlot()
    def on_btnAutoHeight_clicked(self):
        self.ui.tableWidget.resizeRowsToContents()
    #auto width
    @pyqtSlot()
    def on_btnAutoWidth_clicked(self):
        self.ui.tableWidget.resizeColumnsToContents()
    #editable
    @pyqtSlot(bool)
    def on_cbEditable_clicked(self,checked):
        if checked:
            trig=(QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)
        else:
            trig=QAbstractItemView.NoEditTriggers
        self.ui.tableWidget.setEditTriggers(trig)
    #head title
    @pyqtSlot(bool)
    def on_cbHeadTitle_clicked(self,checked):
        self.ui.tableWidget.horizontalHeader().setVisible(checked)
    #column title
    @pyqtSlot(bool)
    def on_cbColumnTitle_clicked(self,checked):
        self.ui.tableWidget.verticalHeader().setVisible(checked)
    #color
    @pyqtSlot(bool)
    def on_cbStripe_clicked(self,checked):
        self.ui.tableWidget.setAlternatingRowColors(checked)
    #row select
    @pyqtSlot()
    def on_rbRowSelect_clicked(self):
        selMode=QAbstractItemView.SelectRows
        self.ui.tableWidget.setSelectionBehavior(selMode)
    @pyqtSlot()
    def on_rbGridSelect_clicked(self):
        selMode=QAbstractItemView.SelectItems
        self.ui.tableWidget.setSelectionBehavior(selMode)
    @pyqtSlot()
    def on_btnContent2text_clicked(self):
        self.ui.plainTextEdit.clear()
        rowCount=self.ui.tableWidget.rowCount()
        colCount=self.ui.tableWidget.columnCount()
        print(rowCount)
        for i in range(rowCount):
            strText='%d '%(i+1)
            for j in range(colCount-1):
                cellItem=self.ui.tableWidget.item(i,j)
                strText=strText+cellItem.text()+' '
            cellItem=self.ui.tableWidget.item(i,colCount-1)
            if cellItem.checkState()==Qt.Checked:
                strText+='partisan'
            else:
                strText+='masses'
            self.ui.plainTextEdit.appendPlainText(strText)
    

if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=Q()
    form.show()
    sys.exit(app.exec_())