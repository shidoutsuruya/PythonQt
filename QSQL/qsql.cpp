#include "qsql.h"
#include "ui_qsql.h"

QSQL::QSQL(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::QSQL)
{
    ui->setupUi(this);
}

QSQL::~QSQL()
{
    delete ui;
}
