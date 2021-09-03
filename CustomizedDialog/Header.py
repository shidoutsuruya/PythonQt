from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from dialogheaders import Ui_DialogHeader

class QmyDialogHeaders(QDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.ui=Ui_DialogHeader()
        self.ui.setupUi(self)

        self.__model=QStringListModel()
        self.ui.listView.setModel(self.__model)
        self.ui.listView.setAlternatingRowColors(True)
        self.ui.listView.setDragDropMode(QAbstractItemView.InternalMove)
        self.ui.listView.setDefaultDropAction(Qt.MoveAction)

    def __del__(self):
        print('header delete')

    def setHeaderList(self,headerStrList):
        self.__model.setStringList(headerStrList)
    def headerList(self):
        return self.__model.stringList()



