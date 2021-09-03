import sys
sys.path.append(r"C:\Users\max21\Desktop\Python\PythonQt\QpushButton")
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtGui import QFont
from ui_widget import Ui_Widget
class QmyWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui=Ui_Widget()
        self.ui.setupUi(self) 

    def on_leftBtn_clicked(self):
        self.ui.textEdit.setAlignment(Qt.AlignLeft)
    def on_middleBtn_clicked(self):
        self.ui.textEdit.setAlignment(Qt.AlignCenter)
    def on_rightBtn_clicked(self):
        self.ui.textEdit.setAlignment(Qt.AlignRight)
    
    @pyqtSlot(bool)
    def on_boldBtn_clicked(self,checked):
        font=self.ui.textEdit.font()
        font.setBold(checked)
        self.ui.textEdit.setFont(font)
    @pyqtSlot(bool)
    def on_italicBtn_clicked(self,checked):
        font=self.ui.textEdit.font()
        font.setItalic(checked)
        self.ui.textEdit.setFont(font)
    @pyqtSlot(bool)
    def on_underlineBtn_clicked(self,checked):
        font=self.ui.textEdit.font()
        font.setUnderline(checked)
        self.ui.textEdit.setFont(font)



    @pyqtSlot(bool)
    def on_rendonly_clicked(self,checked):
        self.ui.textEdit.setReadOnly(checked)
    @pyqtSlot(bool)
    def on_enabled_clicked(self,checked):
        self.ui.textEdit.setEnabled(checked)
    @pyqtSlot(bool)
    def on_clearbtn_clicked(self,checked):
        self.ui.textEdit.clear()

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=QmyWidget()
    form.show()
    sys.exit(app.exec_())






