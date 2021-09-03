#include "sqlquery.h"
#include "ui_sqlquery.h"

SqlQuery::SqlQuery(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::SqlQuery)
{
    ui->setupUi(this);
}

SqlQuery::~SqlQuery()
{
    delete ui;
}
