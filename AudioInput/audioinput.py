import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from ui_audioinput import Ui_AudioInput

class Q(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_AudioInput()
        self.ui.setupUi(self)
        
        self.ui.pbMax.setMaximum(256)
        self.ui.pbMin.setMaximum(256)
        self.ui.pbDifference.setMaximum(256)
        self.ui.SliderVolume.setMaximum(100)
        self.ui.SliderVolume.setValue(100)
        
        self.ui.cbEquip.clear()
        self.__deviceList=QAudioDeviceInfo.availableDevices(QAudio.AudioInput)
        #device list
        for i in range(len(self.__deviceList)):
            device = self.__deviceList[i]
            self.ui.cbEquip.addItem(device.deviceName())
            
        self.audioDevice=None
        self.buffer_size=4000
        self.IODevice=None
        self.recordFile=QFile()
        
        if len(self.__deviceList)>0:
            self.ui.cbEquip.setCurrentIndex(0)
        else:
            self.ui.actionRecord.setEnabled(False)
            self.ui.actionStart.setEnabled(False)
            self.ui.groupBoxDevice.setTitle('none device')
            
    @pyqtSlot(int)
    def on_cbEquip_currentIndexChanged(self,index):
        deviceInfo=self.__deviceList[index]
        #codec
        self.ui.cbCodec.clear()
        codecs=deviceInfo.supportedCodecs()
        for i in codecs:
            self.ui.cbCodec.addItem(i)
        #sample rate    
        self.ui.cbFrequency.clear()
        sampleRates=deviceInfo.supportedSampleRates()
        for i in sampleRates:
            self.ui.cbFrequency.addItem('%d'%i)
        #channel
        self.ui.cbChannels.clear()
        channels=deviceInfo.supportedChannelCounts()
        for i in channels:
            self.ui.cbChannels.addItem('%d'%i)
        #sample type
        self.ui.cbSampleType.clear()
        sampleTypes=deviceInfo.supportedSampleTypes()     
        for i in sampleTypes:
            sampleTypeStr=self.__getSampleTypeStr(i)
            self.ui.cbSampleType.addItem(sampleTypeStr,i)
        #sample size
        self.ui.cbSampleSize.clear()
        sampleSizes=deviceInfo.supportedSampleSizes()
        for i in sampleSizes:
            self.ui.cbSampleSize.addItem('%d'%i)
        #endian
        self.ui.cbEndianess.clear()
        endians=deviceInfo.supportedByteOrders()
        for i in endians:
            self.ui.cbEndianess.addItem(self.__getByteOrderStr(i))
            
    def __getSampleTypeStr(self,sampleType):
        result='Unknown'
        if sampleType==QAudioFormat.SignedInt:
            result='SignedInt'
        elif sampleType==QAudioFormat.UnSignedInt:
            result='UnsignedInt'
        elif sampleType==QAudioFormat.Float:
            result='Float'
        elif sampleType==QAudioFormat.Unknown:
            result='Unknown'
        return result
    
    def __getByteOrderStr(self,endian):
        if endian==QAudioFormat.LittleEndian:
            return 'LittleEndian'
        else:
            return 'BigEndian'
        
    @pyqtSlot()
    def on_actionRecord_triggered(self):
        settings=QAudioFormat()
        settings.setCodec(self.ui.cbCodec.currentText())
        settings.setSampleRate(int(self.ui.cbFrequency.currentText()))
        settings.setChannelCount(int(self.ui.cbChannels.currentText()))
        
        k=self.ui.cbSampleType.currentData()
        settings.setSampleType(k)
        settings.setSampleSize(int(self.ui.cbSampleSize.currentText()))
        if self.ui.cbEndianess.currentText()=='LittleEndian':
            settings.setByteOrder(QAudioFormat.LittleEndian)
        else:
            settings.setByteOrder(QAudioFormat.BigEndian)
            
        index=self.ui.cbEquip.currentIndex()
        deviceInfo=self.__deviceList[index]
        if deviceInfo.isFormatSupported(settings):
            QMessageBox.information(self,'message','success')
        else:
            QMessageBox.information(self,'error','fail')
    
    @pyqtSlot()
    def on_rbtDevice_clicked(self):
        self.ui.groupBoxBuffer.setVisible(True)
        
    @pyqtSlot() 
    def on_rbtQFile_clicked(self):
        self.ui.groupBoxBuffer.setVisible(False)
        
    @pyqtSlot(int) 
    def on_SliderVolume_valueChanged(self,value):
        self.ui.labelVolume.setText('volume(%d%%)'%value)
        
    @pyqtSlot()
    def on_actionStart_triggered(self):
        audioFormat=QAudioFormat()
        audioFormat.setSampleRate(8000)
        audioFormat.setChannelCount(1)
        audioFormat.setSampleSize(8)
        audioFormat.setCodec('audio/pcm')
        audioFormat.setByteOrder(QAudioFormat.LittleEndian)
        audioFormat.setSampleType(QAudioFormat.UnSignedInt)
        
        index=self.ui.cbEquip.currentIndex()
        deviceInfo=self.__deviceList[index]
        if False==deviceInfo.isFormatSupported(audioFormat):
            QMessageBox.critical(self,'error','fail')
            return
        
        self.audioDevice=QAudioInput(deviceInfo,audioFormat)
        self.audioDevice.setBufferSize(self.buffer_size) 
        self.audioDevice.stateChanged.connect(self.do_stateChanged)
        
        if self.ui.rbtDevice.isChecked():
            self.IODevice=self.audioDevice.start()
            self.IODevice.readyRead.connect(self.do_IO_readyRead)
            
        if self.ui.rbtQFile.isChecked():
            self.recordFile.setFileName('test.raw')
            self.recordFile.open(QIODevice.WriteOnly)
            self.audioDevice.start(self.recordFile)
            
    @pyqtSlot()
    def on_actionStop_triggered(self):
        self.audioDevice.stop()
        self.audioDevice.deleteLater()
        if self.ui.rbtQFile.isChecked():
            self.recordFile.close()
                   
    def do_stateChanged(self,state):
        isStoped=(state==QAudio.StoppedState)
        self.ui.groupBox.setEnabled(isStoped)
        self.ui.SliderVolume.setEnabled(isStoped)
        self.ui.actionStart.setEnabled(isStoped)
        self.ui.actionStop.setEnabled(not isStoped)
        self.ui.actionRecord.setEnabled(isStoped)
        
        if state==QAudio.ActiveState:
            self.ui.statusBar.showMessage('state:ActiveState')
        elif state==QAudio.SuspendedState:
            self.ui.statusBar.showMessage('state:SuspendedState')
        elif state==QAudio.StoppedState:
            self.ui.statusBar.showMessage('state:StoppedState')
        elif state==QAudio.IdleState:
            self.ui.statusBar.showMessage('state:IdleState')
        elif state==QAudio.InterruptedState:
            self.ui.statusBar.showMessage('state:InterruptedState')
            
    def do_IO_readyRead(self):
        self.ui.labelBufferSize.setText('bufferSize:%d'%self.audioDevice.bufferSize())
        byteCount=self.audioDevice.bytesReady()
        self.ui.labelBytesReady.setText('bytesReady:%d'%byteCount)
        if byteCount>self.buffer_size:
            byteCount=self.buffer_size
        buffer=self.IODevice.read(byteCount)
        maxSize=len(buffer)
        self.ui.labelIODevice.setText('IODevice:%d'%maxSize)
        
        maxV=0
        minV=255
        for k in range(maxSize):
            v=buffer[k]
            if v>maxV:
                maxV=v
            if v<minV:
                minV=v
                
        self.ui.pbMax.setValue(maxV)
        self.ui.pbMin.setValue(minV)
        self.ui.pbDifference.setValue(maxV-minV)
            
                   
        
        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=Q()
    form.show()
    sys.exit(app.exec_())
    