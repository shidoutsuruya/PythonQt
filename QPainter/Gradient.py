import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setPalette(QPalette(Qt.white))
        self.setAutoFillBackground(True)
        self.resize(800,600)
        self.setWindowTitle('hello world')
    def paintEvent1(self,event):
        painter=QPainter(self)
        pen=QPen()
        pen.setStyle(Qt.NoPen)
        painter.setPen(pen)
        w=self.width()
        h=self.height()
        rect=QRect(w/4,h/4,w/2,h/2)
        linearGrad=QLinearGradient(rect.left(),rect.top(),rect.right(),rect.top())
        linearGrad.setColorAt(0,Qt.blue)
        linearGrad.setColorAt(0.5,Qt.white)
        linearGrad.setColorAt(0.7,Qt.red)
        linearGrad.setColorAt(0.3,Qt.yellow)
        linearGrad.setColorAt(0.4,Qt.darkRed)
        linearGrad.setColorAt(1,Qt.green)
        painter.setBrush(linearGrad)
        painter.drawRect(rect)
    '''def paintEvent2(self,event):
        painter=QPainter(self)
        pen=QPen()
        pen.setStyle(Qt.NoPen)
        painter.setPen(pen)
        w=self.width()
        h=self.height()
        rec=QRect(w/4,h/4,w/2,h/2)
        radialGrad=QRadialGradient(w/2,h/2,w/3,w/2,h/2)
        radialGrad.setColorAt(0,Qt.white)
        radialGrad.setColorAt(1,Qt.blue)
        painter.setBrush(radialGrad)
        painter.drawRect(rec)'''
        brush=QBrush()
        brush.setColor(Qt.yellow)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    form=QmyWidget()
    form.show()
    sys.exit(app.exec_())