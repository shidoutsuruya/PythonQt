import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from PyQt5.QtGui import *
from ui_dialog import Ui_Dialog

class Dialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.__record=QSqlRecord()
    def setInsertRecord(self,recData):
        self.__record=recData
        self.ui.spinBoxID.setEnabled(True)
        self.setWindowTitle('insert new record')
        self.ui.spinBoxID.setValue(recData.value('ID'))
        sexList=['MALE','FEMALE']
        for i in sexList:    
            self.ui.comboBoxSex.addItem(i)    
        self.ui.comboBoxSex.setCurrentText(recData.value('Sex'))
    def setUpdateRecord(self,recData):
        self.__record=recData
        self.ui.spinBoxID.setEnabled(False)
        self.setWindowTitle('update new record')
        self.ui.spinBoxID.setValue(recData.value('ID'))
        self.ui.lineEditName.setText(recData.value('Name'))
        sexList=['MALE','FEMALE']
        for i in sexList:    
            self.ui.comboBoxSex.addItem(i)    
        self.ui.comboBoxSex.setCurrentText(recData.value('Sex'))
        birth=recData.value('Birth')
        birth_date=QDate.fromString(birth,'yyyy-MM-dd')
        self.ui.dateEdit.setDate(birth_date)
        self.ui.lineEditCountry.setText(recData.value('Country'))
        self.ui.spinBoxAge.setValue(recData.value('Age'))
        self.ui.doubleSpinBoxSalary.setValue(recData.value('Salary'))
        picData=recData.value('Image')
        if picData=="":
            self.ui.LabImage.clear()
        else:
            pic=QPixmap()
            pic.loadFromData(picData)
            h=self.ui.LabImage.size().width()
            self.ui.LabImage.setPixmap(pic.scaledToWidth(h))
    def getRecordData(self):
        self.__record.setValue('ID',self.ui.spinBoxID.value())
        self.__record.setValue('Name',self.ui.lineEditName.text())
        self.__record.setValue('Sex',self.ui.comboBoxSex.currentText())
        self.__record.setValue('Birth',self.ui.dateEdit.date())
        self.__record.setValue('Country',self.ui.lineEditCountry.text())
        self.__record.setValue('Age',self.ui.spinBoxAge.value())
        self.__record.setValue('Salary',self.ui.doubleSpinBoxSalary.value())
        return self.__record
        
    @pyqtSlot()
    def on_btnImport_clicked(self):
        fileName,filt=QFileDialog.getOpenFileName(self,'select image','','image(*.jpg *.png *.bmp)')
        if fileName=='':
            return
        file=QFile(fileName)
        file.open(QIODevice.ReadOnly)
        data=file.readAll()
        file.close()
        
        self.__record.setValue('Image',data)
        pic=QPixmap()
        pic.loadFromData(data)
        h=self.ui.LabImage.height()
        self.ui.LabImage.setPixmap(pic.scaledToWidth(h))
    @pyqtSlot()
    def on_btnClear_clicked(self):
        self.ui.LabImage.clear()
        self.__record.setNull('Image')
if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Dialog()
    form.show()
    sys.exit(app.exec_())
