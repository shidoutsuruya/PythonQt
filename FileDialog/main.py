import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Dialog import Ui_Dialog

class QmyDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
    #open one file
    @pyqtSlot()
    def on_btnOpenFile_clicked(self):
        curpath=QDir.currentPath()
        dlgTitle='select a file'
        filt='all(*.*);;text(*.txt);;image(*.jpg *.gif *.png)'
        filename,filterUsed=QFileDialog.getOpenFileName(self,dlgTitle,curpath,filt)
        self.ui.plainTextEdit.appendPlainText(filename)
        self.ui.plainTextEdit.appendPlainText('\n'+filterUsed)
    #open files
    @pyqtSlot()
    def on_btnOpenMoreFile_clicked(self):
        curpath=QDir.currentPath()
        dlgTitle='select files'
        filt='all(*.*);;text(*.txt);;image(*.jpg *.gif *.png)'
        fileList,filtUsed=QFileDialog.getOpenFileNames(self,dlgTitle,curpath,filt)
        for i in range(len(fileList)):
            self.ui.plainTextEdit.appendPlainText(fileList[i])
        self.ui.plainTextEdit.appendPlainText('\n'+filtUsed)
    #save file
    @pyqtSlot()
    def on_btnSave_clicked(self):
        curPath=QDir.currentPath()
        dlgTitle='save file'
        filt='save file(*.*);;text(*.txt);;image(*.jpg *.gif *.png)'
        filename,filtUsed=QFileDialog.getSaveFileName(self,dlgTitle,curPath,filt)
        self.ui.plainTextEdit.appendPlainText(filename)
        self.ui.plainTextEdit.appendPlainText('\n'+filtUsed)
    #select direction
    @pyqtSlot()
    def on_btnSelectDirection_clicked(self):
        curPath=QDir.currentPath()
        dlgTitle='select a direction'
        selectedDir=QFileDialog.getExistingDirectory(self,dlgTitle,curPath,QFileDialog.ShowDirsOnly)
        self.ui.plainTextEdit.appendPlainText('\n'+selectedDir)
    @pyqtSlot()
    def on_btnColor_clicked(self):
        pal=self.ui.plainTextEdit.palette()
        iniColor=pal.color(QPalette.Text)
        color=QColorDialog.getColor(iniColor,self,'select color')
        if color.isValid():
            pal.setColor(QPalette.Text,color)
            self.ui.plainTextEdit.setPalette(pal)
    @pyqtSlot()
    def on_btnFont_clicked(self):
        iniFont=self.ui.plainTextEdit.font()
        font,ok=QFontDialog.getFont(iniFont)
        if ok:
            self.ui.plainTextEdit.setFont(font)
    @pyqtSlot()
    def on_btnProgress_clicked(self):
        labelText='copy!!!'
        btnText='cancel'
        minV=0
        maxV=200
        dlgProgress=QProgressDialog(labelText,btnText,minV,maxV,self)
        dlgProgress.canceled.connect(self.do_progress_canceled)
        dlgProgress.setWindowTitle('copy document')
        dlgProgress.setWindowModality(Qt.WindowModal)
        dlgProgress.setAutoReset(True)
        dlgProgress.setAutoClose(True)

        msCounter=QTime()
        for i in range(minV,maxV+1):
            dlgProgress.setValue(i)
            dlgProgress.setLabelText('copy your file %d'%i)
            msCounter.start()
            while (msCounter.elapsed()<30):
                None
            if dlgProgress.wasCanceled():
                break

    def do_progress_canceled(self):
        self.ui.plainTextEdit.appendPlainText('cancel!!!')

    @pyqtSlot()
    def on_btnInputString_clicked(self):
        dlgTitle='input dialog'
        txtLabel='input your filename'
        defaultInput='new.txt'
        echoMode=QLineEdit.Normal
        #echoMode=QLineEdit.Password
        text,ok=QInputDialog.getText(self,dlgTitle,txtLabel,echoMode,defaultInput)
        if (ok):
            self.ui.plainTextEdit.appendPlainText(text)
    @pyqtSlot()
    def on_btnInputInteger_clicked(self):
        dlgTitle='input Digital'
        txtLabel='set fontsize'
        defaultValue=self.ui.plainTextEdit.font().pointSize()
        minValue=6
        maxValue=50
        stepValue=1
        inputValue,ok=QInputDialog.getInt(self,dlgTitle,txtLabel,defaultValue,minValue,maxValue,stepValue)

        if ok:
            font=self.ui.plainTextEdit.font()
            font.setPointSize(inputValue)
            self.ui.plainTextEdit.setFont(font)
    @pyqtSlot()
    def on_inputFloat_clicked(self):
        dlgTitle='input float'
        textLabel='input a float'
        defaultValue=0.00
        minValue=0
        maxValue=10000
        decimals=2
        inputvalue,ok=QInputDialog.getDouble(self,dlgTitle,textLabel,defaultValue,minValue,maxValue,decimals)

        if ok:
            text='input float:%.2f'%inputvalue
            self.ui.plainTextEdit.appendPlainText(text)
        
    @pyqtSlot()
    def on_btnItem_clicked(self):
        dlgTitle='xxx'
        textLabel='select level'
        curIndex=0
        editable=True
        items=['easy','normal','hard','veteran']
        text,ok=QInputDialog.getItem(self,dlgTitle,textLabel,items,curIndex,editable)
        if ok:
            self.ui.plainTextEdit.appendPlainText(text)
        
    @pyqtSlot()
    def on_btnInfo_clicked(self):
        dlgTitle='infomation'
        strInfo='open successfully'
        QMessageBox.information(self,dlgTitle,strInfo)

    @pyqtSlot()
    def on_btnWarning_clicked(self):
        dlgTitle='warning'
        strInfo='changed'
        QMessageBox.warning(self,dlgTitle,strInfo)
    @pyqtSlot()
    def on_btnCritical_clicked(self):
        dlgTitle='critical'
        strInfo='error'
        QMessageBox.critical(self,dlgTitle,strInfo)

    @pyqtSlot()
    def on_btnAbout_clicked(self):
        dlgTitle='message'
        strInfo='about'
        QMessageBox.about(self,dlgTitle,strInfo)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        dlgTitle='infomation'
        strInfo='changed'
        defaultBtn=QMessageBox.NoButton
        result=QMessageBox.question(self,dlgTitle,strInfo,QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel,defaultBtn)
        if result==QMessageBox.Yes:
            self.ui.plainTextEdit.appendPlainText('Question:Yes')
        elif result==QMessageBox.No:
            self.ui.plainTextEdit.appendPlainText('Question:No')
        elif result==QMessageBox.Cancel:
            self.ui.plainTextEdit.appendPlainText('Question:cancel')
        else:
            self.ui.plainTextEdit.appendPlainText('Question:not select')
    


        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QmyDialog()
    window.show()
    sys.exit(app.exec_())