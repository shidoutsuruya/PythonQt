#include "multimedia.h"
#include "ui_multimedia.h"

multimedia::multimedia(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::multimedia)
{
    ui->setupUi(this);
}

multimedia::~multimedia()
{
    delete ui;
}

void multimedia::on_btnAdd_clicked()
{

}

void multimedia::on_btnDelete_clicked()
{

}
