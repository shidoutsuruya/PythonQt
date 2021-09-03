import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setPalette(QPalette(Qt.yellow))
        self.setAutoFillBackground(True)
        self.resize(300,300)
        self.setWindowTitle('window and viewpoint')
    def paintEvent(self,event):
        painter=QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        w=self.width()
        h=self.height()
        side=min(w,h)
        rect=QRect((w-side)/2,(h-side)/2,side,side)
        painter.drawRect(rect)
        painter.setViewport(rect)
        painter.setWindow(-100,-100,200,200)
    #set pen
        pen=QPen()
        pen.setWidth(1)
        pen.setColor(Qt.blue)
        pen.setStyle(Qt.SolidLine)
        painter.setPen(pen)
    #set gradient
        linearGrad=QLinearGradient(0,0,100,0)
        linearGrad.setColorAt(0,Qt.red)
        linearGrad.setColorAt(0.8,Qt.green)
        linearGrad.setSpread(QGradient.ReflectSpread)
        painter.setBrush(linearGrad)  
        for i in range(36):
            painter.drawEllipse(QPoint(50,0),50,50)
            painter.rotate(10)
            
if __name__=='__main__':
    app=QApplication(sys.argv)
    form=QmyWidget()
    form.show()
    sys.exit(app.exec_())
        
        