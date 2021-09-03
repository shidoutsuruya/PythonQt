#include "plt_gui.h"
#include "ui_plt_gui.h"

plt_gui::plt_gui(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::plt_gui)
{
    ui->setupUi(this);
}

plt_gui::~plt_gui()
{
    delete ui;
}
