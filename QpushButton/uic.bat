pyrcc5  .\Widget\res.qrc -o res_rc.py
copy .\Widget\widget.ui widget.ui
pyuic5 -o ui_widget.py widget.ui
