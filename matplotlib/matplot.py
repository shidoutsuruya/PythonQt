import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import *


class Q(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle('hello world')
        plt.rcParams['font.sans-serif']=['KaiTi','SimHei']
        plt.rcParams['font.size']=12
        plt.rcParams['axes.unicode_minus']=False
        self.__iniFigure()
        self.__drawFigure()
    
    def __iniFigure(self):
        self.__fig=plt.figure(figsize=(8,5))
        self.__fig.suptitle('plot in GUI')
        figCanvas=FigureCanvas(self.__fig)
        
        naviToolbar=NavigationToolbar2QT(figCanvas,self)
        naviToolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(naviToolbar)
        self.setCentralWidget(figCanvas)
        
    def __drawFigure(self):
        t=np.linspace(0,10,40)
        y1=np.sin(t)
        y2=np.tan(2*t)
        
        ax1=self.__fig.add_subplot(1,2,1)
        ax1.plot(t,y1,'r-o',label='sin',linewidth=1,markersize=5)
        ax1.legend()
        
        ax2=self.__fig.add_subplot(1,2,2)
        ax2.scatter(t,y2)
                
        
        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=Q()
    form.show()
    sys.exit(app.exec_())