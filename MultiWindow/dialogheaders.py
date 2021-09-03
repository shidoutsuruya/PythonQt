import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_dialogheaders import Ui_headers

class QmyDialogHeaders(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_headers()
        self.ui.setupUi(self)

        self.__model=QStringListModel()
        self.ui.listView.setModel(self.__model)
        self.ui.listView.setAlternatingRowColors(True)
        self.ui.listView.setDragDropMode(QAbstractItemView.InternalMove)
        self.ui.listView.setDefaultDropAction(Qt.MoveAction)

    def __del__(self):
        print('myDialogHeader is deleted')

    def setHeaderList(self,headerStrList):
        self.__model.setStringList(headerStrList)

    def headerList(self):
        return self.__model.stringList()

if  __name__ == "__main__":         
    app = QApplication(sys.argv)    
    form=QmyDialogHeaders()      
    form.show()
    sys.exit(app.exec_())