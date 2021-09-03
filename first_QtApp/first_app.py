import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import *
from ui_Qt import Ui_qt

class QmyDialog(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui=Ui_qt()
        self.ui.setupUi(self)
        self.ui.Black.clicked.connect(self.setTextColor)
        self.ui.Red.clicked.connect(self.setTextColor)
        self.ui.Blue.clicked.connect(self.setTextColor)
    def on_clear_clicked(self):
        self.ui.plainTextEdit.clear()
    def on_Bold_toggled(self,checked):
        font=self.ui.plainTextEdit.font()
        font.setBold(checked)
        self.ui.plainTextEdit.setFont(font)
    def on_Underline_clicked(self):
        checked=self.ui.Underline.isChecked()
        font=self.ui.plainTextEdit.font()
        font.setUnderline(checked)
        self.ui.plainTextEdit.setFont(font)
    @pyqtSlot(bool)      #overload singal
    def on_Italic_clicked(self,checked):
        font=self.ui.plainTextEdit.font()
        font.setItalic(checked)
        self.ui.plainTextEdit.setFont(font)

    def setTextColor(self): ##__personal defination
        plet=self.ui.plainTextEdit.palette()
        if (self.ui.Black.isChecked()):
            plet.setColor(QPalette.Text,Qt.black)
        elif (self.ui.Red.isChecked()):
            plet.setColor(QPalette.Text,Qt.red)
        elif (self.ui.Blue.isChecked()):
            plet.setColor(QPalette.Text,Qt.blue)
        self.ui.plainTextEdit.setPalette(plet)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=QmyDialog()
    form.show()
    sys.exit(app.exec_())


