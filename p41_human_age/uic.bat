copy .\Qt\qt.ui qt.ui
pyuic5 -o ui_Qt.py qt.ui
pyrcc5  .\Qt\res.qrc -o res_rc.py
