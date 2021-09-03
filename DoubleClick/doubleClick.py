import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QL(QLabel):
    doubleClicked=pyqtSignal()
    def mouseDoubleClickEvent(self,event):
        self.doubleClicked.emit()

class QW(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(280,150)
        self.setWindowTitle('signal')
        LabHello=QL(self)
        LabHello.setText('click double')
        font=LabHello.font()
        font.setPointSize(14)
        font.setBold(True)
        LabHello.setFont(font)
        size=LabHello.sizeHint()
        LabHello.setGeometry(70,60,size.width(),size.height())
        LabHello.doubleClicked.connect(self.do_doubleClicked)
    def do_doubleClicked(self):
        print('clicked')
    def mouseDoubleClickEvent(self,event):
        print('!!!!')

if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=QW()
    form.show()
    sys.exit(app.exec_())