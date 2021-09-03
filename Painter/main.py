import sys,random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from GraphicsView import GraphicsView
from ui_painter import Ui_Painter

class QMain(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Painter()
        self.ui.setupUi(self)
        
        self.__buildStatusBar()
        self.__iniGraphicsSystem()
        self.__itemID=1
        self.__itemDesc=2
        
        self.__seqNum=0
        self.__back=0
        self.__front=0
        
    def __buildStatusBar(self):
        self.__labViewCord=QLabel('view')
        self.__labViewCord.setMinimumWidth(150)
        self.ui.statusBar.addWidget(self.__labViewCord)
        
        self.__labSceneCord=QLabel('coordination')
        self.__labSceneCord.setMinimumWidth(150)
        self.ui.statusBar.addWidget(self.__labSceneCord)
        
        self.__labItemCord=QLabel('item:')
        self.__labItemCord.setMinimumWidth(150)
        self.ui.statusBar.addWidget(self.__labItemCord)
        
        self.__labItemInfo=QLabel('ItemInfo:')
        self.ui.statusBar.addPermanentWidget(self.__labItemInfo)
        
    def __iniGraphicsSystem(self):
        self.view=GraphicsView(self)
        self.setCentralWidget(self.view)
        self.scene=QGraphicsScene(-300,-200,600,200)
        self.view.setScene(self.scene)
        
        self.view.setCursor(Qt.CrossCursor)
        self.view.setMouseTracking(True)
        self.view.setDragMode(QGraphicsView.RubberBandDrag)
        
        self.view.mouseMove.connect(self.do_mouseMove)
        self.view.mouseClicked.connect(self.do_mouseClicked)
        self.view.mouseDoubleClick.connect(self.do_mouseDoubleClick)
        self.view.keyPress.connect(self.do_keyPress)
        
    @pyqtSlot()
    def on_actionRectangle_triggered(self):
        item=QGraphicsRectItem(-50,-25,100,50)
        item.setBrush(QBrush(Qt.yellow))
        self.__setItemProperties(item,'rectangle')
        
    @pyqtSlot()
    def on_actionEllipse_triggered(self):
        item=QGraphicsEllipseItem(-50,-30,100,60)
        item.setBrush(QBrush(Qt.blue))
        self.__setItemProperties(item,'ellipse') 
    @pyqtSlot()
    def on_actionCircle_triggered(self):
        item=QGraphicsEllipseItem(-50,-50,100,100)
        item.setBrush(QBrush(Qt.cyan))
        self.__setItemProperties(item,'circle')
    @pyqtSlot()
    def on_actionTriangle_triggered(self):
        item=QGraphicsPolygonItem()      
        points=[QPointF(0,-40),QPointF(60,40),QPointF(-60,40)]
        item.setPolygon(QPolygonF(points))
        item.setBrush(QBrush(Qt.magenta))
        self.__setItemProperties(item,'triangle')
    @pyqtSlot()
    def on_actionTrapezium_triggered(self):
        item=QGraphicsPolygonItem()
        points=[QPointF(-40,-40),QPointF(40,-40),QPointF(100,40),QPointF(-100,40)]
        item.setPolygon(QPolygonF(points))
        item.setBrush(QBrush(Qt.green))
        self.__setItemProperties(item,'trapezium')
    @pyqtSlot()
    def on_actionLine_triggered(self):
        item=QGraphicsLineItem(-100,0,100,0)
        pen=QPen(Qt.red)
        pen.setWidth(4)
        item.setPen(pen)
        self.__setItemProperties(item,'line')
    @pyqtSlot()
    def on_actionText_triggered(self):
        strText,ok=QInputDialog.getText(self,'input','input text')
        if (not ok):
            return
        item=QGraphicsTextItem(strText)
        font=self.font()
        font.setPointSize(20)
        font.setBold(True)
        item.setFont(font)
        item.setDefaultTextColor(Qt.black)
        self.__setItemProperties(item,'text')
#################################################################################
    @pyqtSlot()
    def on_actionZoomIn_triggered(self):
        items=self.scene.selectedItems()
        cnt=len(items)
        if cnt==1:
            item=items[0]
            item.setScale(0.1+item.scale())
        else:
            self.view.scale(1.1,1.1)
    @pyqtSlot()
    def on_actionZoomOut_triggered(self):
        items=self.scene.selectedItems()
        cnt=len(items)
        if cnt==1:
            item=items[0]
            item.setScale(item.scale()-0.1)
        else:
            self.view.scale(0.9,0.9)
    
    @pyqtSlot()
    def on_actionRotateLeft_triggered(self):
        items=self.scene.selectedItems()
        cnt=len(items)
        if cnt==1:
            item=items[0]
            item.setRotation(-30+item.rotation())
        else:
            self.view.rotate(-30)
        
    @pyqtSlot()
    def on_actionRotateRight_triggered(self):
        items=self.scene.selectedItems()
        cnt=len(items)
        if cnt==1:
            item=items[0]
            item.setRotation(30+item.rotation())
        else:
            self.view.rotate(30)
    @pyqtSlot()
    def on_actionRestore_triggered(self):
        items=self.scene.selectedItems()
        cnt=len(items)
        if cnt==1:
            item=items[0]
            item.setScale(1)
            item.setRotation(0)
        else:
            self.view.resetTransform()
    @pyqtSlot()
    def on_actionFront_triggered(self):
        items=self.scene.selectedItems()
        cnt=len(items)
        if cnt>0:
            item=items[0]
            self.__front=1+self.__front
            item.setZValue(self.__front)
            
            
    @pyqtSlot()
    def on_actionBack_triggered(self):
        items=self.scene.selectedItems()
        cnt=len(items)
        if cnt>0:
            item=items[0]
            self.__back=self.__back-1 
            item.setZValue(self.__back) 
                
    @pyqtSlot()
    def on_actionGroup_triggered(self):
        items=self.scene.selectedItems()
        cnt=len(items)
        if cnt<=1:
            return     
        group=QGraphicsItemGroup()
        self.scene.addItem(group)
        for i in range(cnt):
            item=items[i]
            item.setSelected(False)
            item.clearFocus()
            group.addToGroup(item)
        group.setFlag(QGraphicsItem.ItemIsFocusable)
        group.setFlag(QGraphicsItem.ItemIsMovable)
        group.setFlag(QGraphicsItem.ItemIsSelectable)
        self.__front+=1
        group.setZValue(self.__front)
        self.scene.clearSelection()
        group.setSelected(True)
        
    @pyqtSlot()
    def on_actionUngroup_triggered(self):
        items=self.scene.selectedItems()
        cnt=len(items)
        if cnt==1:
            group=items[0]
            self.scene.destroyItemGroup(group)
        
        
    @pyqtSlot()
    def on_actionDelete_triggered(self):
        items=self.scene.selectedItems()
        cnt=len(items)
        for i in range(cnt):
            item=items[i]
            self.scene.removeItem(item)
    
    
    
        
    def __setItemProperties(self,item,desc):
        item.setFlag(QGraphicsItem.ItemIsFocusable)
        item.setFlag(QGraphicsItem.ItemIsMovable)
        item.setFlag(QGraphicsItem.ItemIsSelectable)
        
        self.__front=1+self.__front
        item.setZValue(self.__front)
        item.setPos(-150+random.randint(1,200),-200+random.randint(1,200))
        self.__seqNum+=1
        item.setData(self.__itemID,self.__seqNum)
        item.setData(self.__itemDesc,desc)
        
        self.scene.addItem(item)
        self.scene.clearSelection()
        item.setSelected(True)
        
    def do_mouseMove(self,point):
        self.__labViewCord.setText('view coordinate:%d,%d'%(point.x(),point.y()))
        pt=self.view.mapToScene(point)
        self.__labSceneCord.setText('scene coordinate:%.0f,%.0f'%(pt.x(),pt.y()))
        
    def do_mouseClicked(self,point):
        pt=self.view.mapToScene(point)
        item=self.scene.itemAt(pt,self.view.transform())
        if item==None:
            return
        pm=item.mapFromScene(pt)
        self.__labItemCord.setText('coordinate:%0.f,%0.f'%(pm.x(),pm.y()))
        self.__labItemInfo.setText(str(item.data(self.__itemDesc))+',itemID='+str(item.data(self.__itemID)))
        
    def do_mouseDoubleClick(self,point):
        pt=self.view.mapToScene(point)
        item=self.scene.itemAt(pt,self.view.transform())
        if item==None:
            return
        className=str(type(item))
        if (className.find('QGraphicsRectItem')>=0):
            self.__setBrushColor(item)
        elif className.find('QGraphicsEllipseItem')>=0:
            self.__setBrushColor(item)
        elif className.find(('QGraphicsPolygonItem')>=0):
            self.__setBrushColor(item)
        elif className.find('QGraphicsLineItem')>=0:
            pen=item.pen()
            color=item.pen().color()
            color=QColorDialog.getColor(color,self,'select line color')
            if color.isValid():
                pen.setColor(color)
                item.setPen(pen)
        elif className.find('QGraphicsTextItem')>=0:
            font=item.font()
            font,ok=QFontDialog.getFont(font)
            if ok:
                item.setFont(font)
                
    def __setBrushColor(self,item):
        color=item.brush().color()
        color=QColorDialog.getColor(color,self,'select fill in color')
        if color.isValid():
            item.setBrush(QBrush(color))
            
    def do_keyPress(self,event):
        items=self.scene.selectedItems()
        cnt=len(items)
        if (cnt!=1):
            return
        
        item=items[0]
        key=event.key()
        if key==Qt.Key_Delete:
            self.scene.removeItem(item)
        elif key==Qt.Key_Space:
            item.setRotation(90+item.rotation())
        elif key==Qt.Key_PageUp:
            item.setScale(0.1+item.scale())
        elif key==Qt.Key_PageDown:
            item.setScale(-0.1+item.scale())
        elif key==Qt.Key_Left:
            item.setX(-1+item.x())
        elif key==Qt.Key_Right:
            item.setX(1+item.x())
        elif key==Qt.Key_Up:
            item.setY(-1+item.y())
        elif key==Qt.Key_Down:
            item.setY(1+item.y())
    
        
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    form=QMain()
    form.show()
    sys.exit(app.exec_())