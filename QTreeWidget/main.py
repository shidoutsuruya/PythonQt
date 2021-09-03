import sys
from PyQt5.QtWidgets import *
from enum import Enum
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon,QPixmap
from TreeWidget import Ui_TreeWidget

class TreeItemType(Enum):
    itTopItem=1001
    itGroupItem=1002
    itImageItem=1003

class TreeColNum(Enum):
    colItem=0
    colItemType=1

class Q(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_TreeWidget()
        self.ui.setupUi(self)

        self.curPixmap=QPixmap()#show picture
        self.pixRatio=1#ratio of picture
        self.itemFlags=(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsAutoTristate)
        self.setCentralWidget(self.ui.scrollArea)
        self.__iniTree()

    def __iniTree(self):
        self.ui.treeWidget.clear()
        icon=QIcon(':/icons/icons/15.ico')
        item=QTreeWidgetItem(TreeItemType.itTopItem.value)
        item.setIcon(TreeColNum.colItem.value,icon)
        item.setText(TreeColNum.colItem.value,'files')
        item.setFlags(self.itemFlags)
        item.setCheckState(TreeColNum.colItem.value,Qt.Checked)
        item.setData(TreeColNum.colItem.value,Qt.UserRole,"")
        self.ui.treeWidget.addTopLevelItem(item)
        self.ui.actionAdd.setEnabled(False)
        self.ui.actionAddDocument.setEnabled(False)
        self.ui.actionDelete.setEnabled(False)

    @pyqtSlot()
    def on_actionAdd_triggered(self):
        dirStr=QFileDialog.getExistingDirectory()
        if (dirStr==""):
            return
        parItem=self.ui.treeWidget.currentItem()
        if (parItem==None):
            parItem=self.ui.treeWidget.topLevelItem(0)
        icon=QIcon(':/icons/icons/open3.bmp')
        dirObj=QDir(dirStr)
        nodeText=dirObj.dirName()
        item=QTreeWidgetItem(TreeItemType.itGroupItem.value)
        item.setIcon(TreeColNum.colItem.value,icon)
        item.setText(TreeColNum.colItem.value,nodeText)
        item.setText(TreeColNum.colItemType.value,'Group')
        item.setFlags(self.itemFlags)
        item.setCheckState(TreeColNum.colItem.value,Qt.Checked)
        item.setData(TreeColNum.colItem.value,Qt.UserRole,dirStr)
        parItem.addChild(item)
        parItem.setExpanded(True)
    
    @pyqtSlot()
    def on_actionAddDocument_triggered(self):
        fileList,flt=QFileDialog.getOpenFileNames(self,'select one or more',"res",'Images(*.jpg)')
        if (len(fileList)<1):
            return
        item=self.ui.treeWidget.currentItem()
        print(item)
        if (item.type()==TreeItemType.itImageItem.value):
            parItem=item.parent()
        else:
            parItem=item
        
        icon=QIcon(r':/icons/icons/31.ico')
        for i in range(len(fileList)):
            fullFileName=fileList[i]
            fileinfo=QFileInfo(fullFileName)
            nodeText=fileinfo.fileName()
            item=QTreeWidgetItem(TreeItemType.itImageItem.value)
            item.setIcon(TreeColNum.colItem.value,icon)
            item.setText(TreeColNum.colItem.value,nodeText)
            item.setText(TreeColNum.colItem.value,'image')
            item.setFlags(self.itemFlags)
            item.setCheckState(TreeColNum.colItem.value,Qt.Checked)
            item.setData(TreeColNum.colItem.value,Qt.UserRole,fullFileName)
            parItem.addChild(item)
        parItem.setExpanded(True)

    def on_treeWidget_currentItemChanged(self,current,previous):
        if (current==None):
            return
        nodeType=current.type()
        if (nodeType==TreeItemType.itTopItem.value):
            self.ui.actionAdd.setEnabled(True)
            self.ui.actionAddDocument.setEnabled(True)
            self.ui.actionDelete.setEnabled(False)
        elif (nodeType==TreeItemType.itGroupItem.value):
            self.ui.actionAdd.setEnabled(True)
            self.ui.actionAddDocument.setEnabled(True)
            self.ui.actionDelete.setEnabled(True)
        elif (nodeType==TreeItemType.itImageItem.value):
            self.ui.actionAdd.setEnabled(False)
            self.ui.actionAddDocument.setEnabled(True)
            self.ui.actionDelete.setEnabled(True)
            self.__displayImage(current)
    @pyqtSlot()
    def on_actionDelete_triggered(self):
        item=self.ui.treeWidget.currentItem()
        parItem=item.parent()
        parItem.removeChild(item)
    def on_actionTraverse_triggered(self):
        count=self.ui.treeWidget.topLevelItemCount()
        for i in range(count):
            item=self.ui.treeWidget.topLevelItem(i)
            self.__changeItemCaption(item)
    def __changeItemCaption(self,item):
        title='*'+item.text(TreeColNum.colItem.value)
        item.setText(TreeColNum.colItem.value,title)
        if (item.childCount()>0):
            for i in range(item.childCount()):
                self.__changeItemCaption(item.child(i)) 

    def __displayImage(self,item):
        filename=item.data(TreeColNum.colItem.value,Qt.UserRole)
        self.ui.statusBar.showMessage(filename)
        self.curPixmap.load(filename)
        self.on_actionHeight_triggered()
        self.ui.actionHeight.setEnabled(True)
        self.ui.actionWidth.setEnabled(True)  
        self.ui.actionMagnify.setEnabled(True)
        self.ui.actionMinify.setEnabled(True)
        self.ui.actionVisiable.setEnabled(True)
     #picture handle
    @pyqtSlot()
    def on_actionHeight_triggered(self):
        H=self.ui.scrollArea.height()
        realH=self.curPixmap.height()
        self.pixRatio=float(H)/realH
        pix=self.curPixmap.scaledToHeight(H-30)
        self.ui.label.setPixmap(pix)
   
    @pyqtSlot()
    def on_actionWidth_triggered(self):
        W=self.ui.scrollArea.width()-20
        realW=self.curPixmap.width()
        self.pixRatio=float(W)/realW
        pix=self.curPixmap.scaledToWidth(W-30)
        self.ui.label.setPixmap(pix)

    @pyqtSlot()
    def on_actionMagnify_triggered(self):
        self.pixRatio=self.pixRatio*1.2
        W=self.pixRatio*self.curPixmap.width()
        H=self.pixRatio*self.curPixmap.height()
        pix=self.curPixmap.scaled(W,H)
        self.ui.label.setPixmap(pix)
    @pyqtSlot()
    def on_actionMinify_triggered(self):
        self.pixRatio=self.pixRatio*0.8
        W=self.pixRatio*self.curPixmap.width()
        H=self.pixRatio*self.curPixmap.height()
        pix=self.curPixmap.scaled(W,H)
        self.ui.label.setPixmap(pix)
    @pyqtSlot()
    def on_actionVisiable_triggered(self):
        self.pixRatio=1
        self.ui.label.setPixmap(self.curPixmap)
    @pyqtSlot(bool)
    def on_actionFloat_triggered(self,checked):
        self.ui.dockWidget.setFloating(checked)
    @pyqtSlot(bool)
    def on_actionVisible_triggered(self,checked):
        self.ui.dockWidget.setVisible(checked)
    @pyqtSlot(bool)
    def on_dockWidget_topLevelChanged(self,topLevel):
        self.ui.actionFloat.setChecked(topLevel)
    @pyqtSlot(bool)
    def on_dockWidget_visibilityChanged(self,visible):
        self.ui.actionVisible.setChecked(visible)    
  


    

        
        



if __name__=='__main__':
    app = QApplication(sys.argv)    
    mainform=Q()        
    mainform.show()                
    sys.exit(app.exec_())    

