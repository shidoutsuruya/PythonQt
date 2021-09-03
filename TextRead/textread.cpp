#include "textread.h"
#include "ui_textread.h"

TextRead::TextRead(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::TextRead)
{
    ui->setupUi(this);
}

TextRead::~TextRead()
{
    delete ui;
}

void TextRead::on_actionExit_triggered()
{

}
