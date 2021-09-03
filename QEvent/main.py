import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Event import Ui_Event

class Q(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Event()
        self.ui.setupUi(self)

    def paintEvent(self,event):
        painter=QPainter(self)
        pic=QPixmap(r'C:\Users\max21\Desktop\Python\PythonQt\QEvent\bg.jpg')
        painter.drawPixmap(0,0,self.width(),self.height(),pic)
        super().paintEvent(event)

    def resizeEvent(self,event):
        W=self.width()
        H=self.height()
        Wbtn=self.ui.pushButton_1.width()
        Hbtn=self.ui.pushButton_1.height()
        self.ui.pushButton_1.setGeometry((W-Wbtn)/2,(H-Hbtn)/2,Wbtn,Hbtn)

    def closeEvent(self,event):
        digTitle='close'
        strInfo='Are you sure?'
        defaultBtn=QMessageBox.NoButton
        result=QMessageBox.question(self,digTitle,strInfo,QMessageBox.Yes|QMessageBox.No,defaultBtn)
        if result==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def mousePressEvent(self,event):
        pt=event.pos() #mouse point
        if (event.button()==Qt.LeftButton):
            self.ui.label.setText('(x,y)=(%d,%d)'%(pt.x(),pt.y()))
            rect=self.ui.label.geometry()
            self.ui.label.setGeometry(pt.x(),pt.y(),rect.width(),rect.height())
        super().mousePressEvent(event)
    
    def keyPressEvent(self,event):
        rect=self.ui.pushButton_2.geometry()
        if event.key() in set([Qt.Key_A,Qt.Key_Left]):
            self.ui.pushButton_2.setGeometry(rect.left()-20,rect.top(),rect.width(),rect.height())
        elif event.key() in set([Qt.Key_D,Qt.Key_Right]):
            self.ui.pushButton_2.setGeometry(rect.left()+20,rect.top(),rect.width(),rect.height())
        elif event.key() in set([Qt.Key_W,Qt.Key_Up]):
            self.ui.pushButton_2.setGeometry(rect.left(),rect.top()-20,rect.width(),rect.height())
        elif event.key() in set([Qt.Key_S,Qt.Key_Down]):
            self.ui.pushButton_2.setGeometry(rect.left(),rect.top()+20,rect.width(),rect.height())
        





if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainform=Q()
    mainform.show()
    sys.exit(app.exec_())