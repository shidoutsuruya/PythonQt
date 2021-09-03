#include "qtmysql.h"
#include "ui_qtmysql.h"

QtMySQL::QtMySQL(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::QtMySQL)
{
    ui->setupUi(this);
}

QtMySQL::~QtMySQL()
{
    delete ui;
}

void QtMySQL::on_actionOpen_triggered()
{

}
