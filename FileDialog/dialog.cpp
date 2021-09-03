#include "dialog.h"
#include "ui_dialog.h"

Dialog::Dialog(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Dialog)
{
    ui->setupUi(this);
}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::on_btnOpenFile_clicked()
{

}

void Dialog::on_btnOpenMoreFile_clicked()
{

}

void Dialog::on_btnSave_clicked()
{

}

void Dialog::on_btnSelectDirection_clicked()
{

}

void Dialog::on_btnColor_clicked()
{

}

void Dialog::on_btnFont_clicked()
{

}

void Dialog::on_btnProgress_clicked()
{

}

void Dialog::on_btnInputString_clicked()
{

}

void Dialog::on_btnInputInteger_clicked()
{

}

void Dialog::on_inputFloat_clicked()
{

}

void Dialog::on_btnItem_clicked()
{

}

void Dialog::on_btnInfo_clicked()
{

}

void Dialog::on_btnWarning_clicked()
{

}

void Dialog::on_btnCritical_clicked()
{

}

void Dialog::on_btnAbout_clicked()
{

}

void Dialog::on_pushButton_clicked()
{

}
