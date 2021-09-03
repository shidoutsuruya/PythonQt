#include "audioinput.h"
#include "ui_audioinput.h"

AudioInput::AudioInput(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::AudioInput)
{
    ui->setupUi(this);
}

AudioInput::~AudioInput()
{
    delete ui;
}

void AudioInput::on_actionStart_triggered()
{

}
