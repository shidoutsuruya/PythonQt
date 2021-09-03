#include "event.h"
#include "ui_event.h"

Event::Event(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Event)
{
    ui->setupUi(this);
}

Event::~Event()
{
    delete ui;
}
