import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from ui_audiorecorder import Ui_AudioRecorder

class Q(QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.ui=Ui_AudioRecorder()
        self.ui.setupUi(self)
        self.recorder=QAudioRecorder(self)
        self.recorder.stateChanged.connect(self.do_stateChanged)
        self.recorder.durationChanged.connect(self.do_durationChanged)
        self.probe=QAudioProbe(self)
        self.probe.setSource(self.recorder)
        self.probe.audioBufferProbed.connect(self.do_processBuffer)
        
        #initial condidtion
        self.ui.actionPause.setEnabled(False)
        self.ui.actionStop.setEnabled(False)
        
        if self.recorder.defaultAudioInput()=="":
            return
        #equipment
        for d in self.recorder.audioInputs():
            self.ui.comboBoxEquip.addItem(d)
        #encoding
        for i in self.recorder.supportedAudioCodecs():
            self.ui.comboBoxEncoding.addItem(i)
        #sampling rate
        sampleList,isContinuous=self.recorder.supportedAudioSampleRates()
        for i in range(len(sampleList)):
            self.ui.comboBoxSamplingRate.addItem('%d'%sampleList[i])
    #channel
        channel=['1','2','4']
        for i in channel:
            self.ui.comboBoxChannels.addItem(i)
    #quality
        self.ui.horizontalSlider.setRange(0,QMultimedia.VeryHighQuality)
        self.ui.horizontalSlider.setValue(QMultimedia.NormalQuality)
    #bitrates
        bitrates=['32000','64000','96000','128000']
        for j in bitrates:
            self.ui.comboBoxBiteRate.addItem(j)
        
    def do_stateChanged(self,state):
        isRecording=(state==QMediaRecorder.RecordingState)
        self.ui.actionRecord.setEnabled(not isRecording)
        self.ui.actionPause.setEnabled(isRecording)
        self.ui.actionStop.setEnabled(isRecording)
        isStoped=(state==QMediaRecorder.StoppedState)
        self.ui.btnExport.setEnabled(isStoped)
        self.ui.exportLineEdit.setEnabled(isStoped)
        
    def do_durationChanged(self,duration):
        self.ui.labelTime.setText('record time:%d'%(duration/1000))
        
        
    @pyqtSlot()
    def on_actionRecord_triggered(self):
        success=True
        if self.recorder.state()==QMediaRecorder.StoppedState:
            success=self.__setRecordParams()
        if success:
            self.recorder.record()
            self.ui.actionPause.setEnabled(True)
            self.ui.actionStop.setEnabled(True)
            
    @pyqtSlot()
    def on_actionPause_triggered(self):
        self.recorder.pause()
    
    @pyqtSlot()
    def on_actionStop_triggered(self):
        self.recorder.stop()
        
    #set input parameter
    def __setRecordParams(self):
        selectedFile=self.ui.exportLineEdit.text().strip()
        if selectedFile=='':
            QMessageBox.critical(self,'wrong','please set your file')
            return False
        if os.path.exists(selectedFile):
            os.remove(selectedFile)
        #set output file
        recordFile=QUrl.fromLocalFile(selectedFile)
        self.recorder.setOutputLocation(recordFile)
        #set equipment
        recordDevice=self.ui.comboBoxEquip.currentText()
        self.recorder.setAudioInput(recordDevice)
        
        #encoding setting
        settings=QAudioEncoderSettings()
        settings.setCodec(self.ui.comboBoxEncoding.currentText())
        #sampling rate
        sampleRate=int(self.ui.comboBoxSamplingRate.currentText())
        settings.setSampleRate(sampleRate)
        #bit rate
        bitRate=int(self.ui.comboBoxBiteRate.currentText())
        settings.setBitRate(bitRate)
        #channel count
        channelCount=int(self.ui.comboBoxChannels.currentText())
        settings.setChannelCount(channelCount)
        #quality
        quality=QMultimedia.EncodingQuality(self.ui.horizontalSlider.value())
        settings.setChannelCount(channelCount)
        
        if self.ui.radioButtonBitRate.isChecked():
            settings.setEncodingMode(QMultimedia.ConstantQualityEncoding)
        else:
            settings.setEncodingMode(QMultimedia.ConstantBitRateEncoding)
            
        self.recorder.setAudioSettings(settings)
        return True
    
    
    def do_processBuffer(self,buffer):
        audioFormat=buffer.format()
        self.ui.spinBoxChannelCount.setValue(audioFormat.channelCount())
        self.ui.spinBoxSampleSize.setValue(audioFormat.sampleSize())
        self.ui.spinBoxSampleRate.setValue(audioFormat.sampleRate())
        self.ui.spinBoxBPF.setValue(audioFormat.bytesPerFrame())
        if audioFormat.byteOrder()==QAudioFormat.LittleEndian:
            self.ui.lineEditByteOrder.setText('LittleEndian')
        else:
            self.ui.lineEditByteOrder.setText('BigEndian')
        self.ui.lineEditCodec.setText(audioFormat.codec())
        
        if audioFormat.sampleType()==QAudioFormat.SignedInt:
            self.ui.lineEditSampleType.setText('SignedInt')
        elif audioFormat.sampleType()==QAudioFormat.UnSignedInt:
            self.ui.lineEditSampleType.setText('UnSignedInt')
        elif audioFormat.sampleType()==QAudioFormat.Float:
            self.ui.lineEditSampleType.setText('Float')
        else:
            self.ui.lineEditSampleType.setText('Unknown')
        
        self.ui.spinBoxBytes.setValue(buffer.byteCount())
        
        self.ui.spinBoxFPS.setValue(buffer.frameCount())
        self.ui.spinBoxSample.setValue(buffer.sampleCount())
        self.ui.spinBoxDuration.setValue(buffer.duration()/1000)    
    
        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=Q()
    form.show()
    sys.exit(app.exec_())