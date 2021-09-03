import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from DragWidget import Ui_DragWidget

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_DragWidget()
        self.ui.setupUi(self)

        self.ui.listSource.installEventFilter(self) #eventfilter
        self.ui.listWidget.installEventFilter(self)
        self.ui.treeWidget.installEventFilter(self)
        self.ui.tableWidget.installEventFilter(self)

        self.ui.listSource.setAcceptDrops(True)
        self.ui.listSource.setDragDropMode(QAbstractItemView.DragDrop)
        self.ui.listSource.setDragEnabled(True)
        self.ui.listSource.setDefaultDropAction(Qt.CopyAction)

        self.ui.listWidget.setAcceptDrops(True)
        self.ui.listWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.ui.listWidget.setDragEnabled(True)
        self.ui.listWidget.setDefaultDropAction(Qt.MoveAction)

        self.ui.treeWidget.setAcceptDrops(True)
        self.ui.treeWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.ui.treeWidget.setDragEnabled(True)
        self.ui.treeWidget.setDefaultDropAction(Qt.MoveAction)

        self.ui.tableWidget.setAcceptDrops(True)
        self.ui.tableWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.ui.tableWidget.setDragEnabled(True)
        self.ui.tableWidget.setDefaultDropAction(Qt.MoveAction)

        self.__itemView=None
        self.on_rbtListSource_clicked()

    @pyqtSlot()#list source
    def on_rbtListSource_clicked(self):
        self.__itemView=self.ui.listSource
        self.__refreshToUI()
    @pyqtSlot()
    def on_rbtListWidget_clicked(self):
        self.__itemView=self.ui.listWidget
        self.__refreshToUI()
    @pyqtSlot()
    def on_rbtTreeWidget_clicked(self):
        self.__itemView=self.ui.treeWidget
        self.__refreshToUI()
    @pyqtSlot()
    def on_rbtTableWidget_clicked(self):
        self.__itemView=self.ui.tableWidget
        self.__refreshToUI()

    def __refreshToUI(self):
        self.ui.checkBox_1.setChecked(self.__itemView.acceptDrops())
        self.ui.checkBox_2.setChecked(self.__itemView.dragEnabled())
        self.ui.comboBox_1.setCurrentIndex(self.__itemView.dragDropMode())
        index=self.__getDropActionIndex(self.__itemView.defaultDropAction())
        self.ui.comboBox_2.setCurrentIndex(index)
    def __getDropActionIndex(self,actionType):
        if actionType==Qt.CopyAction:
            return 0
        elif actionType==Qt.MoveAction:
            return 1
        elif actionType==Qt.LinkAction:
            return 2
        elif actionType==Qt.IgnoreAction:
            return 3
        else:
            return 0
    
    @pyqtSlot(bool)
    def on_checkBox_1_clicked(self,checked):
        self.__itemView.setAcceptDrops(checked)
    @pyqtSlot(bool)
    def on_checkBox_2_clicked(self,checked):
        self.__itemView.setDragEnabled(checked)
    @pyqtSlot(int)
    def on_comboBox_1_currentIndexChanged(self,index):
        mode=QAbstractItemView.DragDropMode(index)
        self.__itemView.setDragDropMode(mode)
    @pyqtSlot(int)
    def on_comboBox_2_currentIndexChanged(self,index):
        actionType=self.__getDropActionType(index)
        self.__itemView.setDefaultDropAction(actionType)
     
    def __getDropActionType(self,index):
        if index==0:
            return Qt.CopyAction
        elif index==1:
            return Qt.MoveAction
        elif index==2:
            return Qt.LinkAction
        elif index==3:
            return Qt.IgnoreAction
        else:
            return Qt.CopyAction

    
    def eventFilter(self,watched,event):
        if (event.type()==QEvent.KeyPress) and (event.key()==Qt.Key_Delete):
            if (watched==self.ui.listSource):
                self.ui.listSource.takeItem(self.ui.listSource.currentRow())
            elif (watched==self.ui.listWidget):
                self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
            elif (watched==self.ui.treeWidget):
                curItem=self.ui.treeWidget.currentItem()
                if (curItem.parent()!=None):
                    parItem=curItem.parent()
                    parItem.removeChild(curItem)
                else:
                    index=self.ui.treeWidget.indexOfTopLevelItem(curItem)
                    self.ui.treeWidget.takeTopLevelItem(index)
            elif (watched==self.ui.tableWidget):
                self.ui.tableWidget.takeItem(self.ui.tableWidget.currentRow(),self.ui.tableWidget.currentColumn())

        return super().eventFilter(watched,event)
        





if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=QmyWidget()
    form.show()
    sys.exit(app.exec_())