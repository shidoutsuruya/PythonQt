import sys
sys.path.append(r"C:\Users\max21\Desktop\Python\PythonQt\p41_human_age")
from ui_Qt import Ui_qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Signal import Human

class QMywidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui=Ui_qt()
        self.ui.setupUi(self)

        self.boy=Human('boy',20)
        self.boy.nameChange.connect(self.do_nameChanged)
        self.boy.ageChange[int].connect(self.do_ageChanged_int)
        self.boy.ageChange[str].connect(self.do_ageChanged_str)
#relative
    def on_SliderSetAge_valueChanged(self,value):
         self.boy.setAge(value)

    def on_btnSetName_clicked(self):
        hisName=self.ui.lineEdit_3.text()
        self.boy.setName(hisName)
#self_defined
    def do_nameChanged(self,name):
        self.ui.lineEdit_4.setText('Hello,'+name) 
    @pyqtSlot(int)
    def do_ageChanged_int(self,age):
        self.ui.lineEdit.setText(str(age))
    @pyqtSlot(str)
    def do_ageChanged_str(self,info):
        self.ui.lineEdit_2.setText(info)


if __name__=='__main__':
    app=QApplication(sys.argv)
    icon=QIcon(r'C:\Users\max21\Desktop\Python\PythonQt\p41_human_age\Qt\images\icon.jpg')
    app.setWindowIcon(icon)
    form=QMywidget()
    form.show()
    sys.exit(app.exec_())

