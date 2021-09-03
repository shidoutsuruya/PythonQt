import sys
from PyQt5 import QtWidgets,QtCore,QtGui
app=QtWidgets.QApplication(sys.argv)#create app
widgetHello=QtWidgets.QWidget() #create widget
widgetHello.resize(300,150)   #set height and width
widgetHello.setWindowTitle('Demo2_1')  #set title text

LabHello=QtWidgets.QLabel(widgetHello)# set log
LabHello.setText("Hello world,PyQt5")
font=QtGui.QFont()
font.setPointSize(12)
font.setBold(True)
LabHello.setFont(font)
size=LabHello.sizeHint()
LabHello.setGeometry(70,60,size.width(),size.height())
widgetHello.show()
sys.exit(app.exec_())



