#include "relationtable.h"
#include "ui_relationtable.h"

relationTable::relationTable(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::relationTable)
{
    ui->setupUi(this);
}

relationTable::~relationTable()
{
    delete ui;
}

void relationTable::on_actionExit_triggered()
{

}
