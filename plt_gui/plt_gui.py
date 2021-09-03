import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import *
from ui_plt import Ui_plt_gui

class Q(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui=Ui_plt_gui()
        self.ui.setupUi(self)
        
        self.setWindowTitle('hello world')
        plt.style.use('classic')
        plt.rcParams['font.sans-serif']=['Time New Roman']
        plt.rcParams['font.size']=12
        plt.rcParams['axes.unicode_minus']=False
        
        self.__fig=None
        self.__curAxes=None
        self.__curLine=None
        self.__createFigure()
        self.__drawFig2X1()
        
        axesList=self.__fig.axes
        for i in axesList:
            self.__comboAxes.addItem(i.get_label())
            
        legend = ['best','upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center']
        self.ui.cbLegendPosition.addItems(legend)
        styleList=plt.style.available
        self.ui.cbFigureStyle.addItems(styleList)
        
    def __createFigure(self):
        self.__fig=plt.figure()
        figCanvas=FigureCanvas(self.__fig)
        naviToolbar=NavigationToolbar2QT(figCanvas,self)
        actList=naviToolbar.actions()
        count=len(actList)
        lastAction=actList[count-1]
        
        labCurAxes=QLabel('subplot')
        naviToolbar.insertWidget(lastAction,labCurAxes)
        self.__comboAxes=QComboBox(self)
        self.__comboAxes.setToolTip('select subplot')
        self.__comboAxes.currentIndexChanged.connect(self.do_currentAxesChanged)
        naviToolbar.insertWidget(lastAction,self.__comboAxes)
        naviToolbar.insertAction(lastAction,self.ui.actionExit)
        self.addToolBar(naviToolbar)
        
        splitter=QSplitter(self)
        splitter.setOrientation(Qt.Horizontal)
        splitter.addWidget(self.ui.toolBox)
        splitter.addWidget(figCanvas)
        self.setCentralWidget(splitter)
        
    def __drawFig2X1(self):
        ax1=self.__fig.add_subplot(221)
        x=np.linspace(0,10,100)
        y=np.tan(x)+2*np.cos(x)
        ax1.plot(x,y)
        ax1.legend('xxx')
        
        ax2=self.__fig.add_subplot(222,label='222')
        ax2.plot(x,np.sin(y))
        ax2.legend('dsds')
        
        ax3=self.__fig.add_subplot(223,label='223')
        ax3.plot(x,y+1,'r')
        ax3.legend('ds')
        
        ax4=self.__fig.add_subplot(224,label='224')
        ax4.plot(x,np.sin(y)/np.arctan(y),'o')
        ax4.legend('sds')
        
        
    def __setFig_suptitle(self,refreshDraw=True):
        #set text
        textStr=self.ui.lineEditTitle.text()
        objText=self.__fig.suptitle(textStr)
        objText.set_fontsize(self.ui.spinBoxFontSize.value())
        if self.ui.cbBold.isChecked():
            objText.set_fontweight('bold')
        else:
            objText.set_fontweight('normal')
            
        if self.ui.cbItalic.isChecked():
            objText.set_fontstyle('italic')
        else:
            objText.set_fontstyle('normal')
            
        if refreshDraw:
            self.__fig.canvas.draw()
        return objText
        
    @pyqtSlot()
    def on_btnTitle_clicked(self):
        self.__setFig_suptitle()
    @pyqtSlot(int) 
    def on_spinBoxFontSize_valueChanged(self,arg1):
        self.__setFig_suptitle()
    @pyqtSlot(bool)
    def on_cbBold_clicked(self):
        self.__setFig_suptitle()
    @pyqtSlot(bool)
    def on_cbItalic_clicked(self):
        self.__setFig_suptitle()
        
    @pyqtSlot()
    def on_btnFontColor_clicked(self):
        color=QColorDialog.getColor()
        if color.isValid():
            r,g,b,a=color.getRgbF()
            objText=self.__setFig_suptitle(False)
            objText.set_color((r,g,b,a))
            self.__fig.canvas.draw()
    @pyqtSlot()
    def on_btnBackgroundColor_clicked(self):
        color=QColorDialog.getColor()
        if color.isValid():
            r,g,b,a=color.getRgbF()
            objText = self.__setFig_suptitle(False)
            objText.set_backgroundcolor((r,g,b,a))
            self.__fig.canvas.draw()
            
    @pyqtSlot(bool)
    def on_cbShow_clicked(self,checked):
        self.__fig.set_frameon(checked)
        self.ui.btnSetColor.setEnabled(checked)
        self.__fig.canvas.draw()
    @pyqtSlot()
    def on_btnSetColor_clicked(self):
        color=QColorDialog.getColor()
        if color.isValid():
            r,g,b,a=color.getRgbF()
            self.__fig.set_facecolor((r,g,b))
            self.__fig.canvas.draw()
    @pyqtSlot(str)
    def on_cbFigureStyle_currentIndexChanged(self,arg1):
        plt.style.use(arg1)
        plt.rcParams['font.sans-serif']=['Time New Roman']
        plt.rcParams['axes.unicode_minus']=False
        plt.rcParams['font.size']=12
        self.__fig.clear()
        self.__drawFig2X1()
        self.__fig.canvas.draw()
#tight layout
    @pyqtSlot()
    def on_btnTightLayout_clicked(self):
        self.__fig.tight_layout()
        self.__fig.canvas.draw()
#left right bottom top wspace hspace
    @pyqtSlot(float)
    def on_dsbLeft_valueChanged(self,value):
            self.__fig.subplots_adjust(left=value)
            self.__fig.canvas.draw()
    @pyqtSlot(float)
    def on_dsbRight_valueChanged(self,value):
            self.__fig.subplots_adjust(right=value)
            self.__fig.canvas.draw()
    @pyqtSlot(float)
    def on_dsbBottom_valueChanged(self,value):
        self.__fig.subplots_adjust(bottom=value)
        self.__fig.canvas.draw()
    @pyqtSlot(float)
    def on_dsbTop_valueChanged(self,value):
        self.__fig.subplots_adjust(top=value)
        self.__fig.canvas.draw()
    @pyqtSlot(float)
    def on_dsbWspace_valueChanged(self,value):
        self.__fig.subplots_adjust(wspace=value)
        self.__fig.canvas.draw()
    @pyqtSlot(float)
    def on_dsbHspace_valueChanged(self,value):
        self.__fig.subplots_adjust(hspace=value)
        self.__fig.canvas.draw()
        
#axes operation
    @pyqtSlot(int)
    def do_currentAxesChanged(self,index):
        axesList=self.__fig.axes
        self.__curAxes=self.__fig.axes[index]
        self.ui.cbCurrentLine.clear()
        lines=self.__curAxes.get_lines()
        for i in lines:
            self.ui.cbCurrentLine.addItem(i.get_label())
        
        #visible subplot
        axesLabel=self.__curAxes.get_label()
        self.ui.cbVisible.setText('visible')
        axesVisible=self.__curAxes.get_visible()
        self.ui.cbVisible.setChecked(axesVisible)
        self.on_cbVisible_clicked(axesVisible)
        #appearance
        isFrameOn=self.__curAxes.get_frame_on()
        self.ui.cbShow_2.setChecked(isFrameOn)
        #marker
        legend=self.__curAxes.get_legend()
        self.ui.gbLegend.setChecked(legend.get_visible())
        self.ui.cbDraggable.setChecked(legend.get_draggable())
        #toolbox
        xmin,xmax=self.__curAxes.get_xbound()
        self.ui.dsbXmin.setValue(xmin)
        self.ui.dsbXmax.setValue(xmax)
        
        textStr=self.__curAxes.get_xlabel()
        self.ui.lineEditXTitle.setText(textStr)
        textStr=self.__curAxes.get_xscale()
        self.ui.cbCoordinate_2.setCurrentText(textStr)
        #toolbox
        ymin,ymax=self.__curAxes.get_ybound()
        self.ui.dsbYmin.setValue(ymin)
        self.ui.dsbYmax.setValue(ymax)
        
        textStr = self.__curAxes.get_ylabel()
        self.ui.lineEditXTitle_2.setText(textStr)
        textStr = self.__curAxes.get_yscale()
        self.ui.cbCoordinate_3.setCurrentText(textStr)
   #groupbox visible     
    @pyqtSlot(bool)
    def on_cbVisible_clicked(self,checked):
        self.__curAxes.set_visible(checked)
        self.__fig.canvas.draw()
        self.ui.gbTitle.setEnabled(checked)
        self.ui.gbAppearance.setEnabled(checked)
        self.ui.gbLegend.setEnabled(checked)
        self.ui.pageSeries.setEnabled(checked)
        
    def __setAxesTitle(self):
        textStr=self.ui.lineEditPlotTitle.text()
        objText=self.__curAxes.set_title(textStr)
        objText.set_fontsize(self.ui.spinBoxfontSize_2.value())
        if self.ui.cbBold_2.isChecked():
            objText.set_fontweight('bold')
        else:
            objText.set_fontweight('normal')
        
        if self.ui.cbItalic_2.isChecked():
            objText.set_fontstyle('italic')
        else:
            objText.set_fontstyle('normal')
        self.__fig.canvas.draw()
        return objText
        
    @pyqtSlot()
    def on_btnSetTitle_clicked(self):
        self.__setAxesTitle()
    @pyqtSlot(bool)
    def on_cbBold_2_clicked(self):
        self.__setAxesTitle()
    @pyqtSlot(bool)
    def on_cbItalic_2_clicked(self):
        self.__setAxesTitle()
        
#appearance
    @pyqtSlot(bool)
    def on_cbShow_2_clicked(self,checked):
        self.__curAxes.set_frame_on(checked)
        self.ui.btnSetColor_2.setEnabled(checked)
        self.__fig.canvas.draw()
    
    @pyqtSlot(bool)
    def on_cbXgrid_clicked(self,checked):
        self.__curAxes.grid(b=checked,which='both',axis='x')
        self.__fig.canvas.draw()
        
           
        
    
    
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
            
        
        
        
        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=Q()
    form.show()
    sys.exit(app.exec_())