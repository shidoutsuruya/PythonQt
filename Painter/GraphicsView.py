from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class GraphicsView(QGraphicsView):
    mouseMove=pyqtSignal(QPoint)
    mouseClicked=pyqtSignal(QPoint)
    mouseDoubleClick=pyqtSignal(QPoint)
    keyPress=pyqtSignal(QKeyEvent)
    
    def mouseMoveEvent(self,event):
        point=event.pos()
        self.mouseMove.emit(point)
        super().mouseMoveEvent(event)

    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton:
            point=event.pos()
            self.mouseClicked.emit(point)
        super().mousePressEvent(event)
    
    def mouseDoubleClickEvent(self,event):
        if event.button()==Qt.LeftButton:
            point=event.pos()
            self.mouseDoubleClick.emit(point)
        super().mouseDoubleClickEvent(event)
        
    def keyPressEvent(self,event):
        self.keyPress.emit(event)
        super().keyPressEvent(event)
        
        