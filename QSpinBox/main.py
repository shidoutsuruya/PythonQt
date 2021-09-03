import sys
sys.path.append(r'C:\Users\max21\Desktop\Python\PythonQt\QSpinBox')
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtCore import pyqtSlot
from ui_widget import Ui_Widget
class QmyWidget(QMainWindow):
    def __init__(self, parent=None):
         super().__init__(parent=parent)
         self.ui=Ui_Widget()
         self.ui.setupUi(self)
         self.ui.spinBox.setSuffix('kg')
         self.ui.doubleSpinBox.setPrefix('$')
         self.ui.doubleSpinBox_2.setPrefix('$')
         self.ui.spinBox.setMaximum(999999999)
         self.ui.doubleSpinBox.setMaximum(99999999999)
         self.ui.doubleSpinBox_2.setMaximum(9999999999999)

    def on_pushButton_clicked(self):
        try:
            num=int(self.ui.lineEdit.text())
        except:
            pass
        try:
            price=float(self.ui.lineEdit_2.text())
        except:
            pass
        try:
            total=num*price
            self.ui.lineEdit_3.setText("%.2f"%total)
        except:
            self.ui.lineEdit_3.setText('error')
    @pyqtSlot(int)
    def on_spinBox_valueChanged(self,count):
        price=self.ui.doubleSpinBox.value()
        
        self.ui.doubleSpinBox_2.setValue(count*price)
    @pyqtSlot(float)
    def on_doubleSpinBox_valueChanged(self,price):
        count=self.ui.spinBox.value()
        self.ui.doubleSpinBox_2.setValue(count*price)

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=QmyWidget()
    form.show()
    sys.exit(app.exec_())


