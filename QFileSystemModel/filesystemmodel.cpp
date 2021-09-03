#include "filesystemmodel.h"
#include "ui_filesystemmodel.h"

FileSystemModel::FileSystemModel(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::FileSystemModel)
{
    ui->setupUi(this);
}

FileSystemModel::~FileSystemModel()
{
    delete ui;
}

void FileSystemModel::on_treeView_clicked(const QModelIndex &index)
{

}
