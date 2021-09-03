import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QCursor
from PyQt5.QtCore import pyqtSlot,Qt
from ListWidget import Ui_QListWidget

class Q(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_QListWidget()
        self.ui.setupUi(self)
        self.__setActionsForButton()
        self.__createSelectionPopMenu()
        self.__FlagEditable=(Qt.ItemFlag.ItemIsSelectable | Qt.ItemIsUserCheckable
                            | Qt.ItemIsEnabled | Qt.ItemIsEditable)
        self.__FlagNotEditable =(Qt.ItemIsSelectable
                           | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
    def __setActionsForButton(self):
        self.ui.btnList.setDefaultAction(self.ui.actionlist)
        self.ui.btnPlus.setDefaultAction(self.ui.actionplus)
        self.ui.btnInsert.setDefaultAction(self.ui.actioninsert)
        self.ui.btnDelete.setDefaultAction(self.ui.actiondelete)
        self.ui.btnSelect.setDefaultAction(self.ui.actionselect)
        self.ui.btnAll.setDefaultAction(self.ui.actionselect_all)
        self.ui.btnUnall.setDefaultAction(self.ui.actionunselect_all)
        self.ui.btnInverse.setDefaultAction(self.ui.actioninverse)
    def __createSelectionPopMenu(self):
        menuSelection=QMenu(self)
        menuSelection.addAction(self.ui.actionselect_all)
        menuSelection.addAction(self.ui.actionunselect_all)
        menuSelection.addAction(self.ui.actioninverse)
        self.ui.toolButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.ui.toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.ui.toolButton.setDefaultAction(self.ui.actionPopMenu)
        self.ui.toolButton.setMenu(menuSelection)
        toolBtn=QToolButton(self)
        toolBtn.setPopupMode(QToolButton.InstantPopup)
        toolBtn.setDefaultAction(self.ui.actionPopMenu)
        toolBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolBtn.setMenu(menuSelection)
        self.ui.mainToolBar.addWidget(toolBtn)
        self.ui.mainToolBar.addSeparator()
        self.ui.mainToolBar.addAction(self.ui.actionexit)
    @pyqtSlot(bool)
    def on_checkBox_clicked(self,checked):   ##change edit condotion
        if (checked == True):
            Flag=self.__FlagEditable
        else:
            Flag=self.__FlagNotEditable
            
        for i in range(self.ui.listWidget.count()):
            aItem=self.ui.listWidget.item(i)
            aItem.setFlags(Flag)

    @pyqtSlot() #insert
    def on_actioninsert_triggered(self):
        icon=QIcon(r':/icons/iamges/724.bmp')
        editable=self.ui.checkBox.isChecked()
        if (editable==True):
            Flag=self.__FlagEditable
        else:
            Flag=self.__FlagNotEditable
        aItem=QListWidgetItem()
        aItem.setText('insert_Item')
        aItem.setIcon(icon)
        aItem.setCheckState(Qt.Checked)
        aItem.setFlags(Flag)
        curRow=self.ui.listWidget.currentRow()
        self.ui.listWidget.insertItem(curRow,aItem)
    @pyqtSlot()
    def on_actionlist_triggered(self):#initialize
        icon=icon=QIcon(r':/icons/iamges/724.bmp')
        editable=self.ui.checkBox.isChecked()
        if (editable==True):
            Flag=self.__FlagEditable
        else:
            Flag=self.__FlagNotEditable
        self.ui.listWidget.clear()
        for i in range(10):
            itemStr='Item:%d'%i
            aItem=QListWidgetItem()
            aItem.setText(itemStr)
            aItem.setIcon(icon)
            aItem.setCheckState(Qt.Checked)
            aItem.setFlags(Flag)
            self.ui.listWidget.addItem(aItem)
    @pyqtSlot()#delete
    def on_actiondelete_triggered(self):
        row=self.ui.listWidget.currentRow()
        self.ui.listWidget.takeItem(row)
    @pyqtSlot()#clear
    def on_actionclear_triggered(self):
        self.ui.listWidget.clear()
    @pyqtSlot()#select all
    def on_actionselect_all_triggered(self):
        for i in range(self.ui.listWidget.count()):
            aItem=self.ui.listWidget.item(i)
            aItem.setCheckState(Qt.Checked)
    @pyqtSlot()#unselect all
    def on_actionunselect_all_triggered(self):
        for i in range(self.ui.listWidget.count()):
            aItem=self.ui.listWidget.item(i)
            aItem.setCheckState(Qt.Unchecked)
    @pyqtSlot()#inverse
    def on_actioninverse_triggered(self):
        for i in range(self.ui.listWidget.count()):
            aItem=self.ui.listWidget.item(i)
            if aItem.checkState()!=Qt.Checked:
                aItem.setCheckState(Qt.Checked)
            else:
                aItem.setCheckState(Qt.Unchecked)
    def on_listWidget_currentItemChanged(self,current,previous):
        strInfo=""
        if (current!=None):
            if previous==None:
                strInfo='previous:'+current.text()             
            else:
                strInfo='previous:'+previous.text()+',current:'+current.text()
        self.ui.lineEdit.setText(strInfo)
    
    def on_listWidget_customContextMenuRequested(self,pos):
        menuList=QMenu(self)
        menuList.addAction(self.ui.actionlist)
        menuList.addAction(self.ui.actionplus)
        menuList.addAction(self.ui.actioninsert)
        menuList.addAction(self.ui.actiondelete)
        menuList.addAction(self.ui.actionselect)
        menuList.addSeparator()
        menuList.addAction(self.ui.actionselect_all)
        menuList.addAction(self.ui.actionunselect_all)
        menuList.addAction(self.ui.actioninverse)
        menuList.exec(QCursor.pos())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Q()
    window.show()
    sys.exit(app.exec_())
