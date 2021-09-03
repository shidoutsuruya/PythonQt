import sys
sys.path.append(r'C:\Users\max21\Desktop\Python\PythonQt') 
from PyQt5.QtWidgets import *
from HW import Ui_Form

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.__ui=Ui_Form() #create UI
        self.__ui.setupUi(self) #construct UI

        self.Lab='single inheritance'
        self.__ui.label.setText(self.Lab)
    def setBtnText(self,aText):
        self.__ui.pushButton.setText(aText)

if __name__=='__main__':
    app=QApplication(sys.argv)
    myWidget=QmyWidget()
    myWidget.show()
    myWidget.setBtnText('setting!')
    sys.exit(app.exec_())






