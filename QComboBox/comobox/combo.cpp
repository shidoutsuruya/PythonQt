#include "combo.h"
#include "ui_combo.h"

combo::combo(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::combo)
{
    ui->setupUi(this);
}

combo::~combo()
{
    delete ui;
}
