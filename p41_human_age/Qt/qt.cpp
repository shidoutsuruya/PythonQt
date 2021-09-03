#include "qt.h"
#include "ui_qt.h"

qt::qt(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::qt)
{
    ui->setupUi(this);
}

qt::~qt()
{
    delete ui;
}





void qt::on_SliderSetAge_valueChanged(int value)
{

}

void qt::on_btnSetName_clicked()
{

}
