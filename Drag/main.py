import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Drag import Ui_Drag

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Drag()
        self.ui.setupUi(self)

        self.setAcceptDrops(True)
        self.ui.plainTextEdit.setAcceptDrops(False)
        self.ui.label.setAcceptDrops(False)
        self.ui.label.setScaledContents(True)

    def dragEnterEvent(self,event):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.appendPlainText('drag event mimeData().formats()')
        for i in event.mimeData().formats():
            self.ui.plainTextEdit.appendPlainText(i)
        self.ui.plainTextEdit.appendPlainText('event.mimeData().urls()')
        for url in event.mimeData().urls():  
            self.ui.plainTextEdit.appendPlainText(url.path())
        if (event.mimeData().hasUrls()):
            filename=event.mimeData().urls()[0].fileName() #only filename
            basename,ext=os.path.splitext(filename)
            ext=ext.upper()
            if (ext=='.jpg'or'.JPG'):
                event.acceptProposedAction()
            else:
                event.ignore()
        else:
            event.ignore()
    
    def dropEvent(self,event):
        filename=event.mimeData().urls()[0].path()
        cnt=len(filename)
        realname=filename[1:cnt]
        pixmap=QPixmap(realname)
        self.ui.label.setPixmap(pixmap)
        event.accept()



    
if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=QmyWidget()
    form.show()
    sys.exit(app.exec_())