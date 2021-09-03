#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_pushButton_clicked()
{

}

void Widget::on_spinBox_valueChanged(int arg1)
{

}



void Widget::on_doubleSpinBox_valueChanged(const QString &arg1)
{

}
