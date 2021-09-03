import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTime,QTimer
from QTimer import Ui_Timer

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Timer()
        self.ui.setupUi(self)
        self.timer=QTimer()
        self.timer.stop()
        self.timer.setInterval(1000)  
        self.timer.timeout.connect(self.do_timer_timeout)
        self.counter=QTime()
    def on_btnStart_clicked(self):
        self.timer.start()
        self.counter.start()
        self.ui.btnStart.setEnabled(False)
        self.ui.btnStop.setEnabled(True)
        self.ui.btnSetPeriod.setEnabled(False)
    def on_btnSetPeriod_clicked(self):
        self.timer.setInterval(self.ui.spinBox.value())
       
    def on_btnStop_clicked(self):
        self.timer.stop()
        tmMS=self.counter.elapsed()
        ms=tmMS%1000
        sec=tmMS/1000
        timeStr='time fleeting:%ds,%dms'%(sec,ms)
        self.ui.label.setText(timeStr)
        self.ui.btnStart.setEnabled(True)
        self.ui.btnStop.setEnabled(False)
        self.ui.btnSetPeriod.setEnabled(True)
    def do_timer_timeout(self):
        curtime=QTime.currentTime()
        self.ui.LCDhour.display(curtime.hour())
        self.ui.LCDminute.display(curtime.minute())
        self.ui.LCDsecond.display(curtime.second())


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=QmyWidget()
    form.show()
    sys.exit(app.exec_())