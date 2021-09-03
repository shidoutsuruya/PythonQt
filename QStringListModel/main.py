import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from StringListModel import Ui_QStringListModel

class Q(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_QStringListModel()
        self.ui.setupUi(self)
        self.__provinces=['Beijing','Shanghai','Tokyo','NewYork','Washinton','London']
        self.model=QStringListModel(self)
        self.model.setStringList(self.__provinces)
        self.ui.listView.setModel(self.model)
        self.ui.listView.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)
        #uneditable
        #self.ui.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
    @pyqtSlot()
    def on_btnAdd_clicked(self):          
        lastRow=self.model.rowCount()
        self.model.insertRow(lastRow)
        index=self.model.index(lastRow,0)
        self.model.setData(index,'new item',Qt.DisplayRole)
        self.ui.listView.setCurrentIndex(index)
    @pyqtSlot()
    def on_btnInsert_clicked(self):
        index=self.ui.listView.currentIndex()
        self.model.insertRow(index.row())
        self.model.setData(index,'inserted item',Qt.DisplayRole)
        self.ui.listView.setCurrentIndex(index)
    @pyqtSlot()
    def on_btnDelete_clicked(self):
        count=self.model.rowCount()
        self.model.removeRows(0,count)
    @pyqtSlot()
    def on_btnClear_clicked(self):
        count=self.model.rowCount()
        self.model.removeRows(0,count)
    @pyqtSlot()
    def on_btnShowList_clicked(self):
        strList=self.model.stringList()
        self.ui.plainTextEdit.clear()
        for i in strList:
            self.ui.plainTextEdit.appendPlainText(i)
    @pyqtSlot()
    def on_btnClearText_clicked(self):
        self.ui.plainTextEdit.clear()
    
    
        
        


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Q()
    form.show()
    sys.exit(app.exec_())