import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

from ui_mediaplayer import Ui_MediaPlayer
class Q(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_MediaPlayer()
        self.ui.setupUi(self)
        
        self.player=QMediaPlayer(self)
        self.player.setNotifyInterval(1000)
        self.player.setVideoOutput(self.ui.widget)
        self.ui.widget.installEventFilter(self)
        self.__duration=''
        self.__curPos=''
        self.player.stateChanged.connect(self.do_stateChanged)
        self.player.positionChanged.connect(self.do_positionChanged)
        self.player.durationChanged.connect(self.do_durationChanged)
        self.ui.SliderVolume.setValue(50)
        
        
    def eventFilter(self,watched,event):
        if watched!=self.ui.widget:
            return super().eventFilter(watched,event)
        #mouse left button
        if event.type()==QEvent.MouseButtonPress:
            if event.button()==Qt.LeftButton:
                if self.player.state()==QMediaPlayer.PlayingState:
                    self.player.pause()
                else:
                    self.player.play()
                    
        if event.type()==QEvent.KeyPress:
            if event.key()==Qt.Key_Escape:
                if self.ui.widget.isFullScreen():
                    self.ui.widget.setFullScreen(False)
        return super().eventFilter(watched,event)
    
    @pyqtSlot()
    def on_pbtOpen_clicked(self):
        curpath=QDir.currentPath()
        title='select video'
        filt='video(*.wmv *.avi *.mp4 *.mkv);;music(*.mp3 *.wma);;all(*.*)'
        fileName,flt=QFileDialog.getOpenFileName(self,title,curpath,filt)
        if (fileName==""):
            return
        
        fileInfo=QFileInfo(fileName)
        baseName=fileInfo.fileName()
        self.ui.labelFile.setText(baseName)
        
        curpath=fileInfo.absolutePath()
        QDir.setCurrent(curpath)
        media=QMediaContent(QUrl.fromLocalFile(fileName))
        self.player.setMedia(media)
        self.player.play()
        
        
    @pyqtSlot() 
    def on_pbtPlay_clicked(self):
        self.player.play()
    @pyqtSlot() 
    def on_pbtPause_clicked(self):
        self.player.pause()
    @pyqtSlot()
    def on_pbtStop_clicked(self):
        self.player.stop()
    @pyqtSlot()
    def on_pbtVolume_clicked(self):
        mute=self.player.isMuted()
        self.player.setMuted(not mute)
        if mute:
            self.ui.pbtVolume.setIcon(QIcon(':/images/volumn.bmp'))
        else:
            self.ui.pbtVolume.setIcon(QIcon(':/images/mute.bmp'))
        
    @pyqtSlot(int)
    def on_SliderVolume_valueChanged(self,value):
        self.player.setVolume(value)
    @pyqtSlot(int)
    def on_SliderProgress_valueChanged(self,value):
        self.player.setPosition(value) 
        
    def do_stateChanged(self,state):
        isPlaying=(state==QMediaPlayer.PlayingState)
        self.ui.pbtPlay.setEnabled(not isPlaying)
        self.ui.pbtPause.setEnabled(isPlaying)
        self.ui.pbtStop.setEnabled(isPlaying)
        
    def do_durationChanged(self,duration):
        self.ui.SliderProgress.setMaximum(duration)
        secs=duration/1000
        mins=secs/60
        secs=secs%60
        self.__duration='%d:%d'%(mins,secs)
        self.ui.labelTime.setText(self.__curPos+'/'+self.__duration)
        
    def do_positionChanged(self,position):
        if self.ui.SliderProgress.isSliderDown():
            return 
        self.ui.SliderProgress.setSliderPosition(position)
        secs=position/1000
        mins=secs/60
        secs=secs%60
        self.__curPos='%d:%d'%(mins,secs)
        self.ui.labelTime.setText(self.__curPos+'/'+self.__duration)
        
        

                    
        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=Q()
    form.show()
    sys.exit(app.exec_())
        