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
    def paintEvent(self,event):
        painter=QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)    
    #set pen   
        pen=QPen()
        pen.setWidth(3)
        pen.setColor(Qt.green)
        pen.setStyle(Qt.DashLine)
        pen.setCapStyle(Qt.FlatCap)
        pen.setJoinStyle(Qt.MiterJoin)
        painter.setPen(pen)    
    #set brush
        brush=QBrush()
        brush.setColor(Qt.yellow)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
    #draw
        w=self.width()
        h=self.height()
        rec=QRect(w/4,h/4,w/2,h/2)
        painter.drawRect(rec)
        
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    form=QmyWidget()
    form.show()
    sys.exit(app.exec_())