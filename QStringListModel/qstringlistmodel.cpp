#include "qstringlistmodel.h"
#include "ui_qstringlistmodel.h"

QStringListModel::QStringListModel(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::QStringListModel)
{
    ui->setupUi(this);
}

QStringListModel::~QStringListModel()
{
    delete ui;
}

void QStringListModel::on_btnAdd_clicked()
{

}

void QStringListModel::on_btnInsert_clicked()
{

}

void QStringListModel::on_btnClear_clicked()
{

}
