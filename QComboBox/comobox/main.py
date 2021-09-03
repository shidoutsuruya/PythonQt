import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

from combobox import Ui_ComboBox
class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_ComboBox()
        self.ui.setupUi(self)
    def on_btnInitialize_clicked(self):
        icon=QIcon(r':\icons\images\unit.ico')
        self.ui.CBprovince.clear()
        provinces=['Washington, D.C.','Alabama','Alaska','Arizona','Arkansas','California','Colorado']
        for i in range(len(provinces)):
            self.ui.CBprovince.addItem(icon,provinces[i])
    @pyqtSlot(bool)
    def on_cbEdit_clicked(self,checked):
        self.ui.CBprovince.setEditable(checked)

    def on_btnCityarea_clicked(self):
        icon=QIcon(r':\icons\images\app.ico')
        self.ui.CBcity.clear()
        provinces=['Washington, D.C.','Alabama','Alaska','Arizona','Arkansas','California','Colorado']
        num=[1,5,43,3,4,34,5]
        dicts=dict(zip(provinces,num))
        for i in dicts:
            self.ui.CBcity.addItem(icon,i,dicts[i])
    @pyqtSlot(str)
    def on_CBcity_currentIndexChanged(self,curText):
        self.ui.lineEdit.setText(curText)
        zone=self.ui.CBcity.currentData()
        if zone!=None:
            self.ui.lineEdit.setText(curText+':%d'%zone)
        
    def on_btnClear_clicked(self):
        self.ui.CBcity.clear()
        self.ui.CBprovince.clear()

        


   
    
if __name__=='__main__':
    app=QApplication(sys.argv)
    form=QmyWidget()
    form.show()
    sys.exit(app.exec_())
