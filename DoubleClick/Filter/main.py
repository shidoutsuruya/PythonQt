import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Filter import Ui_Filter

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Filter()
        self.ui.setupUi(self)
        self.ui.label.installEventFilter(self)
        self.ui.pushButton.installEventFilter(self)

    def eventFilter(self,watched,event):
        if (watched==self.ui.label):
            if event.type()==QEvent.Enter:
                self.ui.label.setStyleSheet('background-color:rgb(170,255,255)')
            elif (event.type()==QEvent.Leave):
                self.ui.label.setStyleSheet('')
                self.ui.label.setText('close me')
            elif (event.type()==QEvent.MouseButtonPress):
                self.ui.label.setText('button press')
            elif (event.type()==QEvent.MouseButtonRelease):
                self.ui.label.setText('button release')

        if watched==self.ui.pushButton:
            if (event.type()==QEvent.Enter):
                self.ui.pushButton.setStyleSheet('background-color:rgb(94,223,30)')
            elif (event.type()==QEvent.Leave):
                self.ui.pushButton.setStyleSheet('')
                self.ui.pushButton.setText('hello world')
            elif (event.type()==QEvent.MouseButtonDblClick):
                self.ui.pushButton.setText('double')

        return super().eventFilter(watched,event)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=QmyWidget()
    form.show()
    sys.exit(app.exec_())