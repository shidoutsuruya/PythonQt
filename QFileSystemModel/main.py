import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from FileSystemModel import Ui_FileSystemModel

class Q(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_FileSystemModel()
        self.ui.setupUi(self)
        self.__buildModelView()
    def __buildModelView(self):
        self.model=QFileSystemModel(self)
        self.model.setRootPath(QDir.currentPath())
        self.ui.treeView.setModel(self.model)
        self.ui.listView.setModel(self.model)
        self.ui.tableView.setModel(self.model)
        self.ui.treeView.clicked.connect(self.ui.listView.setRootIndex)
        self.ui.treeView.clicked.connect(self.ui.tableView.setRootIndex)
    def on_treeView_clicked(self,index):
        self.ui.checkBox.setChecked(self.model.isDir(index))
        self.ui.label_1.setText(self.model.filePath(index))
        self.ui.label_2.setText(self.model.type(index))
        self.ui.label_3.setText(self.model.fileName(index))
        fileSize=self.model.size(index)/1024
        if (fileSize<1024):
            self.ui.label_4.setText('%d KB'%fileSize)
        else:
            self.ui.label_4.setText('%.2f MB'%(fileSize/1024.0))
    
    
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Q()
    window.show()
    sys.exit(app.exec_())