import sys
sys.path.append(r'C:\Users\max21\Desktop\Python\PythonQt') 
from PyQt5.QtWidgets import *
from HW import Ui_Form

class QmyWidget(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.Lab='inhert Qmywidget'
        self.setupUi(self) # self=QWidget
        self.label.setText(self.Lab)

if __name__=='__main__':
    app=QApplication(sys.argv)
    myWidget=QmyWidget()
    myWidget.show()
    myWidget.pushButton.setText('not close!!!')
    sys.exit(app.exec_())






