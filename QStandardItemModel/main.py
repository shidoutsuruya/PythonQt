import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from StandardItemModel import Ui_StandardItemModel
from DoubleSpinBox import QS,QC

class Q(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_StandardItemModel()
        self.ui.setupUi(self)

        self.__colCount=9 #colume of the table
        self.itemModel=QStandardItemModel(5,self.__colCount,self)
        self.selectionModel=QItemSelectionModel(self.itemModel)
        self.selectionModel.currentChanged.connect(self.do_curChanged)
        self.__lastColumnTitle='try'
        self.__lastColumnFlags=(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
        #table view
        self.ui.tableView.setModel(self.itemModel)
        self.ui.tableView.setSelectionModel(self.selectionModel)
        oneOrMore=QAbstractItemView.ExtendedSelection
        self.ui.tableView.setSelectionMode(oneOrMore)
        itemOrRow=QAbstractItemView.SelectItems
        self.ui.tableView.setSelectionBehavior(itemOrRow)
        self.ui.tableView.verticalHeader().setDefaultSectionSize(22)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.setEnabled(False)
        self.ui.actionsave.setEnabled(False)
        self.ui.actionDelete_row.setEnabled(False)
        self.ui.actionInsert_row.setEnabled(False)
        self.ui.actionAdd_row.setEnabled(False)
        self.__buildStatusBar()
#customize
        self.spinCeShen=QS(0,1000,0,self)
        self.spinLength=QS(0,6000,2,self)
        self.spinDegree=QS(0,360,1,self)
        self.ui.tableView.setItemDelegateForColumn(2,self.spinCeShen)
        self.ui.tableView.setItemDelegateForColumn(3,self.spinLength)
        self.ui.tableView.setItemDelegateForColumn(4,self.spinDegree)

        quality=['A','B','C','D']
        self.comboDelegate=QC(self)
        self.comboDelegate.setItems(quality,False)
        self.ui.tableView.setItemDelegateForColumn(4,self.comboDelegate)
#---------function
    def __buildStatusBar(self):
        self.LabCellPos=QLabel('current cell',self)
        self.LabCellPos.setMinimumWidth(180)
        self.ui.statusBar.addWidget(self.LabCellPos)

        self.LabCellText=QLabel('content cell',self)
        self.LabCellText.setMinimumWidth(150)
        self.ui.statusBar.addWidget(self.LabCellText)

        self.LabCurFile=QLabel('now document:',self)
        self.ui.statusBar.addPermanentWidget(self.LabCurFile)
    def do_curChanged(self,current,previous):
        if (current!=None):
            text='now cell %d row %d column'%(current.row(),current.column())
            self.LabCellPos.setText(text)
            item=self.itemModel.itemFromIndex(current)
            self.LabCellText.setText('content:'+item.text())
            font=item.font()
            self.ui.actionBold.setChecked(font.bold())
    @pyqtSlot()
    def on_actionfile_triggered(self):
        curPath=os.getcwd()
        filename,flt=QFileDialog.getOpenFileName(self,'open file',curPath,'all(*.*)')
        if (filename==""):
            return
        self.LabCurFile.setText('current file:'+filename)
        self.ui.plainTextEdit.clear()
        aFile=open(filename,'r',encoding='utf-8')
        allLines=aFile.readlines()
        aFile.close()
       
        for i in allLines:
            self.ui.plainTextEdit.appendPlainText(i.strip())
        self.__iniModelFromStringList(allLines)
        self.ui.tableView.setEnabled(True)
        self.ui.actionAdd_row.setEnabled(True)
        self.ui.actionInsert_row.setEnabled(True)
        self.ui.actionDelete_row.setEnabled(True)
        self.ui.actionsave.setEnabled(True)
        self.ui.actionmodel_data.setEnabled(True)
    
    def __iniModelFromStringList(self,allLines):
        rowCnt=len(allLines)
        self.itemModel.setRowCount(rowCnt-1)
        headerText=allLines[0].strip()
        headerList=headerText.split(',')
        self.itemModel.setHorizontalHeaderLabels(headerList)
        self.__lastColumnTitle=headerList[len(headerList)-1]

        lastColNo=self.__colCount-1
        for i in range(rowCnt-1):
            lineText=allLines[i+1].strip()
            strList=lineText.split(',')
            for j in range(self.__colCount-1):
                item=QStandardItem(strList[j])
                self.itemModel.setItem(i,j,item)
            item=QStandardItem(self.__lastColumnTitle)
            item.setFlags(self.__lastColumnFlags)
            item.setCheckable(True)
            if (strList[lastColNo]=='0'):
                item.setCheckState(Qt.Unchecked)
            else:
                item.setCheckState(Qt.Checked)
            self.itemModel.setItem(i,lastColNo,item)
    @pyqtSlot()
    def on_actionAdd_row_triggered(self):
        itemlist=[]
        for i in range(self.__colCount-1):
            item=QStandardItem('0')
            itemlist.append(item)
        item=QStandardItem(self.__lastColumnTitle)
        item.setCheckable(True)
        item.setFlags(self.__lastColumnFlags)
        itemlist.append(item)

        self.itemModel.appendRow(itemlist)
        curIndex=self.itemModel.index(self.itemModel.rowCount()-1,0)
        self.selectionModel.clearSelection()
        self.selectionModel.setCurrentIndex(curIndex,QItemSelectionModel.Select)
    @pyqtSlot()
    def on_actionInsert_row_triggered(self):
        itemlist=[]
        for i in range(self.__colCount-1):
            item=QStandardItem('0')
            itemlist.append(item)
        item=QStandardItem(self.__lastColumnTitle)
        item.setFlags(self.__lastColumnFlags)
        item.setCheckable(True)
        item.setCheckState(Qt.Checked)
        itemlist.append(item)

        curIndex=self.selectionModel.currentIndex()
        self.itemModel.insertRow(curIndex.row(),itemlist)
        self.selectionModel.clearSelection()
        self.selectionModel.setCurrentIndex(curIndex,QItemSelectionModel.Select)

    @pyqtSlot()
    def on_actionDelete_row_triggered(self):
        curIndex=self.selectionModel.currentIndex()
        self.itemModel.removeRow(curIndex.row())
    #alignment
    @pyqtSlot()
    def on_actionLeft_triggered(self):
        self.__setCellAlignment(Qt.AlignLeft|Qt.AlignVCenter)
    @pyqtSlot()
    def on_actionCenter_triggered(self):
        self.__setCellAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
    @pyqtSlot()
    def on_actionRight_triggered(self):
        self.__setCellAlignment(Qt.AlignRight|Qt.AlignVCenter)
    
    def __setCellAlignment(self,align=Qt.AlignHCenter):
        if (not self.selectionModel.hasSelection()):
            return
        selectedIndex=self.selectionModel.selectedIndexes()
        count=len(selectedIndex)
        for i in range(count):
            index=selectedIndex[i]
            item=self.itemModel.itemFromIndex(index)
            item.setTextAlignment(align)

    @pyqtSlot(bool)
    def on_actionBold_triggered(self,checked):
        if not self.selectionModel.hasSelection():
            return
        selectedIndex=self.selectionModel.selectedIndexes()
        count=len(selectedIndex)
        for i in range(count):
            index=selectedIndex[i]
            item=self.itemModel.itemFromIndex(index)
            font=item.font()
            font.setBold(checked)
            item.setFont(font)
    @pyqtSlot()
    def on_actionmodel_data_triggered(self):
        self.ui.plainTextEdit.clear()
        lineStr=''
        for i in range(self.itemModel.columnCount()-1):
            item=self.itemModel.horizontalHeaderItem(i)
            lineStr=lineStr+item.text()+'\t'
        item=self.itemModel.horizontalHeaderItem(self.__colCount-1)
        lineStr=lineStr+item.text()
        self.ui.plainTextEdit.appendPlainText(lineStr)

        for i in range(self.itemModel.rowCount()):
            lineStr=""
            for j in range(self.itemModel.columnCount()-1):
                item=self.itemModel.item(i,j)
                lineStr=lineStr+item.text()+'\t'
            item=self.itemModel.item(i,self.__colCount-1)
            if (item.checkState()==Qt.Checked):
                lineStr=lineStr+'1'
            else:
                lineStr=lineStr+'0'
            self.ui.plainTextEdit.appendPlainText(lineStr)
    @pyqtSlot()
    def on_actionsave_triggered(self):
        curPath=os.getcwd()
        filename,flt=QFileDialog.getSaveFileName(self,'save file',curPath,'(*.txt);;(*.*)')
        if filename=="":
            return
        self.on_actionmodel_data_triggered()
        aFile=open(filename,'w',encoding='utf-8')
        aFile.write(self.ui.plainTextEdit.toPlainText())
        aFile.close()



    








if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Q()
    form.show()
    sys.exit(app.exec_())
