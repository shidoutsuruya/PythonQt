import sys
sys.path.append(r'C:\Users\max21\Desktop\Python\PythonQt\Qtime')
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from qtime import Ui_TIME
class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_TIME()
        self.ui.setupUi(self)
    def on_Readtime_clicked(self):
        curDateTime=QDateTime.currentDateTime()
        self.ui.timeEdit.setTime(curDateTime.time())
        self.ui.lineEdit_time.setText(curDateTime.toString('hh:mm:ss'))
        self.ui.dateEdit.setDate(curDateTime.date())
        self.ui.lineEdit_date.setText(curDateTime.toString('yyyy-MM-dd'))
        self.ui.dateTimeEdit.setDateTime(curDateTime)
        self.ui.lineEdit_datetime.setText(curDateTime.toString('yyyy-MM-dd hh:mm:ss'))
    def on_calendar_selectionChanged(self):
        date=self.ui.calendar.selectedDate()
        self.ui.lineEdit_select.setText(date.toString('yyyy/M/d'))
    def on_setTime_clicked(self):
        tmStr=self.ui.lineEdit_time.text()
        tm=QTime.fromString(tmStr,'hh:mm:ss')
        self.ui.timeEdit.setTime(tm)
    def on_setDate_clicked(self):
        dStr=self.ui.lineEdit_date.text()
        dt=QDate.fromString(dStr,'yyyy-MM-dd')
        self.ui.dateEdit.setDate(dt)
    def on_setDatetime_clicked(self):
        string=self.ui.lineEdit_datetime.text()
        dttm=QDateTime.fromString(string,'yyyy-MM-dd hh:mm:ss')
        self.ui.dateTimeEdit.setDateTime(dttm)

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=QmyWidget()
    form.show()
    sys.exit(app.exec_())