import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from ui_multimedia import Ui_multimedia

class Q(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_multimedia()
        self.ui.setupUi(self)
        
        self.player=QMediaPlayer(self)
        self.playlist=QMediaPlaylist(self)
        self.player.setPlaylist(self.playlist)
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.__duration=''
        self.__curPos=''

        self.player.stateChanged.connect(self.do_stateChanged)
        self.player.positionChanged.connect(self.do_positionChanged)
        self.player.durationChanged.connect(self.do_durationChanged)
        self.playlist.currentIndexChanged.connect(self.do_currentChanged)
  
        self.ui.btnPause.setEnabled(False)
        self.ui.btnPlay.setEnabled(False)
        self.ui.btnStop.setEnabled(False)
        self.ui.btnNext.setEnabled(False)
        self.ui.btnBack.setEnabled(False)
        self.ui.btnDelete.setEnabled(False)
        self.ui.btnClear.setEnabled(False)
    
    def do_stateChanged(self,state):
        self.ui.btnPlay.setEnabled(state!=QMediaPlayer.PlayingState)
        self.ui.btnPause.setEnabled(state==QMediaPlayer.PlayingState)
        self.ui.btnStop.setEnabled(state==QMediaPlayer.PlayingState)
        
    def do_positionChanged(self,position):
        if self.ui.SliderSong.isSliderDown():
            return
        self.ui.SliderSong.setSliderPosition(position)
        secs=position/1000
        mins=secs/60
        secs=secs%60
        self.__curPos='%d:%d'%(mins,secs)
        self.ui.labelTime.setText(self.__curPos+'/'+self.__duration)
    
    def do_durationChanged(self,duration):
        self.ui.SliderSong.setMaximum(duration)
        secs=duration/1000
        mins=secs/60
        secs=secs%60
        self.__duration='%d:%d'%(mins,secs)
        self.ui.labelTime.setText(self.__curPos+'/'+self.__duration)
        
    def do_currentChanged(self,position):
        self.ui.listWidget.setCurrentRow(position)
        item=self.ui.listWidget.currentItem()
        if item!=None:
            self.ui.labelName.setText(item.text())
            
    #add file
    @pyqtSlot()
    def on_btnAdd_clicked(self):
        curPath=QDir.currentPath()
        dlgTitle='select music'
        filt='media file(*.mp3 *.wav *.wma);;all(*.*)'
        fileList,flt=QFileDialog.getOpenFileNames(self,dlgTitle,curPath,filt)
        count=len(fileList)
        if count<1:
            return 
        self.ui.btnPause.setEnabled(True)
        self.ui.btnPlay.setEnabled(True)
        self.ui.btnStop.setEnabled(True)
        self.ui.btnNext.setEnabled(True)
        self.ui.btnBack.setEnabled(True)
        self.ui.btnDelete.setEnabled(True)
        self.ui.btnClear.setEnabled(True)
        filename=fileList[0]
        fileInfo=QFileInfo(filename)
        QDir.setCurrent(fileInfo.absolutePath())
        for i in range(count):
            filename=fileList[i]
            fileInfo.setFile(filename)
            song=QMediaContent(QUrl.fromLocalFile(filename))
            self.playlist.addMedia(song)
            basename=fileInfo.baseName()
            self.ui.listWidget.addItem(basename)
        if self.player.state()!=QMediaPlayer.PlayingState:
            self.playlist.setCurrentIndex(0)
            self.player.play()
            
    @pyqtSlot()
    def on_btnDelete_clicked(self):
        pos=self.ui.listWidget.currentRow()
        item=self.ui.listWidget.takeItem(pos)
        if self.playlist.currentIndex()==pos:
            nextPos=0
            if pos>=1:
                nextPos=pos-1
            self.playlist.removeMedia(pos)
            if self.ui.listWidget.count()>0:
                self.playlist.setCurrentIndex(nextPos)
                self.do_currentChanged(nextPos)
            else:
                self.player.stop()
                self.ui.labelName.setText('None')
                self.ui.btnPause.setEnabled(False)
                self.ui.btnPlay.setEnabled(False)
                self.ui.btnStop.setEnabled(False)
                self.ui.btnNext.setEnabled(False)
                self.ui.btnBack.setEnabled(False)
                self.ui.btnDelete.setEnabled(False)
                self.ui.btnClear.setEnabled(False)                
        else:
            self.playlist.removeMedia(pos)
            
    @pyqtSlot()
    def on_btnClear_clicked(self):
        self.playlist.clear()
        self.ui.listWidget.clear()
        self.player.stop()
        self.ui.btnPause.setEnabled(False)
        self.ui.btnPlay.setEnabled(False)
        self.ui.btnStop.setEnabled(False)
        self.ui.btnNext.setEnabled(False)
        self.ui.btnBack.setEnabled(False)
        self.ui.btnDelete.setEnabled(False)
        self.ui.btnClear.setEnabled(False)
        self.ui.labelName.setText('None')
        
    @pyqtSlot()
    def on_btnBack_clicked(self):
        self.playlist.previous()
    
    @pyqtSlot()
    def on_btnNext_clicked(self):
        self.playlist.next()
    #double click
    def on_listWidget_doubleClicked(self,index):
        rowNo=index.row()
        self.playlist.setCurrentIndex(rowNo)
        self.player.play()
        
    @pyqtSlot()
    def on_btnPlay_clicked(self):
        if self.playlist.currentIndex()<0:
            self.playlist.setCurrentIndex(0)
        self.player.play()
        
    @pyqtSlot()
    def on_btnPause_clicked(self):
        self.player.pause()
        
    @pyqtSlot()
    def on_btnStop_clicked(self):
        self.player.stop()
        
    @pyqtSlot()
    def on_btnVolume_clicked(self):
        mute=self.player.isMuted()
        self.player.setMuted(not mute)
        if mute:
            self.ui.btnVolume.setIcon(QIcon(':/images/volumn.bmp'))     
        else:
            self.ui.btnVolume.setIcon(QIcon(':/images/mute.bmp'))
            self.ui.SliderVolume.setValue(0)
            
    @pyqtSlot(int)
    def on_SliderVolume_valueChanged(self,value):
        self.player.setVolume(value)
    @pyqtSlot(int)
    def on_SliderSong_valueChanged(self,value):
        self.player.setPosition(value)
    
            
        
        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=Q()
    form.show()
    sys.exit(app.exec_())