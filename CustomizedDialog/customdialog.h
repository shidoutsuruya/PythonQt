#ifndef CUSTOMDIALOG_H
#define CUSTOMDIALOG_H

#include <QMainWindow>

namespace Ui {
class CustomDialog;
}

class CustomDialog : public QMainWindow
{
    Q_OBJECT

public:
    explicit CustomDialog(QWidget *parent = nullptr);
    ~CustomDialog();

private slots:
    void on_actionSet_line_triggered();

private:
    Ui::CustomDialog *ui;
};

#endif // CUSTOMDIALOG_H
