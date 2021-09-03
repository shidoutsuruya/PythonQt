#include "dirfile.h"
#include "ui_dirfile.h"

DirFile::DirFile(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::DirFile)
{
    ui->setupUi(this);
}

DirFile::~DirFile()
{
    delete ui;
}
