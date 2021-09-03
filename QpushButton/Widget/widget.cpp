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

void Widget::on_underlineBtn_clicked()
{

}

void Widget::on_leftBtn_clicked()
{

}

void Widget::on_middleBtn_clicked()
{

}

void Widget::on_rightBtn_clicked()
{

}

void Widget::on_boldBtn_clicked()
{

}

void Widget::on_rendonly_clicked()
{

}

void Widget::on_enabled_clicked()
{

}

void Widget::on_clearbtn_clicked()
{

}

void Widget::on_boldBtn_clicked(bool checked)
{

}
