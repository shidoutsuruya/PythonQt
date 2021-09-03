import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import numpy as np

class Qmywidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setPalette(QPalette(Qt.white))
        self.setAutoFillBackground(True)
        self.resize(600,300)
        self.setWindowTitle('draw star')
        
    def paintEvent(self,event):
        painter=QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)
        r=100.0
        deg=np.pi*72/180
        points=[QPoint(r,0),
                QPoint(r*np.cos(deg),-r*np.sin(deg)),
                QPoint(r*np.cos(2*deg),-r*np.sin(2*deg)),
                QPoint(r*np.cos(3*deg),-r*np.sin(3*deg)),
                QPoint(r*np.cos(4*deg),-r*np.sin(4*deg))]
        font=painter.font()
        font.setPointSize(12)
        font.setBold(False)
        painter.setFont(font)
    #set pen
        pen=QPen()
        pen.setWidth(2)
        pen.setColor(Qt.blue)
        pen.setStyle(Qt.SolidLine)
        pen.setCapStyle(Qt.FlatCap)
        pen.setJoinStyle(Qt.BevelJoin)
        painter.setPen(pen)
    #set brush 
        brush=QBrush()
        brush.setColor(Qt.yellow)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
    #set star path
        starPath=QPainterPath()
        starPath.moveTo(points[0])
        starPath.lineTo(points[2])
        starPath.lineTo(points[4])
        starPath.lineTo(points[1])
        starPath.lineTo(points[3])
        starPath.closeSubpath()
    #set point text
        for i in range(0,5):
            starPath.addText(points[i],font,str(i))
    #draw
        painter.save()
        painter.translate(100,120)
        painter.drawPath(starPath)
        painter.drawText(0,0,'s1')
        painter.restore()
    #translation1
        painter.translate(400,120)
        painter.scale(0.8,0.8)
        painter.rotate(90)
        painter.drawPath(starPath)
        painter.drawText(0,0,'s2')
    #translation2
        painter.resetTransform()
        painter.translate(600,120)
        painter.rotate(-145)
        painter.drawPath(starPath)
        painter.drawText(0,0,'s3')
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Qmywidget()
    form.show()
    sys.exit(app.exec_())
    
            
        