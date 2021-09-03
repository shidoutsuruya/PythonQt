#include "standarditemmodel.h"
#include "ui_standarditemmodel.h"

StandardItemModel::StandardItemModel(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::StandardItemModel)
{
    ui->setupUi(this);
}

StandardItemModel::~StandardItemModel()
{
    delete ui;
}

void StandardItemModel::on_actionfile_triggered()
{

}

void StandardItemModel::on_actionDelete_row_triggered()
{

}

void StandardItemModel::on_actionLeft_triggered()
{

}

void StandardItemModel::on_actionCenter_triggered()
{

}

void StandardItemModel::on_actionRight_triggered()
{

}

void StandardItemModel::on_actionAdd_row_triggered()
{

}

void StandardItemModel::on_actionBold_triggered()
{

}

void StandardItemModel::on_actionmodel_data_triggered()
{

}

void StandardItemModel::on_actionsave_triggered()
{

}
