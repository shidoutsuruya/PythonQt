#include "drag.h"
#include "ui_drag.h"

Drag::Drag(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Drag)
{
    ui->setupUi(this);
}

Drag::~Drag()
{
    delete ui;
}
