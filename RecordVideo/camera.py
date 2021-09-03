import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

from ui_camera import Ui_video

class Q(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_video()
        self.ui.setupUi(self)
        
        self.__LabCameraState=QLabel('state')
        self.__LabCameraState.setMinimumWidth(150)
        self.ui.statusBar.addWidget(self.__LabCameraState)
        self.__LabImageID=QLabel('picture ID:')
        self.__LabImageID.setMinimumWidth(100)
        self.ui.statusBar.addWidget(self.__LabImageID)
        self.__LabImageFile=QLabel('')
        self.ui.statusBar.addPermanentWidget(self.__LabImageFile)
        self.camera=None
        cameras=QCameraInfo.availableCameras()
        if len(cameras)>0:
            self.__iniCamera()
            self.__iniImageCapture()
            self.camera.start()
            
    def __iniCamera(self):
        camInfo=QCameraInfo.defaultCamera()
        self.ui.cbDevice.addItem(camInfo.description())
        self.ui.cbDevice.setCurrentIndex(0)
        self.camera=QCamera(camInfo)
        self.camera.setViewfinder(self.ui.widgetCamera)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)      
        mode=QCamera.CaptureStillImage
        #picture
        supported=self.camera.isCaptureModeSupported(mode)
        self.ui.cbPicture.setChecked(supported)
        #record
        supported=self.camera.isCaptureModeSupported(QCamera.CaptureVideo)
        self.ui.cbRecord.setChecked(supported)
        #focus
        supported=self.camera.focus().isAvailable()
        self.ui.cbFocus.setChecked(supported)
        #exposure
        supported=self.camera.exposure().isAvailable()
        self.ui.cbExposure.setChecked(supported)
        
        self.camera.stateChanged.connect(self.do_cameraStateChanged)
        
    def do_cameraStateChanged(self,state):
        if state==QCamera.UnloadedState:
            self.__LabCameraState.setText('state:unloaded state')
        elif state==QCamera.LoadedState:
            self.__LabCameraState.setText('state:load state')
        elif state==QCamera.ActiveState:
            self.__LabCameraState.setText('state:active state')
        self.ui.actionOpenCamera.setEnabled(state!=QCamera.ActiveState)
        self.ui.actionCloseCamera.setEnabled(state==QCamera.ActiveState)
        
    def __iniImageCapture(self):
        self.capturer=QCameraImageCapture(self.camera)
        settings=QImageEncoderSettings()
        settings.setCodec('image/jpg')
        settings.setResolution(1280,700)
        settings.setQuality(QMultimedia.HighQuality)
        self.capturer.setEncodingSettings(settings)
        if self.ui.cbSavePicture.isChecked():
            dest=QCameraImageCapture.CaptureToFile
        else:
            dest=QCameraImageCapture.CaptureToBuffer
        self.capturer.setCaptureDestination(dest)
        
        self.capturer.readyForCaptureChanged.connect(self.do_imageReady)
        self.capturer.imageCaptured.connect(self.do_imageCaptured)
        self.capturer.imageSaved.connect(self.do_imageSaved)
        
    @pyqtSlot(bool)
    def on_cbSavePicture_clicked(self,checked):
        if checked:
            dest=QCameraImageCapture.CaptureToFile
        else:
            dest=QCameraImageCapture.CaptureToBuffer
        self.capturer.setCaptureDestination(dest)
        
    @pyqtSlot()
    def on_actionTakePhoto_triggered(self):
        QSound.play(r'C:\Users\max21\Desktop\Python\PythonQt\RecordVideo\shutter.wav')
        self.camera.searchAndLock()
        self.capturer.capture()
        self.camera.unlock()
        
    @pyqtSlot() 
    def on_actionOpenCamera_triggered(self):
        self.camera.start()
    @pyqtSlot()
    def on_actionCloseCamera_triggered(self):
        self.camera.stop()
        
    def do_imageReady(self,ready):
        self.ui.actionTakePhoto.setEnabled(ready)
        
    def do_imageCaptured(self,imageID,preview):
        h=self.ui.labCatch.height()
        w=self.ui.labCatch.width()
        
        scaledImage=preview.scaled(w,h,Qt.KeepAspectRatio,Qt.SmoothTransformation)
        self.ui.labCatch.setPixmap(QPixmap.fromImage(scaledImage))
        self.__LabImageID.setText('picture ID:%d'%imageID)
        self.__labImageFile.setText('save file:'+fileName)
        
    def do_imageSaved(self,imageID,fileName):
        self.__LabImageID.setText('document:%d'%imageID)
        self.__LabImageFile.setText('save as:'+fileName)
        
        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=Q()
    form.show()
    sys.exit(app.exec_())
        
        
        
        