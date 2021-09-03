import sys
sys.path.append(r'C:\Users\max21\Desktop\Python\PythonQt') 
from PyQt5 import QtWidgets
import HW

app=QtWidgets.QApplication(sys.argv)
baseWidget=QtWidgets.QWidget()

ui=HW.Ui_Form()
ui.setupUi(baseWidget)
baseWidget.show()
ui.label.setText('program')
sys.exit(app.exec_())






