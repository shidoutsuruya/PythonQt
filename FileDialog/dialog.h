#ifndef DIALOG_H
#define DIALOG_H

#include <QWidget>

namespace Ui {
class Dialog;
}

class Dialog : public QWidget
{
    Q_OBJECT

public:
    explicit Dialog(QWidget *parent = nullptr);
    ~Dialog();

private slots:
    void on_btnOpenFile_clicked();

    void on_btnOpenMoreFile_clicked();

    void on_btnSave_clicked();

    void on_btnSelectDirection_clicked();

    void on_btnColor_clicked();

    void on_btnFont_clicked();

    void on_btnProgress_clicked();

    void on_btnInputString_clicked();

    void on_btnInputInteger_clicked();

    void on_inputFloat_clicked();

    void on_btnItem_clicked();

    void on_btnInfo_clicked();

    void on_btnWarning_clicked();

    void on_btnCritical_clicked();

    void on_btnAbout_clicked();

    void on_pushButton_clicked();

private:
    Ui::Dialog *ui;
};

#endif // DIALOG_H
